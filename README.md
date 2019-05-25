# fundPredict
可根据基金代码爬取基金历史数据再通过局部线性回归进行简单预测

Predict the fund with local weighted linear regression

* download the history data with **fundCode** automatically
* predict the trendency for the fund
* use **matplotlib** for drawing the picture 



**cauction**

​	The project will predict the future and write it into the predict_xxxxxx.csv fisrt.

​	After finishing the predicting job, it will handle the history data for drawing the picture. If you don't care about the picture, just stop the program and open the predict_xxxxxx.csv.



**注意**

​	该项目会优先预测未来的结果，并且写入到 predict_xxxxxx.csv 中。

​	预测完后，会跑一遍过去的历史数据来画出拟合曲线。如果你不在乎数据可视化，可以在预测完成后终止程序，然后打开 predict_xxxxxx.csv 直接看结果



新手项目，欢迎批评和建议。