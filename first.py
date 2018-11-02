"""sum=0
num=11
while(num<=10):
     sum=sum+num
     num=num+1
     print('the sun of bumber is' + str(sum))"""

"""balance= 100
rate=1.5
year=1
while(year<=10):
    balance=balance*rate
    year=year+1
    print('year is : ' + str(year) + ' balance is ' + str(balance))"""
"""average=0.0
total=0.0
count=0.0
print('Enter the number (-1 to quit)')
cupid=int(input())
while(cupid!=-1):
    total=total+cupid
    count=count+1
    print('Enter the numberr(-1 to quit )')
    cupid=int(input())
average=total/count
print('Average is '+ str(average))"""

"""numo=0.0
demo=0.0
while(demo!=-1):
    print('Enter the value of numerator: ')
    numo=float(input())
    print('Enter the value of denomerator: ')
    demo=float(input())
    if (demo==0):
        continue
    print('the result is :'+str(numo/demo))"""

"""total=0.0
count=0.0
while True:
    print('Enter the value of number: ')
    number=float(input())
    if number == -1:
        break
    total=total+number
    count=count+1
average=total/count
print('Average is : ' + str(average))"""

"""outFile = open('text.txt','w')
outFile.write('this is it !\n')
outFile.write('that was it !!\n')
outFile.close()"""

"""print(r'c:\number\nam')"""

"""print('Enter a number:')
i=int(input())
for j in range(i,10,2):
     print(j)"""
"""num=0
num=int(input())
for num in range(1,num):
     if(num==42):
          break
     print(num)

num=0
while(True):
     if(num==42):
          break
     print(num)"""

"""x,y=input().split()
x=int(input())
y=float(input())
if(y>=x +.5 and x%5==0):
     print("{:.2f}".format(y-(x+.5)))
else:
     print("{:0.2f}".format(y))"""

"""from time import time
def contains(collections,target):
     return target in collections
def performance():
     n=1024
     while n<50000000:
          sorted = range(n)
          now = time()
          contains(sorted,-1)
          done=time()
print (n, (done-now)*1000)
          n *=2"""
"""print("Enter the value for T")
t=int(input())
print("Enter the value for a,b,c,d")
#t=int(input())
a=int(input())
b=int(input())
c=int(input())
d=int(input())
for t in range (1,4):
    if(a==b and c==d):
        print("Yes")
        break
    elif(a==c and b==d):
        print("Yes")
        break
    elif(a==d and c==b):
        print("Yes")
        break
    else:
        print("No")
        break"""



"""t = int(input())

for t in range(0, t):
    inp = list(map(int, input().split()))
    a = inp[0]
    b = inp[1]
    c = inp[2]
    d = inp[3]
    if (a == b and c == d):
        print("YES")
        continue
    elif (a == c and b == d):
        print("YES")
        continue
    elif (a == d and c == b):
        print("YES")
        continue
    else:
        print("NO") 
        continue"""


"""print("Enter the Array a ")
a = list(map(int,input().split()))

def maxSubArraySum(a, size):
    max_so_far = a[0]
    curr_max = a[0]

    for i in range(1, size):
        curr_max = max(a[i], curr_max + a[i])
        max_so_far = max(max_so_far, curr_max)
    return max_so_far
print("Maximum continous sum is ", maxSubArraySum(a, len(a)))"""
"""
    t = int(input())
    for t in range(0, t):
        inp = list(map(int, input().split()))
        N = inp[0]
        K = inp[1]
        S = inp[2]

        if (N < K):
            print("-1")
            continue
        elif (S <= 6):
            print(int(S * K + N - 1) / N)
            continue
        elif (6 * N < 7 * K):
            print("-1")
            continue
        else:
            print(int((S * K + N - 1) / N))"""

# for i in "python":
#   print(i,end=" ")


"""import sys

x,y= input().split()
x=int(x)
y=int(y)
difference= x-y
if(difference%100==9):
    skadoosh=difference-1
else:
    skadoosh=difference+1
print("skadoosh")"""

"""import collections
the_string= 'hello'
results = collections.Counter(the_string)
print(results)"""

"""t = int(input())
i=0
for t in range(0, t):
    inp = list(map(str, input().split()))
    s = inp[0]
    if((s.find("chef"))):
        print("lovely" + str(i+1))
        i=i+1
    if((s.find("fche"))):
        print("lovely" + str(i+1))"""

"""nStr = 'ifchefisgoodforchesschef'
pattern = 'chef'
count =0
flag=True
start=0
while flag:
    a = nStr.find(pattern,start)  # find() returns -1 if the word is not found,
                                  #start i the starting index from the search starts(default value is 0)
    if a==-1:          #if pattern not found set flag to False
        flag=False
    else:               # if word is found increase count and set starting index to a+1
        count+=1
        start=a+1
print("lovelly",count)"""


"""t = int(input())
for t in range(0, t):
    inp = list(map(str, input().split()))
    s = inp[0]

    if(("chef" or "chfe"  or "cfeh" or "cehf" or "cefh" or "cfhe" or "echf" or "efhc" or "ehfc" or "efch" or "ehcf" or "echf" or "hcef" or "hecf" or "hfec" or "hfce" or "hcfe" or "hefc" or "fche" or "fech" or "fhec" or "fehc" or "fceh" or "fhce") in s):
     print("lovely",s.count('chef')+s.count('chfe')+s.count('cfeh')+s.count('cehf')+s.count('cefh')+s.count('cfhe')+s.count('echf')+s.count('efhc')+s.count('ehfc')+s.count('efch')+s.count('ehcf')+s.count('echf')+s.count('hcef')+s.count('hecf')+s.count('hfec')+s.count('hfce')+s.count('hcfe')+s.count('hefc')+s.count('fche')+s.count('fech')+s.count('fhec')+s.count('fehc')+s.count('fceh')+s.count('fhce'))
    else:
     print("normal")"""

