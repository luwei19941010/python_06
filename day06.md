### day06

#### 今日内容

- 集合
- 内存相关
- 深浅拷贝

#### 回顾补充

补充：列表list    reverse 反转。

###### list

- reverse 反转

  ```
  v1=[12,123,121,4551,21,123145]
  v1.reverse()
  print(v1)
  -->[123145, 21, 4551, 121, 123, 12]
  ```

- sort(reverse=False) 默认从小到大排序，（reverse=True）从大到小排序

  ```
  v1=[12,123,121,4551,21,123145]
  #v1.sort(reverse=False)#从小到大排序，默认
  v1.sort(reverse=True)#从大到小排序
  print(v1)
  ```

  

###### dict

- keys/values/items
- get

```
info={'k1':'v1','k2':'v2'}
v1=info.get('k22')#None 就是python中的空
v2=info.get('k1',123)
print(v1)
print(v2)

--> None
--> v1
#None数据类型，该类型表示空（无任何功能，专门用于提供空值）
```

- pop  删除值可以进行赋值

```
info={'k1':'v1','k2':'v2'}
result=info.pop('k2')
print(info,result)
-->{'k1': 'v1'} v2
```

- update

```
#如果key不存在直接添加，如果key存在则覆盖更新原来的value值
info={'k1':'v1','k2':'v2'}
info1={'k3':'v3','k4':'v4'}
info2={'k3':'v3','k1':'v4'}
#info['k3']='v3'
info.update(info1)
info.update(info2)
print(info)
```



```
info={'k1':'v1','k2':'v2'}
#默认按照键判断，即：判断X是否是字典的键
if 'x' in info：
	pass
#请判断：k1是否在其中
if 'k1' in v:
	pass
#请判断:v2是否在其中
方式一：循环判断
flag='不存在'
for v in  v.values()
	if v=='v2':
		flag='存在'
print(flag)
方式二：循环判断
if 'v2' in list(v.values()):#强制转换成列表['v1','v2','v3']
	pass
方式三：直接判断测试可以
if 'v1' in v.values()
	pass
#请判断：k2:v2是否在其中
value=v.get('k2')
if value=='v2'
	print('存在')
else：
	print('不存在')
```



- 练习题

```
#让用户输入任意字符串，然后判断此字符串是否包含指定的敏感字符
char_list=['大小王','淘宝'，'京东']

success=True
char_list=['大小王','淘宝','京东']
content=input('请输入:')

for i in char_list:
    #print(i)
    if i in content:
        success=False
        #print('含有敏感')
if success:
    print(content)
else:
    print('敏感')
```



#### 内容详细

##### 1.集合SET

特点：无重复且没有顺序的

```
v1={1,2,3,4,5,99,100 }
注意：v={}为dict，空集合表示v=set()
```



数据类型完整格式

```
None
int
	v1=123
bool
	v2=True/Flase
str
	v3=''
	v3=str()
list
	v4=[]
	v4=list()
tuple
	v5=()
	v5=tuple()
dict
	v6={}
	v6=dict()
set	
	v7=set()
```

###### 独有功能

添加add

```
v={1,2,3}
v.add(1)
v.add(4)
print(v)
```

删除/discard 清空/clear 随意移除/pop 移除/remove

```
#注意 remove不存在则报错，discard不存在不会报错，随意discard比remove好用
v={1,2,'李少奇'}
v.discard('李少奇')
print(v)
-->{1, 2}
-->set()
v={1,2,'李少奇'}
v.pop()
```



update 批量添加

```
v={1,2,'李少奇'}
v.update({11,22,33})
print(v)

-->{1, 2, 33, '李少奇', 22, 11}
```



交集（intersection）	

```
v={1,2,'李少奇'}
v1={1,2,3,4,5,}
result=v.intersection(v1)#####注意v1可以是列表，元组
print(result)
-->{1, 2}
```

并集（union）

```
v={1,2,'李少奇'}
v1={1,2,3,4,5,}
result=v.union(v1)#####注意v1可以是列表，元组
print(result)
-->{1, 2, 3, 4, 5, '李少奇'}
```

