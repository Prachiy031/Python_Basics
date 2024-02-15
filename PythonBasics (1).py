#!/usr/bin/env python
# coding: utf-8

# # basic Python

# needed for ds
# 

# In[1]:


print("Hello")


# # variables

# In[2]:


x = 2
print(type(x))


# In[3]:


y  = 4.567
print(type(y))


# multiple assignment

# In[15]:


a,d,l,k = 4.5,6,'i',78800
print(type(a))
print(type(d))


# In[7]:


c = 3+7j
print(type(c))


# In[8]:


del a #deletes a


# In[12]:


print(a)     #verified as a is deleted or not


# all variables in notebook using whos
# 
# 

# In[16]:


get_ipython().run_line_magic('whos', '')


# # operators
# 

# In[18]:


r = 6+7
print(r)


# In[19]:


t = 8**5  #power
print(t)


# In[20]:


6/7


# In[21]:


_         # this is most recent value ..inbuilt in python dont reassign _ to any value


# In[26]:


5//2         #floor division


# # boolean

# In[28]:


l = True
m =  False
n = True
get_ipython().run_line_magic('whos', '')


# In[30]:


print(l and m)
print(m and n)
print(l or m)


# In[38]:


not(l)



# In[42]:


#initially and will apply then or if parenthesis is not there
print(True or False and False)           #and -false => true or false =true
print((True or False) and False)           #true or false = true=> true and false = false


# comparison operators are same like other lang

# rounding function =>

# In[51]:


print(round(2.5343)) #nearest integer
print(round(4.55758,3))   # rounding number upto no. of 2nd argument after decimal point


# divmod function
# 

# In[52]:


divmod(27,5)   #return quotient and remainder


# In[53]:


type(_)


# isinstance function

# In[54]:


print(isinstance(1,int))            #return  true if 1st argument is an instance of that class .multipleclasses can also be checked at once


# In[55]:


print(isinstance(1.0,int))       


# In[58]:


print(isinstance(1.0,(int,float))) 


# power function

# In[59]:


pow(3,4)


# In[60]:


pow(3,3,4)  #if three arguments then 3 raised to 3 modulo 4 


# input function

# In[61]:


a = input("enter number") #even number is considerd as string


# In[62]:


type(a)


# In[63]:


a = int(a)


# In[64]:


type(a)


# In[65]:


#or initially also do 
u = float(input("enter real value : "))


# In[66]:


type(u)


# control flow
# 

# In[70]:


a = 5
b = 7
if a==b:
    print("hello")
elif a>b:
    print("bye")
else:
    print("heya")


# In[72]:


a = 5    #short form of above
b = 7
print("hello") if a==b else print("bye") if a>b else print("heya")


# In[8]:


n = int(input('Max iterations : '))
i = 1
while i<n :
    print(i)
    i+=1         #i=i+1
print('done')


# break continue statement
# 

# In[10]:


n = 10
i = 1
while True:
    
    if i%9 == 0:
        print("inside if")
        break;
        
    else:
        print("inside else")
        i+=1
        
print("done")


# In[22]:


n = 10
i = 1
while True:
    if i%9 != 0:
        print("inside if")
        i+=1
        continue 
    print("something")
    print("someting else")
    break
    
print("done")


# In[42]:


L = []   #list(collection of elements)              #control flow (for loop)
for i in range(10):
   print(i+1)
   L.append(i**2)
print(L)


# In[44]:


L = []   #list(collection of elements)              #control flow (for loop)
for i in range(0,10,2):     #initial,end,iteration
   print(i)
   L.append(i**2)
print(L)


# else in for loop

# In[68]:


S = {"apple",4.9,"cherry"}
for x in S:
     print(x)
else:
    print("Loop completes its iteration")
print("out side the loop")


# In[95]:


S = {"apple",4.9,"cherry"}
i = 1
for x in S:
     print(x)
     i+=1
     if i==3:
        break
     else:
        pass