# cook your dish here
"""t = int(input())
for t in range(0, t):
    inp = list(map(str, input().split()))
    s = inp[0]

    if ('hecf' in s or 'chef' in s or 'chfe' in s or 'cfeh' in s or 'cehf' in s or 'cefh' in s or 'cfhe' in s or 'echf' in s or 'efhc' in s or 'ehfc' in s or 'efch' in s or 'ehcf' in s or 'echf' in s or 'hcef' in s or 'hfec' in s or 'hfce' in s or 'hcfe' in s or 'hefc' in s or 'fche' in s or 'fech' in s or 'fhec' in s or 'fehc' in s or 'fceh' in s or 'fhce' in s):

        print("lovely",
              s.count('chef') + s.count('chfe') + s.count('cfeh') + s.count('cehf') + s.count('cefh') + s.count(
                  'cfhe') + s.count('echf') + s.count('efhc') + s.count('ehfc') + s.count('efch') + s.count(
                  'ehcf') + s.count('echf') + s.count('hcef') + s.count('hecf') + s.count('hfec') + s.count(
                  'hfce') + s.count('hcfe') + s.count('hefc') + s.count('fche') + s.count('fech') + s.count(
                  'fhec') + s.count('fehc') + s.count('fceh') + s.count('fhce'))
    else:
        print("normal")"""

"""def permute(a, l, r):
    if l == r:
        print(str(a))
    else:
        for i in range(l, r + 1):
            a[l], a[i] = a[i], a[l]
            permute(a, l + 1, r)
            a[l], a[i] = a[i], a[l] # backtrack
# Driver program to test the above function
string = str(input())
n = len(string)
a = list(string)
permute(a, 0, n - 1)
# function to check string is
# palindrome or not
def isPalindrome(string):
    # Using predefined function to # reverse to string print(s) 
    rev = ''.join(reversed(string))
    # Checking if both string are  # equal or not
    if (string == rev):
        return True
    return False
# main function
#s=bss
ans = isPalindrome(string)
if (ans):
    print("Yes")
else:
    print("No")"""


"""t = int(input())
for t in range(0, t):
    # inp = list(map(str, input().split()))
    s = input()
temp = 0
for i in range(len(s) - 3):
    if ((s[i:i + 4].find('c') != -1) and (s[i:i + 4].find('h') != -1) and (s[i:i + 4].find('e') != -1) and (s[i:i + 4].find('f') != -1)):
        temp = temp + 1
if (temp != 0):
    print("lovely", temp)
else:
    print("normal")"""


"""t = int(input())
for t in range(0, t):
    inp = list(map(int, input().split()))
    a = inp[0]
    b = inp[1]
    c= (a*(a+1))/2+((a-1)*b)
    print(int(c))"""
#x=int(input())
#n=int(input())
#x,n=input().split()
#x=int(input())
#n#=int(input())
""""def exponent(x,n):
    if (n==0):
        return 1
    if (n==1):
        return x

    if(n%2):
        return x * exponent(x*x,(n-1)/2)
    else:
        return exponent(x*x,(n-1)/2)"""


"""#skadoosh 11
t = int(input())
for t in range(0, t):
    n= int(input())
    L1= list(map(int, input().split()[:n]))
    L2= list(map(int, input().split()[:n]))
    if((L2 >= L1) and (L2[::-1]<=L1)):
        print("both")
    elif(L2>=L1):
        print("front")
    elif(L2[::-1]<=L1):
        print("back")
    else:
        print("none")"""

"""t=int(input())
for t in range (0,t):
    d=int(input())
    for d in range(0,d):
    #for t in range(0,t):
        inp = list(map(int, input().split()))
        n = inp[0]
        k = inp[1]
        s = inp[2]
    #for i in range(k):
        a=n+(n/100)*s
        b=(a/100)*s
        b=a-b
        b=n-b
        c=b*k
        
    #a=
    #print(a)
    #b=a*k
    #print(b)"""


"""student={
    "name":"wolf",
    "student_Id":13232,
    "feedback":None
}
student["last_name"]="skadoosh"
try:
    last_name=student["last_name"]
    numbered_last_name=3+last_name
except KeyError:
    print("error in finding ur key!!")
except TypeError as error:
    print("i cant Add these two ")
    print(error)"""
"""except Exception:
    print("unknown")
print("mission complete")"""

"""def var_args(name,**kwargs):
    print(name)
    print(kwargs["description"],kwargs["feedback"])
var_args("Nikhil",description="a love wolf",feedback=None,will_change_the_world=True)"""

"""t = int(input())
for t in range(0, t):
    n= int(input())
    L1= list(map(int, input().split()[:n]))
    if (len(L1)==len(set(L1))):
        print("0")
    else:
        L2=[]
        temp=0
        for i in L1:
            if (i not in L2):
                L2.append(i)
                
            else:
                L2[i]=L2[i]+L2[i-1]
                print(L2)
                temp+=temp
                print(temp)"""

"""def Remove(L1):
    count = 0
    final_list = []
    for num in L1:
        if num not in final_list:
            final_list.append(num)
            # count=count+1
    return final_list
print(Remove(L1))"""


"""from codecs import encode
l1=str(input())
print(encode (l1,'rot(13)'))"""

"""t = int(input())
for t in range(0, t):
    # inp = list(map(str, input().split()))
    s = input()
temp = 0
for i in range(len(s) - 2):
    if ((s[i:i + 2].find('c') != -1) and (s[i:i + 2].find('h') != -1) and (s[i:i + 2].find('e') != -1) and (s[i:i + 2].find('f') != -1)):
        temp = temp + 1
if (temp != 0):
    print("lovely", temp)
else:
    print("normal")"""


