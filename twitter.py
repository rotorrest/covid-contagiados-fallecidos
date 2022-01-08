import tweepy
import os

from dotenv import load_dotenv

class Twitter:
    
    def __init__(self) -> None:
        load_dotenv()
 
        auth = tweepy.OAuthHandler(os.getenv('API_Key'), os.getenv('API_Key_Secret'))
        auth.set_access_token(os.getenv('Access_Token'), os.getenv('Access_Token_Secret'))        
        self.api = tweepy.API(auth)
         
        self.departamentos, self.imgs, self.htmls = Twitter.img_html_paths()
        
    def UpdateTwitter(self, date):

        aux_tweet = self.api.update_status_with_media(status="Peru", filename="img/peru.jpg", )
        aux_id_holder = aux_tweet.id
        
        #for i in range(len(self.departamentos)):
        for i in range(4):
            text = "Estado de contagios y fallecidos COVID-19 en " + self.departamentos[i] +"\n" + "fecha de actualización: " + date  +"\n" + "link: " + self.htmls[i] + "\n" + "Compartir en whatsapp: https://wa/test "
            
            
            aux_id_holder = Twitter.reply_to_status(self, aux_id_holder, status=text,filename=self.imgs[i])
            
            

    def img_html_paths():
        
        departamentos = ['AMAZONAS','ANCASH','APURIMAC','AREQUIPA','AYACUCHO','CAJAMARCA','CALLAO','CUSCO','HUANCAVELICA','HUANUCO','ICA','JUNIN','LA LIBERTAD','LAMBAYEQUE','LIMA','LORETO','MADRE DE DIOS','MOQUEGUA','PASCO','PIURA','PUNO','SAN MARTIN','TACNA','TUMBES','UCAYALI']
        departamentos = [w.title() for w in departamentos]
        imgs = ["img/" + w.title() + ".png" for w in departamentos]
        htmls = ["https://optimistic-aryabhata-c23029.netlify.app/html/" + w.title().replace(" ", "") for w in departamentos]
        
        return departamentos, imgs, htmls
    
    def reply_to_status(self, id, status,filename):

        tweet = self.api.update_status_with_media(filename=filename,
                                            status=status, 
                                            in_reply_to_status_id=id)
        
        return tweet.id