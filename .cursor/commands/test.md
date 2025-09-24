# Test Command

## Description
Run the project's test suite.

## Usage
```bash
npm test
```

## Prerequisites
- Project dependencies must be installed
- Test framework must be configured

## Parameters
- `--watch`: Run tests in watch mode (optional)
- `--coverage`: Generate coverage report (optional)
- `--verbose`: Show detailed test output (optional)

## Examples
```bash
# Run all tests
cursor run test

# Run tests with coverage
cursor run test --coverage

# Run tests in watch mode
cursor run test --watch

# Run specific test file
cursor run test -- --testPathPattern=user.test.js
```

## Output
- Test results will be displayed in the terminal
- Coverage reports (if enabled) will be saved to `coverage/` directory