"""t = int(input())
for t in range(0, t):
    s = input()
temp = 0
for i in range (len(s)):
    if("ch" in s or "ce" in s or "cf" in s or "hc " in s or "he" in s or "hf" in s or "ec" in s or "eh" in s or "ef" in s or "fc" in s or "fe" in s or "fh" in s ):
        temp=temp+1
    if (temp!=0):
        print(temp)"""

"""n=int(input())
L1= list(map(int, input().split()[:n]))
L2= list(map(int, input().split()[:n]))

for i in range(0,len(L2)):
    if():
        print()"""

"""t=int(input())
for t in range (0,t):
    d=int(input())
    L1 = list(map(int, input().split()[:d]))
    L2 = list(map(int, input().split()[:d]))

    for j in range(0,len(L2)):
        if(L2[j]==1 or L2[j]==2 or L2[j]==3):"""



"""t = int(input())
for t in range(0, t):
    n, sum = input().split()
    n = int(input())
    sum = int(input())

    def countRec(n, sum):
        if (n == 0):
            return (sum == 0)

        if (sum == 0):
            return 1

        ans = 0

        for i in range(0, 10):
            if (sum - i >= 0):
               ans = ans + countRec(n - 1, sum - i)

        return ans


    def finalCount(n, sum):

        ans = 0


        for i in range(1, 10):
            if (sum - i >= 0):
                ans = ans + countRec(n - 1, sum - i)

        return ans

    print(finalCount(n, sum))"""


"""t = int(input())
for t in range(0, t):

    inp = list(map(int, input().split()))

    N = inp[0]
    M = inp[1]
    if((N%M)%2==1):
        print("ODD")
    else:
        print("EVEN")"""

"""t= int(input())
for t in range(0,t):
    imp=list(map(int, input().split()))
    x1=imp[0]
    x2=imp[1]
    x3=imp[2]
    y1=imp[3]
    y2=imp[4]

    n=(x3-x1)/y1
    #print(n)
    g=(x2-x3)/y2
    #print(g)

    if(n==g):
        print("Draw")
    elif(n>g):
        print("Kefa")
    elif(n<g):
        print("Chef")"""

"""t= int(input())
for t in range(0,t):
    d = int(input())
    l = list(map(int, input().split()[:d]))
    def find_gcd(x, y):
        while (y):
            x, y = y, x % y

        return x

    num1 = l[0]
    num2 = l[1]
    gcd = find_gcd(num1, num2)

    for i in range(2, len(l)):
        gcd = find_gcd(gcd, l[i])

    print(gcd)

    if(gcd==1):
        print("0")
    else:
        print("-1")"""

"""t= int(input())
for t in range(0,t):
    imp=list(map(int, input().split()))
    n=imp[0]
    l= list(map(int, input().split()[:n]))
    a=imp[1]
    b=imp[2]
    g=l.count(a)
    h=l.count(b)

    if(a in l and b in l):
        c=g/n
        #print(c)
        d=h/n
        #print(d)
        e=c*d
        print('{:0<12}'.format(e))

    else:
        print("0")
#skadoosh"""

"""t= int(input())
for t in range(0,t):
    imp=list(map(int,input().split()))
    a=imp[0]
    b=imp[1]

    c=bin(a)
    d=bin(b)

  #  print(c)
    z=int(c,2)
   # print(d)"""


"""t=int(input())
for t in range(0,t):
    imp = list(map(int, input().split()))
    a = imp[0]
    b = imp[1]
    c=  imp[2]
    d=a**c
    print(d)
    e=b**c
  #  print(e)

    if(d/e):
        print("1")
    elif(d/e):
        print("2")
    elif(d==e):
        print("0")
#skadoosh"""





"""imp = list(map(int, input().split()))
a = imp[0]
b = imp[1]
c=  imp[2]
d=a+b+c

if(d==6):
    print("its true!!")
else:
    print("No comments")"""


"""d = int(input())
l = list(map(int, input().split()[:d]))
l.sort()
#print(l)
temp=0
for i in range(len(l)):
     if(l[i]!=0):
        l[i+1]=l[i+1]-l[i]
        l[i]+=1
        temp+=1
        print(i)"""


"""t=int(input())
for t in range(0,t):
    imp = list(map(int, input().split()))
    l = imp[0]
    r = imp[1]
    count=0
   # if(l==2 and l==3 and l==9):
   #     print("1")
    while(l%10):
        if(l%10==2 or l%10==3 or l%10==9):
            count+=1
        l+=1
    while(r%10):
        if(r%10==2 or r%10==3 or r%10==9):
            count+=1
        r-=1
    a=(r-l)/10
    count+=3*a
    print(int(count))"""

#skadoosh

"""t=int(input())
for t in range (t):
    inp = list(map(int, input().split()))
    n = inp[0]
    m = inp[1]
    l = list(map(int, input().split()[:n]))

    def subCount(l, n, m):

        mod = []
        for i in range(m + 1):
            mod.append(0)

        cumSum = 0
        for i in range(n):
            cumSum = cumSum + l[i]

            mod[((cumSum % m) + m) % m] = mod[((cumSum % m) + m) % m] + 1

        result = 0


        for i in range(m):

            if (mod[i] > 1):
                result = result + (mod[i] * (mod[i] - 1)) // 2

        result = result + mod[0]

        return result

    print(subCount(l,n, m))"""


"""from fractions import Fraction

t=int(input())
for t in range (t):
    n=int(input())
    q=9**n

    def palindrome(n):
        if((n%2)>1):
            return 9*(10**(int((n-1)/2)))
        else:
            return 9*(10**(int((n-2)/2)))

    p=palindrome(n)
    c=p/q
    a=(Fraction(c).limit_denominator())
    print(a.numerator,a.denominator,end=" ")"""

#skadoosh

#    print(str(Fraction(c).limit_denominator()))


#print(int(2.5))
#   print (sum ([str(i)==str(i)[::-1] for i in range(1,n)]))




