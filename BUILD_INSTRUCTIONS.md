# Building the Standalone Executable

This guide explains how to build a standalone executable (`.exe`) for the Global Translator application.

## Prerequisites

1. **Python 3.10 or higher** installed
2. **All dependencies** installed (from `requirements.txt`)
3. **PyInstaller** installed (from `build_requirements.txt`)

## Step-by-Step Build Instructions

### 1. Install Build Dependencies

```bash
pip install -r build_requirements.txt
```

### 2. Build the Executable

Run PyInstaller with the spec file:

```bash
pyinstaller build_exe.spec
```

This will create:
- `dist/GlobalTranslator/` - Directory containing the executable and dependencies
- `dist/GlobalTranslator.exe` - Standalone executable (if one-file mode)
- `build/` - Temporary build files (can be deleted after building)

### 3. Test the Executable

1. Navigate to the `dist` folder
2. Run `GlobalTranslator.exe`
3. The app should open in your default browser at `http://localhost:8501`

### 4. Distribution

To distribute the application:
- **Option 1**: Share the entire `dist/GlobalTranslator/` folder
- **Option 2**: Create a ZIP file of the `dist/GlobalTranslator/` folder
- **Option 3**: Use an installer tool (like Inno Setup or NSIS) to create an installer

## Build Options

### Hide Console Window

To hide the console window when running the executable, edit `build_exe.spec` and change:
```python
console=True,  # Change to False
```

### Add an Icon

1. Create or obtain an `.ico` file
2. Edit `build_exe.spec` and set:
```python
icon='path/to/your/icon.ico',
```

### One-File vs One-Directory

The current spec creates a one-directory build. For a single-file executable, modify the `EXE` section in `build_exe.spec` to use `onefile=True` (though this may have slower startup time).

## Troubleshooting

### Import Errors

If you encounter import errors when running the executable:
1. Check that all required packages are in `hiddenimports` in `build_exe.spec`
2. Add missing imports to the `hiddenimports` list
3. Rebuild

### pymupdf/fitz Import Errors

If you see errors about `fitz` or `pymupdf`:
1. Ensure `pymupdf` is installed: `pip install pymupdf`
2. The spec file includes `pymupdf` and `pymupdf.fitz` in hidden imports
3. If issues persist, try: `pip install --upgrade pymupdf`

### Streamlit Not Starting

If Streamlit doesn't start:
1. Check that `launcher.py` is included in the build
2. Verify that Streamlit data files are collected (check `datas` in spec file)
3. Run with console enabled to see error messages
4. Check that port 8501 is not already in use

### Large File Size

The executable will be large (100-300 MB) because it includes:
- Python interpreter
- All dependencies (Streamlit, OpenAI, pymupdf, etc.)
- All required data files

This is normal for PyInstaller bundles. The excludes list in the spec file helps reduce size by excluding unnecessary packages.

## Notes

- The first run may be slower as files are extracted
- Antivirus software may flag the executable (false positive) - this is common with PyInstaller
- Users will need to enter their OpenAI API key in the app's Settings sidebar (no `.env` file needed)

