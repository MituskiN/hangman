"""#犬の画像100枚を自動スクレイピング 1000枚まで可能
from icrawler.builtin import BingImageCrawler
crawler = BingImageCrawler(storage={"root_dir": "dogs"})
crawler.crawl(keyword="犬", max_num=100)
"""
"""#猫の画像100枚を自動スクレイピング
from icrawler.builtin import BingImageCrawler
crawler = BingImageCrawler(storage={"root_dir": "cats"})
crawler.crawl(keyword="猫", max_num=100)
"""
"""#Excelファイルに猫画像貼り付け
import pathlib
import pandas as pd
values=[]
my_path=pathlib.Path(r'cats')
for p in my_path.glob('*.jpg'):
    values.append(p)

df=pd.DataFrame(values) 

df.to_excel(r"cats_and_dogs.xlsx",sheet_name='cats',header=['URL'])
"""
"""#既存のファイルに犬の画像URL貼り付け できない！
import pathlib
import pandas as pd
filename=r"cats_and_dogs.xlsx"
values=[]
my_path=pathlib.Path(r'dogs')
for p in my_path.glob('*.jpg'):
    values.append(p)
df=pd.Series(values) 
with pd.ExcelWriter(filename,mode='a') as writer:
    df.to_excel(writer,sheet_name='dogs')
"""
"""#新しいExcelファイルに犬の画像URL貼り付け
import pathlib
import pandas as pd
filename=r"cats_and_dogs.xlsx"
values=[]
my_path=pathlib.Path(r'dogs')
for p in my_path.glob('*.jpg'):
    values.append(p)
df=pd.DataFrame(values)
df.to_excel(r'dogs.xlsx')
"""
"""#画像のサイズやファイルパスを確認できる
from openpyxl.drawing.image import Image
import pathlib
from PIL import Image
my_path=pathlib.Path(r'cats')
for img in my_path.glob('*.jpg'):
    im=Image.open(img)
    print(im.size)
"""

"""#画像のサイズを統一する(resize)
from openpyxl.drawing.image import Image
import pathlib
from PIL import Image

my_path=pathlib.Path(r'cats')
width,height=1000,1000
for p in my_path.glob('*.jpg'):
    im=Image.open(p)
    im.resize((width,height))
"""
"""#画像のサイズを統一する(resize)
import os
from PIL import Image
#ファイル名を宣言
FromImgName = r'cats'
ToImgName = r'cats_resize'

#imgフォルダ内の画像名をまとめて取得
files = os.listdir(FromImgName) #listdir()関数では、( )内に記入したパスのファイル名・ディレクトリ名の一覧をリスト型で取得

#for文で画像サイズを一括変更
for file in files:
    #path.join()関数は、二つの文字列を結合させ、一つのパスにする事ができる。複数のファイルを一つのファイルとして扱う。
    img = Image.open(os.path.join(FromImgName, file)) #画像のパスを生成し、imgへ画像を格納
    img_resize = img.resize((600,600))  #画像サイズ変更
    img_resize.save(os.path.join(ToImgName, file))  #resizeフォルダへ保存
"""








