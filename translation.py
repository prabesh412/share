from data import title
from googletrans import Translator

translater = Translator()
for titles in title:
    output = translater.translate(titles, dest='en')
    print(output.text())