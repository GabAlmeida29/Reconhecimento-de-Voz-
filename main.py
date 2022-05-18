from email.mime import audio
import webbrowser as web
import speech_recognition as sr
import os

#Pegar Audio
rec = sr.Recognizer()

#Ligar Microfone
#print(sr.Microphone().list_microphone_names())
with sr.Microphone(3) as mic:
    rec.adjust_for_ambient_noise(mic)
    print("Boa tarde, o que deseja?")
    audio = rec.listen(mic)
    txt = rec.recognize_google(audio, language="pt-BR")

#Abrir programas e sites para o trabalho
    if "navegador" in txt:
        os.system("start Chrome.exe")
    if "Excel" in txt:
        os.system("start Excel.exe")
    if "Word" in txt:
        os.system("start winword.exe")
    if "fertisystem" in txt:
        web.open("https://www.fertisystem.com.br")
    if "agromac" in txt:
        web.open("https://www.fertisystem.com.br")
    if "isobus" in txt:
        web.open("http://isobus.fertisystem.com.br")
    if "e-mail" in txt:
        os.system("start outlook.exe")
    if "portal" in txt:
        web.open("https://admin.microsoft.com/Adminportal/Home?#/homepage")
    if "monitoramento" in txt:
        web.open("https://suporteti.fertisystem.com.br/")
    if "trabalho" in txt:
        os.system("start mstsc.exe")

 #Imprime o que foi dito
    print(txt)

