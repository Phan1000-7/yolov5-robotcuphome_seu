# yolov5目标检测说明文档

[TOC]

## 运行方法

- 运行命令为 `python detect.py` 

## 数据说明

- dataset：共有39294张训练照片，以10：1的比例分为训练集与测试集
- class：依据规则书，共19类物品

## divide.py

将dataset以10：1分为训练集及验证集，并以如下方式部署照片与标签。

![image-20220929135229193](C:\Users\Phantom\AppData\Roaming\Typora\typora-user-images\image-20220929135229193.png)

## 配置data.yaml

data.yaml作为train.py中使用的数据集配置文件，标注了将进行分类的19个class以及训练集和验证集的路径

![image-20220929135420945](C:\Users\Phantom\AppData\Roaming\Typora\typora-user-images\image-20220929135420945.png)



## train.py

训练过程即是使用train.py训练模型

我们训练过程中给予50个epoch，采用预配置yolov5s.pt权重文件来检测小物体，并配置批大小为4（个人pc训练显卡不支持更多）。为训练能够分时进行，我们将resume设为True使模型支持断点训练。

![image-20220929135737667](C:\Users\Phantom\AppData\Roaming\Typora\typora-user-images\image-20220929135737667.png)

![image-20220929135744547](C:\Users\Phantom\AppData\Roaming\Typora\typora-user-images\image-20220929135744547.png)

![image-20220929135752830](C:\Users\Phantom\AppData\Roaming\Typora\typora-user-images\image-20220929135752830.png)

![image-20220929135800517](C:\Users\Phantom\AppData\Roaming\Typora\typora-user-images\image-20220929135800517.png)

![image-20220929135806777](C:\Users\Phantom\AppData\Roaming\Typora\typora-user-images\image-20220929135806777.png)

最终模型参数保存为***best.pt***,所在目录为 ***runs/train/exp***



## detect.py

detect.py作为预测的文件，需要给与待预测目标的路径，反映在参数--**source**

中。 结果保存在 ***runs/detect/exp***

![image-20220929140229172](C:\Users\Phantom\AppData\Roaming\Typora\typora-user-images\image-20220929140229172.png)





