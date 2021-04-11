import requests , markdownify
class Source:
    def __init__(self , plain_source , language , author , url=None):
        self.plain_source = plain_source
        self.language = language
        self.author = author
        self.url = url
    def discord_ready_embed(self): 
        rezolvare = f"```{self.language}\n{self.plain_source}```scris de {self.author}"
        if self.url:
            rezolvare+=f"\n{self.url}"
        return rezolvare
    def __repr__(self):
        return f"Source code({self.language})\n{self.plain_source}\n\nby {self.author}"

class Exemplu:
    def __init__(self , continut , explicatie=None):
        self.continut = continut
        self.explicatie = explicatie
    
    def markdownify_continut(self):
        return markdownify.markdownify(self.continut.replace("<p>" , "\n").replace("</p>" , "\n").replace("<code>" , "`").replace("</code>" , "`"))
    
    def markdownify_explicatie(self):
        return markdownify.markdownify(self.explicatie.replace("<code>" , "`").replace("</code>" , "`"))

    def __repr__(self):
        return f"Continutul Exemplului:\n{self.continut}\nExplicatie:\n{self.explicatie}"

class Problema_PBInfo:
    def __init__(self ,cod, nume , description , cerinta , date_intrare , date_iesire , restrictii ,important ,  exemple=None , sursa=None):
        self.cod = cod
        self.nume = nume
        self.description = description
        self.cerinta = cerinta
        self.date_intrare = date_intrare
        self.date_iesire = date_iesire
        self.restrictii = restrictii
        self.important = important
        self.exemple = exemple
        self.url = f"https://www.pbinfo.ro/probleme/{self.cod}"
        self.sursa = sursa

    def markdownify(self , content):
        return markdownify.markdownify(content.replace("<code>" , "`").replace("</code>" , "`"))

    def __repr__(self):
        ret_str = f"{self.nume}#{self.cod}\n\n{self.description}\n\nCerinta\n{self.cerinta}"
        if self.date_intrare:
            ret_str+= f"\nDate de intrare\n{self.date_intrare}"
        if self.date_iesire:
            ret_str+= f"\nDate de iesire\n{self.date_iesire}"
        if self.restrictii:
            ret_str+= f"\nRestrictii si precizari\n{self.restrictii}"
        if self.important:
            ret_str+= f"\nImportant\n{self.important}"
        if self.exemple:
            for index , exemplu in enumerate(self.exemple):
                ret_str+=f"\nExemplul {index+1}\n{exemplu.continut}\n"
                if exemplu.explicatie:
                    ret_str += f"\nExplicatie\n{exemplu.explicatie}"
            return ret_str

    