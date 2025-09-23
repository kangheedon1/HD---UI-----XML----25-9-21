# Cursor Commands

This directory contains custom commands for the Cursor editor. Each command is defined in a separate markdown file following the pattern `[command].md`.

## Structure

Each command file should follow this structure:

```markdown
# Command Name

## Description
Brief description of what the command does.

## Usage
```bash
command-to-execute
```

## Prerequisites
- List any requirements
- Dependencies that need to be installed
- Configuration that needs to be done

## Parameters
- `--param1`: Description of parameter 1
- `--param2`: Description of parameter 2

## Examples
```bash
# Example usage 1
cursor run command-name

# Example usage 2
cursor run command-name --param1 value
```

## Output
Description of what the command outputs or produces.

## Notes
Any additional notes or considerations.
```

## Available Commands

- `example.md` - Example command demonstrating the structure
- `build.md` - Build the project
- `test.md` - Run the test suite

## Usage

Commands can be executed using:
```bash
cursor run [command-name]
```

## Creating New Commands

1. Create a new `.md` file in this directory
2. Follow the structure outlined above
3. Name the file after your command (e.g., `deploy.md` for a deploy command)
4. Define the command's behavior in the Usage section

## Best Practices

- Use clear, descriptive command names
- Provide comprehensive examples
- Document all parameters and prerequisites
- Include error handling information where relevant
- Keep commands focused on a single responsibility