"""import itertools

t=int(input())
for t in range(t):
    imp=list(map(int, input().split()))
    n=imp[0]
    k=imp[1]
    l=list(map(int,input().split()[:n]))

    p=list(itertools.combinations(l, k))
    print(p)


import numpy as np

a = np.array([1, 2, 3])   # Create a rank 1 array
print(type(a))"""""

"""def pypart(n):

    # outer loop to handle number of rows
    # n in this case
    for i in range(0, n):

        # inner loop to handle number of columns
        # values changing acc. to outer loop
        for j in range(0, i + 1):
            # printing stars
            print("a ", end="")

        # ending line after each row
        print("\r")


# Driver Code
n = 5
pypart(n)"""
"""BreadthFirstSearchS
class Node(object):
    def __init__(self,name):
        self.name=name
        self.adjancylist=[]
        self.visited=False
        self.predecessor=None

class BreadthFirstSearch(object):
    def bfs(self,startNode):
        queue=[]
        queue.append(startNode)
        startNode.visited=True

        while queue:

            actualNode=queue.pop(0)
            print("%s" %actualNode.name)
            for n in actualNode.adjancylist:
                if  not n.visited:
                    n.visited=True
                    queue.append(n)

node1=Node("A")
node2=Node("b")
node3=Node("C")
node4=Node("d")
node5=Node("E")

node1.adjancylist.append(node2)
node1.adjancylist.append(node3)
node2.adjancylist.append(node4)
node4.adjancylist.append(node5)

bfs=BreadthFirstSearch()
bfs.bfs(node1)"""

"""DeapthFirstSearch
class Node(object):
    def __init__(self,name):
        self.name=name
        self.visited=False
        self.adjancylist=[]
        self.predecessor=None

class DeapthFirstSearch(object):
    def dfs(self,startnode):
        startnode.visited=True
        print("%s" %startnode.name)

        for n in startnode.adjancylist:
            if not n.visited:
                self.dfs(n)

node1=Node("A")
node2=Node("b")
node3=Node("C")
node4=Node("d")
node5=Node("E")

node1.adjancylist.append(node2)
node1.adjancylist.append(node3)
node2.adjancylist.append(node4)
node4.adjancylist.append(node5)

dfs= DeapthFirstSearch()
dfs.dfs(node1)"""


"""DJ Algorithm  
import sys
import heapq

class Edge(object):

    def __init__(self,weight, startvertev , targetvertex ):
        self.startvertex=startvertev
        self.targetvertex=targetvertex
        self.weight=weight
        
class node(object):

    def __init__(self,name):
        self.name=name
        self.visited=True
        self.adjancylist=[]
        self.predecessor=None
        self.mimdistance=sys.maxsize

    def __cmp__(self, othervertex):
        return self.__cmp__(self.mimdistance), (othervertex.mimdistance)

    def __lt__(self, other):
        self.priority=self.mimdistance
        other.priority=other.mimdistance
        return self.priority < other.priority

class Algorithm(object):

    def calculateShortestPath(self,vertexlist,startvertex):

        q=[]
        startvertex.mimdistance=0
        heapq.heappush(q,startvertex)

        while(len(q) > 0):
            actualvertex=heapq.heappop(q)

            for edge in actualvertex.adjancyliist:
                u=edge.startvertex
                v=edge.targetvertex
                newdistsnce=u.mimdistance + edge.weight

                if (newdistsnce<v.mimdistance):
                    v.predecessor=u
                    v.mimdistance=newdistsnce
                    heapq.heappush(q,v)

    def getShortestPath(self,targetvertex):
        print("shortest path for the given vertex is :" ,targetvertex.mimdistance)

        node=targetvertex
        while node is not None:
            print("%s " %node.name)
            node=node.predecessor


node1= node("A")
node2= node("B")
node3= node("C")
node4= node("D")
node5= node("E")
node6= node("F")
node7= node("G")
node8= node("H")

edge1= Edge(5,node1,node2)
edge2= Edge(8,node1,node8)
edge3= Edge(9,node1,node5)
edge4= Edge(15,node2,node4)
edge5= Edge(12,node2,node3)
edge6= Edge(4,node2,node8)
edge7= Edge(7,node8,node3)
edge8= Edge(6,node8,node6)
edge9= Edge(5,node5,node8)
edge10= Edge(4,node5,node6)
edge11= Edge(20,node5,node7)
edge12= Edge(1,node6,node3)
edge13= Edge(13,node6,node7)
edge14= Edge(3,node3,node4)
edge15= Edge(11,node3,node7)
edge16= Edge(9,node4,node7)

node1.adjancylist.append(edge1)
node1.adjancylist.append(edge2)
node1.adjancylist.append(edge3)
node2.adjancylist.append(edge4)
node2.adjancylist.append(edge5)
node2.adjancylist.append(edge6)
node8.adjancylist.append(edge7)
node8.adjancylist.append(edge8)
node5.adjancylist.append(edge9)
node5.adjancylist.append(edge10)
node5.adjancylist.append(edge11)
node6.adjancylist.append(edge12)
node6.adjancylist.append(edge13)
node3.adjancylist.append(edge14)
node3.adjancylist.append(edge15)
node4.adjancylist.append(edge16)

vertexlist=(node1,node2,node3,node4,node5,node6,node7,node8)

algorith=Algorithm()
algorith.calculateShortestPath(vertexlist,node1)
algorith.getShortestPath(node7)"""


"""import turtle
#import time
                                                       
                                            
turtle.forward(150)
turtle.right(200)
turtle.forward(150)
turtle.circle(75)
turtle.done()
#time.sleep(4)"""

"""t=int(input())
for i in range(t):
    n,m=list(map(int,input().split()))
    L=list(map(int,input().split()))
    s=0                    
    for j in L:
        if j%m==0:
            s+=1
    print(2**s-1)"""

