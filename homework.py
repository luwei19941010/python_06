#-*-coding:utf-8-*-
# Author:Lu Wei
#1. 列举你了解的字典中的功能（字典独有）。
##get,update,del,pop,clear,key,values,items,
#
# 列举你了解的集合中的功能（集合独有）。
##intersection,union,difference,add,update,pop,remove,discard
#
# 列举你了解的可以转换为 布尔值且为False的值。
###0,'',[],(),{},set()
'''
#4.请用代码实现
info = {'name':'王刚蛋','hobby':'铁锤'}
循环提示用户输入，根据用户输入的值为键去字典中获取对应的值并输出。
循环提示用户输入，根据用户输入的值为键去字典中获取对应的值并输出
（如果key不存在，则获取默认“键不存在”，并输出）。 注意：无需考虑循环终止（写死循环即可）

info = {'name':'王刚蛋','hobby':'铁锤'}
while True:
    k=input('请输入name或hobby:')
    if k in info:
        print(info[k])
    else:
        print('建不存在')
        break

#5.请用代码验证 "name" 是否在字典的键中？
info = {'name':'王刚蛋','hobby':'铁锤','age':'18'}
if 'name' in info.keys():
    print('yes')
else:
    print('no')


#6.请用代码验证 "alex" 是否在字典的值中？
info = {'name':'王刚蛋','hobby':'铁锤','age':'18'}
if 'alex' in info.values():
    print('yes')
else:
    print('no')
#
flag='no'
for i in info.keys():
    if info[i]=='alex':
        flag='yes'
print(flag)
#
if 'alex' in list(info.values()):
    print('yes')
else:
    print('no')



#7.有如下
v1 = {'武沛齐','李杰','太白','景女神'}
v2 = {'李杰','景女神'}
# 请得到 v1 和 v2 的交集并输出
print(v1.intersection(v2))
# 请得到 v1 和 v2 的并集并输出
print(v1.union(v2))
# 请得到 v1 和 v2 的 差集并输出
print(v1.difference(v2))
# 请得到 v2 和 v1 的 差集并输出
print(v2.difference(v1))




#8. 循环提示用户输入，并将输入内容追加到列表中（如果输入N或n则停止循环）
User_list = []
while True:
    User_input=input('请输入：')
    if  User_input.lower()=='n':
        break
    User_list.append(User_input)
print(User_list)


#9. 循环提示用户输入，并将输入内容添加到集合中（如果输入N或n则停止循环）
User_Set=set()
while True:
    User_input=input('请输入：')
    if  User_input.lower()=='n':
        break
    User_Set.add(User_input)
print(User_Set)


#10.写代码实现
# 循环提示用户输入，如果输入值在v1中存在，则追加到v2中，如果v1中不存在，则添加到v1中。（如果输入N或n则停止循环）
v1 = {'alex','武sir','肖大'}
v2 = []
while True:
    User_input=input('请输入：')
    if User_input.upper()=='N':
        break
    if User_input in v1:
        v2.append(User_input)
    else:
        v1.add(User_input)
print(v1)
print(v2)

#11.判断以下值那个能做字典的key ？那个能做集合的元素？
# 1   key/value
# -1  key/value
# ""  key/value
# None key/value
# [1,2] value
# (1,)  key/value
# {11,22,33,4} value
# {'name':'wupeiq','age':18} value
d={'':1,'':'',None:None}
print(d)

#12.is 和 == 的区别？
###is判断内存地址是否相同，==判断值是否相同
#13.type使用方式及作用？
d={}
print(type(d))
###查看类型

#14.id的使用方式及作用？
d={}
print(id(d))
###查看内存地址
#15.看代码写结果并解释原因
v1 = {'k1':'v1','k2':[1,2,3]}
v2 = {'k1':'v1','k2':[1,2,3]}

result1 = v1 == v2
result2 = v1 is v2
print(result1)#Ture
print(result2)#False

#16.看代码写结果并解释原因

v1 = {'k1':'v1','k2':[1,2,3]}
v2 = v1

result1 = v1 == v2
result2 = v1 is v2
print(result1)#True
print(result2)#True


#17.看代码写结果并解释原因

v1 = {'k1':'v1','k2':[1,2,3]}
v2 = v1

v1['k1'] = 'wupeiqi'
print(v2)#{'k1':'wupeiqi','k2':[1,2,3]}

#18.看代码写结果并解释原因

v1 = '人生苦短，我用Python'
v2 = [1,2,3,4,v1]

v1 = "人生苦短，用毛线Python"

print(v2)#[1,2,3,4,'人生苦短，我用Python']

#19.看代码写结果并解释原因

info = [1,2,3]
userinfo = {'account':info, 'num':info, 'money':info}

info.append(9)#[1,2,3,9]
print(userinfo)#{'account':[1,2,3,9], 'num':[1,2,3,9], 'money':[1,2,3,9]}

info = "题怎么这么多"
print(userinfo)#{'account':[1,2,3,9], 'num':[1,2,3,9], 'money':[1,2,3,9]}


#20.看代码写结果并解释原因

info = [1,2,3]
userinfo = [info,info,info,info,info]

info[0] = '不仅多，还特么难呢'#['不仅多，还特么难呢',2,3]
print(info,userinfo)#[['不仅多，还特么难呢',2,3],['不仅多，还特么难呢',2,3],['不仅多，还特么难呢',2,3],['不仅多，还特么难呢',2,3]]


#21.看代码写结果并解释原因

info = [1,2,3]
userinfo = [info,info,info,info,info]

userinfo[2][0] = '闭嘴'#[['闭嘴',2,3],['闭嘴',2,3]，['闭嘴',2,3]，['闭嘴',2,3]，['闭嘴',2,3]]
print(info,userinfo)#


#22.看代码写结果并解释原因

info = [1,2,3]
user_list = []
for item in range(10):
    user_list.append(info)#[[1,2,3],[1,2,3],[1,2,3]...[1,2,3]]

info[1] = "是谁说Python好学的？"#

print(user_list)#[[1,"是谁说Python好学的？",3],[1,"是谁说Python好学的？",3],[1,"是谁说Python好学的？",3]...[1,"是谁说Python好学的？",3]]



#23.看代码写结果并解释原因

data = {}
for i in range(10):
    data['user'] = i#{'user'=9}

print(data)#{'user'=9}



#24.看代码写结果并解释原因

data_list = []
data = {}
for i in range(10):
    data['user'] = i#{'user'=9}
    print(id(data))
    data_list.append(data)#[{'user'=9},{'user'=9}..{'user'=9}]
print(data)
print(data_list)

#25.看代码写结果并解释原因

# data_list = []
# for i in range(10):
#     data = {}
#     data['user'] = i
#     data_list.append(data)#[{'user'=0},{'user'=2}..{'user'=9}]
# print(data_list)
'''
l=[1,2,3,4]
t=(1,2,3,4)
d = {}
e =set()
print(type(t))
a=l.pop()
b=l.remove(1)

print(a,b)


print(id(l))