else:             #this is for "for" loop if for loop is breaked then else will not work 
    print("Loop completes its iteration")
print("out side the loop")


# In[98]:


#dictionary
d = {"apple":44,"cherry":"game"} #key :value
for x in d:
    print(x,d[x])


# In[125]:


l = [1,2,3,4,-5,-6]
for j in range(len(l)):
  min = l[j]
  idx = j
  c = j
  for i in range(j,len(l)):
    if l[i]<min:
        min = l[i]
        idx = c
    c+=1
    temp = l[j]
    l[j] = min
    l[idx] = temp


#i+=1
    


# In[126]:


l


# # functions

# In[134]:


def printSuccess():        #definition of function 
    """test cases status"""   #this is documentation for function i.e docsum
    print("Test case successfully executed")


# In[139]:


printSuccess()  #calling of function


# In[148]:


printSuccess?? #this will show docstring also 


# In[149]:


printSuccess??  #whole implementation


# In[150]:


help(printSuccess)


# input arguments

# In[162]:


def printMessage(msg):
    print(msg)


# In[163]:


printMessage("heya")


# In[194]:


def printm(msg):
   """this function prints message supplied by 
   user or prints that msg is not in form of string """ 
  
            if isinstance(msg,str):
              print(msg)
            else:
             print("your input argument is not string")
             print("here is type of your input: ",type(msg))


# In[197]:


printm("moye moye")


# In[198]:


printm(45)


# In[199]:


def f(a,b,c):
    print("a is ",a)
    print("b is ",b)
    print("c is ",c)


# In[200]:


f("game",90,6.67)


# In[201]:


f(a=90,b="prachi",c=800)


# In[202]:


f(b="prachi",c=800,a=90) #even though order is changed output remain same


# In[203]:


def f():
    s=9
    g=8
    return s+g


# In[204]:


f()


# In[205]:


type(f())


# In[215]:


def g():
    print("heyaaa")
    return          #return has act as a break statement
    print("function has returned nothing")


# In[213]:


g()


# In[214]:


print(type(g()))


# In[222]:


def f():         #return multiple values
    s=9
    g=8
    y=90
    return s,g,y


# In[223]:


f()


# In[233]:


#variable number of arguments
def add(*args):      """*args acts as a list its length depends upon no. of arguments passing"""
    sum=0
    for i in range(len(args)):
     sum+=args[i]
    return sum
    


# In[234]:


add(6,4,2)


# In[235]:


add(6,2,34,4)


# In[245]:


def printAllVariablesAndVAlues(**args):   #for dictionary (key value pair)
    for x in args:
        print("variable name is :",x," and values are : ",args[x])


# In[246]:


printAllVariablesAndVAlues(a=90,g=908,h="yusja")


# In[251]:


#default value function 
def ff(l=[4,5]):  #this list is created when function is defined
    for i in l:
        print(i)


# In[252]:


l2=[24,58,6]


# In[254]:


ff(l2)  


# In[257]:


ff()   #now l value cant be l2 as by defalut l value is given in ff


# In[263]:


#not default value function
   l=[4,5]
   l2=l
   l2[0] = -89
   print(l)
   
       


# # module

# file containing set of functions,may contain variables that you have to use further so you can import that

# In[36]:


import sys
sys.path.append("C:/Users/Prachi Yadav/Desktop/TY/projects/python/modules/UniversalFunctions.py")


# In[37]:


import UniversalFunctions


# In[38]:


myfs.addAllNumerics(4,5,6,7,8)


# you can import whole model or required function in model

# In[39]:


from UniversalFunctions import addAllNumerics


# In[40]:


print(addAllNumerics(5,6,7))


#  # package:set of  modules 
string
# In[1]:


v = "Python and R are useful for ds"


# In[2]:


print(v)


# In[3]:


g = "do you wanted to be data engineer?"


# In[4]:


print(g+" "+v)


# In[6]:


price = 900
print("price of course is : "+str(price))
#or
print("price of course is : ",price)