"""t=int(input())
for t in range (t):
    imp=list(map(int,input().split()))
    a=imp[0]
    b=imp[1]
    c=imp[2]
    x=imp[3]
    y=imp[4]
    if((a+b+c)==(x+y)):
        if(min(a,b,c)<=min(x,y)):
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
    #print(l)"""

"""t=int(input())
for t in range (t):
    l1=list(map(str,input().split()))

    l2=list(map(str,input().split()))

    if ((l1[0] or (l2[0])=='b') and ((l1[1] or l2[1]) == 'o') and ((l1[2]) or (l2[2]) == 'b')):
        print("yes")

    elif(l1[2]=='o' or l1[0]=='o'):
        l1[2], l1[1] = l1[1], l1[2]
        print(l1)
        l2[2], l2[1] = l2[1], l2[2]
        print(l2)
        #print(l1[1])
        if (((l1[0] or l2[0]) == 'b') and ((l1[1] or l2[1]) == 'o') and ((l1[2] or l2[2]) == 'b')):
            print('yes')
        else:
            print('no')
            continue

    elif(l2[0]=='o' or l2[2]=='o'):
        l1[1], l1[0] = l1[0], l1[1]
        print(l1)
        l2[1], l2[0] = l2[0], l2[1]
        print(l2)
        print(l1[1])
        if (((l1[0] or l2[0]) == 'b') and ((l1[1] or l2[1]) == 'o') and ((l1[2] or l2[2]) == 'b')):
            print('yes')
        else:
            print('no')
            continue
    else:
        print('no')"""

"""import  math
t=int(input())
for t in range(0,t):
    n=int(input())
    def power_two(n):
        return int(math.log(n, 2))

   # n=4
    p=power_two(n)
    m=n-2**p
    if(m==0):
        print("1")

    else:
        def power_two(m):
            return int(math.log(m, 2))

        q=power_two(m)
        a=m-2**q
        #print(q)
        print(a)"""

"""t= int(input())
for t in range(t):
    l1=str(input())
    l2=str(input())
    l1=list(l1)
    l2=list(l2)
    a=l1[0]
    b=l1[1]
    c=l1[2]
    x=l2[0]
    y=l2[1]
    z=l2[2]

    if(((a=='b')or(x=='b')) and ((b=='o')or(y=='o'))and ((c=='b')or(z=='b'))):
        print("yes")

    elif(c=='o'):
        c, b = b, c
        z, y = y, z
        if (((a == 'b') or (x == 'b')) and ((b == 'o') or (y == 'o')) and ((c == 'b') or (z == 'b'))):
            print("yes")
        else:
            print("no")

    elif(a =='o'):
        a,b=b,a
        x,y=y,x
        if (((a == 'b') or (x == 'b')) and ((b == 'o') or (y == 'o')) and ((c == 'b') or (z == 'b'))):
            print("yes")
        else:
            print("no")

    elif((x =='o')):
        b, a = a, b
        y, x = x, y
        if (((a == 'b') or (x == 'b')) and ((b == 'o') or (y == 'o')) and ((c == 'b') or (z == 'b'))):
            print("yes")
        else:
            print("no")

    elif(z =='o'):
        c,b=b,c
        z,y=y,z
        if (((a == 'b') or (x == 'b')) and ((b == 'o') or (y == 'o')) and ((c == 'b') or (z == 'b'))):
            print("yes")
        else:
            print("no")
    else:
        print("no")"""



""""def matched(str):
    count = 0
    for i in str:
        if i == "(":
            count += 1
        elif i == ")":
            count -= 1
        if count < 0:
            return False
    return count == 0
str=str(input())
print(matched(str))

def check_parentheses(s):
    j = 0
    for c in s:
        if c == ')':
            j -= 1
            if j < 0:
                return False
        elif c == '(':
            j += 1
    return j == 0
s=input()
print(check_parentheses(s))"""


#l=list(map(int ,input(). split()))
"""import math

def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    sqr = int(math.sqrt(n)) + 1

    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True
#def is_prime(n):
#    return(factor(n)==[1,n])


def isprime(n):
    return(factor(n)==[1,n])

def primeupto(n):
    primelist=[]
    for i in range(1,n+1):
        if isprime(i):
            primelist.append(i)
    return(primelist)

def nprime(n):
    (count,i,plist)=(0,1,[])
    while(count<n):
        if(isprime(i)):
            count=count+1
            plist.append(i)
        i=i+1
    return (plist)

n=int(input())
#print(factor(n))
#print(isprime(n))
#print(primeupto(n))
print(nprime(n))"""

"""def update(l,i,v):
    if((i>=0)and (i<len(l))):
        l[i]=v
        return (l)
    else:
        v = v+1
        return(l)
l=list(map(int,input().split()))
i=int(input())
v=int(input())
print(update(l,i,v))
#print(update(l,4,v))"""



"""t=int(input())
for t in range(t):
    n=int(input())
    l=list(map(int,input().split()[:n]))
    #c=[]
    l.sort()
    #print(l)
    c=l[1]-l[0]
    if (c==0):
        print("0")
    else:
        print(c)"""


"""t=int(input())
for t in range(0,t):
    def findMinDiff(l, n):
        diff = 100 **20
        for i in range(n - 1):
            for j in range(i + 1, n):
                if abs(l[i] - l[j]) < diff:
                    diff = abs(l[i] - l[j])

        return diff

    n=int(input())
    l=list(map(int,input().split()[:n]))
    print(findMinDiff(l, n))

t=int(input())
for t in range(0,t):
    def findMinDiff(arr, n):
        arr = sorted(arr)
        diff = 10 **20
        for i in range(n-  1):
            if arr[i + 1] - arr[i] < diff:
                diff = arr[i + 1] - arr[i]
        return diff
n=int(input())
arr=list(map(int,input().split()[:n]))"""

