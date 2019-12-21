#-*-coding:utf-8-*-
# Author:Lu Wei

'''
#####集合独有功能

#添加
v={1,2,3}
v.add(1)
v.add(4)
print(v)

#删除
v={1,2,'李少奇'}
v.discard('李少奇')
print(v)
v.clear()
print(v)


#update
v={1,2,'李少奇'}
v.update({11,22,33})
print(v)




#交集
v={1,2,'李少奇'}
v1={1,2,3,4,5,}
result=v.intersection(v1)
print(result)
#




#并集
v={1,2,'李少奇'}
v1={1,2,3,4,5,}
result=v.union(v1)
print(result)


#差集
v={1,2,'李少奇'}
v1={1,2,3,4,5,}
result=v.difference(v1)#v中有且v1中没有的
print(result)



#对称差集
v={1,2,'李少奇'}
v1={1,2,3,4,5,}
result=v.symmetric_difference(v1)
print(result)

v={1,2,'李少奇'}
for  i  in v:
    print(i)
'''
# 3. 特殊情况
info = {0, 2, 3, 1,True,4, False, "国风", None, (1, 2, 3)}
print(info)

info = {
    1:'alex',
    True:'oldboy'
}
print(info)
