import requests
import pandas as pd
import re
import json
import math

fundCode = '260108'
pageIndex = 1
url = 'http://api.fund.eastmoney.com/f10/lsjz'
params = {
    'callback': 'jQuery18307633215694564663_1548321266367',
    'fundCode': fundCode,
    'pageIndex': pageIndex,
    'pageSize': 20,
}
headers = {
    'Referer': 'http://fundf10.eastmoney.com/jjjz_%s.html' % fundCode,
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
}


def reload_data(code):
    global fundCode, params, headers
    fundCode = code
    params['fundCode'] = fundCode
    headers['Referer'] = 'http://fundf10.eastmoney.com/jjjz_%s.html' % fundCode


def get_totalcount():
    r = requests.get(url=url, headers=headers, params=params)
    text = re.findall('\((.*?)\)', r.text)[0] # find the dict
    TotalCount = json.loads(text)['TotalCount'] # get the num of all the data
    return TotalCount


def data_get(pageIndex):
    params['pageIndex'] = pageIndex
    r = requests.get(url=url, headers=headers, params=params) # get the page you want
    text = re.findall('\((.*?)\)', r.text)[0]
    history_list = json.loads(text)['Data']['LSJZList'] #get the list in the response
    history_df = pd.DataFrame(history_list)  # change to dataframe
    # drop the data that we don't need
    history_df = history_df.drop(columns=["ACTUALSYI", 'DTYPE', 'FHFCBZ', 'FHFCZ', 'FHSP', 'NAVTYPE', 'SDATE', 'SGZT', 'SHZT'])
    return history_df


def main(code = fundCode):
    global fundCode
    if code != fundCode:
        reload_data(code) # reload the requests' data if run from the run_all.py
    total_pages = math.ceil(get_totalcount()/20) + 1
    data = pd.DataFrame()

    # download all the data with iterations
    for i in range(1,total_pages):
        print("catching page %d ..." % i)
        data_piece = data_get(i)
        data = pd.concat([data,data_piece])
    print(data)
    data.to_csv('.\\data\\data_for_%s.csv' % fundCode, index=False)


if __name__ == '__main__':
    main()
