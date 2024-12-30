class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    def insert_at_beginning(self,data):
      node=Node(data,self.head)
      self.head=node
    def insert_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
        else:
            itr = self.head
            while itr.next:
                itr = itr.next
            itr.next = Node(data, None)
    
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
                
    def print(self):
        if self.head is None:
            print("Empty")
        else:
            itr = self.head
            LL = ''
            while itr:
                LL += str(itr.data) + "-->"
                itr = itr.next
            print(LL[:-3])  # Remove the trailing '-->'
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

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print()
    ll.insert_after_value("mango","apple") # insert apple after mango
    ll.print()
    ll.remove_by_value("orange") # remove orange from linked list
    ll.print()
    ll.remove_by_value("figs")
    ll.print()
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    ll.print()