# In[8]:


#multiline string
a= """this is 1st line
  this is 2nd
and this is 3rd
"""
print(a)


# In[9]:


print("""shortcuts:
         F : find and replace
         Ctrl-Shift-F: open the command palette
        Ctrl-Shift-P: open the command palette
""")


# indexing and slicing

# In[19]:


a = "machine learning"
print(a[3:10])       #inclusive:exclusive


# In[24]:


print(a[-5:-1])   # go till -5 then again go back to -1 including 


# In[26]:


a[-12:-3]


# slicing:access part of string

# In[29]:


#strings are immutable.....cant be change same string
#slicing
print(a[0:16:2])     # [start:end:step]  start from 0 until 16 with steps of 2


# In[30]:


a[:16]     #default start is 0 if not mentioned


# In[32]:


a[0:]     #default end is last 


# In[34]:


a[2:5] #default step is one


# In[47]:


a[::-1]   #if start and end is not mentioned then they are reversed


# In[51]:


r = slice(2,7,3)   #slice function 
print(a[r])


# In[55]:


stringhavingspaces="      hi      this    is prachi    "
print(stringhavingspaces.strip())    #strip function will remove spaces from initial and end


# In[57]:


r = "HJKy ljka s"  
r.lower() #lower case            #originial string is not modified as this functions give new string


# In[59]:


r.upper()  #upper case


# In[1]:


"wed".upper()


# In[61]:


r.replace('K','O') #replace


# split (used to split string into list of strings based using caharacter provided

# In[62]:


y="ipajnjkan;adba;uaidb"
print(y.split(";")) #split from ; we get list of those further we can access them 


# In[69]:


r.isupper()


# In[1]:


"abc"=="abc"   #comparison


# In[3]:


"abc"<"gds"  #according to alphabetical order


# In[5]:


#esacape character
print("we are learning \"string\"here")  #whatever after \ is considered as it is it doesent mean that it is special string there 


# In[8]:


print('learning "string"') #' ' this is also escape character


# In[9]:


print("we are \t learning strings  ")  #\t is tab


# In[12]:


print("c:\name\drive")   #here \n from name is considerd as a new line to avoid above use r in front of string so it is considered as a raw string  


# In[13]:


print(r"c:\name\drive")


# inserting values inside string

# In[7]:


cost_of_ice_bag = 30
profit_margin = 0.02
number_of_bags = 8
out_template = """If a grocery strore sells ice bags at ${} per bag,with profit margin of ${} then total profit by selling is ${} ice bags is ${}"""
print(out_template)


# by writing {} inside string and further formating what values are to be added in format () as arguments in sequence

# In[10]:


total_profit = cost_of_ice_bag * number_of_bags*profit_margin
out_msg = out_template.format(cost_of_ice_bag,profit_margin*100,total_profit,number_of_bags)
print(out_msg)


# or you can add those using string concatenation but inthis youve to convert it into string first 
# e.g.
# "profit is "+string(profit)

# # data structures

# List
# 

# ordered mutable(changeable) duplicates

# Tuple
# 

# ordered immutable duplicates

# set

# unordered mutable(addable,removable) no duplicates

# dictionary

# unorderd changeable no duplicates

# In[65]:


List = [1,23,4,5,63,7.8,"name",90]
Tuple = (1,23,4,5,63,7.8,"name",90)
Set = {1,23,4,5,63,7.8,"name",90}
Dict = {23:"twentythree","bob":56,78:"prachi","hu":"ji"}


# In[66]:


print("the type of List is :",type(List))
print("the type of Tuple is :",type(Tuple))
print("the type of Set is :",type(Set))
print("the type of Dict is :",type(Dict))


# In[67]:


#accessing
print(List[3])
print(Tuple[3])
print(23 in Set) #return true if present otherwise false
print(Dict[23]) #return key


# In[68]:


#indexing 


# In[69]:


List[1:3]


# In[70]:


