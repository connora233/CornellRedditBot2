import requests
from bs4 import BeautifulSoup
f = open("cornell_classes.txt", "a")
url = 'https://classes.cornell.edu/search/roster/FA20?q=&subjects%5B%5D=STSCI&subjects%5B%5D=SUMER&subjects%5B%5D=SWAHL&subjects%5B%5D=SYSEN&subjects%5B%5D=TAG&subjects%5B%5D=TAMIL&subjects%5B%5D=THAI&subjects%5B%5D=TIBET&subjects%5B%5D=TOX&subjects%5B%5D=TURK&subjects%5B%5D=UKRAN&subjects%5B%5D=URDU&subjects%5B%5D=VTBMS&subjects%5B%5D=VETCS&subjects%5B%5D=VETMI&subjects%5B%5D=VTMED&subjects%5B%5D=VETMM&subjects%5B%5D=VIET&subjects%5B%5D=VISST&subjects%5B%5D=VIEN&subjects%5B%5D=WOLOF&subjects%5B%5D=WRIT&subjects%5B%5D=YORUB&subjects%5B%5D=ZULU&days-type=any&crseAttrs-type=any&breadthDistr-type=any&pi='
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'lxml')
for heading in soup.find_all(["h3"]):
    name_raw = heading.text.strip().split(" ")
    if len(name_raw) > 1 and name_raw[0][1].isupper():
        f.write(name_raw[0] + " " + name_raw[1][0:4] + "\n")
