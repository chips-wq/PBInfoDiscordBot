from bs4 import BeautifulSoup
from bot.models.models import Problema_PBInfo , Exemplu
class Generate_PBInfo_Problem:
    def __init__(self , response): 
        response.encoding = 'utf8'
        self.soup = BeautifulSoup(response.text , 'lxml')
        self.enunt_intreg = self.soup.find('article' , id='enunt')
        self.cleanup_enunt()
        self.cod = response.url.split("/")[4]
        self.nume = str(self.soup.title.string).split("|")[0]
        self.description = self.get_description()
        self.cerinta = None
        self.date_intrare = None
        self.date_iesire = None
        self.restrictii = None
        self.important = None
        self.exemple=None
        self.update_problema_main()

    def cleanup_enunt(self):
        useles_div = self.enunt_intreg.select('div' , class_="float-right")
        for s in useles_div:
            s.extract()

        ads = self.enunt_intreg.select('script')
        for s in ads:
            s.extract()

        for s in self.enunt_intreg.select('ins'):
            s.extract()

    def preia_pana_la_h1(self, start , arr_elemente):
        #returneaza toate elementele pana la urmatorul heading
        content = ""
        for i in range(start+1 , len(arr_elemente)):
            if arr_elemente[i].name == 'h1':
                break
            content+=str(arr_elemente[i])
        return content

    def is_next_h1_explicatie(self , arr_elemente , start):
        """
        mai intai adauga in exemplu_content toate elementele pana la urmatorul heading
        daca urmatorul heading e o explicatie adauga in explicatie_content toate elementele pana la urmatorul heading folosind functie preia_pana_la_h1
        daca urmatorul heading nu e explicatie returneaza exemplu_content si un string gol
        """
        exemplu_content = ""
        for j in range(start+1 , len(arr_elemente)):
            if arr_elemente[j].name == 'h1' or arr_elemente[j].name == 'h3':
                if str(arr_elemente[j].string).startswith("Explica"):
                    explicatie_content = self.preia_pana_la_h1(j , arr_elemente)
                    return exemplu_content , explicatie_content
                break
            exemplu_content+=str(arr_elemente[j])

        return exemplu_content , None

    def update_problema_main(self):
        enunt_elemente_principale = self.enunt_intreg.find_all(['h1' , 'h3' , 'p' , 'ul' , 'pre'])

        self.cerinta = self.preia_pana_la_h1(-1 , enunt_elemente_principale)#preia paragrafele deasupra cerintei daca exista si adaugale in cerinta
        exemple = []

        for i , elem in enumerate(enunt_elemente_principale):
            if elem.name == 'h1' or elem.name == 'h3':
                if str(elem.string).startswith("Explica"):
                    continue
                elif str(elem.string).startswith("Exemp"):
                    exemplu_content , explicatie_content = self.is_next_h1_explicatie(enunt_elemente_principale , i)
                    exemplu = Exemplu(exemplu_content , explicatie_content)
                    exemple.append(exemplu)
                elif str(elem.string).startswith("Cerin"):
                    self.cerinta += self.preia_pana_la_h1(i , enunt_elemente_principale)
                elif str(elem.string).startswith("Date de intrare"):
                    self.date_intrare = self.preia_pana_la_h1(i , enunt_elemente_principale)
                elif str(elem.string).startswith("Date de ie"):
                    self.date_iesire = self.preia_pana_la_h1(i , enunt_elemente_principale)
                elif str(elem.string).startswith("Restric"):
                    self.restrictii = self.preia_pana_la_h1(i , enunt_elemente_principale)
                elif str(elem.string).startswith("Important"):
                    self.important = self.preia_pana_la_h1(i , enunt_elemente_principale)
        
        self.exemple = exemple

    def get_description(self):
        description_arr = []
        description = self.soup.find('ol' , class_='breadcrumb')

        for elem in description.find_all('li'):
            a_link = elem.find('a' , recursive=False)
            if a_link:
                description_arr.append(str(a_link.string).strip())
            else:
                description_arr.append(str(elem.string).strip())

        return " / ".join(description_arr)

    def generate_problem(self):
        problema = Problema_PBInfo(self.cod , self.nume , self.description , self.cerinta , self.date_intrare , self.date_iesire , self.restrictii , self.important , self.exemple)
        return problema


def genereaza_problema(response):
    instance = Generate_PBInfo_Problem(response)
    return instance.generate_problem()

"""
if __name__ == '__main__':
    import requests
    response = requests.get("https://www.pbinfo.ro/probleme/343/soarece1")
    problema = genereaza_problema(response)
    print(problema)
"""