import tweepy
import os

from dotenv import load_dotenv

class Twitter:
    
    def __init__(self) -> None:
        load_dotenv()
        self.API_Key = os.getenv('API_Key')
        self.API_Key_Secret = os.getenv('API_Key_Secret')
        self.Bearer_Token = os.getenv('Bearer_Token')
        self.Access_Token = os.getenv('Access_Token')
        self.Access_Token_Secret = os.getenv('Access_Token_Secret')

    def get_api(self):

        Authenticate to Twitter
        auth = tweepy.OAuthHandler(self.API_Key, self.API_Key_Secret)
        auth.set_access_token(self.Access_Token, self.Access_Token_Secret)

        Create API object
        api = tweepy.API(auth)

        try:
            api.verify_credentials()
            print("Authentication OK")
        except:
            print("Error during authentication")

        return api
    
    def fist_tweet(self, api, imgs, htmls):
        api.update_with_media(imgs[0], htmls[0])
                
    def UpdateTwitter(self):
        api = self.get_api()
        imgs, htmls = self.img_html_paths()
    
        self.fist_tweet(api, imgs, htmls)
        
        self.todos_los_demas(api, imgs, htmls)


    def img_html_paths():
        
        departamentos = ['AMAZONAS','ANCASH','APURIMAC','AREQUIPA','AYACUCHO','CAJAMARCA','CALLAO','CUSCO','HUANCAVELICA','HUANUCO','ICA','JUNIN','LA LIBERTAD','LAMBAYEQUE','LIMA','LORETO','MADRE DE DIOS','MOQUEGUA','PASCO','PIURA','PUNO','SAN MARTIN','TACNA','TUMBES','UCAYALI']
        imgs = ["img/" + w.title() + ".png" for w in departamentos]
        htmls = ["https://optimistic-aryabhata-c23029.netlify.app/html/" + w.title().replace(" ", "") for w in departamentos]
        
        return imgs, htmls