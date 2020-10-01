import requests

from bs4 import BeautifulSoup

mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}

#put your city's link here in text

# get the link from https://weather.com and search your city in the search bar of the site

text = 'https://weather.com/en-IN/weather/today/l/a1ffe804270c234b184bc01e9146f9dfc5753e591f063b027e85a5323afe0192'

page = requests.get(text, headers=mozhdr)

soup = BeautifulSoup(page.content, 'html.parser')

temp = soup.find_all('div', class_="today_nowcard-temp")

templist = []

for x in temp:

	temperature = x.find('span')	templist.append(temperature.text)

print(templist)

# the program tells the current temperature in Narela, delhi!
