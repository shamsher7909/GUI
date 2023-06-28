# final_1.spec

# Import the necessary modules
from PyInstaller.utils.hooks import collect_data_files
from PyInstaller.utils.hooks import collect_submodules

# Configuration for PyInstaller
block_cipher = None

# Create the Analysis object
a = Analysis(['final_1.py'],
             pathex=['C:\\Users\\Peter\\Downloads'],
             binaries=[],
             datas=collect_data_files('path/to/data/folder'),
             hiddenimports=collect_submodules('package_name'),
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

# Create the PYZ (Python Zip) object
pyz = PYZ(a.pure, a.zipped_data,
          cipher=block_cipher)

# Create the EXE (Executable) object
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='gui_app',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True)
