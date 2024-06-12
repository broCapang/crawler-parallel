import aiohttp
import asyncio
from bs4 import BeautifulSoup
from tqdm.asyncio import tqdm
import json

url = "https://www.apu.edu.my/sitemap.xml"
ignore = ["http://www.apu.edu.my/china", "http://www.apu.edu.my/our-courses-chi"]
dataset = []

async def fetch(session, url):
    try:
        async with session.get(url, allow_redirects=True, max_redirects=10) as response:
            return await response.text()
    except aiohttp.ClientResponseError as e:
        print(f"Request failed: {e}")
    except aiohttp.TooManyRedirects:
        print(f"Too many redirects for URL: {url}")
    except Exception as e:
        print(f"An error occurred: {e}")
    return None

async def crawl(session, url):
    content = await fetch(session, url)
    if content is None:
        return
    soup = BeautifulSoup(content, "lxml")
    title = soup.find('h1', {'id': 'page-title'})
    if url in ignore or title is None or title.text.strip() == "Access denied":
        return
    data = {
        'url': url,
        'title': title.text.strip(),
        'body': soup.find('div', {'class': 'content-middle'}).get_text(separator="\n"),
    }
    dataset.append(data)

async def main():
    async with aiohttp.ClientSession() as session:
        response = await fetch(session, url)
        if response is None:
            return
        soup = BeautifulSoup(response, "xml")
        locs = soup.find_all('loc')
        urls = [loc.get_text() for loc in locs]
        
        tasks = [crawl(session, url) for url in urls]
        for task in tqdm(asyncio.as_completed(tasks), total=len(tasks)):
            await task

asyncio.run(main())

with open('apu.edu.jsonl', 'w') as file:
    for entry in dataset:
        json.dump(entry, file)
        file.write('\n')
