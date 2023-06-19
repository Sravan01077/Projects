import requests
from bs4 import BeautifulSoup
url = 'https://www.cricbuzz.com/live-cricket-scorecard/53350/eng-vs-aus-1st-test-the-ashes-2023'
response=requests.get(url)
soup=BeautifulSoup(response.text, 'html.parser')
details=soup.select('.cb-col .cb-col-100 .cb-scrd-hdr-rw')
for i in details:
    print(i.getText())
