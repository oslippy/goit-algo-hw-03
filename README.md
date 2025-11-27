## Usage

### Basic Usage

Run the script with a required `--source` argument:

```bash
python task1.py --source /path/to/source/directory
```

This will copy all files from the source directory to a `dist` folder (default destination) in the current working directory, organized by file extension.

### Specify Custom Destination

You can specify a custom destination directory using the `--destination` argument:

```bash
python task1.py --source /path/to/source/directory --destination /path/to/destination
```

### Examples

**Example 1: Organize files from current directory**
```bash
python task1.py --source .
```

**Example 2: Organize files from a specific folder to a custom destination**
```bash
python task1.py --source ~/Downloads --destination ~/OrganizedFiles
```

**Example 3: Organize files with relative paths**
```bash
python task1.py --source ./myfiles --destination ./sorted
```

## Command-Line Arguments

- `--source` (required): Path to the source directory to scan
- `--destination` (optional): Path to the destination directory where files will be copied. Defaults to `dist` in the current directory
