import requests
from bs4 import BeautifulSoup
import pandas as pd
z = 0
for z in range(0,4):
    if z == 0:
        url = "https://www.npci.org.in/what-we-do/aeps/live-members"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        state = soup.find("table", class_="table table-bordered")

        g = []


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
        bhp = [i.text for i in soup.select('td:nth-child(9)')]
        tok = [i.text for i in soup.select('td:nth-child(10)')]
        ass = [i.text for i in soup.select('td:nth-child(11)')]
        # head2 = [i.text for i in soup.select('h5:nth-child(1)')]
        for m in range(0,5):
            head = soup.find_all('h5', class_='mb-3 font-weight-bold')[m]
            g.append(head)

        df0 = pd.DataFrame(g,columns=["Type of Banks"])
        df1 = pd.DataFrame(sr_no, columns=["Sr. No."])
        df2 = pd.DataFrame(code, columns=["Bank Name"])
        df3 = pd.DataFrame(beneficiary, columns=["Non Financial Auth"])
        df4 = pd.DataFrame(txn, columns=["Non Financial Demo Auth"])
        df5 = pd.DataFrame(cbr, columns=["Non Financial eKYC"])
        df6 = pd.DataFrame(cb, columns=["ONUS"])
        df7 = pd.DataFrame(rep, columns=["Off Us - Acquirer"])
        df8 = pd.DataFrame(cba, columns=["Off Us - Issuer"])
        df9 = pd.DataFrame(bhp, columns=["BHIM Aadhar Pay"])
        df10 = pd.DataFrame(tok, columns=["Tokenization"])
        df11 = pd.DataFrame(ass, columns=["Aadhar Seeding Status"])

        final_df = pd.concat([df0, df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11], axis=1)

        final_df.to_csv("aepslm.csv")
        z += 1

        #----------------------------------------------------------------------------------
    elif z == 1:
        url = "https://www.npci.org.in/what-we-do/aeps/steering-committee"
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")

        state = soup.find("table", class_="table table-bordered")

        sr_no = [i.text for i in soup.select('td:nth-child(1)')]
        code = [i.text for i in soup.select('td:nth-child(2)')]
        head = soup.find('h5', class_='mb-3')

        df1 = pd.DataFrame(sr_no, columns=["Sr. No."])
        df2 = pd.DataFrame(code, columns=["Bank Name"])

        final_df = pd.concat([df1, df2], axis=1)
        writer = pd.ExcelWriter('output.xlsx')
        final_df.to_excel(writer, sheet_name='Sheet1', startrow=1, header=False, index=False)

        workbook = writer.book
        worksheet = writer.sheets['Sheet1']

        worksheet.write(0, 0, 'AePS Steering Committee Members')

        writer._save()
        z += 1

        #----------------------------------------------------------------------------------

    elif z == 2:

        # year = ['2023-24', '2022-23', '2021-22', '2020-21', '2019-20', '2018-19', '2017-18', '2016-17', '2015-16']

        url = "https://www.npci.org.in/what-we-do/aeps/product-statistics/2023-24"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        sr_no = [i.text for i in soup.select('td:nth-child(1)')]
        code = [i.text for i in soup.select('td:nth-child(2)')]
        beneficiary = [i.text for i in soup.select('td:nth-child(3)')]
        txn = [i.text for i in soup.select('td:nth-child(4)')]
        cbr = [i.text for i in soup.select('td:nth-child(5)')]
        cb = [i.text for i in soup.select('td:nth-child(6)')]
        rep = [i.text for i in soup.select('td:nth-child(7)')]
        cba = [i.text for i in soup.select('td:nth-child(8)')]
        bhp = [i.text for i in soup.select('td:nth-child(9)')]

        df1 = pd.DataFrame(sr_no, columns=["Month Wise"])
        df2 = pd.DataFrame(code, columns=["Total Approved Transaction(In Mn"])
        df3 = pd.DataFrame(beneficiary, columns=["Approved Offus Transaction(In Mn)"])
        df4 = pd.DataFrame(txn, columns=["Approved Offus Value(In Crores)"])
        df5 = pd.DataFrame(cbr, columns=["Approved BHIM Aadhaar Pay Transaction(In Mn)"])
        df6 = pd.DataFrame(cb, columns=["Approved BHIM Aadhaar Pay Value(In Crores)"])
        df7 = pd.DataFrame(rep, columns=["Approved Onus Transaction(In Mn)"])
        df8 = pd.DataFrame(cba, columns=["Successful eKYC(In Mn)"])
        df9 = pd.DataFrame(bhp, columns=["Approved Demo Auth - Authenticated(In Mn)"])

        final_df = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9], axis=1)

        # ------------------------------------------------------------------------------------------------------------------

        url = "https://www.npci.org.in/what-we-do/aeps/product-statistics/2022-23"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        sr_no = [i.text for i in soup.select('td:nth-child(1)')]
        code = [i.text for i in soup.select('td:nth-child(2)')]
        beneficiary = [i.text for i in soup.select('td:nth-child(3)')]
        txn = [i.text for i in soup.select('td:nth-child(4)')]
        cbr = [i.text for i in soup.select('td:nth-child(5)')]
        cb = [i.text for i in soup.select('td:nth-child(6)')]
        rep = [i.text for i in soup.select('td:nth-child(7)')]
        cba = [i.text for i in soup.select('td:nth-child(8)')]
        bhp = [i.text for i in soup.select('td:nth-child(9)')]

        df1 = pd.DataFrame(sr_no, columns=["Month Wise"])
        df2 = pd.DataFrame(code, columns=["Total Approved Transaction(In Mn"])
        df3 = pd.DataFrame(beneficiary, columns=["Approved Offus Transaction(In Mn)"])
        df4 = pd.DataFrame(txn, columns=["Approved Offus Value(In Crores)"])
        df5 = pd.DataFrame(cbr, columns=["Approved BHIM Aadhaar Pay Transaction(In Mn)"])
        df6 = pd.DataFrame(cb, columns=["Approved BHIM Aadhaar Pay Value(In Crores)"])
        df7 = pd.DataFrame(rep, columns=["Approved Onus Transaction(In Mn)"])
        df8 = pd.DataFrame(cba, columns=["Successful eKYC(In Mn)"])
        df9 = pd.DataFrame(bhp, columns=["Approved Demo Auth - Authenticated(In Mn)"])

        final_df2 = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9], axis=1)
        dfff = pd.concat([final_df, final_df2])

        writer2 = pd.ExcelWriter('aepspd.xlsx')
        dfff.to_excel(writer2, sheet_name='Sheet2', startrow=1, header=True, index=False)

        writer2._save()

        # ------------------------------------------------------------------------------------------------------------------

        url3 = "https://www.npci.org.in/what-we-do/aeps/product-statistics/2021-22"
        response3 = requests.get(url3)
        soup3 = BeautifulSoup(response3.text, "html.parser")


        sr_no = [i.text for i in soup3.select('td:nth-child(1)')]
        code = [i.text for i in soup3.select('td:nth-child(2)')]
        beneficiary = [i.text for i in soup3.select('td:nth-child(3)')]
        txn = [i.text for i in soup3.select('td:nth-child(4)')]
        cbr = [i.text for i in soup3.select('td:nth-child(5)')]
        cb = [i.text for i in soup3.select('td:nth-child(6)')]
        rep = [i.text for i in soup3.select('td:nth-child(7)')]
        cba = [i.text for i in soup3.select('td:nth-child(8)')]
        bhp = [i.text for i in soup3.select('td:nth-child(9)')]

        df1 = pd.DataFrame(sr_no, columns=["Month Wise"])
        df2 = pd.DataFrame(code, columns=["Total Approved Transaction(In Mn"])
        df3 = pd.DataFrame(beneficiary, columns=["Approved Offus Transaction(In Mn)"])
        df4 = pd.DataFrame(txn, columns=["Approved Offus Value(In Crores)"])
        df5 = pd.DataFrame(cbr, columns=["Approved BHIM Aadhaar Pay Transaction(In Mn)"])
        df6 = pd.DataFrame(cb, columns=["Approved BHIM Aadhaar Pay Value(In Crores)"])
        df7 = pd.DataFrame(rep, columns=["Approved Onus Transaction(In Mn)"])
        df8 = pd.DataFrame(cba, columns=["Successful eKYC(In Mn)"])
        df9 = pd.DataFrame(bhp, columns=["Approved Demo Auth - Authenticated(In Mn)"])

        final_df3 = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9], axis=1)

        # ------------------------------------------------------------------------------------------------------------------

        url = "https://www.npci.org.in/what-we-do/aeps/product-statistics/2020-21"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        sr_no = [i.text for i in soup.select('td:nth-child(1)')]
        code = [i.text for i in soup.select('td:nth-child(2)')]
        beneficiary = [i.text for i in soup.select('td:nth-child(3)')]
        txn = [i.text for i in soup.select('td:nth-child(4)')]
        cbr = [i.text for i in soup.select('td:nth-child(5)')]
        cb = [i.text for i in soup.select('td:nth-child(6)')]
        rep = [i.text for i in soup.select('td:nth-child(7)')]
        cba = [i.text for i in soup.select('td:nth-child(8)')]
        bhp = [i.text for i in soup.select('td:nth-child(9)')]

        df1 = pd.DataFrame(sr_no, columns=["Month Wise"])
        df2 = pd.DataFrame(code, columns=["Total Approved Transaction(In Mn"])
        df3 = pd.DataFrame(beneficiary, columns=["Approved Offus Transaction(In Mn)"])
        df4 = pd.DataFrame(txn, columns=["Approved Offus Value(In Crores)"])
        df5 = pd.DataFrame(cbr, columns=["Approved BHIM Aadhaar Pay Transaction(In Mn)"])
        df6 = pd.DataFrame(cb, columns=["Approved BHIM Aadhaar Pay Value(In Crores)"])
        df7 = pd.DataFrame(rep, columns=["Approved Onus Transaction(In Mn)"])
        df8 = pd.DataFrame(cba, columns=["Successful eKYC(In Mn)"])
        df9 = pd.DataFrame(bhp, columns=["Approved Demo Auth - Authenticated(In Mn)"])

        final_df4 = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9], axis=1)

        # ------------------------------------------------------------------------------------------------------------------

        url = "https://www.npci.org.in/what-we-do/aeps/product-statistics/2019-20"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        sr_no = [i.text for i in soup.select('td:nth-child(1)')]
        code = [i.text for i in soup.select('td:nth-child(2)')]
        beneficiary = [i.text for i in soup.select('td:nth-child(3)')]
        txn = [i.text for i in soup.select('td:nth-child(4)')]
        cbr = [i.text for i in soup.select('td:nth-child(5)')]
        cb = [i.text for i in soup.select('td:nth-child(6)')]
        rep = [i.text for i in soup.select('td:nth-child(7)')]
        cba = [i.text for i in soup.select('td:nth-child(8)')]
        bhp = [i.text for i in soup.select('td:nth-child(9)')]

        df1 = pd.DataFrame(sr_no, columns=["Month Wise"])
        df2 = pd.DataFrame(code, columns=["Total Approved Transaction(In Mn"])
        df3 = pd.DataFrame(beneficiary, columns=["Approved Offus Transaction(In Mn)"])
        df4 = pd.DataFrame(txn, columns=["Approved Offus Value(In Crores)"])
        df5 = pd.DataFrame(cbr, columns=["Approved BHIM Aadhaar Pay Transaction(In Mn)"])
        df6 = pd.DataFrame(cb, columns=["Approved BHIM Aadhaar Pay Value(In Crores)"])
        df7 = pd.DataFrame(rep, columns=["Approved Onus Transaction(In Mn)"])
        df8 = pd.DataFrame(cba, columns=["Successful eKYC(In Mn)"])
        df9 = pd.DataFrame(bhp, columns=["Approved Demo Auth - Authenticated(In Mn)"])

        final_df5 = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9], axis=1)

        # ------------------------------------------------------------------------------------------------------------------

        url = "https://www.npci.org.in/what-we-do/aeps/product-statistics/2018-19"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        sr_no = [i.text for i in soup.select('td:nth-child(1)')]
        code = [i.text for i in soup.select('td:nth-child(2)')]
        beneficiary = [i.text for i in soup.select('td:nth-child(3)')]
        txn = [i.text for i in soup.select('td:nth-child(4)')]
        cbr = [i.text for i in soup.select('td:nth-child(5)')]
        cb = [i.text for i in soup.select('td:nth-child(6)')]
        rep = [i.text for i in soup.select('td:nth-child(7)')]
        cba = [i.text for i in soup.select('td:nth-child(8)')]
        bhp = [i.text for i in soup.select('td:nth-child(9)')]

        df1 = pd.DataFrame(sr_no, columns=["Month Wise"])
        df2 = pd.DataFrame(code, columns=["Total Approved Transaction(In Mn"])
        df3 = pd.DataFrame(beneficiary, columns=["Approved Offus Transaction(In Mn)"])
        df4 = pd.DataFrame(txn, columns=["Approved Offus Value(In Crores)"])
        df5 = pd.DataFrame(cbr, columns=["Approved BHIM Aadhaar Pay Transaction(In Mn)"])
        df6 = pd.DataFrame(cb, columns=["Approved BHIM Aadhaar Pay Value(In Crores)"])
        df7 = pd.DataFrame(rep, columns=["Approved Onus Transaction(In Mn)"])
        df8 = pd.DataFrame(cba, columns=["Successful eKYC(In Mn)"])
        df9 = pd.DataFrame(bhp, columns=["Approved Demo Auth - Authenticated(In Mn)"])

        final_df6 = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9], axis=1)

        # ------------------------------------------------------------------------------------------------------------------

        url = "https://www.npci.org.in/what-we-do/aeps/product-statistics/2027-18"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        sr_no = [i.text for i in soup.select('td:nth-child(1)')]
        code = [i.text for i in soup.select('td:nth-child(2)')]
        beneficiary = [i.text for i in soup.select('td:nth-child(3)')]
        txn = [i.text for i in soup.select('td:nth-child(4)')]
        cbr = [i.text for i in soup.select('td:nth-child(5)')]
        cb = [i.text for i in soup.select('td:nth-child(6)')]
        rep = [i.text for i in soup.select('td:nth-child(7)')]
        cba = [i.text for i in soup.select('td:nth-child(8)')]
        bhp = [i.text for i in soup.select('td:nth-child(9)')]

        df1 = pd.DataFrame(sr_no, columns=["Month Wise"])
        df2 = pd.DataFrame(code, columns=["Total Approved Transaction(In Mn"])
        df3 = pd.DataFrame(beneficiary, columns=["Approved Offus Transaction(In Mn)"])
        df4 = pd.DataFrame(txn, columns=["Approved Offus Value(In Crores)"])
        df5 = pd.DataFrame(cbr, columns=["Approved BHIM Aadhaar Pay Transaction(In Mn)"])
        df6 = pd.DataFrame(cb, columns=["Approved BHIM Aadhaar Pay Value(In Crores)"])
        df7 = pd.DataFrame(rep, columns=["Approved Onus Transaction(In Mn)"])
        df8 = pd.DataFrame(cba, columns=["Successful eKYC(In Mn)"])
        df9 = pd.DataFrame(bhp, columns=["Approved Demo Auth - Authenticated(In Mn)"])

        final_df7 = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9], axis=1)

        # ------------------------------------------------------------------------------------------------------------------

        url = "https://www.npci.org.in/what-we-do/aeps/product-statistics/2016-17"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        sr_no = [i.text for i in soup.select('td:nth-child(1)')]
        code = [i.text for i in soup.select('td:nth-child(2)')]
        beneficiary = [i.text for i in soup.select('td:nth-child(3)')]
        txn = [i.text for i in soup.select('td:nth-child(4)')]
        cbr = [i.text for i in soup.select('td:nth-child(5)')]
        cb = [i.text for i in soup.select('td:nth-child(6)')]
        rep = [i.text for i in soup.select('td:nth-child(7)')]
        cba = [i.text for i in soup.select('td:nth-child(8)')]
        bhp = [i.text for i in soup.select('td:nth-child(9)')]

        df1 = pd.DataFrame(sr_no, columns=["Month Wise"])
        df2 = pd.DataFrame(code, columns=["Total Approved Transaction(In Mn"])
        df3 = pd.DataFrame(beneficiary, columns=["Approved Offus Transaction(In Mn)"])
        df4 = pd.DataFrame(txn, columns=["Approved Offus Value(In Crores)"])
        df5 = pd.DataFrame(cbr, columns=["Approved BHIM Aadhaar Pay Transaction(In Mn)"])
        df6 = pd.DataFrame(cb, columns=["Approved BHIM Aadhaar Pay Value(In Crores)"])
        df7 = pd.DataFrame(rep, columns=["Approved Onus Transaction(In Mn)"])
        df8 = pd.DataFrame(cba, columns=["Successful eKYC(In Mn)"])
        df9 = pd.DataFrame(bhp, columns=["Approved Demo Auth - Authenticated(In Mn)"])

        final_df8 = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9], axis=1)

        # ------------------------------------------------------------------------------------------------------------------

        url = "https://www.npci.org.in/what-we-do/aeps/product-statistics/2015-16"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        sr_no = [i.text for i in soup.select('td:nth-child(1)')]
        code = [i.text for i in soup.select('td:nth-child(2)')]
        beneficiary = [i.text for i in soup.select('td:nth-child(3)')]
        txn = [i.text for i in soup.select('td:nth-child(4)')]
        cbr = [i.text for i in soup.select('td:nth-child(5)')]
        cb = [i.text for i in soup.select('td:nth-child(6)')]
        rep = [i.text for i in soup.select('td:nth-child(7)')]
        cba = [i.text for i in soup.select('td:nth-child(8)')]
        bhp = [i.text for i in soup.select('td:nth-child(9)')]

        df1 = pd.DataFrame(sr_no, columns=["Month Wise"])
        df2 = pd.DataFrame(code, columns=["Total Approved Transaction(In Mn"])
        df3 = pd.DataFrame(beneficiary, columns=["Approved Offus Transaction(In Mn)"])
        df4 = pd.DataFrame(txn, columns=["Approved Offus Value(In Crores)"])
        df5 = pd.DataFrame(cbr, columns=["Approved BHIM Aadhaar Pay Transaction(In Mn)"])
        df6 = pd.DataFrame(cb, columns=["Approved BHIM Aadhaar Pay Value(In Crores)"])
        df7 = pd.DataFrame(rep, columns=["Approved Onus Transaction(In Mn)"])
        df8 = pd.DataFrame(cba, columns=["Successful eKYC(In Mn)"])
        df9 = pd.DataFrame(bhp, columns=["Approved Demo Auth - Authenticated(In Mn)"])

        final_df9 = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9], axis=1)

        merger = pd.concat(
            [final_df, final_df2, final_df3, final_df4, final_df5, final_df6, final_df7, final_df8, final_df9])
        writer = pd.ExcelWriter('aepspd.xlsx')
        merger.to_excel(writer, sheet_name='Sheet1', startrow=1, header=True, index=False)

        workbook = writer.book
        worksheet = writer.sheets['Sheet1']

        worksheet.write(0, 0, 'AePS Statistics 2016 - 2023')

        writer._save()

        z += 1


        # ----------------------------------------------------------------------------------------
    elif z == 3:

        url = "https://www.npci.org.in/what-we-do/aeps/chargeback"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        ls = []
        ff = []
        state = soup.find("table", class_="table table-bordered")
        dropdown = soup.select('select')[0]  # Assuming there's only one dropdown on the page
        options = dropdown.find_all('option')

        for option in options:
            ls.append(option.text)
        ls.reverse()

        sr_no = [i.text for i in soup.select('td:nth-child(1)')]
        code = [i.text for i in soup.select('td:nth-child(2)')]
        beneficiary = [i.text for i in soup.select('td:nth-child(3)')]
        txn = [i.text for i in soup.select('td:nth-child(4)')]
        cbr = [i.text for i in soup.select('td:nth-child(5)')]
        cb = [i.text for i in soup.select('td:nth-child(6)')]
        rep = [i.text for i in soup.select('td:nth-child(7)')]

        df1 = pd.DataFrame(sr_no, columns=["Bank Code"])
        df2 = pd.DataFrame(code, columns=["Bank Name"])
        df3 = pd.DataFrame(beneficiary, columns=["CB Accepted + Deemed Accepted"])
        df4 = pd.DataFrame(txn, columns=["Represented"])
        df5 = pd.DataFrame(cbr, columns=["CB Raised"])
        df6 = pd.DataFrame(cb, columns=["Net CB %"])
        df7 = pd.DataFrame(rep, columns=["Total Volume"])
        final_df = pd.concat([df1, df2, df3, df4, df5, df6, df7], axis=1)

        df0 = pd.DataFrame(ls, columns=["Months"])

        final_df2 = pd.concat([df0, final_df], axis=1)

        final_df2.to_csv("AePS_Chargeback.csv")

        print("All Files Exported!")


