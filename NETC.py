import requests
from bs4 import BeautifulSoup
import pandas as pd

q = 1
for q in range(1,6):
    if q == 1:

        url = "https://www.npci.org.in/what-we-do/netc-fastag/live-members/"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        sr_no = [i.text for i in soup.select('td:nth-child(1)')]
        name = [i.text for i in soup.select('td:nth-child(2)')]
        issuer = [i.text for i in soup.select('td:nth-child(3)')]
        acquirer = [i.text for i in soup.select('td:nth-child(4)')]

        df1 = pd.DataFrame(sr_no, columns=["Sr. No."])
        df2 = pd.DataFrame(name, columns=["Bank Name"])
        df3 = pd.DataFrame(issuer, columns=["Issuer"])
        df4 = pd.DataFrame(acquirer, columns=["Acquirer"])

        final_df = pd.concat([df1, df2, df3, df4], axis=1)
        final_df.to_excel("NETC_live.xlsx")
        q+=1

    elif q == 2:

        url = "https://www.npci.org.in/what-we-do/netc-fastag/steering-committee/"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        state = soup.find("table", class_="table table-bordered")

        sr_no = [i.text for i in soup.select('td:nth-child(1)')]
        code = [i.text for i in soup.select('td:nth-child(2)')]

        df1 = pd.DataFrame(sr_no, columns=["Sr. No."])
        df2 = pd.DataFrame(code, columns=["Bank Name"])

        final_df = pd.concat([df1, df2], axis=1)
        writer = pd.ExcelWriter('netc_steer.xlsx')
        final_df.to_excel(writer, sheet_name='Sheet1', startrow=1, header=False, index=False)

        workbook = writer.book
        worksheet = writer.sheets['Sheet1']

        worksheet.write(0, 0, 'NETC FASTag Steering Committee')

        writer._save()
        q+=1

    elif q == 3:

        url = "https://www.npci.org.in/what-we-do/netc-fastag/product-statistics"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        sr_no = [i.text for i in soup.select('td:nth-child(1)')]
        code = [i.text for i in soup.select('td:nth-child(2)')]
        beneficiary = [i.text for i in soup.select('td:nth-child(3)')]
        txn = [i.text for i in soup.select('td:nth-child(4)')]
        cbr = [i.text for i in soup.select('td:nth-child(5)')]


        df1 = pd.DataFrame(sr_no, columns=["Month"])
        df2 = pd.DataFrame(code, columns=["No. of Banks Live on NETC"])
        df3 = pd.DataFrame(beneficiary, columns=["Tag Issuance (In Nos.)"])
        df4 = pd.DataFrame(txn, columns=["Volume (In Mn)"])
        df5 = pd.DataFrame(cbr, columns=["Amount (In Cr)"])

        final_df2 = pd.concat([df1, df2, df3, df4, df5], axis=1)

        writer = pd.ExcelWriter('netc_ps.xlsx')
        final_df2.to_excel(writer, sheet_name='Sheet2', startrow=1, header=True, index=False)
        worksheet = writer.sheets['Sheet2']
        worksheet.write(0, 0, 'NETC FASTag Product Statistics')

        writer._save()
        q+=1

    elif q == 4:

        url = "https://www.npci.org.in/what-we-do/netc-fastag/netc-dispute-statistics"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        remit = soup.find_all("table", class_="table-bordered")

        a, b, c, d, e, f, m = ([] for i in range(7))

        for i in remit:
            month_temp = i.find_all("th", colspan="7")[0].text.split('(')[1].split(')')
            if len(i.find_all("th", colspan="7")) != 0:
                if 'Dispute Data' in i.find_all("th", colspan="7")[0].text.split(" (")[0]:
                    demit = i.find_all('tr')

                    for j in demit[1:]:
                        m.append(month_temp)
                        a.append(j.text.split('\n')[2])
                        b.append(j.text.split('\n')[3])
                        c.append(j.text.split('\n')[4])
                        d.append(j.text.split('\n')[5])
                        e.append(j.text.split('\n')[6])
                        f.append(j.text.split('\n')[7])



            else:
                pass
        data = pd.DataFrame({})
        data['Months'] = m
        data['Bank Name'] = a
        data['Total Volume (In Mn)'] = b
        data['NET Chargeback RATIO'] = c
        data['Chargeback Received'] = d
        data['Re-Presented'] = e
        data['Accepted/Deemed Accepted'] = f

        data.to_excel("Netc_disp.xlsx")
        q+=1

    elif q == 5:

        url = "https://www.npci.org.in/what-we-do/netc-fastag/netc-ecosystem-statistics"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        remit = pd.read_html(url)

        remit[1]['month']= ""
        column_name = remit[1].columns

        df = pd.DataFrame()
        for i in range(0, len(remit), 2):
            # print(i)
            month = remit[i].columns[1][0].split('(')[1]
            remit[i]['month'] = month
            remit[i].columns = range(remit[i].shape[1])

            # print(remit[i])

            df = pd.concat([df, pd.DataFrame(remit[i])], axis=0)
        df.columns = ["Index", "Issuer Bannk Name", "Total Volume(Mn)", "Approved(%)", "Denied Approved(%)", "Month"]
        # month = remit[2].columns[1][0].split('(')[1]
        dt = pd.DataFrame(remit[1])
        # remit[3]['month']= month

        df.to_excel("NETC - IssuerBanks.xlsx")

        remit[1]['month']= ""
        column_name = remit[1].columns

        df1 = pd.DataFrame()
        for i in range(1, len(remit)+1, 2):
            # print(i)
            month = remit[i].columns[1][0].split('(')[1].split(")")[0]
            remit[i]['month'] = month
            remit[i].columns = range(remit[i].shape[1])

            # print(remit[i])

            df1 = pd.concat([df1, pd.DataFrame(remit[i])], axis=0)
        df1.columns = ["Index", "Issuer Bannk Name", "Total Approved Volume(Mn)", "Approved(%)", "Denied BD(%)",
                      "Denied TD(%)","Month"]
        # month = remit[2].columns[1][0].split('(')[1]
        dt = pd.DataFrame(remit[1])
        # remit[3]['month']= month

        df1.to_excel("NETC - AcquirerBanks.xlsx")
        print("ALL FILES EXPORTED!")


