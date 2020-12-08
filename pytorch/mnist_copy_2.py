import torch
from torchvision import transforms
from torchvision import datasets
from torch.utils.data import DataLoader
import torch.nn.functional as  F
import torch.optim as optim
import os
import sys
  
batch_size = 64
transform = transforms.Compose(
    [
        transforms.ToTensor(),     #将0-255变成0-1
        transforms.Normalize((0.1307,),(0.3081,)) #正则化
    ]
)
train_dataset =datasets.MNIST(root='../dataset/mnist',
                                train = True,
                                download = True,
                                transform = transform)
train_loader = DataLoader(train_dataset,
                        shuffle=True,
                        batch_size=batch_size)
test_dataset =datasets.MNIST(root='../dataset/mnist',
                                train = False,
                                download = True,
                                transform = transform)
test_loader = DataLoader(test_dataset,
                        shuffle = False,
                        batch_size=batch_size)
class  Net(torch.nn.Module):
    def __init__(self):
        super(Net,self).__init__()
        self.f1 = torch.nn.Linear(784,512)
        self.f2 = torch.nn.Linear(512,256)
        self.f3 = torch.nn.Linear(256,128)
        self.f4 = torch.nn.Linear(128,64)
        self.f5 = torch.nn.Linear(64,10)
    def forward(self,x):
        #这里将
        x = x.view(-1,784)  #展成1*784
        x = F.relu(self.f1(x))
        x = F.relu(self.f2(x))
        x = F.relu(self.f3(x))
        x = F.relu(self.f4(x))
        return self.f5(x)
model = Net()
#loss--交叉熵
criterion = torch.nn.CrossEntropyLoss()  
#带冲量
optimzer = optim.SGD(model.parameters(),lr=0.01,momentum = 0.5)
#训练
def train(epoch):
    running_loss =0.0
    for batch_idx,data in enumerate(train_loader):
        inputs,target = data
        optimzer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs,target)
        loss.backward()
        optimzer.step()
        running_loss += loss.item()
        if batch_idx%300==299:
            print('[%d,%5d] loss:%.3f' % (epoch+1,batch_idx+1,running_loss/300))
            running_loss = 0.0
def test():
    correct = 0
    total = 0
    with torch.no_grad():
        for batch_idx,data in enumerate(test_loader):
            images,labels = data
            outputs = model(images)
            _,predicted = torch.max(outputs.data,dim=1)
            total += labels.size(0)
            correct += (predicted==labels).sum().item()
     
    print('Accuracy on test set:%.2f %%' % (100*correct/total)) 
if __name__== '__main__':
        for epoch in range(7):
            train(epoch)
            test()
        #保存网络参数
