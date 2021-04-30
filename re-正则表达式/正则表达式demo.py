import re
a = 'a\nb' #    ‘\n'将被编译器替换成换行符

#  原始类型字符串可以简单的通过在普通字符串的双引号前面加一个字符‘r'来创建  保证其不被编译器修改
b = r'a\nb'

  re.match #从开始位置开始匹配，如果开头没有则无

  re.search   #搜索整个字符串

  re.findall  #搜索整个字符串，返回一个list

  所有匹配对象 目前为止在Python中我使用的最多的查找方法是findall()方法,我们可以非常简单的得到一个所有匹配模式的列表
print(re.match(r'l','liuyan1').group())  #返回l
print(re.match(r'y','liuyan1')) #返回None
print(re.search(r'y','liuyan1').group()) #返回y

print(re.search(r'[a-z]+','liuyaN1234ab9').group())#返回'liuya'
print(re.search(r'[a-z]+','liuyaN1234ab9', re.I).group()) #返回'liuyaN'，对大小写不敏感

#如果匹配成功，则打印m，否则返回Null
if re.match(r'[0-9]','g123mmm'):
    print ('m')
else:
    print('None')

#用空格分割
print(re.split(r'\s+', 'a b c'))
#用逗号分隔
print(re.split(r'[\s\,]+', 'a b c  d'))


(?:a{6})*

print(re.search('(?:a{6})*','abc'))

