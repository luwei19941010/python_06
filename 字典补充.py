#-*-coding:utf-8-*-
# Author:Lu Wei
############get
'''
info={'k1':'v1','k2':'v2'}
v1=info.get('k22')#None 就是python中的空
v2=info.get('k1',123)
print(v1)
print(v2)

############pop
info={'k1':'v1','k2':'v2'}
result=info.pop('k2')
print(info,result)

###########update
#如果key不存在直接添加，如果key存在则覆盖原来的value值
info={'k1':'v1','k2':'v2'}
info1={'k3':'v3','k4':'v4'}
info2={'k3':'v3','k1':'v4'}
#info['k3']='v3'
info.update(info1)
info.update(info2)
print(info)

info={'k1':'v1','k2':'v2'}
i='v3'
if i in info.values():
    print('1')
else:
    print('2')


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



v1={}
v2=set()
print(type(v1),type(v2))

'''















