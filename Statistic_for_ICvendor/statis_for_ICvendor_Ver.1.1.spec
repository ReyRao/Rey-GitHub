# -*- mode: python ; coding: utf-8 -*-

import sys
sys.setrecursionlimit(5000)


block_cipher = None


a = Analysis(['statis_for_ICvendor_Ver.1.1.py'],
             pathex=['C:\\Users\\party\\Desktop\\MyGitHub\\Python'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='statis_for_ICvendor_Ver.1.1',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
