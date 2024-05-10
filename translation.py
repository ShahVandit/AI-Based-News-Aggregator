# coding=utf8
from googletrans import Translator
translator = Translator()
translation = translator.translate("Business", dest='gu')
print(translation.text)