Tuple[3:6]


# In[77]:


#adding in list
List = List + ["Hey","are","anyone","available"]


# In[78]:


List.append("hey")


# In[79]:


List


# In[80]:


Tuple2 = ("fsaf",8939,"kjdsf")
Tuple3 = Tuple+Tuple2    #cannot add,update,delete element from tuple but for adding we can add another tuple in previous tuple


# In[81]:


Tuple3


# In[90]:


Set.add(78)


# In[91]:


Set


# In[92]:


Set.add("yiyas")


# In[93]:


Set


# In[96]:


Dict["newKey"]="newValue"
Dict


# In[97]:


#adding two dictionaries using'|'operator
Dict2 = {"j":'jiya','p':"priya"}


# In[98]:


Dict2


# In[149]:


#print(Dict|Dict2)       
#OR using function update

Dict.update(Dict2)
Dict


# In[104]:


#deleting data
del List[3]       #using indexing


# In[105]:


List 


# In[106]:


#cannot delete from tuple


# In[137]:


Set.remove('yiyas')    


# In[138]:


Set


# In[143]:


del Dict[23]


# In[144]:


Dict


# In[150]:


#copy
List


# In[151]:


L2 = List


# In[152]:


L2


# In[157]:


L2[2]="four"
L2


# In[158]:


List


# In[159]:


#As List and l2 both are pointing to same structure in memory(accessing same memory) so
#whatever changed in L2 it will change in List too


# In[160]:


#so to avoid this (whatever changes in l2 should not reflect in List)
L3 = List.copy()      #same goes for set and dictionary
L3[2] = 4.5


# In[161]:


L3


# In[162]:


List


# In[167]:


Set2 =  Set


# In[168]:


Set2


# In[169]:


Set2.add(900)


# In[170]:


Set2


# In[171]:


Set


# In[172]:


Set3 = Set.copy()    


# In[173]:


Set3.add(899)


# In[174]:


Set3


# In[175]:


Set


# In[179]:


#copy function is not available for tuple
Tuple3 = Tuple


# In[180]:


Tuple3


# In[181]:


#slicing in List by default chooses copy of List ...it doesent consider reference


# In[182]:


L3 = List[1:4]    #it doesent change original list


# In[183]:


L3


# In[184]:


List


# In[187]:


Tuple.count(23)


# In[188]:


Dict.items()


# In[189]:


#list can contain anything in it like list,tuple,set,dict


# In[190]:


Dict0 = {"A":Dict,"B":List,"C":Tuple,"D":Set} #we have stored various datastructures in dictionary using key value pair


# In[ ]:


Dict0["A"]   


# In[ ]:


Dict0["B"][5]  #can access particular element from index


# In[ ]:


Dict0["D"]


# if dict doeseent have  any specific  key then default value is returned 

# In[14]:


persons = {"y":1,"g":7}


# In[17]:


persons.get("f","d")   #if not present then d will print otherwise its value will print


# In[13]:


"f" in persons


# In[ ]:


Set3 = {x**4 for x in range(2,10,3)}  #added 4th power of x in set


# In[ ]:





# In[ ]:


Set3


# In[ ]:


def getData():
    Data = {}
    while True:
        studentId = input("enter Student ID")
        marklist = input("enter marks in csv format")
        moreStudents = input('enter "no" to quit')
        if studentId in Data:
            print(studentId," is already available")
        else:
            Data[studentId] = marklist.split(",")
        if moreStudents.lower() == "no":
            return Data
        
        


# In[ ]:


StudentData = getData()


# In[ ]:


def getAvg(Data):
    avgMarks ={}
    for x in Data:
        List = Data[x]
        sum= 0
        for marks in L:
            sum+=int(marks)
        avgMarks[x] = s/len(List)
    return avgMarks


# In[ ]:


avgM = avgMarks(StudentData)


# In[ ]:


for x in avgM:
    print("student ",x," got avg marks as: ",avgM[x])


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