"""def bsearch(seq,v,l,r):
    if((r-l)==0):
        return(False)
    mid=(l-r)//2
    if(v==seq[mid]):
        return(True)
    if(v<seq[mid]):
        return(bsearch(seq,v,l,mid))
    else:
        return(bsearch(seq,v,mid+1,r))

seq=[1,2,3,4,5,6,7,8,9,10]
v=10
print(bsearch(seq,v,0,11))"""

"""for i in range(int(input())):
    n,m=map(int,input().split())
    ans=0
    ans+=m*n
    for i in range(1,min(n,m)):
        #print(ans)
        ans+=(n-i)*(m-i)*(i+1)*(i+1)
    print(ans)"""
"""t=int(input())
for t in range(t):
    inp = list(map(int, input().split()))
    a = inp[0]
    b = inp[1]
    c = inp[2]
    d = inp[3]

    if(((a-c)or(c-a))>1 and ((b-d)or(d-b))>1):
        print("Line")
    else:
        print("Point")
    print("Nothing")"""

"""n,q=map(int,input().split())
a=list(map(int,input().split()[:n]))
for i in range(q):
    x=int(input())
    if(x in a):
        print("YES")
    else:
        print("NO")"""
"""t=int(input())
c=0
for t in range(t):
    n=int(input())
    for i in range(n):
        for j in range(i+1,n):
            if((i+j)==n):
                c=min(i,j)
                
                if((c%2)==0):
                    print("0")
                else:
                    print("1")"""

"""t=int(input())
for t in range(t):
    n,m=map(int,input().split())
    a=list(map(int,input().split()[:n]))
    b=list(map(int,input().split()[:m]))
    c=sorted(a)
    d=sorted(b)
    for i in range(len(c)):
        for j in range(i,len(d)):
            if(c[i]>=d[j]):
                print("yes")"""
"""n=int(input())
l=list(map(int,input().split()[:n]))
l.sort()
print(*l,sep=' ')"""

"""t=int(input())
for t in range(t):
    n=int(input())
    a=list(map(int,input().split()[:n]))
    b,c = a[::2], a[1::2]
    print(b)
    print(c)
    e=sum(b)
    f=sum(c)
    print(e)
    print(f)
    print("Case ",t+1," :",max(e,f),sep="")"""
"""t=int(input())
a=list(map(int,input().split()[:t]))
b = list(map(int, input().split()[:t]))
c=[x + y for x, y in zip(a, b)]
print(*c,sep=" "):"""

"""def intrevese(n):
    return(print((str(n)[::-1])))
#n=int(input())
intrevese(int(input()))"""


"""def intrevese(n):#1st function
    return(print((str(n)[::-1])))
n=int(input())
intrevese(n)

def matched(s):#2nd function
    nesting = 0
    for c in s:
        if c == '(':
            nesting += 1
        elif c == ')':
            nesting -= 1
        if nesting < 0:
            return(False)
    return(nesting == 0)
s=str(input())
print(matched(s))

def is_prime(n):#3.5 function
    if n < 2:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0:
        return False

    length = int(n**.5) + 1
    for i in range(3, length, 2):
        if n % i == 0:
            return False
    return True
def sumprimes(l):#3.5 function
    return sum(n for n in l if is_prime(n))
l=list(map(int,input().split()))
print(sumprimes(l))

fncall=input()
if (fncall=="intreverse"):
    n=int(input())
    print(intrevese(n))
if (fncall=="matched"):
    s=str(input())
    print(matched(s))
if (fncall=="sumprimes"):
    l=list(map(int,input().split()))
    print(sumprimes(l))"""

"""t=int(input())
c=0
for t in range(t):
    n,x,y=map(int,input().split())
    for i in range(y):
        a,b=map(int,input().split())

        if(a==x):
            x=b
            a,b=b,a
            #x=b
            #print(a)
            #print(x)
        else:
            x=a
            b,a=a,b
            #x=a
            #print(b)
            #print(x)
    print(x)
        #print(a)
        #print(b)"""

"""t = int(input())
c = 0
for t in range(t):
    n, x, y = map(int, input().split())
    for i in range(y):
        a, b = map(int, input().split())
        if (a == x):
            x = b
            # a,b=b,a
            # x=b
            # print(a)
            # print(x)
        elif (x == b):
            x = a
            # b,a=a,b
            # x=a
            # print(b)
            # print(x)
    print(x)
    # print(a)
    # print(b)"""

"""t=int(input())
for t in range(t):
    a,b,c,d=map(int,input().split())
    (p,k)=(1,1)
    (e,f)=(p+1,k+1)
    if((e==a)and(f==b)):
        print("Chefirnemo")
    elif():
        print("Chefirnemo")"""

#  def f(m,n) :
#      ans = 1
#      while (m - n >= 0):
#          ans = ans * 2
#          m = m - n
#          print(m,n)
#      return(ans)
#
# print(f(120,13))
#
"""dict1={'match':{'player1':57,'player2':38},
        'match2':{'player3':9,'player1':42},
        'match3':{'player2':41,'player4':63,'player3':91}}
def orangecap(dict1):
     dict2={}
     for k1 in dict1:
         for k2 in dict1[k1]:
             dict2[k2]=dict1.get(k2,0)+dict1[k1][k2]
     player=max(dict2,key=dict2.get)
     return player,dict2[player]

print(orangecap(dict1))"""

