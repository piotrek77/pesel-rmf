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

r = requests.get('http://www.rmf.fm/r/pesel.html', verify=True)
soup = BS(r.text, 'html.parser')
zawartosc = soup.find(id = 'xpesele-contents').get_text()
#linie = zawartosc.split('</div>')
linie = zawartosc
linia = zawartosc
#print(linie)
pesel = ''
pesele = []
#for linia in linie:
if linia != '':
    print('linia=['+linia+']')
    pesel=''
    if ')' in linia:
        print(linia.find(')'))
        pesel = linia[linia.find(')')+1:]
        pesel = pesel[:11]
        linia = linia[linia.find(')')+11:]
#    if ':' in linia:
#        pesel = linia[linia.find(':')+1:]
    if (pesel != ''):
        print('pesel ['+pesel+'] dodany')
        pesele.append(pesel)
print("Pesele ze strony RMF:")
if pesele[0]!='???????????':
    print(wyslijEmail.wyslijEmail(peselrmfParams.do, 'RMF dzisiajszy pesel: '+pesele[0],''))
for pesel in pesele:    
    print(pesel)
print("Pesele z pliku:")
for pesel in listaPeseliList:
    print(pesel)
znalezionych = 0
wszystkich = 0
    
print("Znalezione:")
#dla każdego elementy z RMF sprawdzamy jego istnienie w liscie peseli
for pesel in pesele:
    wszystkich = 0
    for pesel2 in listaPeseliList:
        wszystkich += 1
        if len(pesel2)==2:
            if pesel == pesel2[0]:
                wynik = wyslijEmail.wyslijEmail(peselrmfParams.do, datetime.datetime.now().strftime('%y-%m-%d %H-%M-%S')+' PESEL '+pesel +' '+pesel2[1],'')
                znalezionych += 1
                print(pesel, pesel2[1])
                print(wynik)

print('Przeanalizowalem '+str(wszystkich) +' zapisow z pliku')
print('Znaleziono '+ str(znalezionych)+' pasujacych zapisow')
    
