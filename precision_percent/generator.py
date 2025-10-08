from __future__ import annotations

import random
from dataclasses import dataclass
from typing import Iterable, Iterator, Tuple


SCALE = 10  # 0.1% precision; store as integer of tenths of percent
MIN_TENTHS = 0
MAX_TENTHS = 1000  # 100.0%


@dataclass(frozen=True, order=True)
class Percent:
    """Fixed-point percent with 0.1% precision and no float error.

    Internally stores integer number of tenths of a percent in [0, 1000].
    """

    tenths: int

    def __post_init__(self) -> None:
        if not isinstance(self.tenths, int):
            raise TypeError("tenths must be int")
        if self.tenths < MIN_TENTHS or self.tenths > MAX_TENTHS:
            raise ValueError("tenths out of range [0, 1000]")

    @classmethod
    def from_bps(cls, basis_points: int) -> "Percent":
        # basis points: 1% == 100 bps; 0.1% == 10 bps
        if not isinstance(basis_points, int):
            raise TypeError("basis_points must be int")
        if basis_points < 0 or basis_points > 10000:
            raise ValueError("basis_points out of range [0, 10000]")
        tenths = basis_points // 10
        if basis_points % 10 != 0:
            raise ValueError("basis_points must be multiple of 10 for 0.1% precision")
        return cls(tenths)

    @property
    def as_percent(self) -> float:
        # lossless to one decimal representation using integer division, returned as float for convenience
        return self.tenths / SCALE

    @property
    def as_fraction(self) -> float:
        # exact rational to float; still represents a finite decimal with 1 place.
        return self.tenths / (SCALE * 100.0)

    def to_bps(self) -> int:
        return self.tenths * 10

    def __str__(self) -> str:
        return format_percent(self)

    def __repr__(self) -> str:
        return f"Percent(tenths={self.tenths})"


def parse_percent(text: str) -> Percent:
    """Parse strings like '12.3%', '12%', '0.1', '12.0', '100', '100.0%'.

    Enforces one decimal place max and range [0, 100]. No float math used.
    """
    if not isinstance(text, str):
        raise TypeError("text must be str")
    s = text.strip().rstrip("%")
    if not s:
        raise ValueError("empty percent string")

    negative = s.startswith("-")
    if negative:
        raise ValueError("percent cannot be negative")

    if "." in s:
        whole, frac = s.split(".", 1)
        if not whole:
            whole = "0"
        if not whole.isdigit() or not frac.isdigit():
            raise ValueError("invalid percent format")
        if len(frac) > 1:
            # disallow >1 decimal to ensure strict 0.1% precision
            raise ValueError("too many decimal places; max 1")
        tenth = int(frac[0]) if frac else 0
        tenths = int(whole) * SCALE + tenth
    else:
        if not s.isdigit():
            raise ValueError("invalid percent format")
        tenths = int(s) * SCALE

    if tenths < MIN_TENTHS or tenths > MAX_TENTHS:
        raise ValueError("percent out of range [0, 100]")

    return Percent(tenths)


def format_percent(p: Percent, suffix: str = "%") -> str:
    whole = p.tenths // SCALE
    tenth = p.tenths % SCALE
    if tenth == 0:
        return f"{whole}{suffix}" if suffix else f"{whole}"
    return f"{whole}.{tenth}{suffix}" if suffix else f"{whole}.{tenth}"


def random_percent(min_inclusive: Percent | int | str = 0,
                    max_inclusive: Percent | int | str = 100) -> Percent:
    """Return uniformly random Percent in [min, max] with 0.1% precision.

    Accepts `Percent`, int (percent), or str (parseable) for bounds.
    """
    min_p = _ensure_percent(min_inclusive)
    max_p = _ensure_percent(max_inclusive)
    if min_p.tenths > max_p.tenths:
        raise ValueError("min cannot be greater than max")
    tenths = random.randint(min_p.tenths, max_p.tenths)
    return Percent(tenths)


def percent_range(start: Percent | int | str,
                   end: Percent | int | str,
                   step: int | None = None) -> Iterator[Percent]:
    """Yield Percent values from start to end inclusive by tenths step.

    step defaults to 1 tenth (0.1%). Set step in tenths.
    """
    s = _ensure_percent(start)
    e = _ensure_percent(end)
    if s.tenths > e.tenths:
        raise ValueError("start cannot be greater than end")
    step_tenths = 1 if step is None else int(step)
    if step_tenths <= 0:
        raise ValueError("step must be positive tenths")
    for t in range(s.tenths, e.tenths + 1, step_tenths):
        yield Percent(t)


def _ensure_percent(value: Percent | int | str) -> Percent:
    if isinstance(value, Percent):
        return value
    if isinstance(value, int):
        return Percent(value * SCALE)
    if isinstance(value, str):
        return parse_percent(value)
    raise TypeError("unsupported percent value type")
