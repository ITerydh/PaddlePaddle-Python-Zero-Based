#!/usr/bin/env python
# coding: utf-8

# In[1]:


print('Hello World!')


# In[2]:


print('上课时间：', 2,'小时')


# In[3]:


n = input('输入您的名字:')
print(n)


# In[4]:


# python的小Demo代码
"""
猜数字小游戏  
"""

my_number = 3200  # 这是真实的价格
guess_number = input('这台冰箱多少钱？')   # 所有符号都是英文标点（半角字符）
guess_number = int(guess_number)            #input默认全部为string，转换为int数字
while guess_number != my_number:          #循环进行游戏
    if guess_number<my_number:               # 使用缩进来标识代码段
        guess_number = input('猜低了！再猜')
        guess_number = int(guess_number)
    else:
        guess_number = input('猜高了！再猜')
        guess_number = int(guess_number)
print('\n恭喜您，猜对了！\n')


# In[5]:


# 认识运算符
print(1+2)   # 加法
print(1-2)   # 减法
print(1*2)   # 乘法
print(1/2)   # 除法
print(1//2)  # 整除 (向下取整)
print(1%2)   # 取余数
print(2**2)  # 幂运算
print(2020- 5*5/2 +8**1)   #结合顺序和一般的数学运算符一样

# 浮点数的计算精度
print(0.1+0.2)

#此外浮点数+整数会变为浮点数
print(1+0.1)


# In[7]:


print('this is a string')
print("yes")
print('爸爸说："今天我做饭"')
print("爸爸说：\"今天我做饭\"")
print(len('hello world!'))


# In[8]:


print(1==2)
print(1==1)


# In[9]:


number = 1
number = 5.5
number = 'number'

# 给变量赋值
Number = 5
number = 10.5
NUMBER = 20

name = 'iterhui'
beautiful = True 

# 给变量赋值
number += 2
number -= 5
number *= 4
number /= 6
number %= 2
number **= 5
number //= 5


# In[11]:


a = int(2.5)
b= str(4)
c = bool(3)  # 非0： Ture 其它 False
d = float('0.6')

print(a,b,c,d)


# In[14]:


list1 = [1, 2, 3, 4, 5 ]
list2 = ["a", "b", "c", "d","e","f"]
list3 = ['physics', 'chemistry', 1997, 2000]
print(list1)
print(list2)
print(list3)

len(list1)
print(len(list1))

list1[4]
print(list1[4])

list3.append(5)
print(list3)

list1.pop()
print(list1)


# In[15]:


tuple1 = (1, 2, 3, 4, 5 )
tuple2 = ("a", "b", "c", "d","e","f")
tuple3 = ('physics', 'chemistry', 1997, 2000)
print(tuple1)
print(tuple2)
print(tuple3)

print(len(tuple1))

tuple1.append(3)
print(tuple1)


# In[17]:


word = {'apple':'苹果','banana':'香蕉'}
scores = {'小张':100, '小李':80}
grad = {4:'很好',3: '好',2:'中',1:'差',0:'很差'}

print(word.get('apple'))

#增加数据 
scores['小赵']=60
print(scores)


# In[19]:


s = [1,1,2,3,4,8,5]

s =set(s)

#注意看，set是集合的意思，集合就会自动去重复和排序
print(s)


# In[20]:


score = 80
if score < 60:
    print('不及格')
else:
    print('及格')


# In[21]:


# 多分支：红灯停 绿灯行

light = '红灯'

if light == '红灯':
    print('停')
elif light == '绿灯':
    print('行')
else:
    print('等一等')


# In[22]:


# 从1数到9
number = 1
while number<10:   # 注意边界条件
    print(number)
    number+=1

my_number = 3200  # 这是真实的价格
guess_number = input('这台冰箱多少钱？') 
guess_number = int(guess_number)
while guess_number != my_number:
    if guess_number<my_number:   
        guess_number = input('猜低了！再猜')
        guess_number = int(guess_number)
    else:
        guess_number = input('猜高了！再猜')
        guess_number = int(guess_number)
print('\n恭喜您，猜对了！\n')


# In[23]:


for i in range(9):
    print(i+1)

fruits = ['banana', 'apple',  'mango']
for fruit in fruits:        # 第一个实例
    print( '当前水果 :', fruit)
    
for letter in 'Python':     # 第二个实例
    print( '当前字母 :', letter)
 


# In[26]:


# continue : 跳过本轮 
# 打印1-10中的偶数 
for i in range(10):
    num = i+1
    if num%2 != 0:
        continue
    print(num)


# In[31]:


# 查找list_1 中的数字
list_1 = [1,6,3,2,8,4,3]
for number in list_1:
    if number == 3:
        print("找到了",list_1[number])
        break  
        
print() #换行用
        
#结果没有输出两个，证明break执行了
list_1 = [1,6,3,2,8,4,3]
for number in list_1:
    if number == 3:
        print("找到了",list_1[number])


# In[32]:


# pass： 占位，还没想好怎么写，先让程序跑起来
for i in range(5):
    pass


# In[34]:


name = 'molly'
a = name[1]  
b = name[-4]
c = name[1:4]
d = name[::-1]
print(a)
print(b)
print(c)
print(d)

# 小练习
string = 'Hello world!'
a = string[2]
b = string[2:5]
c =  string[3:]
d = string[8:2:-1]
print(a)
print(b)
print(c)
print(d)


# In[35]:


# 如果字符串以'p'结尾，则打印
list_string = ['apple','banana_p','orange','cherry_p']
for fruit in list_string:
    if fruit[-1] == 'p':
        print(fruit)


# In[37]:


my_string = 'hello_world'
a = my_string.count('o')
print(a)

article = 'Disney and Marvel’s upcoming superhero epic should light the box office on fire when it launches this weekend, with the hopes of setting domestic, international, and global records. In North America alone, “Avengers: Endgame” is expected to earn between $250 million and $268 million in its first three days of release. If it hits the higher part of that range it would qualify as the biggest domestic debut of all time, a distinction currently held by 2018’s “Avengers: Infinity War,” the precursor to “Endgame,” which launched with $257.7 million.'
b=  article.count('and')
print(b)

my_string = 'aabcabca'
c = my_string.count('abca')
print(c)


# In[38]:


my_string = 'hello_world'
a = my_string.find('o')
print(a)

my_string = 'hello_world'
b= my_string.index('o')
print(b)


# In[40]:


my_string = 'hello_world'
a = my_string.startswith('hello')  # 是否以hello开始
b = string.endswith('world')   # 是否以world结尾
print(a)
print(b)


# In[42]:


my_string = 'hello_world'
a = my_string.split('_')

print(a) #默认 为数组，也就是列表
print(type(a))


# In[43]:


my_string = 'hello_world'
newStr = my_string.replace('_',' ')
print(newStr)


# In[44]:


my_string = ' hello world\n'
str = my_string.strip()
print(str)


# In[45]:


my_string = 'Hello_World'
up = my_string.upper()
low = my_string.lower()
cap = my_string.capitalize()
print(up)
print(low)
print(cap)


# In[54]:


accuracy = 80/123
print('老板！我的模型正确率是', accuracy,'!')

accuracy = 80/123
print('老板！我的模型正确率是%s!' % accuracy)

accuracy = 80/123
print('老板！我的模型正确率是%.2f!' % accuracy)

name = 'iterhui'
hight = 172.1
score_math = 150
score_cet4 = 710
print('大家好！我叫%s，我的身高是%d cm, 数学成绩%.2f分,英语成绩%d分' % (name, hight, score_math, score_cet4))
print('大家好！我叫{}，我的身高是{:d} cm, 数学成绩{:.2f}分,英语成绩{}分'.format(name, int(hight), score_math, score_cet4))
#python3.6之后的
print(f"大家好！我叫{name}，我的身高是{hight:.0f} cm, 数学成绩{score_math:.2f}分,英语成绩{score_cet4}分")


# In[55]:


list1 = ['a','b','c','d','e','f']
list1[2]
list1[2:5]


# In[56]:


list1 = ['a','b','c','d','e','f']
list1.append('g') # 在末尾添加元素
print(list1)
list1.insert(2, 'ooo')  # 在指定位置添加元素，如果指定的下标不存在，那么就是在末尾添加
print(list1)

list2 = ['z','y','x']
list1.extend(list2) #合并两个list   list2中仍有元素
print(list1)
print(list2)


# In[57]:


list1 = ['a','b','a','d','a','f']
print(list1.count('a')) 

list1 = ['a','b','a','d','a','f']
print(list1.index('a')) 

print('a' in list1)


# In[58]:


list1 = ['a','b','a','d','a','f']
print(list1.pop(3)) 
print(list1)
list1.remove('a')
print(list1)


# In[59]:


# 有点土但是有效的方法
list_1 = [1,2,3,4,5]
for i in range(len(list_1)):
    list_1[i] += 1

list_1  


# In[60]:


# pythonic的方法 完全等效但是非常简洁
[n+1 for n in list_1]


# In[61]:


# 1-10之间所有数的平方 
[(n+1)**2 for n in range(10)]


# In[69]:


list1 = ['a','b','a','d','a','f']
a = ['app_%s'%n for n in range(10)]
print(a)


# In[65]:


[m + n for m in 'ABC' for n in 'XYZ']


# In[72]:


# 第一种方法：类似列表生成式
L = [x * x for x in range(10)]
print(L)


# In[73]:


g = (x * x for x in range(10))
print(g)


# In[74]:


next(g)


# In[75]:


next(g)


# In[77]:


# 练习 斐波那契数列
def feb(max_num):
    n_1 = 1
    n_2 = 1
    n = 0
    while n<max_num:
        if n == 0 or n == 1:
            yield 1
            n += 1
        else:
            yield n_1 + n_2
            new_n_2 = n_1 
            n_1 = n_1 + n_2
            n_2 = new_n_2
            n += 1
g = feb(20)
for n in g:
    print(n,end="    ")


# In[78]:


list1 = [1,2,3,4,'5',6,7,8]
n=1
for i in range(len(list1)):
    print(i)
    try:
        list1[i]+=1
        print(list1)
    except IOError as e:
        print(e)
        print('输入输出异常')
    except:
        print('有错误发生')
    else:
        print('正确执行')
    finally:
        print('我总是会被执行')


# In[80]:


def student_name(name):
    "打印学生的名字"
    print('姓名：', name)
    return {'姓名':name}
rst = student_name('Alice')
type(rst) 


# In[81]:


## 函数的嵌套调用
def worker(s):
    rst = 10 / float(s)
    return rst

def group_leader(s):
    rst = worker(s) * 2
    return rst

def CTO(s):
    return group_leader(s)

CTO('4')


# In[82]:


def student_name_and_age(name, age):
    print('姓名：%s 年龄 %s' %(name, age))

student_name_and_age('张三', 18)


# In[83]:


def student_name_and_age(name, age='不愿透露'):
    "设置默认参数"
    print('姓名：%s 年龄 %s' %(name, age))
student_name_and_age('张三')


# In[84]:


def all_student_names(*names):
    for name in names:
        print('姓名：', name)
        
all_student_names('张三','李四','王五')


# In[85]:


def student_info(name, age, **kw):
    print(f'我的名字叫：{name},年龄：{age},其它信息：{kw}')
student_info('张三', 18, height=180)


# In[86]:


def print_person_info(name, age, *, height, weight):
    print('我的名字叫：', name, '年龄：', age,'身高', height, '体重', weight)
print_person_info('张三', 18, height=180, weight=75)


# In[87]:


def student_info(name, age=18, *books, **kw):
    print('我的名字叫：', name, '年龄：', age,'其它信息：',kw)
    if 'city' in kw:
        print('来自：', kw['city'])
    for book in books:
        print('我有',book,'书')
student_info('张三', 18, '语文','数学','计算机', city='北京', height=180, weight=75)


# In[88]:


lambda arg1, arg2: arg1 + arg2


# In[89]:


(lambda arg1, arg2: arg1 + arg2)(1,2)


# In[90]:


sorted([36, 5, -12, 9, -21])


# In[91]:


sorted([36, 5, -12, 9, -21], reverse=True)


# In[93]:


points = [(5,2), (7,3), (3,4),(1,1),(2,6)]  # 按x坐标排序 y坐标排序 和0点距离排序
print(points)


# In[94]:


import time 


# In[95]:


print(time.time())
time.sleep(1)
print(time.time())


# In[96]:


class Athlete:
   def __init__(self,a_name,a_dob=None,a_times=[]):
       self.name = a_name
       self.dob = a_dob
       self.times = a_times
   def top3(self):
       return sorted(set([self.sanitize(t) for t in self.times]))[0:3]
   def sanitize(self,time_string):
       if '-' in time_string:
           splitter = '-'
       elif ':' in time_string:
           splitter = ':'
       else:
           return (time_string)
       (mins,secs) = time_string.split(splitter)
       return (mins+'.'+secs)


class Rugby(Athlete):
   def __init__(self,a_name,a_dob,a_squat,a_times):
       
       #调用父类的构造方法，传递的参数为a_dob、a_times
       Athlete.__init__(self,a_name,a_dob,a_times)   
       #将a_squat赋值给类属性squat
       self.squat = a_squat


# In[97]:


#代码1，定义OtherAthlete类继承Athlete
class OtherAthlete(Athlete):
    def __init__(self,a_name,a_dob,a_squat,a_times):
        Athlete.__init__(self,a_name,a_dob,a_times)

        self.squat = a_squat

    def top3(self):
    #代码2，定义无参数top3函数，对self.times属性应用统一化和排序功能
        return sorted([self.sanitize(t) for t in self.times])[0:3]


# In[105]:


#3题 定义print_rugby函数，以多态的方式调用子类属性和方法  （5分）
def get_coach_data(filename):
    with open(filename) as f:
        line = f.readline()
    return line.strip().split(',')

loren = get_coach_data('loren.txt')
mark = get_coach_data('mark.txt')

loren = Rugby(loren.pop(0),loren.pop(0),loren.pop(0),loren)
mark = OtherAthlete(mark.pop(0),mark.pop(0),mark.pop(0),mark)

def print_rugby(athlete):
    print(athlete.name)
    #代码1，打印athlete的属性dob、squat和top3方法的返回值
    print(athlete.dob)
    print(athlete.squat)
    print(athlete.top3())
    
#代码2，调用print_rugby函数，参数为loren
print_rugby(loren)

#代码3，调用print_rugby函数，参数为mark
print_rugby(mark)


# In[ ]:


# 请在此处完成代码
def get_coach_data(filename):
    with open(filename) as f:
        line = f.readline()
    return line.strip().split(',')

class Student:
    def __init__(self,name,dob,age,gender,score=[]):
        self.name = name
        self.dob = dob
        self.age = age
        self.gender = gender
        self.score = score

    def top3(self):
        return sorted(set([self.sanitize(t) for t in self.score]))[-3:]

    def sanitize(self,time_string):
        if '-' in time_string:
            splitter = '-'
        else:
            return (time_string)
        (mins,secs) = time_string.split(splitter)
        return secs

    def print_info(self):
        print('姓名:',self.name,end='')
        print(' 生日:',self.dob,end='')
        print(' 年龄:',self.age,end='')
        print(' 性别:',self.gender,end='')
        print(' 分数:',self.top3(),end='\n')

stu1_data = get_coach_data('stu1.txt')
stu2_data = get_coach_data('stu2.txt')
stu3_data = get_coach_data('stu3.txt')
stu4_data = get_coach_data('stu4.txt')

stu_list = []

stu_list.append(Student(stu1_data.pop(0),stu1_data.pop(0),stu1_data.pop(0),stu1_data.pop(0),stu1_data).print_info())
stu_list.append(Student(stu2_data.pop(0),stu2_data.pop(0),stu2_data.pop(0),stu2_data.pop(0),stu2_data).print_info())
stu_list.append(Student(stu3_data.pop(0),stu3_data.pop(0),stu3_data.pop(0),stu3_data.pop(0),stu3_data).print_info())
stu_list.append(Student(stu4_data.pop(0),stu4_data.pop(0),stu4_data.pop(0),stu4_data.pop(0),stu4_data).print_info())


# In[ ]:


# 请在此处完成代码
class Spostudent(Student):
    def __init__(self,name,dob,age,gender,spe,score=[]):
        #调用父类__init__
        Student.__init__(self,name,dob,age,gender,score)
        self.spe = spe

    def top3(self):
        return sorted(list([self.sanitize(t) for t in self.score]))[:3]

    def print_info(self):
        print('姓名:',self.name,end='')
        print(' 生日:',self.dob,end='')
        print(' 年龄:',self.age,end='')
        print(' 性别:',self.gender,end='')
        print(' 分数:',self.top3(),end='')
        print(' 特长分:',self.spe,end='\n')

class Artstudent(Spostudent):
    def __init__(self,name,dob,age,gender,spe,score=[]):
        #调用父类__init__
        Spostudent.__init__(self,name,dob,age,gender,spe,score)

    def top3(self):
        return sorted(list([self.sanitize(t) for t in self.score]))[-3:]

stu5_data = get_coach_data('stu5.txt')
stu6_data = get_coach_data('stu6.txt')

Spostudent(stu5_data.pop(0),stu5_data.pop(0),stu5_data.pop(0),stu5_data.pop(0),stu5_data.pop(0),stu5_data).print_info()

Artstudent(stu6_data.pop(0),stu6_data.pop(0),stu6_data.pop(0),stu6_data.pop(0),stu6_data.pop(0),stu6_data).print_info()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




