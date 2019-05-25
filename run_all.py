import catch_data
import data_prepare
import create_predict_data
import local_weighted_linear_reg


funCode = '260108'


if __name__ == '__main__':
    catch_data.main(funCode)
    data_prepare.main(funCode)
    create_predict_data.main(funCode, ['2019/5/25', '2019/5/26', '2019/5/27'])
    local_weighted_linear_reg.main(funCode)
