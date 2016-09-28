# Opis

Program sprawdza pesele ze strony RMF:

http://www.rmf.fm/f/pesel.html

I porównuje z listą w pliku listaPeseli.csv

W przypadku zgodności wysyła email

# Instalacja

zmiemiamy nazwy plików:

listaPeseli_dist.csv na listaPeseli.csv

peselrmfParams_dist.py na peselrmfParams.py

wyslijEmailParams_dist.py na wyslijEmailParams.py

Edytujemy powyższe pliki ustawiając własne parametry

# Uruchomienie

python3 pesel-rmf.py
