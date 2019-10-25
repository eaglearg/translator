from language.language import language
from translate import Translator

def translation(translateTo, translateFrom, translatePhrase):
    translator = Translator(to_lang=translateTo.strip(), from_lang=translateFrom.strip())
    return translator.translate(translatePhrase)

while True:
    translateMode = input("please tell me if you want to translate in the command shell (c) or a file (f): ")
    if (translateMode.strip() == "c" or translateMode.strip() == "f"):
        break
    else:
        print('please enter c in case that you want to use the command shell or f if you want to translate from a file')
while True:
    translateFrom = input("Tell us in which language is the phrase: e.g. es, en, pt, zh ")
    if (language.get(translateFrom.strip(), 0) == 0):
        print('you need to enter a valid language available in the following list', language.keys())
    else:
        break

while True:
    translateTo = input("Tell us in which language you want to translate the phrase: e.g. es, en, pt, zh ")
    if (language.get(translateTo.strip(), 0) == 0):
        print('you need to enter a valid language available in the following list', language.keys())
    else:
        break

if translateMode == 'c':
    while True:
        translatePhrase = input("Please enter the phrase that you want to translate ")
        if (len(translatePhrase.strip()) > 0):
            break
        else:
            print('You didn\'t enter anything. Please enter the phrase')

    translation = print(translation(translateTo, translateFrom, translatePhrase))
else:
    try:
        with open('./translate.txt', mode='r') as myFile:
            translatePhrase = myFile.read()
            translation = translation(translateTo, translateFrom, translatePhrase)
            with open('./test-translated.txt', mode='w') as myFile2:
                myFile2.write(translation)
    except Exception as err:
        print('error', err)