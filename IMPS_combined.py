import requests
from bs4 import BeautifulSoup
import pandas as pd

correct = 0

site = ['product-statistics', 'imps-bank-performance', 'live-members','steering-committee', 'imps-uptime','chargeback']


if site[correct] == 'product-statistics':
    url = "https://www.npci.org.in/what-we-do/imps/"+str(site[correct])
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    print(url)
    state = soup.find("table", class_="table table-bordered")

    month = [i.text for i in soup.select('td:nth-child(1)')]
    live_banks = [i.text for i in soup.select('td:nth-child(2)')]
    volume = [i.text for i in soup.select('td:nth-child(3)')]
    value = [i.text for i in soup.select('td:nth-child(4)')]

    df1 = pd.DataFrame(month, columns=["Month"])
    df2 = pd.DataFrame(live_banks, columns=["No. of Member Banks"])
    df3 = pd.DataFrame(volume, columns=["No. of Transactions (in Mn"])
    df4 = pd.DataFrame(value, columns=["Amount (in Cr"])

    final_df = pd.concat([df1, df2, df3, df4], axis=1)
    final_df.to_excel("IMPS_Product Statistics1.xlsx")
    correct+=1

if site[correct] == 'imps-bank-performance':
    url = "https://www.npci.org.in/what-we-do/imps/"+str(site[correct])
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    print(url)
    remit = soup.find_all("table", class_="table-bordered")

    a, b, c, d, e, f, m = ([] for i in range(7))

    for i in remit:
        demit = i.find_all('tr')
        for j in demit[2:]:

            a.append(j.text.split('\n')[2])
            b.append(j.text.split('\n')[3])
            c.append(j.text.split('\n')[4])
            d.append(j.text.split('\n')[5])
            e.append(j.text.split('\n')[6])
            f.append(j.text.split('\n')[7])
        else:
            pass
    data = pd.DataFrame({})

    data['IMPS Beneficiary Banks'] = a
    data['Total Volume (In Mn)'] = b
    data['Approved %'] = c
    data['BD %'] = d
    data['TD%'] = e
    data['Deemed Approved'] = f

    data.to_excel("IMPS_remitter.xlsx")
    correct+=1
if site[correct] == 'live-members':
    url = "https://www.npci.org.in/what-we-do/imps/"+str(site[correct])
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    state = soup.find("table", class_="table table-bordered")
    print(url)
    deflt = []
    for x in state.find_all('tbody'):
        data = x.find_all("tr")
        for t in data:
            deflt.append(t.text)

    sr_no = [i.text for i in soup.select('td:nth-child(1)')]
    code = [i.text for i in soup.select('td:nth-child(2)')]
    beneficiary = [i.text for i in soup.select('td:nth-child(3)')]
    txn = [i.text for i in soup.select('td:nth-child(4)')]
    cbr = [i.text for i in soup.select('td:nth-child(5)')]
    cb = [i.text for i in soup.select('td:nth-child(6)')]
    rep = [i.text for i in soup.select('td:nth-child(7)')]
    cba = [i.text for i in soup.select('td:nth-child(8)')]

    df1 = pd.DataFrame(sr_no, columns=["Sr. No."])
    df2 = pd.DataFrame(code, columns=["Bank Name"])
    df3 = pd.DataFrame(beneficiary, columns=["Using Mobile No. & MMID (P2P)"])
    df4 = pd.DataFrame(txn, columns=["Using Account No. & IFS Code (P2A)"])
    df5 = pd.DataFrame(cbr, columns=["Internet"])
    df6 = pd.DataFrame(cb, columns=["Branch"])
    df7 = pd.DataFrame(rep, columns=["Mobile"])
    df8 = pd.DataFrame(cba, columns=["ATM"])
    final_df = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8], axis=1)
    final_df.to_excel("imps_live.xlsx")
    correct+=1

if site[correct] == 'steering-committee':
    url = "https://www.npci.org.in/what-we-do/imps/"+str(site[correct])
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    print(url)
    remit = soup.find_all("table", class_="table-bordered")

    a, b, c, d, e, m = ([] for i in range(6))

    for i in remit:
        if len(i.find_all("th", colspan="6")) != 0:
            if 'UPI Payer PSP Performance' in i.find_all("th", colspan="6")[0].text:
                demit = i.find_all('tr')
                month_temp = i.find_all("th", colspan="6")[0].text.split('(')[1].split(')')[0]
                for j in demit[2:]:
                    m.append(month_temp)
                    a.append(j.text.split('\n')[2])
                    b.append(j.text.split('\n')[3])
                    c.append(j.text.split('\n')[4])
                    d.append(j.text.split('\n')[5])
                    e.append(j.text.split('\n')[6])


        else:
            pass
    data = pd.DataFrame({})
    data['Months'] = m
    data['Payer PSP'] = a
    data['Total Volume (In Mn)'] = b
    data['	Approved %'] = c
    data['BD %'] = d
    data['TD %'] = e

    # data['Total : Value (Cr)'] = k
    data.to_excel("IMPS_PSP Payer.xlsx")
    correct += 1

if site[correct] == 'imps-uptime':

    url = "https://www.npci.org.in/what-we-do/imps/"+str(site[correct])
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    print(url)
    state = soup.find("table", class_="table table-bordered")

    deflt = []
    for x in state.find_all('tbody'):
        data = x.find_all("tr")
        for t in data:
            deflt.append(t.text)

    month = [i.text for i in soup.select('td:nth-child(1)')]
    uptime = [i.text for i in soup.select('td:nth-child(2)')]

    df1 = pd.DataFrame(month, columns=["Month"])
    df2 = pd.DataFrame(uptime, columns=["NPCI Uptime for UPI"])

    final_df = pd.concat([df1, df2], axis=1)
    final_df.to_excel("IMPS_Uptime.xlsx")
    correct += 1

if site[correct] == 'chargeback':
    url = "https://www.npci.org.in/what-we-do/imps/"+str(site[correct])
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    print(url)
    state = soup.find("table", class_="table table-bordered")

    deflt = []
    for x in state.find_all('tbody'):
        data = x.find_all("tr")
        for t in data:
            deflt.append(t.text)

    sr_no = [i.text for i in soup.select('td:nth-child(1)')]
    code = [i.text for i in soup.select('td:nth-child(2)')]
    beneficiary = [i.text for i in soup.select('td:nth-child(3)')]
    txn = [i.text for i in soup.select('td:nth-child(4)')]
    cbr = [i.text for i in soup.select('td:nth-child(5)')]
    cb = [i.text for i in soup.select('td:nth-child(6)')]
    rep = [i.text for i in soup.select('td:nth-child(7)')]
    cba = [i.text for i in soup.select('td:nth-child(8)')]

    df1 = pd.DataFrame(sr_no, columns=["Sr. No."])
    df2 = pd.DataFrame(code, columns=["Code"])
    df3 = pd.DataFrame(beneficiary, columns=["Beneficiary Bank"])
    df4 = pd.DataFrame(txn, columns=["Total Txn during month"])
    df5 = pd.DataFrame(cbr, columns=["CB Ratio"])
    df6 = pd.DataFrame(cb, columns=["Chargeback Received during month"])
    df7 = pd.DataFrame(rep, columns=["Representment raised during month"])
    df8 = pd.DataFrame(cba, columns=["Chargeback Accepted during month"])
    final_df = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8], axis=1)
    final_df.to_excel("IMPS_Chargeback.xlsx")
    correct+=1


