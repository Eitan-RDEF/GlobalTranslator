# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import copy_metadata, collect_data_files, collect_submodules
import importlib.metadata
import os

def safe_copy_metadata(package_name):
    try:
        return copy_metadata(package_name)
    except importlib.metadata.PackageNotFoundError:
        print(f"WARNING: Metadata for package '{package_name}' not found. Skipping.")
        return []
    except Exception as e:
        print(f"WARNING: Error copying metadata for '{package_name}': {e}. Skipping.")
        return []

datas = []
# Critical: Streamlit needs its own metadata to check version
datas += safe_copy_metadata('streamlit')
datas += collect_data_files('streamlit')

# Add other common packages that might need metadata
datas += safe_copy_metadata('openai')
datas += safe_copy_metadata('tqdm')
datas += safe_copy_metadata('regex')
datas += safe_copy_metadata('requests')
datas += safe_copy_metadata('packaging')
datas += safe_copy_metadata('filelock')
datas += safe_copy_metadata('numpy')

# Add application files
datas += [('app.py', '.'), ('config.py', '.')]

# Collect all streamlit submodules to be safe
hiddenimports = collect_submodules('streamlit')
hiddenimports += [
    'streamlit.web.cli',
    'pymupdf',
    'fitz', # alias for pymupdf
    'docx',
    'dotenv',
    'openai',
]

# Add Anaconda Library/bin to pathex to find DLLs
pathex = [
    'C:\\Users\\Eitan\\anaconda3\\Library\\bin',
    'C:\\Users\\Eitan\\GlobalTranslator',
]

# Explicitly add system DLLs that are often missing in Anaconda envs
# These are found in C:\Users\Eitan\anaconda3\Library\bin
dll_path = 'C:\\Users\\Eitan\\anaconda3\\Library\\bin'
binaries = [
    (os.path.join(dll_path, 'ffi-7.dll'), '.'),
    (os.path.join(dll_path, 'ffi-8.dll'), '.'),
    (os.path.join(dll_path, 'ffi.dll'), '.'),
    (os.path.join(dll_path, 'liblzma.dll'), '.'),
    (os.path.join(dll_path, 'libcrypto-3-x64.dll'), '.'),
    (os.path.join(dll_path, 'libssl-3-x64.dll'), '.'),
    (os.path.join(dll_path, 'sqlite3.dll'), '.'),
    (os.path.join(dll_path, 'libexpat.dll'), '.'),
]

a = Analysis(
    ['launcher.py'],
    pathex=pathex,
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='GlobalTranslator',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
