import requests
from bs4 import BeautifulSoup
import pandas as pd

site = ["live-members", "product-statistics"]

for correct in range(0,2):
    if site[correct] == 'live-members':
        url = "https://www.npci.org.in/what-we-do/imps/"+str(site[correct])
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")

        state = soup.find("table")
        state2 = state.find_next("table")
        state3 = state2.find_next("table")

        for table in state:
            rows = []
            for row in state.find_all('tr'):
                row_data = [cell.text.strip() for cell in row.find_all('td')]

                rows.append(row_data)
                df = pd.DataFrame(rows)
        for table2 in state2:
            rows2 = []
            for row in state2.find_all("tr"):
                row_data = [cell.text.strip() for cell in row.find_all('td')]

                rows2.append(row_data)
                df2 = pd.DataFrame(rows2)

        for table3 in state3:
            rows3 = []
            for row in state3.find_all(("tr")):
                row_data = [cell.text.strip() for cell in row.find_all('td')]

                rows3.append(row_data)
                df3 = pd.DataFrame(rows3)

        df.to_excel("99 - LiveBanks.xlsx")
        df2.to_excel("99 - LanguageSupport.xlsx")
        df3.to_excel("99 - LiveTelco.xlsx")
        correct+=1

    elif site[correct] == "product-statistics":
        url = "https://www.npci.org.in/what-we-do/99/"+str(site[correct])
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")

        month = [i.text for i in soup.select('td:nth-child(1)')]
        live_banks = [i.text for i in soup.select('td:nth-child(2)')]
        volume = [i.text for i in soup.select('td:nth-child(3)')]
        value = [i.text for i in soup.select('td:nth-child(4)')]

        df1 = pd.DataFrame(month, columns=["Month"])
        df2 = pd.DataFrame(live_banks, columns=["No. of Banks live on *99#"])
        df3 = pd.DataFrame(volume, columns=["Volume(Mn)"])
        df4 = pd.DataFrame(value, columns=["Value(In Cr)"])

        final_df = pd.concat([df1, df2, df3, df4], axis=1)
        final_df.to_excel("99 - ProdStat.xlsx")

        print("All Files Exported!")

