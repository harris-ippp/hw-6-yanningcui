import requests
for line in open("ELECTION_ID"):
    year, el_id = tuple(line.split())
    resp=requests.get("http://historical.elections.virginia.gov/elections/download/{}/precincts_include:0/".format(el_id))
    with open(str(year) + ".csv", "w") as out:
        out.write(resp.text)
