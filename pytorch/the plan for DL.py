#12.06-pytorch

'''
1.
ML:MATLAB / sk-learn
DL:pytorch / Tensorflow
RL:Gym

2.
pytorch:动态图，灵活性

3.计划
	1.最简模型
	2.后向传播
	3.卷积循环
	4.模型载存、Dataset、预处理
	5.hook
	6.可视化
	
4.包&外部工具
	1.torch:定义数据类型data type/tensor
	2.torch.nn:Module/loss
	3.torch.nn.function:activation
	4.torch.autograd:自动求导
	5.torch.optim:optimizer
	6.torch.utils.data:加载数据
	7.torch.nn.init:初始化
	8.(torch vision/torch text)
	9.numpy/pandas/sklearn/tensorboardx/(visdom)/matplotlib
	
5.最简模型
'''

import torch.nn as nn
import torch.nn.functional as F

class Net(nn.Module):
	def __init__(self):
		super(Net,self).__init__()
		self.conv = nn.Conv2d(1,6,5)
		self.conv = nn.Conv2d(6,16,5)
		self.fc1 = nn.Linear(120,84,,bias = True)# 输入120维，输出84维，对b学习
		self.fc2 = nn.Linear(84,10)
		
	def forward(self,x):
		
		pass
	
	#code