"""data={'match1':{'player1':57, 'player2':38},
'match2':{'player3':9, 'player1':42},
'match3':{'player2':41, 'player4':63,'player3':91} }
print ("=====")
playerCollection=[]
playerTotals={}
for aMatch in data:
    for aPlayer in data[aMatch]:
        #print aPlayer,data[aMatch][aPlayer]
        if aPlayer in playerCollection:
            #aPlayer= aPlayer + data[aMatch][aPlayer]
            playerTotals[aPlayer] = playerTotals[aPlayer] + data[aMatch][aPlayer]
        else:
            playerCollection.append(aPlayer)
            playerTotals[aPlayer] = data[aMatch][aPlayer]
print (playerCollection)
print (playerTotals)
sortToMax = sorted(playerTotals.items(), key=lambda (k,(v2)): v2)
print (sortToMax.pop())"""

#games = {'match1': {'plr1': 15, 'plr2': 25}, 'match2': {'plr2': 30, 'plr3': 40}}

"""games={'match':{'player1':57,'player2':38},
        'match2':{'player3':9,'player1':42},
        'match3':{'player2':41,'player4':63,'player3':91}}

def orangecap(d):
    totalscore = dict()
    for match in d:
        for plr in d[match]:
            if plr in totalscore:
                totalscore[plr] += d[match][plr]
            else:
                totalscore[plr] = d[match][plr]
    best = max(totalscore, key=totalscore.get)
    return best, totalscore[best]

#print(orangecap(games))"""


"""import numpy as np

def addpoly(p1, p2):
        poly1 = np.poly1d(p1)
        poly2 = np.poly1d(p2)
        result = poly1 + poly2
        print(result)
def multpoly(p1, p2):
        poly1 = np.poly1d(p1)
        poly2 = np.poly1d(p2)
        re = poly1 * poly2
        print(re)

equ1=[4,3,3,0]
equ2=[-4,3,2,1]
addpoly(equ1, equ2)
equ1 = [3.0, 0.0, -17.0, -3.0, 5.0]
equ2 = [4.0,  3.0, 5.0]

#test functions
addpoly(equ1, equ2)
multpoly(equ1, equ2)"""


"""def addpoly(p1, p2):
    for i in range(len(p1)):
        for item in p2:
            if p1[i][1] == item[1]:
                p1[i] = ((p1[i][0] + item[0]), p1[i][1])
                p2.remove(item)
    p3 = p1 + p2
    for item in (p3):
        if item[0] == 0:
            p3.remove(item)
    return sorted(p3)

def multpoly(p1, p2):
    for i in range(len(p1)):
        for item in p2:
            p1[i] = ((p1[i][0] * item[0]), (p1[i][1] + item[1]))
            p2.remove(item)
    return p1
print(addpoly([(4,3),(3,0)],[(-4,3),(2,1)]))
print(multpoly([(1,1),(-1,0)],[(1,2),(1,1),(1,0)]))"""

"""def addpoly(p1,p2):
    i=0
    su=0
    j=0
    c=[]
    if len(p1)==0:
        #if p1 empty
        return p2
    if len(p2)==0:
        #if p2 is empty
        return p1
    while i<len(p1) and j<len(p2):
        if int(p1[i][1])==int(p2[j][1]):
            su=p1[i][0]+p2[j][0]
            if su !=0:
                c.append((su,p1[i][1]))
            i=i+1
            j=j+1
        elif p1[i][1]>p2[j][1]:
            c.append((p1[i]))
            i=i+1
        elif p1[i][1]<p2[j][1]:
            c.append((p2[j]))
            j=j+1
    if p1[i:]!=[]:
        for k in p1[i:]:
            c.append(k)
    if p2[j:]!=[]:
        for k in p2[j:]:
            c.append(k)
    return c
def multipoly(p1,p2):
    p=[]
    s=0
    for i in p1:
        c=[]
        for j in p2:
            s=i[0]*j[0]
            e=i[1]+j[1]
            c.append((s,e))
        p=addpoly(c,p)
    return p
print(multipoly([(1,1),(-1,0)],[(1,2),(1,1),(1,0)]))"""

"""def stu_input(l):
    x=input()
    while x!='Grades':
        x=x.split('~')
        x.append(0)
        l.append(x)
        x=input()
def inp_grade(grade):
    x=input()
    while x!='EndOfInput':
        x=x.split('~')
        x=x[len(x)-2:]
        grade.append(x)
        x=input()
def com(x):
    if x=='A':
        return 10
    elif x=='AB':
        return 9
    elif x=='B':
        return 8
    elif x=='BC':
        return 7
    elif x=='C':
        return 6
    elif x=='CD':
        return 5
    else:
        return 4
def cal():
    global li,grade
    for i in li:
        j=0
        sum=0
        while j<len(grade):
            if i[0]==grade[j][0] :
                sum=sum+com(grade[j][1])
                grade.pop(j)
                i[2]+=1
            else :
                j+=1
        if sum!=0 :
            i[2]=round(sum/i[2],2)
        print(i[0]+'~'+i[1]+'~',i[2],sep='')
li=[]
grade=[]
x=input()
while x!='Students':
    x=input()
stu_input(li)
li.sort()
inp_grade(grade)
cal()"""

"""t=int(input())
for t in range(t):
    a,b = map(int, input().split())
    l=list(map(int, input().split()[:a]))
    for i in range(len(l)):
        if ((l[i])<=b):
            b=b-l[i]
            print("1",end="")
            #print(c)
            #print(l[i])
            #print(0)
        else:
            print("0",end="")
            #break
    print()"""


"""def length(self):
    if self.value == None:
        return (0)
    elif self.next == None:
        return (1)
    else:
        return (self.length() is 1 + self.next.length())

print(length())"""

"""t=int(input())
for t in range(t):
    s=str(input())
    r=str(input())
    s=list(s).count()
    r=list(r).count()
    if(r==s):
        print("Arjun")
    else:
        print("Amit")"""


"""import numpy as np

a=np.array([[1, 2, 4], [5, 8, 7]])
print ("Array created using passed list:\n", a)

a = np.array([[1, 2, 3], [3, 4, 5], [9, 6, 10]])

print("\nOriginal array:\n", a)
print("Transpose of array:\n", a.T)"""

