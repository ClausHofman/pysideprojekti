import html
import requests
import random
# API = application programming interface
# JSON = Javascript object notation

API_OSOITE = "https://opentdb.com/api.php?amount=10&difficulty=easy&type=multiple"

def lataa_kysymykset_netista():
    vastaus = requests.get(API_OSOITE)
    tiedot = vastaus.json()
    kysymykset_ja_vastaukset = []
    for juttu in tiedot["results"]:
        kysymys = juttu["question"]
        oikea_vastaus = juttu["correct_answer"]
        vaarat_vastaukset = juttu["incorrect_answers"]
        vastaukset = ["*" + oikea_vastaus] + vaarat_vastaukset
        random.shuffle(vastaukset)
        tekstit = [
            html.unescape(teksti)
            for teksti in [kysymys] + vastaukset
        ]
        kysymykset_ja_vastaukset.append(tekstit)
    return kysymykset_ja_vastaukset


    # print(tiedot)
    # import pprint
    # pprint.pprint(tiedot)

if __name__ == "__main__":
    import pprint
    pprint.pprint(lataa_kysymykset_netista())