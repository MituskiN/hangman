"""#zipファイルの完成形
import shutil
from pathlib import Path

def copy_with_organizing(from_path,to_path):
    to_path.mkdir()
    
    for p in from_path.glob('**/*'):
        suffix=p.suffix[1:] #「.」を削除
        dir=to_path/suffix

        if p.is_file():
            dir.mkdir(exist_ok=True)
            shutil.copy2(p,dir)

extracted=Path(r'ファイルパス1')
shutil.unpack_archive(r'ファイルパス2',extracted)
[shutil.move(p,str(p).encode('cp437').decode('cp932'))
    for p in extracted.glob('**/*')
]

organized=Path(r'ファイルパス1')
copy_with_organizing(extracted,organized)

shutil.make_archive(r'ファイルパス3','zip',organized)
"""

"""#ファイルディレクトリのコピー
import shutil
from pathlib import Path

shutil.copy2(r'nonpro_python/data1.csv',r'nonpro_python/data1')
shutil.copy2(Path(r'nonpro_python/data1.xlsx'),Path(r'nonpro_python/data1'))
shutil.copytree(r'nonpro_python/data1',r'nonpro_python/data2')
"""
"""#ファイルディレクトリの移動と名称変更
import shutil
from pathlib import Path

shutil.move(r'nonpro_python/data2/data2.csv',r'nonpro_python')
shutil.move(r'nonpro_python/data2/data3.csv',r'nonpro_python')
shutil.move(Path(r'nonpro_python/data1/data1.csv'),Path(r'nonpro_python/data1/data1_renamed.csv'))
#shutil.move(r'nonpro_python/data2',r'nonpro_python/data1')
"""

"""#ファイルの圧縮と展開
import shutil
from pathlib import Path

shutil.make_archive(r'nonpro_python/zip/new_archive','zip',r'nonpro_python/data1') #new_archive.zipをnonpro_pythonの中に作成する
shutil.unpack_archive(Path(r'nonpro_python/new_archive.zip'),Path(r'nonpro_python/new_extracted'))
"""

"""#windowsで圧縮されたzipアーカイブの展開
import shutil
from pathlib import Path

shutil.make_archive(r'nonpro_python/zip/data1_win','zip',r'nonpro_python/data1')
shutil.unpack_archive(Path(r'nonpro_python/zip/data1_win.zip'),Path(r'nonpro_python/extracted'))
"""
"""#windows zipアーカイブ展開時の文字化けの訂正
import shutil
from pathlib import Path
extracted=Path(r'nonpro_python/extracted')
shutil.unpack_archive(r'nonpro_python/zip/data1_win.zip',extracted)

for p in extracted.glob('**/*.xlsx'):
    print(p,str(p).encode('cp437').decode('cp932'))
"""
"""#windows標準機能で圧縮されたzipファイルを展開する
import shutil
from pathlib import Path
extracted=Path(r'nonpro_python/extracted')
shutil.unpack_archive(r'nonpro_python/zip/data1_win.zip',extracted)

[shutil.move(p,str(p).encode('cp437').decode('cp932'))
    for p in extracted.glob('**/*')
]
"""

"""#ファイルを拡張子ごとに分類&コピー
import shutil
from pathlib import Path
def copy_with_organizing(from_path,to_path):
    to_path.mkdir()
    for p in from_path.glob('**/*'):
        suffix=p.suffix[1:] #「.」を削除
        dir=to_path/suffix

        if p.is_file():
            dir.mkdir(exist_ok=True)
            shutil.copy2(p,dir)

extracted=Path(r'nonpro_python/extracted')
organized=Path(r'nonpro_python/organized')
copy_with_organizing(extracted,organized)
"""

"""#ディレクトリをzipファイルに圧縮する

import shutil
from pathlib import Path

organized=Path(r'nonpro_python/organized')
shutil.make_archive(r'nonpro_python/archive','zip',organized)
"""

"""#zipファイルを展開、圧縮するツールのまとめ
import shutil
from pathlib import Path

def copy_with_organizing(from_path,to_path):
    to_path.mkdir()
    for p in from_path.glob('**/*'):
        suffix=p.suffix[1:] #「.」を排除
        dir=to_path/suffix

        if p.is_file():
            dir.mkdir(exist_ok=True)
            shutil.copy2(p,dir)


extracted=Path(r'nonpro_python/extracted')
shutil.unpack_archive(r'nonpro_python/zip/data1_win.zip',extracted)

[shutil.move(p,str(p).encode('cp437').decode('cp932'))
    for p in extracted.glob('**/*')
]
organized=Path(r'nonpro_python/organized')
copy_with_organizing(extracted,organized)

shutil.make_archive(r'nonpro_python/archive','zip',organized)
"""




















