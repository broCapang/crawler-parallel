import requests
from bs4 import BeautifulSoup

urls = "https://umexpert.um.edu.my/zaidizabri.html\n"
urls = urls.strip()
response = requests.get(urls)
response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')

title_tag = soup.find('h1', class_='name mt-1 mb-1 text-uppercase text-uppercase')
title = title_tag.get_text(strip=True) if title_tag else "No title found"

about_me_div = soup.find('div', class_='resume-body pl-3 pr-4 pb-4 ml-4 pt-5')
body = about_me_div.get_text(strip=True) if about_me_div else "No content found in 'resume-body' div."

print({'url': "https://umexpert.um.edu.my/fonny.html", 'title': title, 'body': body})