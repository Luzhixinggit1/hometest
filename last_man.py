class Node():  
    def __init__(self,value,next=None):  
        self.value=value  
        self.next=next  
  
def createLink(n):  
    if n<=0:  
        return False  
    if n==1:  
        return Node(1)  
    else:  
        root=Node(1)  
        tmp=root  
        for i in range(2,n+1):  
            tmp.next=Node(i)  
            tmp=tmp.next  
        tmp.next=root  
        return root  
  
def showLink(root):  
    tmp=root  
    while True:  
        print(tmp.value)  
        tmp=tmp.next  
        if tmp==None or tmp==root:  
            break  
  
def thelast(n,k):  
    if k==1:  
        print('最后剩下:',n)  
        return  
    root=createLink(n)  
    tmp=root  
    while True:  
        for i in range(k-2):  
            tmp=tmp.next   
        tmp.next=tmp.next.next  
        tmp=tmp.next  
        if tmp.next==tmp:  
            break  
    print('最后剩下:',tmp.value)  
  
if __name__=='__main__':  
    thelast(8,4)  
    print('-----------------')  
    thelast(10,2)  
    print('-----------------')  
    thelast(10,1)  
    print('-----------------')  
