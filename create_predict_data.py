import pandas as pd


fundCode = '260108'
data = {
        'date': ['2019/5/25', '2019/5/26', '2019/5/27']
    }

def main(code = fundCode, data_array = data['date']):
    fundCode = code
    data['date'] = data_array

    data_pd = pd.DataFrame(data, index=range(3))
    data_pd['date'] = pd.to_datetime(data_pd['date'],infer_datetime_format=True)
    data_pd.to_csv('.\\data\\predict_%s.csv' % fundCode, index=False)
    print("成功创建预测集")

if __name__ == '__main__':
    main()