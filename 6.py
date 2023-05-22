'''6、python实现列表去重的方法
先通过集合去重，在转列表'''
l=[1,1,2]
print(l)
s=set(l)
print(s)
l=list(s)
print(l)