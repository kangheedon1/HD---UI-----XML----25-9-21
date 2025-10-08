from __future__ import annotations

import argparse
import sys
from typing import List

from .generator import Percent, parse_percent, random_percent, percent_range, format_percent


def cmd_random(args: argparse.Namespace) -> int:
    p = random_percent(args.min, args.max)
    print(format_percent(p))
    return 0


def cmd_range(args: argparse.Namespace) -> int:
    step = args.step
    for p in percent_range(args.start, args.end, step):
        print(format_percent(p))
    return 0


def cmd_test(_: argparse.Namespace) -> int:
    # simple invariants
    # Parsing/formatting roundtrip
    samples: List[str] = [
        "0", "0.0", "0%", "0.0%",
        "1", "1.0", "1%", "1.0%",
        "12.3", "12.3%", "100", "100.0%",
    ]
    for s in samples:
        p = parse_percent(s)
        text = format_percent(p, suffix="")
        # Compute canonical fixed-point string from tenths without floats
        whole = p.tenths // 10
        tenth = p.tenths % 10
        expected = f"{whole}" if tenth == 0 else f"{whole}.{tenth}"
        if text != expected:
            print(f"Format canonicalization mismatch for {s} -> {text} (expected {expected})", file=sys.stderr)
            return 1
        # And ensure parsing the formatted output yields the same value
        if parse_percent(text) != p:
            print(f"Parse roundtrip mismatch for {s} -> {text}", file=sys.stderr)
            return 1

    # Range count and endpoints
    seq = list(percent_range("0", "1.0", step=1))
    if len(seq) != 11 or seq[0].tenths != 0 or seq[-1].tenths != 10:
        print("Range invariant failed", file=sys.stderr)
        return 1

    # Random in bounds
    for _ in range(1000):
        r = random_percent("12.3", "45.6")
        if r.tenths < 123 or r.tenths > 456:
            print("Random bounds violated", file=sys.stderr)
            return 1

    print("ok")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="precision-percent", description="0.1%-precision percent generator without float errors")
    sub = p.add_subparsers(dest="cmd", required=True)

    pr = sub.add_parser("random", help="Generate a random percent in range [min,max]")
    pr.add_argument("--min", default="0", help="min percent (e.g., 0, 12.3, 45%)")
    pr.add_argument("--max", default="100", help="max percent (e.g., 100, 99.9%)")
    pr.set_defaults(func=cmd_random)

    prange = sub.add_parser("range", help="Generate inclusive range of percents")
    prange.add_argument("start", help="start percent")
    prange.add_argument("end", help="end percent")
    prange.add_argument("--step", type=int, default=1, help="step in tenths (default 1 -> 0.1%)")
    prange.set_defaults(func=cmd_range)

    ptest = sub.add_parser("self-test", help="Run self-test")
    ptest.set_defaults(func=cmd_test)

    return p


def main(argv: List[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
