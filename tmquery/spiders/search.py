from typing import List
from bs4 import BeautifulSoup
from utils.get_box import get_box
from cache.client import Client


def valid_td(td: BeautifulSoup) -> str:
    links = td.find_all("a")
    for link in links:
        if link["href"] != "#":
            return link["href"]
    return ""


def search(query: str, header: str) -> List[str]:
    
    url = "https://www.transfermarkt.com/schnellsuche/ergebnis/schnellsuche?query=" + query
    soup = Client().scrape(url)

    box = get_box(soup, header)

    rows = box.find("table", class_="items").find("tbody").find_all("tr")

    results = []
    for row in rows:
        tds = row.find_all("td")
        for td in tds:
            link = valid_td(td)
            if (link != ""):
                results.append(link)
                break
    
    return [results[0]]