差集（difference）

```
v={1,2,'李少奇'}
v1={1,2,3,4,5,}
result=v.difference(v1)###注意：v中有且v1中没有的#####注意v1可以是列表，元组
print(result)
-->{'李少奇'}
```

对称差集(sysmmetric_difference)

```
v={1,2,'李少奇'}
v1={1,2,3,4,5,}
result=v.symmetric_difference(v1)#####注意v1可以是列表，元组
print(result)
-->{3, 4, 5, '李少奇'}
```



公共功能

- len

```
v={1,2,'luwei'}
print(len(v))
```

- 索引【无】
- 步长【无】
- 切片【无】
- 修改【无】
- 删除【无】del
- for循环

```
v={1,2,'李少奇'}
for  i  in v:
    print(i)
```

###### 嵌套问题

集合里面可以放 int str bool none tuple 。list、dict、set不行，由于它们可变，并且不能作为dict的key。

```
# ##################################################
# 1. 列表/字典/集合 -> 不能放在集合中+不能作为字典的key（unhashable）
# # info = {1, 2, 3, 4, True, "国风", None, (1, 2, 3)}
# # print(info)
# # 2. hash -> 哈希是怎么回事？
# # 因为在内部会将值进行哈希算法并得到一个数值（对应内存地址），以后用于快速查找。

```



##### 2.内存相关 明白赋值还是修改内部

###### 示例一： 

```
v1=[11,22,33]
v2=[11,22,33]
v1=66
v2=66
v1='asdf'
v2='asdf'
#按理说v1和v2应该是不同的内存地址，特殊:
	1.整型： -5~256
	2.字符串：含有下划线(_),字母，数字，不含有特殊字符.
	以上两类在python中进行了优化，python对常见的整型和字符串的内存地址进行了缓存。含有特殊字符的重新开辟新的内存地址。
```

###### 示例二:

```
v1=[11,22,33,44]
v1=[11,22,33]
print(v1)
-->[11,22,33]
```

###### 示例三：

```
v1=[11,22,33]
v2=v1
#练习一（内部修改）
v1=[11,22,33]
v2=v1
v1.append(666)
print(v2)
v2=[11,22,33,66]
#练习二(重新赋值)
v1=[11,22,33]
v2=v1
v1=[1,2,3,4]
print(v2)
--->[11,22,33]
#练习三(重新赋值)
v1='luwei'
v2=v1
v1='oldboy'
print(v2)
---'luwei'
```



###### 示例四：

```
v=[1,2,3]
values=[11,22,v]
#练习一（内部修改）
v.append(9)
print(values)
-->[11,22,[1,2,3,9]]
#练习二（内部修改）
values[2].append(999)
print(v)
-->[1,2,3,999]
#练习三(重新赋值)
v=999
print(values)
-->[11,22,[1,2,3]]
#练习四(重新赋值)
values[2]=666
print(v)
-->[1,2,3]
```



###### 示例五：

```
v1=[1,2]
v2=[2,3]
v3=[11,22,v1,v2,v1]

```

查看内存地址

```
v1=[1,2,3]
v2=v1
v1.append(999)
print(v1,v2)
-->[1,2,3,999],[1,2,3,999]
print(id(v1),id(v2))

v1=[1,2,3]
v2=v1
print(id(v1),id(v2))#内存地址一样
v1=999
print(id(v1),id(v2))#内存地址不一样
```



##### 重点：

###### is与==区别

- ==用于比较值是否相等
- is用于比较内存地址是否相等

```
v1=[1,2,3,4]
v2=[1,2,3,4,5,7]
v1==v2  # False
v1 is v2 # False

v1=[1,2]
v2=[1,2]
v1==v2   # True
v1 is v2 # False

v1=[1,2]
v2=v1
v1==v2  # True
v1 is v2  # True

v1=10
v2=10
v1==v2  # True
v1 is v2  # True ,python对常用字符串整型内存地址缓存优化

v1=10000
v2=10000

v1==v2   # True
v1 is v2 # False
```











