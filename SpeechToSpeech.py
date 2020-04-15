import requests
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

bot_message = ""
integer = 1
while bot_message != "pa":
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("speak anything: ")
        audio = r.listen(source)

        message = r.recognize_google(audio, language='ro')
        print("you said: {}".format(message))

    if len(message) == 0:
        continue
    print("sending message now")

    r = requests.post(
        "http://localhost:5002/webhooks/rest/webhook",
        json={"message": message}
    )

    print("bot says, ", end=' ')
    for i in r.json():
        bot_message = i['text']
        print(f"{i['text']}")

    myObj = gTTS(text=bot_message, lang='ro')
    fileName = "file" + str(integer) + ".mp3"
    myObj.save(fileName)
    print(fileName)
    print('saved')
    playsound(fileName)
    integer = integer + 1
