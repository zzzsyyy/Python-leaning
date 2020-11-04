#建立Node指针
class Node:#指针类
    def __init__(self,data,next):#构造
    #类的方法与普通的函数只有一个特别的区别
    #它们必须有一个额外的第一个参数名称
    #按照惯例它的名称是 self
    '''__init__表示类的构造函数或初始化方法
    self 代表类的实例，self 在定义类的方法时是必须有的
    虽然在调用时不必传入相应的参数'''
        self.data = data
        self.next = Node
        return
        
    def __str__(self):#
        return str(self.data)
        
    def has_value(self,value):
        if self.data == value:
            return True
        else:
            return False
            
#建立一个值为一的新节点
Node(1)

#初始化方法
class singlelink:
    def __init__(self):
        self.head = Node
        self.tail = Node
        self.length = 0
        return
        
#判断链表是否为空
    def  isempty(self):
        return self.length == 0
    
#向链表尾部添加节点
    def add_node(self,item):
        if not isinstance(item,Node):
            item = Node(item)
        if self.head is None:
            self.head = item
        else:
            sele.tail.next = item
            self.tail = item
        self.length += 1
        return

#在链表中插入节点
    def insert_node(self,index,data):
        if self.isempty():
            print"this link is empty"
        if index < 0 or index > self.length:
            print"error:out of index"
            return  
        item = Node(data)
        if index == 0:
            item.next = self.head
            self.head = item
            self.length += 1
            return
        j = 0
        node = self.head
        prev = self.head
        while node.next and j < index:
            prev = node
            node = node.next
            j += 1
        if j == index:
            item._next = node
            prev._next = item
            self.length += 1

#通过索引，在链表中删除节点
    def delete_node_byid(self,item_id)：
        id = 1
        current_node = self.head
        previous_node = None
        while current_node is not None:
            if id == item_id:
                if previous_node is not None:
                    previous_node.next = current_node.next
                else:
                    self.head = current_node.next
                    return
            previous_node = current_node
            current_node = current_node.next
            id += 1
        self.length -= 1
        return

    '''#判断链表中是否有环
    def is_loop(self):
        p_fast = self.head
        p_slow = self.head
        while p_fast == p_slow:
            p_slow = p_slow.next
            if p_fast  :
                p_fast = p_fast.next.next
            else:
                p_fast = p_fast.next
            if p_fast == p_slow:
                return Ture
            return False
            '''

#通过数值，在链表中找到节点
    def find_node(self,value):
        current_node = self.head
        node_id = 1
        results = []
        while current_node is not None:
            if current_node .has_value(value):
                results.append(node_id)
            current_node = current_node.next
            node_id += node_id
        return results

#按顺序输出链表
    def print_link(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next
        return

#
    
        
