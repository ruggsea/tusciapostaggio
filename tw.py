from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
with open("tusciawebprova.csv","w", newline="",encoding="utf-8") as f:
    csv=csv.writer(f) 
    csv.writerow(["Articoli"])
    for year in range(2012,2021):
        print(year)
        for mese in range(1,13):
            print(mese)
            if mese<10:
                mesetto="0"+str(mese)
            else:
                mesetto=mese
            paginetta= "http://www.tusciaweb.eu/"+str(year)+"/"+str(mesetto)+"/"
            page=urlopen(paginetta)
            print(paginetta)
            soup=BeautifulSoup(page,"html.parser")
            titoli=soup.findAll(attrs={"rel":"bookmark"})
            len(titoli)
            print(type(titoli))
            for titolo in titoli[::2]:
                print(titolo.text)
                csv.writerow([titolo.text])
                
            for i in range(2,30):
                try:
                    page=urlopen(paginetta+"page/"+str(i)+"/")
                except:
                    print("fine pagine di questo mese")
                else:
                    soup=BeautifulSoup(page,"html.parser")
                    titoli=soup.findAll(attrs={"rel":"bookmark"})
                    for titolo in titoli[::2]:
                        print(titolo.text)
                        csv.writerow([titolo.text])

