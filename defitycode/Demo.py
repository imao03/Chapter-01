from pytesseract import pytesseract
from PIL import Image

pic = Image.open('code.jpg')
# pic 为打开的图片,lang指定识别转换的语言库
text = pytesseract.image_to_string(pic, lang='chi_sim')
print(text)
