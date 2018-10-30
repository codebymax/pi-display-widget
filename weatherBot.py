import bs4
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup 

my_url = "https://weather.com/weather/today/l/Ames+IA+USIA0026:1:US"

uClient = urlopen(my_url)

page_html = uClient.read()

uClient.close()

page_soup = soup(page_html, "html.parser")

#Things that we want
#temperature
#phrase
#rain_chance
#feels-like
#humidity
phrase = page_soup.find("div",{"class":"today_nowcard-phrase"}).text
temp = page_soup.find("div",{"class":"today_nowcard-temp"}).text
rain_chance = page_soup.find("span",{"class":"precip-val"}).text
humidity = page_soup.find("span",{"id":"dp0-lb-humidity"}).text
feels_like = page_soup.find("span",{"class":"deg-feels"}).text
10.30.126.31

print( phrase )
print( temp ) 
print( rain_chance )
print( feels_like )
print( humidity )