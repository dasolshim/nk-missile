from bs4 import BeautifulSoup
import requests

url = "https://en.wikipedia.org/wiki/List_of_North_Korean_missile_tests"
response = requests.get(url)
html = response.text
bs = BeautifulSoup(html, "html.parser")
tables = bs.find_all("table")
wiki_table = tables[1]
wiki_table_rows = wiki_table.find_all("tr")

if __name__ == "__main__":
    pass
