from numpy import short
import tweepy
import os
from tqdm import tqdm

import urllib.parse as parse

from dotenv import load_dotenv



class Twitter:
    
    def __init__(self) -> None:
        load_dotenv()
 
        auth = tweepy.OAuthHandler(os.getenv('API_Key'), os.getenv('API_Key_Secret'))
        auth.set_access_token(os.getenv('Access_Token'), os.getenv('Access_Token_Secret'))        
        self.api = tweepy.API(auth)
         
        self.departamentos, self.imgs, self.htmls, self.short_html= Twitter.img_html_paths()
        
    def UpdateTwitter(self, date):

        aux_tweet = self.api.update_status_with_media(status="Peru", filename="img/peru.jpg", )
        aux_id_holder = aux_tweet.id
        
        for i in tqdm(len(self.departamentos), ncols=80, desc="Actualizando Twitter"):
            
            wtp_url = "api.whatsapp.com/send?text=" + parse.quote_plus(self.departamentos[i] + " COVID-19: Contagios y fallecidos " + self.short_html[self.htmls[i]] + "\n Sigue al bot en twitter twitter.com/CovidPeruBot")

            
            text = "COVID-19: Contagios y fallecidos "  + "\n" + '\U0001F4CD' +" "+ self.departamentos[i]   + "\n" + '\U0001F4C5' +" "+ "Actualización: " + date  +"\n" + '\U0001F517' +" "+  "Link: " + self.short_html[self.htmls[i]] + "\n" + '\U0001F7E2' +" "+	 "Comparte en whatsapp: " + wtp_url 

            aux_id_holder = Twitter.reply_to_status(self, aux_id_holder, status=text,filename=self.imgs[i])
            
    def img_html_paths():
        
        departamentos = ['AMAZONAS','ANCASH','APURIMAC','AREQUIPA','AYACUCHO','CAJAMARCA','CALLAO','CUSCO','HUANCAVELICA','HUANUCO','ICA','JUNIN','LA LIBERTAD','LAMBAYEQUE','LIMA','LORETO','MADRE DE DIOS','MOQUEGUA','PASCO','PIURA','PUNO','SAN MARTIN','TACNA','TUMBES','UCAYALI']
        departamentos = [w.title() for w in departamentos]
        imgs = ["img/" + w.title() + ".png" for w in departamentos]
        htmls = ["https://optimistic-aryabhata-c23029.netlify.app/html/" + w.title().replace(" ", "") for w in departamentos]
        
        short_html = {"https://optimistic-aryabhata-c23029.netlify.app/html/Ucayali" : "https://bit.ly/3JSs43t",
                    "https://optimistic-aryabhata-c23029.netlify.app/html/Tumbes" : "https://bit.ly/3JU3WO7",
                    "https://optimistic-aryabhata-c23029.netlify.app/html/Tacna":"https://bit.ly/3G9Vnfx",
                    "https://optimistic-aryabhata-c23029.netlify.app/html/SanMartin":"https://bit.ly/3n5VPUG",
                    "https://optimistic-aryabhata-c23029.netlify.app/html/Puno":"https://bit.ly/3t7NLqd",
                    "https://optimistic-aryabhata-c23029.netlify.app/html/Piura":"https://bit.ly/3t4RNzO",
                    "https://optimistic-aryabhata-c23029.netlify.app/html/Pasco":"https://bit.ly/3zAJ3CO",
                    "https://optimistic-aryabhata-c23029.netlify.app/html/Moquegua":"https://bit.ly/3f2YeLr",
                    "https://optimistic-aryabhata-c23029.netlify.app/html/MadreDeDios":"https://bit.ly/3JQ3L6m",
                    "https://optimistic-aryabhata-c23029.netlify.app/html/Loreto":"https://bit.ly/3zACAYk",
                    "https://optimistic-aryabhata-c23029.netlify.app/html/Lima":"https://bit.ly/3qVY2Du",
                    "https://optimistic-aryabhata-c23029.netlify.app/html/Lambayeque":"https://bit.ly/3F6BOUf",
                    "https://optimistic-aryabhata-c23029.netlify.app/html/LaLibertad":"https://bit.ly/3JQrUJW",
                    "https://optimistic-aryabhata-c23029.netlify.app/html/Junin":"https://bit.ly/3JPd3iR",
                    "https://optimistic-aryabhata-c23029.netlify.app/html/Ica":"https://bit.ly/3JTSzFG",
                    "https://optimistic-aryabhata-c23029.netlify.app/html/Huanuco":"https://bit.ly/3t8retr",
                    "https://optimistic-aryabhata-c23029.netlify.app/html/Huancavelica":"https://bit.ly/3JLG7Id",
                    "https://optimistic-aryabhata-c23029.netlify.app/html/Cusco":"https://bit.ly/3qVY0v7",
                    "https://optimistic-aryabhata-c23029.netlify.app/html/Callao":"https://bit.ly/3qYg5J3",
                    "https://optimistic-aryabhata-c23029.netlify.app/html/Cajamarca":"https://bit.ly/3F6Ay3m",
                    "https://optimistic-aryabhata-c23029.netlify.app/html/Ayacucho":"https://bit.ly/3GbyeJY",
                    "https://optimistic-aryabhata-c23029.netlify.app/html/Arequipa":"https://bit.ly/3zGiDzp",
                    "https://optimistic-aryabhata-c23029.netlify.app/html/Apurimac":"https://bit.ly/32S4fIE",
                    "https://optimistic-aryabhata-c23029.netlify.app/html/Ancash":"https://bit.ly/3q2IYEK",
                    "https://optimistic-aryabhata-c23029.netlify.app/html/Amazonas" : "https://bit.ly/3f23Rth"}
        
        return departamentos, imgs, htmls, short_html
    
    def reply_to_status(self, id, status,filename):

        tweet = self.api.update_status_with_media(filename=filename,
                                            status=status, 
                                            in_reply_to_status_id=id)
        
        return tweet.id