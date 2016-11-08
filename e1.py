import requests
from bs4 import BeautifulSoup as bs
resp=requests.get("http://historical.elections.virginia.gov/elections/search/year_from:1924/year_to:2015/office_id:1/stage:General")
soup = bs(resp.content, "html.parser")
resp.content
l = soup.find_all("tr", "election_item")
lst = []
with open("ELECTION_ID", "w") as out:
    for x in l:
        el_id = int(x["id"].split("-")[-1])
        year = int(x.find("td", "year").string)
        out.write("{} {}\n".format(year, el_id))
