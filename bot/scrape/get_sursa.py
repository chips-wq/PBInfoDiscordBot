import requests 
import bot.db as db
from bot.config import auth
from bs4 import BeautifulSoup
from bot.models.models import Problema_PBInfo , Source
class genereaza_sursa:
    def __init__(self , problema):
        self.problema = problema
        if self.genereaza_sursa_github():
            pass
        elif self.scrape_rezolvari_pbinfo():
            pass
    def genereaza_sursa_github(self):
        db.c.execute("SELECT * FROM githubfiles WHERE name=:problema" , {'problema':self.problema.cod+".cpp"})
        list_problema = db.c.fetchone()
        if list_problema:
            sursa_plain = requests.get(list_problema[3] , auth=auth).text
            sursa = Source(sursa_plain , "c++" , "chips-wq")
            self.problema.sursa = sursa
            return True
        return False

    def scrape_rezolvari_pbinfo(self):
        response = requests.get(f"https://tutoriale-pe.net/problema-{self.problema.cod}")
        response.encoding = 'utf8'
        if response.status_code == 200:
            soup = BeautifulSoup(response.text , 'lxml')
            source = soup.find('pre' , class_="EnlighterJSRAW")
            sursa = Source(str(source.string) , "c++" , "Rezolvari-PBInfo" , url=response.url)
            self.problema.sursa = sursa
            return True
        return False

"""
if __name__ == '__main__':
    problema = Problema_PBInfo("g2r5g" , 'idk' , 'no idea' , 'ups' , None , None , None ,None)
    print(problema.sursa)
    genereaza_sursa(problema)
    print(problema.sursa)
"""