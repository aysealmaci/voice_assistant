from datetime import datetime
import datetime
import random
import time
from gtts import gTTS
import simpleaudio as sa
import speech_recognition as rec
from playsound import playsound
import pyaudio
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import smtplib
import ecapture as ec
import wikipedia
import webbrowser
import pywhatkit


r=rec.Recognizer() #recognizer

class VoiceAssistant:

    def assistant_speech(self, mytext):

        text_speech=gTTS(text=mytext,lang="tr") #language
        speech_file=str(random.randint(0,44444))+".mp3" #generate different speech files and save as mp3

        text_speech.save(speech_file) #record the voice
        playsound(speech_file)
        os.remove(speech_file) #delete the file after user listen


    def mic(self):
        with rec.Microphone() as micr:
            r.adjust_for_ambient_noise(micr,duration=1)
            print("Buyrun sizi dinliyorum. Nasıl yardımcı olabilirim?")
            listen=r.listen(micr) #listen the sound come from the mic
            thevoice=""
            try:
                thevoice = r.recognize_google(listen, language="tr-TR")  # determine the language. Return as a String

            except rec.UnknownValueError: #if voice can't be understood
                self.assistant_speech("Ne dediğinizi anlayamadım")
                assistant.mic()

            return thevoice

    def search_wikipedia(self):
        self.assistant_speech("Wikipedia'da ne aratmak istersiniz?")
        search_query = self.mic()

        page = wikipedia.page(search_query)
        self.assistant_speech(f"{search_query} sayfasını buldum. Şimdi açıyorum.")
        webbrowser.open(page.url)

    def send_email(self):
        self.assistant_speech("E-posta göndermek için gerekli bilgileri verin.")

        # E-posta bilgilerini al
        self.assistant_speech("Alıcı e-posta adresini söyleyin.")
        recipient = self.mic()

        self.assistant_speech("Konuyu söyleyin.")
        subject = self.mic()

        self.assistant_speech("İçeriği söyleyin.")
        content = self.mic()

        # E-posta gönderme işlemi
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login("your-email@gmail.com", "your-password")
            message = f"Subject: {subject}\n\n{content}"
            server.sendmail("your-email@gmail.com", recipient, message)
            server.quit()
            self.assistant_speech("E-posta başarıyla gönderildi.")
        except Exception as e:
            self.assistant_speech("E-posta gönderirken bir hata oluştu.")

    def send_wp_message(self):
        self.assistant_speech("Alıcı ismini söyleyin.")
        n= self.mic()

        if(n=="arezo"):
            recipient="+905524944430"


        self.assistant_speech("Mesajı söyleyin.")
        message = self.mic()

        hour = datetime.datetime.now().hour
        minute = datetime.datetime.now().minute + 1

        pywhatkit.sendwhatmsg(recipient, message, datetime.datetime.now().hour, datetime.datetime.now().minute + 1)
        self.assistant_speech("WhatsApp mesajı başarıyla gönderildi.")

        #AŞAĞIDAKİ KOD YAZI İLE ÇALIŞABİLİYOR
        #  def send_wp_message(self):
        # Alıcı telefon numarasını ve mesajı al
        #recipient = input("+90555xxxxxxx formatındaki alıcı telefon numarasını girin : ")
        #message = input("Mesajı girin: ")
        #pywhatkit.sendwhatmsg(recipient, message, datetime.datetime.now().hour, datetime.datetime.now().minute + 1)


    def play_music(self):
        self.assistant_speech("Tabiki Hangi şarkıyı ya da sanatçıyı açmak istersiniz?")

        ans = self.mic()

        url = "https://www.youtube.com/results?search_query=" + ans
        browser = webdriver.Chrome()
        browser.get(url)

    def answers_to_speech(self,coming_voice):
        if(coming_voice in "Merhaba"):
           self.assistant_speech("Size de merhaba")
        elif(coming_voice in "Merhaba"):
           ec.capture(0,"frame", "saved_picture.png")


        elif(coming_voice in "nasılsın"):
            self.assistant_speech("iyidir sizden naber")
        elif(coming_voice in "saat"):
            now = datetime.now()
            self.assistant_speech("Bugün {} ".format(now))
        elif coming_voice == "müzik ara":
            self.play_music()

        elif coming_voice == "bilgi":
            self.search_wikipedia()

        elif coming_voice=="mesaj":
            self.send_wp_message()

        elif (coming_voice=="mail at"):
            self.send_email()

        elif(coming_voice in "Google araması yap"):
            self.assistant_speech("Tabiki neyi aramamı istersiniz")
            user_answer = self.mic()

            url = "https://www.google.com/search?q=" + user_answer
            self.assistant_speech("Arattığınız {} ile ilgili bunları buldum".format(user_answer))
            browser = webdriver.Chrome()
            browser.get(url)
            time.sleep(30)
            browser.quit()

    #def initialize_func(self,coming_voice):
            #  if(coming_voice in "Hey Siri"):
            # self.assistant_speech("Evet buyrun dinliyorum")
            #the_voice=self.mic() #assign the voice come from mic to the_voice

            #if(the_voice!=""):
    #    self.answers_to_speech(the_voice)
    
assistant=VoiceAssistant()

while True: #mic always listen to user
    coming_voice=assistant.mic()
    if(coming_voice!=""): #if coming voice is not empty
        print(coming_voice) #print what user said
        assistant.answers_to_speech(coming_voice)
        #assistant.initialize_func(coming_voice)
