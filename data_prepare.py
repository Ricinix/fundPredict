import pandas as pd


fundCode = '260108'


def main(code = fundCode):
    fundCode = code
    path = '.\\data\\data_for_%s.csv' % fundCode

    pre_data = pd.read_csv(path)
    pre_data['date']= pre_data['FSRQ']
    pre_data['y'] = pre_data['DWJZ']
    pre_data = pre_data.drop(columns=['FSRQ', 'JZZZL', 'LJJZ', 'DWJZ'])
    # pre_data['date'] = pd.to_datetime(pre_data['date'], infer_datetime_format=True)
    # pre_data['date'] = (pre_data['date'] - pre_data['date'].min()).dt.days + 1
    pre_data.to_csv('.\\data\\train_data_for_%s.csv' % fundCode, index=False)

if __name__ == '__main__':
    main()