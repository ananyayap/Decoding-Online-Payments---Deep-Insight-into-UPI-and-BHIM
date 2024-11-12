import requests
from bs4 import BeautifulSoup
import pandas as pd
correct = 0
site = ['product-statistics', 'upi-ecosystem-statistics', 'uptime-upi-month-wise', 'statistics', 'payee', 'uptime',
        'chargeback']

for correct in range(7):
    if site[correct] == 'product-statistics':
        url = "https://www.npci.org.in/what-we-do/upi/product-statistics"
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")

        state = soup.find("table", class_="table table-bordered")

        deflt = []
        for x in state.find_all('tbody'):
            data = x.find_all("tr")
            for t in data:
                deflt.append(t.text)

        month = [i.text for i in soup.select('td:nth-child(1)')]
        live_banks = [i.text for i in soup.select('td:nth-child(2)')]
        volume = [i.text for i in soup.select('td:nth-child(3)')]
        value = [i.text for i in soup.select('td:nth-child(4)')]

        df1 = pd.DataFrame(month, columns=["Month"])
        df2 = pd.DataFrame(live_banks, columns=["No. of Live Banks"])
        df3 = pd.DataFrame(volume, columns=["Volume"])
        df4 = pd.DataFrame(value, columns=["Value"])

        final_df = pd.concat([df1, df2, df3, df4], axis=1)
        final_df.to_excel("UPI_Product Statistics1.xlsx")
        correct+=1

    elif site[correct] == 'upi-ecosystem-statistics':
        url = "https://www.npci.org.in/what-we-do/upi/upi-ecosystem-statistics"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        remit = soup.find_all("table", class_="table-bordered")

        a, b, c, d, e, f, g, m = ([] for i in range(8))
        t, u, v, w, x, y, z = ([] for i in range(7))
        for i in remit:
            if len(i.find_all("th", colspan="8")) != 0:
                if 'UPI Remitter Banks' in i.find_all("th", colspan="8")[0].text:
                    demit = i.find_all('tr')
                    month_temp = i.find_all("th", colspan="8")[0].text.split('(')[1].split(')')[0]
                    for j in demit[2:]:
                        m.append(month_temp)
                        a.append(j.text.split('\n')[2])
                        b.append(j.text.split('\n')[3])
                        c.append(j.text.split('\n')[4])
                        d.append(j.text.split('\n')[5])
                        e.append(j.text.split('\n')[6])
                        f.append(j.text.split('\n')[7])
                        g.append(j.text.split('\n')[8])
                elif 'UPI Beneficiary Banks' in i.find_all("th", colspan="8")[0].text:
                    demit = i.find_all('tr')
                    month_temp = i.find_all("th", colspan="8")[0].text.split('(')[1].split(')')[0]
                    for j in demit[2:]:
                        z.append(month_temp)
                        t.append(j.text.split('\n')[2])
                        u.append(j.text.split('\n')[3])
                        v.append(j.text.split('\n')[4])
                        w.append(j.text.split('\n')[5])
                        x.append(j.text.split('\n')[6])
                        y.append(j.text.split('\n')[7])


            else:
                pass
        data = pd.DataFrame({})
        data['Month'] = m
        data['UPI Remitter Banks'] = a
        data['Total Volume (In Mn)'] = b
        data['Approved %'] = c
        data['BD %'] = d
        data['TD%'] = e
        data['Total Debit Reversal Count (In Mn)'] = f
        data['Debit Reversal Success %'] = g
        data1 = pd.DataFrame({})
        data1['Month'] = z
        data1['UPI Beneficiary Banks'] = t
        data1['Total Volume'] = u
        data1['Approved %'] = v
        data1['BD%'] = w
        data1['TD%'] = x
        data1['Deemed Approved %'] = y
        data.to_excel("UPI_remitter.xlsx")
        data1.to_excel("UPI_beneficiary.xlsx")

    elif site[correct] == 'uptime-upi-month-wise':
        url = "https://www.npci.org.in/what-we-do/upi/upi-ecosystem-statistics"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        remit = soup.find_all("table", class_="table-bordered")
        a, b, c, d, e, f, g, h, l, p, k, m = ([] for i in range(12))

        for i in remit:
            if len(i.find_all("th", colspan="12")) != 0:
                if 'UPI Apps' in i.find_all("th", colspan="12")[0].text:
                    demit = i.find_all('tr')
                    month_temp = i.find_all("th", colspan="12")[0].text.split('(')[1].split(')')[0]
                    for j in demit[2:]:
                        m.append(month_temp)
                        a.append(j.text.split('\n')[2])
                        b.append(j.text.split('\n')[3])
                        c.append(j.text.split('\n')[4])
                        d.append(j.text.split('\n')[5])
                        e.append(j.text.split('\n')[6])
                        f.append(j.text.split('\n')[7])
                        g.append(j.text.split('\n')[8])
                        h.append(j.text.split('\n')[9])
                        l.append(j.text.split('\n')[10])
                        p.append(j.text.split('\n')[11])


            else:
                pass
        data = pd.DataFrame({})
        data['Months'] = m
        data['Application Name'] = a
        data['CIT : Volume (Mn)'] = b
        data['CIT : Value (Cr)'] = c
        data['B2C : Volume (Mn)'] = d
        data['B2C : Value (Cr)'] = e
        data['B2B : Volume (Mn)'] = f
        data['B2B : Value (Cr)'] = g
        data['OT : Volume (Mn)'] = h
        data['OT : Value (Cr)'] = l
        data['Total : Volume (Mn)'] = p

        data.to_excel("UPI APPS.xlsx")
        correct += 1

    elif site[correct] == 'statistics':
        url = "https://www.npci.org.in/what-we-do/upi/upi-ecosystem-statistics"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

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
        data.to_excel("UPI_PSP Payer.xlsx")
        correct += 1

    elif site[correct] == 'payee':
        url = "https://www.npci.org.in/what-we-do/upi/upi-ecosystem-statistics"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        remit = soup.find_all("table", class_="table-bordered")

        a, b, c, d, e, m = ([] for i in range(6))

        for i in remit:
            if len(i.find_all("th", colspan="6")) != 0:
                if 'UPI Payee PSP Performance' in i.find_all("th", colspan="6")[0].text:
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
        data['Approved %'] = c
        data['BD %'] = d
        data['TD %'] = e

        # data['Total : Value (Cr)'] = k
        data.to_excel("UPI_PSP Payee.xlsx")
        correct += 1

    elif site[correct] == 'uptime':

        url = "https://www.npci.org.in/what-we-do/upi/uptime-upi-month-wise"
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")

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
        final_df.to_excel("UPI_Uptime.xlsx")
        correct += 1

    elif site[correct] == 'chargeback':
        url = "https://www.npci.org.in/what-we-do/upi/chargeback"
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")

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
        final_df.to_excel("UPI_Chargeback.xlsx")
        correct+=1

    else:
        print("All files exported to csv")

