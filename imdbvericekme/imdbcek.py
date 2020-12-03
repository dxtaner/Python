import requests
from bs4 import BeautifulSoup

url="https://www.imdb.com/chart/top"

response=requests.get(url)

htmlicerigi=response.content

soup=BeautifulSoup(htmlicerigi,"html.parser")

basliklar=soup.findAll("td",{"class":"titleColumn"})
ratingler=soup.findAll("td",{"class":"ratingColumn imdbRating"})

deger=float(input("rating girin:"))

for baslik,rating in zip(basliklar,ratingler):
    baslik=baslik.text
    baslik=baslik.strip()
    baslik=baslik.replace("\n","")
    rating=rating.text
    rating=rating.strip()
    rating=rating.replace("\n","")

    if(float(rating)>deger):
        print("film ismi: {} film rating: {}".format(baslik,rating))




