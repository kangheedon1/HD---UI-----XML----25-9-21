# Build Command

## Description
Build the project using the appropriate build system.

## Usage
```bash
npm run build
```

## Prerequisites
- Node.js and npm must be installed
- Dependencies must be installed (`npm install`)

## Parameters
- `--production`: Build for production (optional)
- `--watch`: Enable watch mode (optional)

## Examples
```bash
# Standard build
cursor run build

# Production build
cursor run build --production

# Build with watch mode
cursor run build --watch
```

## Output
- Built files will be placed in the `dist/` directory
- Build logs will show compilation status and any errors