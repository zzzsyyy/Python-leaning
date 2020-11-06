'''
队列是一种先进先出的数据结构
front指向队列的头部
rear指向队列的尾部
两者都指向-1时，表示队列为空
'''

class queue(self):#创立容器
    def __init__(self):
        self.list = []
#入队        
    def enqueue(self,item):
        self.list.append(item)
#出队
    def dequeue(self):
        self.list.pop(0)
#判断是否为空
    def is_empty(self):
        return self.list == []
#队列长度
    def size(self):
        return len(self.list)
        
        
'''
python中的queue类模块提供了一种类型Queue，
q = Queue(maxsize = 0)#0 表示不限制

'''

from queue import Queue 
q = Queue(maxsize = 0)
q.put(1)
q.put(2)
print(q.queue)
#[1,2]
q.get()
print(q.queue)
#[2]
print('队列长度：',q.qsize())
print('队列是否空：',q,empty())
print('队列是否满：',q.full())
#1
#队列长度：1
#队列是否空：False
#队列是否满：False