"""import numpy as np
import time
import sys

size=10000000

l1=range(size)
l2=range(size)

a1=np.arange(size)
a2=np.arange(size)

start=time.time()
result=[(x+y) for x,y in zip(l1,l2)]
print("time list",(time.time()-start)*1000)

start=time.time()
result=a1+a2
print("time numpy",(time.time()-start)*1000)"""

"""import numpy as np
a=np.array([1,2,3])
print(a.ndim)
print(a)
a1=np.array([[1,2,3],[1,2,3],[3,4,5]])
print(a1.ndim)
print(a1)
print(a*a1)
print(a1.shape)
s=np.zeros((3,3))
print(s)"""
"""import numpy as np
n,m=map(int,input().split())
shape = (n, m)
data = np.array(input().split()).reshape(shape)
print(data)
print(data.T)"""
"""import numpy as np
a1=np.array([[1,2,3],[1,2,3],[3,4,5]])
print(a1)
print(a1.sum(axis=0))
print(a1.sum(axis=1))"""

"""import numpy as np
n,m=map(int, input().split())
shape=(n,m)
a=np.array(input().split()).reshape(shape)
print (str(a).replace(' ','').replace('.',' ').replace('[','').replace(']',''))"""

"""import math
def magic():
    infy=math.inf
#2D array
    a,b=map(int,input().split())
    n,m=map(int,input().split())
    l=[[ 0 for  i in range(n)] for j in range(n)]
    l1=list(map(int,input().split()))
    for i in range(m):
        n1,n2,n3=map(int,input().split())
        l[n1-1][n2-1]=n3
        l[n2-1][n1-1]=n3
    #print(l)
   #simple implementation of dijkstra
    for i in range(n):
        for j in range(n):
            if(i != j and l[i][j] == 0):
                l[i][j]=infy
            if (i == j):
                l[i][j] = 0
            elif (j == (b - 1)):
                l[i][j] = l[i][j]
            if (l[i][j] < l1[j] and j != (b - 1) and i != j):
                l[i][j] = l1[j]
            elif (l[i][j] > l1[j] and j != (b - 1) and i != j and l[i][j] != infy):
                ab = int(l[i][j] / l1[j])
                ab1 = l[i][j] - (ab * l1[j])
                if (ab1 == 0):
                    l[i][j] = l[i][j]
                else:
                    ab2 = l1[j] - ab1
                    l[i][j] = l[i][j] + ab2
    for k in range(n):
        for i in range(n):
            for j in range(n):
                c = l[i][k] + l[k][j]
                if (l[i][j] > c):
                    l[i][j] = c
                    #   print(l)
    print(l[a - 1][b - 1])
magic()"""

"""import numpy as np
n = int(input("Enter the number of rows in a matrix: "))
a = [[0] * n for i in range(n)]

for i in range(n):
   for j in range(n):
        a[i][j] = int(input())
print(np.matrix(a))"""

"""c = 'F'
a=ord(c)
#print("The ASCII value of '" + c + "' is",ord(c))
#print(ord(70))
print(a)
d='Q'
b=ord(d)
print(b)
for i in range(a,b):
    print(i)"""
"""c,d='F','Q'
a,b=ord(c),ord(d)
for i in range(a,b):
    print(i)"""

"""n=int(input("Enter the matrix size(row)"))
#m=int(input("column"))
import numpy as np
mat=np.zeros((n,n))
for i in range(n):
    #for j in range(m):
    mat[i]=input().split(" ")

print(mat)
print(' ' + mat[1:-1])"""

"""n = int(input())
ar = []
bestvals = []
best_stored = []
for x in range(n):
  ar.append(int(input()))
  best_stored.append(0)

best_stored[0] = 1

for i in range(n):
  maxval = 1
  for j in range(i):
    if ar[i] % ar[j] == 0:
      maxval = max(maxval,(best_stored[j])+1)
  best_stored[i] = maxval

print(max(best_stored))"""

"""t=int(input())
for t in range(t):
    n,m=map(int,input().split())
    count=0
    l=list(map(int,input().split()[:n]))
    a=sorted(l,reverse=True)
    for i in range(len(a)):
        if(a[i]>=a[m-1]):
            count=count+1
    print(count)"""


"""def printPairs(arr, arr_size, sum):
    # s = set()
    for i in range(0, arr_size):
        temp = sum - arr[i]
        if (temp > 0 and temp in arr):
            # print( arr[i], "and", temp)
            return 1
            # s.add(arr[i])
    return 0

t = int(input())
for t in range(t):
    n = int(input())
    A = [6, 10, 14, 15, 21, 22, 26, 33, 34, 35, 38, 39, 46, 51, 55, 57, 58, 62, 65, 69, 74, 77, 82, 85, 86, 87, 91, 93, 94, 95]
    
    if (n in A):
        print("NO")
    elif (printPairs(A, len(A), n) != 0):
        print("YES")
    elif (printPairs(A, len(A), n) == 0):
        print("NO")"""

"""t=int(input())
for t in range(t):
    l=list(map(int,input().split()))
    a=l[0]
    b=l[1]
    c=l[2]
    if((a+b)//c)%2==0:
        print("CHEF")
    else:
        print("COOK")"""

"""s=input()
print(s.title())"""

# t=int(input())
# for t in range(t):
#     n=[2010,2015,2016,2017,2019]
#     a=int(input())
#     if(a in n):
#         print("HOSTED")
#     else:
#         print("NOT HOSTED")


t=int(input())
for t in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()[:n]))
    #print(a)
    a.sort(reverse=True)
    #print(a)
    for i in range(k):
        a[i]=1
    #print(a)
    n=sum(a)
    #print(n)
    c = [x * x for x in a]
    #print(c)
    g=sum(c)
    #print(g)
    if(g<=n):
        print("YES")
    else:
        print("NO")












