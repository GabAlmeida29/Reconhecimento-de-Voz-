from email.mime import audio
import speech_recognition as sr

rec = sr.Recognizer()

#print(sr.Microphone().list_microphone_names())
with sr.Microphone(2) as mic:
    rec.adjust_for_ambient_noise(mic)
    print("Pode falar !!!")
    audio = rec.listen(mic)
    txt = rec.recognize_google(audio, language="pt-BR")
    print(txt)
