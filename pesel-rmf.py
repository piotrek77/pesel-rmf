import requests
import wyslijEmail
import peselrmfParams
from bs4 import BeautifulSoup as BS
import csv
import time
import datetime
listaPeseli = csv.reader(open('listaPeseli.csv', newline=''), delimiter=';', quotechar='|')
listaPeseliList = list(listaPeseli)
listaPeseliList.pop(0) #usuniecie pierwszego elementu (naglowka)

r = requests.get('http://www.rmf.fm/f/pesel.html', verify=True)
soup = BS(r.text, 'html.parser')
zawartosc = soup.find(id = 'xpesele-contents').get_text()
linie = zawartosc.split('«')
pesel = ''
pesele = []
for linia in linie:
    if ')' in linia:
        pesel = linia[linia.find(')')+1:]
    if ':' in linia:
        pesel = linia[linia.find(':')+1:]
    pesele.append(pesel)
print("Pesele ze strony RMF:")
wyslijEmail.wyslijEmail(peselrmfParams.do, 'RMF dzisiajszy pesel: '+pesele[0],'')
for pesel in pesele:    
    print(pesel)
print("Pesele z pliku:")
for pesel in listaPeseliList:
    print(pesel)

    
print("Znalezione:")
#dla każdego elementy z RMF sprawdzamy jego istnienie w liscie peseli
for pesel in pesele:
    for pesel2 in listaPeseliList:
        if len(pesel2)==2:
            if pesel == pesel2[0]:
                wynik = wyslijEmail.wyslijEmail(peselrmfParams.do, datetime.datetime.now().strftime('%y-%m-%d %H-%M-%S')+' PESEL '+pesel +' '+pesel2[1],'')
                
                print(pesel, pesel2[1])
                print(wynik)
    
