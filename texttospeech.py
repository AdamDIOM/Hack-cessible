import os
import requests
#os.system("say hello world")


def ocr_space_file(filename, overlay=False, api_key='helloworld', language='eng'):

    payload = {'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               }
    with open(filename, 'rb') as f:
        r = requests.post('https://api.ocr.space/parse/image',
                          files={filename: f},
                          data=payload,
                          )
    return r

print("Enter image file path")

text = ocr_space_file(input()).json()

print(text['ParsedResults'][0]['ParsedText'].replace("\n", " . ").replace("\r", " . "))
for line in text['ParsedResults'][0]['ParsedText'].split():
    os.system("say " + line)

os.system("say finished")
