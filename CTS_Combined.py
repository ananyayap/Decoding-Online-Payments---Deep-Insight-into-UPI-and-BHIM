import time

import requests
from bs4 import BeautifulSoup
import pandas as pd

q = 0
for q in range(0, 4):
    if q == 0:

        grid = ["southern-grid", "western-grid", "northern-grid"]
        years = ['2023-24', '2022-23', '2021-22', '2020-21', '2019-20', '2018-19', '2017-18', '2016-17', '2015-16',
                 '2014-15', '2013-14', '2012-13']
        data = pd.DataFrame()

        for x in range(3):
            if grid[x] == "southern-grid":
                for y in years:
                    url = "https://www.npci.org.in/what-we-do/cts/product-statistics/southern-grid/" + str(y)
                    # print(y)
                    response = requests.get(url)
                    soup = BeautifulSoup(response.text, "html.parser")

                    month = [i.text for i in soup.select('td:nth-child(1)')]
                    cheque_vol = [i.text for i in soup.select('td:nth-child(2)')]

                    cheque_val = [i.text for i in soup.select('td:nth-child(3)')]
                    return_cheque_vol = [i.text for i in soup.select('td:nth-child(4)')]
                    return_cheque_val = [i.text for i in soup.select('td:nth-child(5)')]
                    return_cheque_perc = [i.text for i in soup.select('td:nth-child(6)')]

                    df1 = pd.DataFrame(month, columns=["Month"])
                    df2 = pd.DataFrame(cheque_vol, columns=["Presentment Cheque Volume(in Lakhs)"])
                    df3 = pd.DataFrame(cheque_val, columns=["Presentment Cheque Value(INR Lakhs)"])
                    df4 = pd.DataFrame(return_cheque_vol, columns=["Return Cheque Volume(in Lakhs) "])
                    df5 = pd.DataFrame(return_cheque_val, columns=["Return Cheque Value(INR Lakhs)"])
                    df6 = pd.DataFrame(return_cheque_perc,
                                       columns=["Return Cheques as % of Total Presentment Cheque Volume"])

                    final_df = pd.concat([df1, df2, df3, df4, df5, df6], axis=1)
                    time.sleep(1)
                    data = pd.concat([final_df, data])
                    data.to_excel("CTS_Southern.xlsx")

                    x += 1

            elif grid[x] == "western-grid":
                for y in years:
                    url = "https://www.npci.org.in/what-we-do/cts/product-statistics/southern-grid/" + str(y)
                    # print(y)
                    response = requests.get(url)
                    soup = BeautifulSoup(response.text, "html.parser")

                    month = [i.text for i in soup.select('td:nth-child(1)')]
                    cheque_vol = [i.text for i in soup.select('td:nth-child(2)')]

                    cheque_val = [i.text for i in soup.select('td:nth-child(3)')]
                    return_cheque_vol = [i.text for i in soup.select('td:nth-child(4)')]
                    return_cheque_val = [i.text for i in soup.select('td:nth-child(5)')]
                    return_cheque_perc = [i.text for i in soup.select('td:nth-child(6)')]

                    df1 = pd.DataFrame(month, columns=["Month"])
                    df2 = pd.DataFrame(cheque_vol, columns=["Presentment Cheque Volume(in Lakhs)"])
                    df3 = pd.DataFrame(cheque_val, columns=["Presentment Cheque Value(INR Lakhs)"])
                    df4 = pd.DataFrame(return_cheque_vol, columns=["Return Cheque Volume(in Lakhs) "])
                    df5 = pd.DataFrame(return_cheque_val, columns=["Return Cheque Value(INR Lakhs)"])
                    df6 = pd.DataFrame(return_cheque_perc,
                                       columns=["Return Cheques as % of Total Presentment Cheque Volume"])

                    final_df = pd.concat([df1, df2, df3, df4, df5, df6], axis=1)
                    time.sleep(1)
                    data = pd.concat([final_df, data])
                    data.to_excel("CTS_Western.xlsx")

                    x += 1

            elif grid[x] == "northern-grid":
                for y in years:
                    url = "https://www.npci.org.in/what-we-do/cts/product-statistics/southern-grid/" + str(y)
                    # print(y)
                    response = requests.get(url)
                    soup = BeautifulSoup(response.text, "html.parser")

                    month = [i.text for i in soup.select('td:nth-child(1)')]
                    cheque_vol = [i.text for i in soup.select('td:nth-child(2)')]

                    cheque_val = [i.text for i in soup.select('td:nth-child(3)')]
                    return_cheque_vol = [i.text for i in soup.select('td:nth-child(4)')]
                    return_cheque_val = [i.text for i in soup.select('td:nth-child(5)')]
                    return_cheque_perc = [i.text for i in soup.select('td:nth-child(6)')]

                    df1 = pd.DataFrame(month, columns=["Month"])
                    df2 = pd.DataFrame(cheque_vol, columns=["Presentment Cheque Volume(in Lakhs)"])
                    df3 = pd.DataFrame(cheque_val, columns=["Presentment Cheque Value(INR Lakhs)"])
                    df4 = pd.DataFrame(return_cheque_vol, columns=["Return Cheque Volume(in Lakhs) "])
                    df5 = pd.DataFrame(return_cheque_val, columns=["Return Cheque Value(INR Lakhs)"])
                    df6 = pd.DataFrame(return_cheque_perc,
                                       columns=["Return Cheques as % of Total Presentment Cheque Volume"])

                    final_df = pd.concat([df1, df2, df3, df4, df5, df6], axis=1)
                    time.sleep(1)
                    data = pd.concat([final_df, data])
                    data.to_excel("CTS_Northern.xlsx")
                    q+=1

    elif q == 1:
        url = "https://www.npci.org.in/what-we-do/cts/steering-committee"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        org = [i.text for i in soup.select('td:nth-child(2)')][1:8]
        org2 = [i.text for i in soup.select('td:nth-child(2)')][9:15]
        org3 = [i.text for i in soup.select('td:nth-child(3)')][2:3]
        org4 = [i.text for i in soup.select('td:nth-child(3)')][3:]

        org5 = [i.text for i in soup.select('td:nth-child(3)')][0:1] + org
        org6 = [i.text for i in soup.select('td:nth-child(3)')][1:2] + org2

        df3 = pd.DataFrame(org3, columns=['Co-Op'])
        df4 = pd.DataFrame(org4, columns=["Industry Body"])
        df5 = pd.DataFrame(org5, columns=["Public Organizations"])
        df6 = pd.DataFrame(org6, columns=['Private Organizations'])

        final_df = pd.concat([df5, df6, df3, df4], axis=1)

        final_df.to_excel("cts_steer.xlsx")
        q+=1

    elif q == 2:
        grid = ["southern-grid", "western-grid", "northern-grid"]
        for t in range(3):
            if t == 0:
                url = "https://www.npci.org.in/what-we-do/cts/live-members/" + str(grid[t])
                response = requests.get(url)
                soup = BeautifulSoup(response.text, "html.parser")

                sr_no = [i.text for i in soup.select('td:nth-child(1)')]
                name = [i.text for i in soup.select('td:nth-child(2)')]
                routing = [i.text for i in soup.select('td:nth-child(3)')]
                df1 = pd.DataFrame(sr_no, columns=["Sr. No."])
                df2 = pd.DataFrame(name, columns=["Bank Name"])
                df3 = pd.DataFrame(routing, columns=["Routing Number"])

                final_df = pd.concat([df1, df2, df3], axis=1)
                final_df.to_excel("CTS_LM_Southern.xlsx")
                t += 1
            elif t == 1:
                url = "https://www.npci.org.in/what-we-do/cts/live-members/" + str(grid[t])
                response = requests.get(url)
                soup = BeautifulSoup(response.text, "html.parser")

                sr_no = [i.text for i in soup.select('td:nth-child(1)')]
                name = [i.text for i in soup.select('td:nth-child(2)')]
                routing = [i.text for i in soup.select('td:nth-child(3)')]
                df1 = pd.DataFrame(sr_no, columns=["Sr. No."])
                df2 = pd.DataFrame(name, columns=["Bank Name"])
                df3 = pd.DataFrame(routing, columns=["Routing Number"])

                final_df = pd.concat([df1, df2, df3], axis=1)
                final_df.to_excel("CTS_LM_Western.xlsx")
                t += 1
            elif t == 2:
                url = "https://www.npci.org.in/what-we-do/cts/live-members/" + str(grid[t])
                response = requests.get(url)
                soup = BeautifulSoup(response.text, "html.parser")

                sr_no = [i.text for i in soup.select('td:nth-child(1)')]
                name = [i.text for i in soup.select('td:nth-child(2)')]
                routing = [i.text for i in soup.select('td:nth-child(3)')]
                df1 = pd.DataFrame(sr_no, columns=["Sr. No."])
                df2 = pd.DataFrame(name, columns=["Bank Name"])
                df3 = pd.DataFrame(routing, columns=["Routing Number"])

                final_df = pd.concat([df1, df2, df3], axis=1)
                final_df.to_excel("CTS_LM_Northern.xlsx")
                q+=1

    elif q == 3:
        url = "https://www.npci.org.in/what-we-do/cts/p2f-exempted-states"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        remit = pd.read_html(url, index_col="Sr.No.")

        df = pd.DataFrame()
        for i in range(0, len(remit)):
            df = pd.concat([df, pd.DataFrame(remit[i])])
            df.columns = ["State Name", "Grid"]

        df.to_excel("p2fex.xlsx")
        print("All Files Exported!")

