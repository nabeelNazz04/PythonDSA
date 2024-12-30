class Node:
  def __init__(self,data=None,next=None,prev=None):
    self.data=data
    self.next=next
    self.prev=prev
class DLL:
  def __init__(self):
    self.head=None
  def print_forward(self):
    if self.head is None:
      print("Empty")
    itr=self.head
    LL=""
    while itr:
      LL+=itr.data+"-->"
      itr=itr.next
    print(LL[:-3])
  def insert_at_beginning(self,data):
      node=Node(data,self.head)
      self.head=node
  def insert_end(self, data):
        if self.head is None:
            self.head = Node(data, None,None)
        else:
            itr = self.head
            while itr.next:
                itr = itr.next
            itr.next = Node(data, None,itr)
    
  def insert_values(self, data_list):
        self.head = None  # Clear the list before inserting new values
        for data in data_list:
            self.insert_end(data)
  def insert_after_value(self,data_after,data_to_insert):
        itr=self.head
        while itr:
            if itr.data == data_after:
                node=Node(data_to_insert,itr.next)
                itr.next=node
                break
            itr=itr.next
                
  def remove_at_index(self,index):
        if index<0:
            raise Exception("invaild index")
        elif index==0:
            self.head=self.head.next
        else:
            count=0
            itr=self.head
            while itr:
                if count==index-1:#To get the previous element
                    itr.next = itr.next.next
                    break
                itr=itr.next
                count+=1
  def remove_by_value(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next

  def insert_at(self,index,data):
        if index<0:
            raise Exception("Invalid")
        elif index==0:
            self.insert_at_beginning(data)

        else:
            itr=self.head
            count=0
            while itr:
                if count==index-1:
                  node=Node(data,itr.next)#creating a node which points to the next of index
                  itr.next=node
                  break
                else:
                    itr=itr.next
                    count+=1
  def print_backward(self):
      if self.head is None:
        print("Empty")
      DLL=""
      itr=self.head
      while itr.next:
          itr=itr.next
      while itr:
          DLL+=itr.data+"-->"
          itr=itr.prev
      print(DLL[:-3])
if __name__ == '__main__':
    ll =DLL()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print_forward()
    ll.print_backward()
    #