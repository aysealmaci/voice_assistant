from datetime import datetime
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

#sr ye rec dedim

r=rec.Recognizer()

class VoiceAssistant:

    def assistant_speech(self, mytext):

        text_speech=gTTS(text=mytext,lang="tr") #language
        speech_file=str(random.randint(0,44444))+".mp3" #generate different speech files and save as mp3

        text_speech.save(speech_file) #record the voice
        playsound(speech_file)
        os.remove(speech_file) #delete the file after user listen

    def mic(self):
        with rec.Microphone() as micr:
            print("Buyrun sizi dinliyorum. Nasıl yardımcı olabilirim?")
            listen=r.listen(micr) #listen the sound come from the mic
            thevoice=""
            try:
                thevoice = r.recognize_google(listen, language="tr-TR")  # determine the language. Return as a String

            except rec.UnknownValueError: #if voice can't be understood
                self.assistant_speech("Ne dediğinizi anlayamadım")
                assistant.mic()

            return thevoice

    def answers_to_speech(self,coming_voice):
        if(coming_voice in "Merhaba"):
            self.assistant_speech("Size de merhaba")
        elif(coming_voice in "Nasılsın"):
            self.assistant_speech("Çok iyiyim siz nasılsınız")
        elif(coming_voice in "Saat kaç"):
            now = datetime.now()
            print(now)
        elif(coming_voice in "Müzik aç" or coming_voice in "Video aç"):
            try:
                self.assistant_speech("Tabi ne açmamı istersiniz")
                user_answer=self.mic()
                url = "https://www.youtube.com/results?search_query=" + user_answer
                thebrowser = webdriver.Chrome()
                thebrowser.get(url)
                open_the_first_video = thebrowser.find_element(By.XPATH,"//*[@id='video-title']/yt-formatted-string").click()  # open the fist video on youtube search according to user answer
                time.sleep(30)  # wait 30 seconds, then sleep

                self.assistant_speech("İstediğiniz bu muydu")

                user_wants=self.mic()

                if(user_wants in "Hayır"):
                    count=2
                    thebrowser.back()

                    while(count<7):
                        other_videos=thebrowser.find_element(By.XPATH,"//*[@id='contents']/ytd-video-renderer[{}]".format(count)).click()
                        time.sleep(30)

                        self.assistant_speech("İstediğiniz bu muydu")
                        user_wants=self.mic()

                        if(user_wants in "Evet"):
                            self.assistant_speech("Yardımcı olabildiğime sevindim")
                            break
                        else:
                            self.assistant_speech("Anladım o halde diğer videolara bakayım")
                            thebrowser.back()
                            count=count+1

                else:
                    self.assistant_speech("Yardımcı olabildiğime sevindim")


            except:
                self.assistant_speech("Bir hata oluştu birazdan tekrar deneyebilir misiniz")

        elif (coming_voice in "Google araması yap"):
            self.assistant_speech("Tabi neyi aramamı istersiniz")
            user_answer = self.mic()

            url = "https://www.google.com/search?q=" + user_answer
            self.assistant_speech("Arattığınız {} ile ilgili bunları buldum".format(user_answer))
            browser = webdriver.Chrome()  # Düzeltme: webdriver.Chrome() olarak değiştirildi.
            browser.get(url)

            the_first_website = browser.find_element(By.XPATH,
                                                     "//*[@id='rso']/div[1]/div/div/div/div/div/div/div[1]/a/h3").click()
            time.sleep(3000)
            browser.quit()


    def initialize_func(self,coming_voice):
        if(coming_voice in "Hey Siri"):
            self.assistant_speech("Evet buyrun dinliyorum")
            the_voice=self.mic() #assign the voice come from mic to the_voice
            if(the_voice!=""):
                self.answers_to_speech(the_voice)


assistant=VoiceAssistant()

while True: #mic always listen to user
    coming_voice=assistant.mic()
    if(coming_voice!=""): #if coming voice is not empty
        print(coming_voice) #print what user said
        assistant.initialize_func(coming_voice)

