import catch_data
import data_prepare
import create_predict_data
import local_weighted_linear_reg


funCode = '270042'


if __name__ == '__main__':
    catch_data.main(funCode)
    data_prepare.main(funCode)
    # change the date you want to predict here
    create_predict_data.main(funCode, ['2019/5/28', '2019/5/29', '2019/5/30', '2019/5/31', '2019/6/1', '2019/6/2',
                                       '2019/6/3'])
    local_weighted_linear_reg.main(funCode)
