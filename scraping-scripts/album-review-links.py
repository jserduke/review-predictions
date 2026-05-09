#!/usr/bin/env python3

import time
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

def fetch_html(url: str) -> str:
    aoty_headers = {"User-Agent": "Mozilla/5.0 ()"}
    req = Request(url, headers=aoty_headers)
    with urlopen(req) as resp:
        return resp.read().decode()

def extract_album_links(html: str):
    soup = BeautifulSoup(html, "html.parser")
    album_links = soup.select(".albumListTitle a")
    album_hrefs = []
    for album_link in album_links:
        album_href = album_link["href"]
        album_hrefs.append(album_href)
    return album_hrefs

def main():
    aoty_url = "https://www.albumoftheyear.org/ratings/6-highest-rated/2020s/"

    for i in range(1, 188, 2):
        html = fetch_html(aoty_url + str(i))
        album_hrefs = extract_album_links(html)
        with open("review-links.txt", "a") as review_links_file:
            for album_href in album_hrefs:
                review_links_file.write("https://www.albumoftheyear.org" + album_href[:-4] + "/user-reviews/?sort=recent\n")
        print(i, "/188 done", sep="")
        time.sleep(5)

if __name__ == "__main__":
    main()
