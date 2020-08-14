import json
import requests
from googletrans import Translator

class WABot():    
    def __init__(self, json):
        self.json = json
        self.dict_messages = json['messages']
        self.APIUrl = 'https://eu104.chat-api.com/instance161053/'
        self.token = '3wzj1xyi9yhiiye4'
        print(self.dict_messages)
   
    def send_requests(self, method, data):
        url = f"{self.APIUrl}{method}?token={self.token}"
        headers = {'Content-type': 'application/json'}
        answer = requests.post(url, data=json.dumps(data), headers=headers)
        return answer.json()

   

    def en(self, chatID):
        for message in self.dict_messages:
            text = message['body']
            par = text[5:]
            translator = Translator()
            result = translator.translate(par, src='en', dest='id')
            data = {
               "body": result.text,
               "chatId": chatID
            }
            answer = self.send_requests('sendMessage', data)
            return answer

    def idn(self, chatID):
        for message in self.dict_messages:
            text = message['body']
            par = text[5:]
            translator = Translator()
            result = translator.translate(par, src='id', dest='en')
            data = {
               "body": result.text,
               "chatId": chatID
            }
            answer = self.send_requests('sendMessage', data)
            return answer

    def geo(self, chatID):
        for message in self.dict_messages:
            text = message['body']
            from googlesearch import search 
            query = text[2:]
            for i in search(query, tld="com", num=10, stop=10, pause=5):
                data = {
                      "body" : "🔎 Results Pencarian Google :\n\n[1]" +i,
                      "chatId" : chatID
                      }
                answer = self.send_requests('sendMessage', data)
                return answer

   

    def start(self, chatID):
        data = {
            "body": "🤖 _Halo Saya Adalah Whatsapp Bot, Ada Yang Bisa Saya Bantu?_\n\n*Admin :*\n\n📞 : +62 85155477031\n📱 : _fb.me/haliddjubu_ \n\n🚀 *Fitur* \n\n\n✅ _Status Korona Di Gorontalo_ \n✅ _Pencarian Google_ \n✅ _Terjemahan_ \n\n\n _Untuk Menampilkan perintah Ketik_ *Menu*",
            "chatId": chatID
        }
        answer = self.send_requests('sendMessage', data)
        return answer

    def menu(self, chatID):
        data = {
              "body": "*Daftar Perintah* :\n\n🔖 *sk* ( ketik sk untuk mengecek status korona di Gorontalo )\n🔖 *gs* _pertanyaan_ ( contoh: gs surat alfatiha )\n🔖 *tr-id* _text_ ( terjemahan inggris ke indo )\n🔖 *tr-en* _text_ ( terjemahan indo ke inggris )",
              "chatId": chatID
              }
        answer = self.send_requests('sendMessage', data)
        return answer

   

    def korona(self, chatID):
        for message in self.dict_messages:
            text = message['body'] 
            data = {
                  "body": 'https://litu.gdunli.workers.dev/korona.jpg',
                  "filename": 'jpg',
                  "chatId": chatID
                  }

            answer = self.send_requests('sendFile', data)
            return answer 
        
     

        
  
            
    
    
    def processing(self):
        if self.dict_messages != []:
            for message in self.dict_messages:
                text = message['body'].split()
                if not message['fromMe']:
                    id  = message['chatId']
                    if text[0].lower() == 'hi':
                        return self.welcome(id)
                    elif text[0].lower() == 'tr-en':
                        return self.idn(id)
                    elif text[0].lower() == 'tr-id':
                        return self.en(id)
                   
                    elif text[0].lower() == 'mulai':
                        return self.start(id)
                    
                    
                   
                    elif text[0].lower() == 'sk':
                        return self.korona(id)
                  
                    
                    
                    
                    elif text[0].lower() == 'gs':
                        return self.geo(id)
                    elif text[0].lower() == 'menu':
                        return self.menu(id)
                   
                    else:
                        return 'NoCommand'
                else: return 'NoCommand'

           
