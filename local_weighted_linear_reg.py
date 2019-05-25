import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import time


fundCode = '260108'


def load_data(name):
    data_train = pd.read_csv(name)
    return data_train


def get_weights_iteration(X, x_test, k=1.0):
    diff = X - x_test
    temp = np.zeros(diff.shape[0])

    for i in range(temp.shape[0]):
        temp[i] = diff[i].dot(diff[i])

    w = np.exp(-temp / (2 * k**2))
    return w


def run_steep_gradient_descent(X, y, alpha, theta, weights):
    prod = (np.dot(X, theta) - y) * weights
    sum_grad = np.dot(prod, X)
    theta = theta - (alpha / X.shape[0]) * sum_grad
    return theta


def sum_of_square_error(X, y, theta, weights):
    prod = (np.dot(X, theta) - y) * weights
    error = (np.square(prod)).mean()
    return error


def local_weighted_linear_reg(X, y, x_test, iterations = 70000, alpha = 0.000001):
    theta = np.zeros(X.shape[1])
    weights = get_weights_iteration(X, x_test, 1.0)

    start = time.time()
    for i in range(iterations):
        theta = run_steep_gradient_descent(X, y, alpha, theta, weights)
        # error = sum_of_square_error(X, y, theta, weights)
        # print('At Iteration %d - Error is %.5f ' % (i + 1, error))
    time_temp = time.time() - start
    print('本次所花时间：%f秒' % time_temp)

    return theta


def main(code = fundCode):
    fundCode = code
    train_path = '.\\data\\train_data_for_%s.csv' % fundCode
    predict_path = '.\\data\\predict_%s.csv' % fundCode

    data = load_data(train_path)
    data_predict = load_data(predict_path)
    x_label = np.array(data['date'].tolist() + data_predict['date'].tolist())

    x_label = pd.to_datetime(x_label, infer_datetime_format=True)
    data['date'] = pd.to_datetime(data['date'], infer_datetime_format=True)
    data_predict['date'] = pd.to_datetime(data_predict['date'], infer_datetime_format=True)

    X = np.array((data['date'] - data['date'].min()).dt.days + 1)
    y = np.array(data['y'])
    m = X.shape[0]
    ones = np.ones(m)
    X = np.vstack((X, ones)).T

    X_t = np.array((data_predict['date'] - data['date'].min()).dt.days + 1)
    m_t = X_t.shape[0]

    ones = np.ones(m_t)
    X_t = np.vstack((X_t, ones)).T

    result = np.zeros(m_t)
    for i in range(m_t):
        print('正在跑第%d个数据...' % (i + 1))
        theta = local_weighted_linear_reg(X, y, X_t[i])
        result[i] = X_t[i].dot(theta)

    data_predict['y'] = result
    data_predict.to_csv(predict_path, index=False)

    y_predict = np.zeros(m)
    for i in range(m):
        print('正在跑第%d个样本...' % (i + 1))
        theta = local_weighted_linear_reg(X, y, X[i])
        y_predict[i] = X[i].dot(theta)

    y_predict = np.array((y_predict.tolist() + result.tolist()))

    plt.figure(figsize=(18, 6))
    plt.xlabel("date")
    plt.ylabel('Net Asset Value')
    plt.plot(x_label, y_predict, c = 'b')
    plt.scatter(x_label[:m], y, c = 'r', marker='o')
    plt.savefig('.\\picture\\predict_%s' % fundCode)
    plt.show()


if __name__ == '__main__':
    main()