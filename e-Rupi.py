import requests
from bs4 import BeautifulSoup
import pandas as pd
i = 0
for i in range(2):
    if i == 0:

        url = "https://www.npci.org.in/what-we-do/e-rupi/e-rupi-live-partners"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        state = soup.find("table", class_="table table-bordered")

        sr_no = [i.text for i in state.select('td:nth-child(1)')]
        code = [i.text for i in state.select('td:nth-child(2)')]
        beneficiary = [i.text for i in state.select('td:nth-child(3)')]
        txn = [i.text for i in state.select('td:nth-child(4)')]
        cbr = [i.text for i in state.select('td:nth-child(5)')]

        df1 = pd.DataFrame(sr_no, columns=["Sr. No."])
        df2 = pd.DataFrame(code, columns=["Bank Name"])
        df3 = pd.DataFrame(beneficiary, columns=["Issuer)"])
        df4 = pd.DataFrame(txn, columns=["Acquirer"])
        df5 = pd.DataFrame(cbr, columns=["Acquiring App/Entity"])

        final_df = pd.concat([df1, df2, df3, df4, df5], axis=1)
        final_df.to_excel("erupi_live.xlsx")
        i+=1

    elif i ==1:

        url = "https://www.npci.org.in/what-we-do/e-rupi/product-statistics"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        table = soup.find_all("table", class_="table-bordered")
        dropdown = soup.select('select')[0]  # Assuming there's only one dropdown on the page
        options = dropdown.find_all('option')
        df, a, b, c, d = ([] for l in range(5))
        for option in options:
            df.append([option.text])
        for i in table:
            row = i.find_all("tr")

            for j in row:
                a.append(j.text.split('\n')[2])
                b.append(j.text.split('\n')[3])
                c.append(j.text.split('\n')[4])

        data = pd.DataFrame({})

        data['Use Case Name'] = a
        data['Voucher Created Volume'] = b
        data['Voucher Redeemed Volume'] = c

        data.to_excel("rupistat.xlsx")
        print("All Files Exported!")


