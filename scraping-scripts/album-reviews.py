#!/usr/bin/env python3
"""Simple web page fetch + title extraction skeleton (Beautiful Soup)."""

import time
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

def fetch_html(url: str) -> str:
    aoty_headers = {"User-Agent": "Mozilla/5.0 ()"}
    req = Request(url, headers=aoty_headers)
    with urlopen(req) as resp:
        return resp.read().decode(errors="replace")

def get_review_text(review_text_element):
    review_paragraphs = review_text_element.select("p")
    review_text = ""
    for paragraph in review_paragraphs:
        for break_tag in paragraph.select("br"):
            break_tag.replace_with(" ")
        review_text += paragraph.get_text() + " "
    return review_text.strip()

def extract_read_more_review(read_more_url: str):
    read_more_html = fetch_html(read_more_url)
    soup = BeautifulSoup(read_more_html, "html.parser")
    reviewer_name = soup.select_one(".userName").get_text()
    rating = soup.select_one(".albumCriticScore").get_text()
    review_element = soup.select_one(".userReviewText")
    review_text = get_review_text(review_element)
    return (reviewer_name, rating, review_text)

def extract_reviews(html: str):
    soup = BeautifulSoup(html, "html.parser")
    reviews = soup.select(".albumReviewRow")
    review_texts = []
    for review in reviews:
        read_more_link = review.select_one("a.gray")
        if read_more_link:
            review_texts.append(extract_read_more_review("https://www.albumoftheyear.org" + read_more_link["href"]))
            time.sleep(3)
        else:
            reviewer_name = review.select_one(".userReviewName").get_text()
            rating = review.select_one(".rating").get_text()
            review_element = review.select_one(".albumReviewText")
            review_text = get_review_text(review_element)
            review_texts.append((reviewer_name, rating, review_text))
    return review_texts

def main():
    with open("review-links.txt") as review_links_file:
        i = 0
        for review_link in review_links_file:
            current_review_link = review_link[:-1]
            current_album_html = fetch_html(current_review_link)
            time.sleep(3)
            current_reviews = extract_reviews(current_album_html)
            with open("reviews.txt", "a") as reviews_file:
                for current_review in current_reviews:
                    reviews_file.write(current_review[0] + "\t" + current_review[1] + "\t" + current_review[2] + "\n")
            i += 1
            print(i, "/2350 done", sep="")

if __name__ == "__main__":
    main()
