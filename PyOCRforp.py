import os
from PIL import Image, ImageOps
import pyocr
 
def outputText():
    if request.method == 'POST':
        f = flask.request.json
        f_name = f["image"]
        print(f"{f_name}")
        img = Image.open(f"{f_name}")

        return "Response('ok')"



#pyocrへ利用するOCRエンジンをTesseractに指定する。
tools = pyocr.get_available_tools()
tool = tools[0]
 
#OCR対象の画像ファイルを読み込む
img = Image.open("img/img2.png").convert(mode="L")
#白黒化
img = ImageOps.invert(img)

#画像から文字を読み込む
builder = pyocr.builders.TextBuilder(tesseract_layout=4)

#im_crop = img.crop((30, 695, 1535, 840))

#text2 = tool.image_to_string(im_crop, lang="jpn", builder=builder)
text2 = tool.image_to_string(img, lang="jpn", builder=builder)

print(text2)

