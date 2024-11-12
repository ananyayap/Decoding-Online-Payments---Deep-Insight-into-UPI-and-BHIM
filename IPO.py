import requests
from bs4 import BeautifulSoup
import pandas as pd

x = 0
url = "https://www.npci.org.in/what-we-do/ipo/live-partners"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
final_df = pd.DataFrame()
final_df_0 = pd.DataFrame()
final_df_1 = pd.DataFrame()
table = soup.find_all("table", class_="table table-bordered")

if x == 0:
    for k in table:
        for j in k.find_all("thead"):
            j.find_all("th")

            if "Handle" in j.text.split("\n"):
                for l in k.find_all("tr"):
                    sr_no = [i.text for i in l.select('td:nth-child(1)')]
                    code = [i.text for i in l.select('td:nth-child(2)')]
                    beneficiary = [i.text for i in l.select('td:nth-child(3)')]

                    df1 = pd.DataFrame(sr_no, columns=["Sr. No."])
                    df2 = pd.DataFrame(code, columns=["UPI Apps live on PPO"])
                    df3 = pd.DataFrame(beneficiary, columns=["Handle"])
                    final_df0 = pd.concat([df1, df2, df3], axis=1)
                    final_df0.to_excel("IPO_UPIApps.xlsx")

            if "Sponsor Banks live on IPO" in j.text.split("\n"):
                for m in k.find_all("tr"):
                    sr_no = [i.text for i in m.select('td:nth-child(1)')]
                    code = [i.text for i in m.select('td:nth-child(2)')]

                    df4 = pd.DataFrame(sr_no, columns=["Sr. No."])
                    df5 = pd.DataFrame(code, columns=["Sponsor Banks live on IPO"])

                    final_df1 = pd.concat([df4, df5], axis=1)
                    final_df1.to_excel("IPO_Sponsors.xlsx")

            if "SCSBs eligible to act as Issuer Bank (Customer Bank)" in j.text.split("\n"):
                for n in k.find_all("tr"):
                    sr_no = [i.text for i in n.select('td:nth-child(1)')]
                    code = [i.text for i in n.select('td:nth-child(2)')]

                    df6 = pd.DataFrame(sr_no, columns=["Sr. No."])
                    df7 = pd.DataFrame(code, columns=["SCSBs eligible to act as Issuer Bank (Customer Bank)"])

                    final_df2 = pd.concat([df6, df7], axis=1)
                    final_df2.to_excel("IPO_SCSB.xlsx")
