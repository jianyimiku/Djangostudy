'''
Paginator(列表，整数)

返回值  返回的分页对象

属性：count  对象总数

num_pages  页面总数

page_range 页码列表 页码从1开始

方法：page(num) 获得一个Page对象 
如果提供的页码不存在会抛出“InvalidPage”异常

Page对象:

创建对象：Paginator对象的page()方法返回得到的Page对象

不需要手动创建

属性：object_list  当前页上所有的数据(对象)列表

number  当前的页码值

paginator  当前page对象关联的paginator对象

方法：has_next()  判断是否有下一页 如果有返回True

has_previous()  判断是否有上一页 如果有返回True

has_other_pages 判断是否有上一页或者下一页 如果有返回True

next_page_number() 返回下一页的页码 如果下一页不存在 抛出InvalidPage

previous_page_number() 返回上一页的页码 如果上一页不存在 抛出InvalidPage

len() 返回当前页的数据（对象）个数
'''

from django.core.paginator import Paginator 
def studentpage(request， pageid):
	# 所有学生的列表
	alllist = Students.objects.all()
	paginator = Paginator(alllist, 6)
	page = paginator.page(pageid)# 获得一个page对象
	