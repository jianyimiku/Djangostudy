## Django

>在服务器中创建一个project
>
>```python
>django-admin startproject 项目名
>```
>
>1：新建一个文件夹 跟项目名保持一致
>
>2：Tools->Deployment->configuration 进行SFTP的配置与Mapping的配置
>
>![Djiango1](D:\笔记\图片\Djiango1.PNG)
>
>![Djiango2](D:\笔记\图片\Djiango2.PNG)
>
>配置完成以后Sync with deployed to与服务器进行同步
>
>2:File->Setting中新建一个Djiango
>
>![Djiango3](D:\笔记\图片\Djiango3.PNG)
>
>对Project Interpreter进行配置
>
>![Djiango4](D:\笔记\图片\Djiango4.PNG)
>
>![Djiango5](D:\笔记\图片\Djiango5.PNG)

>Debug配置
>
>![Djiango6](D:\笔记\图片\Djiango6.png)
>
>![Djiango7](D:\笔记\图片\Djiango7.png)
>
>出现没法查找到文件的问题
>
>![](D:\笔记\图片\Djan.PNG)

## MVC

>control->model->view

## MTV

>url->view->model->template(模板就是html文件)

## 梳理

>manage.py  一个命令行工具 可以使我们用多种方式对Django项目进行交互
>
>_init_.py   一个空文件 他告诉Python这个目录应该被看作一个Python包
>
>settings.py 项目的配置文件
>
>urls.py  项目的URL声明
>
>wsgi.py 项目于WSGI兼容的web服务器入口

## 基本操作

>1:设计表结构
>
>2：python manage.py startapp 名字
>
>admin.py 站点配置
>
>models.py 模型
>
>viewsp.py 视图
>
>3：python manage.py makemigrations  生成迁移文件
>
>4：python manage.py migrate 执行迁移
>
>**测试数据操作**
>
>In [1]: from myApp.models import Grades,Students                                   
>
>In [2]: from django.utils import timezone                                          
>
>In [3]: from datetime import *     
>
>**查询数据**
>
>类名.objects.all()
>
>**添加数据**
>
>本质：创建一个模型类对象的实例
>
>名字=类名（）
>
>名字.属性=
>
>名字.save（保存数据）
>
>**查询某个对象**
>
>类名.objects.get(pk=？)  （以ID查询）
>
>**修改数据**
>
>例子
>
>```mysql
>g=Grades.object.get(pk=1)
>g.gboynum=60
>g.save()
>```
>
>**删除对象**
>
>模型对象.delete（）
>
>**关联对象**
>
>```python
>In [23]: stu.sname="薛"                                                                                                                                                  
>
>In [24]: stu.sage=20                                                                                                                                                                              
>
>In [25]: stu.scontend="wang"                                                                                                                                                                      
>
>In [26]: stu.sgrade = g    //关联到了1班                                                                                                                                                                       
>
>In [27]: stu.save() 
>
>//获取python04班级的所有学生
>对象名.关联类名小写_set.all()
>g.students_set.all()
>
>//创建曾志伟属于python04班级
>In [3]: g=Grades.objects.get(pk=1)                                                 
>
>In [4]: stu3=g.students_set.create(sname=u'曾志伟',sgender=True,scontend=u'我叫曾志
>...: 伟',sage=45)
>```
>
>**启动服务器**
>
>```python
>python manage.py runserver 0.0.0.0:8080
>```
>
>**Admin站点管理**
>
>>在setting.py文件中的INSTALLED_APPS中添加'django.contrib.admin',默认已经添加
>>
>>创建管理员
>>
>>```python
>>python manage.py createsuperuser
>>```
>>
>>**汉化**
>>
>>```python
>>LANGUAGE_CODE = 'zh-Hans'
>>
>>TIME_ZONE = 'Asia/Shanghai'
>>```
>>
>>**管理数据表**
>>
>>>修改admin.py文件
>>>
>>>```python
>>>from django.contrib import admin
>>># Register your models here.
>>>from .models import Grades,Students
>>>admin.site.register(Grades)
>>>admin.site.register(Students)
>>>```
>>
>>**自定义管理界面**
>>
>>属性说明
>>
>>>列表页的属性
>>>
>>>list_display  显示字段（数据库的）
>>>
>>>list_filter  过滤字段
>>>
>>>search-filed  搜索字段
>>>
>>>list_per_page 分页
>>
>>>添加修改页属性
>>>
>>>fields  属性的先后顺序
>>>
>>>fieldsets 给属性分组
>>>
>>>这两个属性不能同时使用
>>
>>>在创建一个班级时可以直接添加几个学生
>>>
>>>```python
>>>class StudentsInfo(admin.TabularInline):
>>>    model = Students
>>>    extra = 2
>>>class GradesAdmin(admin.ModelAdmin):
>>>    inlines = [StudentsInfo]
>>>
>>>```
>>>
>>>**布尔值现实问题**
>>>
>>>```python
>>> def gender(self):
>>>        if self.sgender:
>>>            return "男"
>>>        else:
>>>            return "女"
>>>    gender.short_description = "sgender"#设置页面列的名称
>>>    list_display = ['pk','sname',gender,'sage','scontend','isDelete','sgrade']
>>>```
>>>
>>>**执行动作位置**
>>>
>>>```python
>>>actions_on_top=False;
>>>actions_on_bottom=True;//将执行动作放到底部
>>>```
>>>
>>>**使用装饰器完成注册**
>>>
>>>```python
>>>@admin.register(Students)
>>>class StudentsAdmin(admin.ModelAdmin):
>>>    def gender(self):
>>>        if self.sgender:
>>>            return "男"
>>>        else:
>>>            return "女"
>>>    gender.short_description = "sgender"
>>>    list_display = ['pk','sname',gender,'sage','scontend','isDelete','sgrade']
>>>    list_per_page = 2
>>>#注册
>>>admin.site.register(Grades,GradesAdmin)
>>># admin.site.register(Students,StudentsAdmin)
>>>```
>>>
>>>
>
>**视图**
>
>视图就是一个Python函数
>
>定义视图
>
>```python
>from django.http import HttpResponse
>def index(request):
>return  HttpResponse("MIKU WITH YOU")
>```
>
>配置URL(修改url.py的 在Myapp应用目录下创建url.py)
>
>```python
>from django.contrib import admin
>from django.urls import path,include
>
>urlpatterns = [
>path('admin/', admin.site.urls),
>path('', include('myApp.url'))
>]
>
>
>myAPP.view
>from django.urls import path
>from . import views
>
>urlpatterns = [
>path('', views.index)
>]
>```
>
>**模板真实使用**
>
>>模板是html页面 可以根据视图中传递过来的数据进行填充
>>
>>创建模板  创建templates目录 在目录下创建对应项目的模板目录（projects->templates->myAPP)
>>
>>**配置模板路径**
>>
>>修改settings.py文件下的TEMPLATES
>>
>>定义grades和students模板
>>
>>模板语法{{输出值，可以是变量 一个可以是对象，属性}}
>>
>>{{%执行代码段%}}
>>
>>在。。。。。/grades输出数据
>>
>>写grades.html模板
>>
>>定义视图 
>
>>增加数据库只需要重新执行迁移文件
>>
>>如果要增加字段 删掉数据库 迁移文件重新来
>>
>
>**ORM**
>
>对象 关系 映射
>
>根据对象的类型生成表结构
>
>将对象 列表的操作转换为SQL语句
>
>将sql语句查询到的结果转换为对象 列表
>
>**定义模型**
>
>一个模型类在数据库中对应一张表 在模型中定义属性 对应该模型对照表中的一个字段
>
>AutoField：一个根据实际ID自动增长的（设置主键）
>
>CharField（max_length= ）:字符串
>
>TextField：大文本字段
>
>IntegerField：整数
>
>DecimalField（max_digits=None,decimal_places=None）
>
>第一个位数总数
>
>第二个小数点后的数字位数		
>
>FloatField
>
>BooleanField
>
>DateField([auto_now =False,auto_now_add=False])
>
>第一个：每次保存对象时候 子哦对那个设置该字段为当前时间
>
>第二个：第一次创建时的时间 以后的对象也用该时间
>
>TimeField
>
>DateTimeField
>
>FileField（保存文本）
>
>ImageField（保存图片）
>
>unique （必须存在唯一值）
>
>ForeignKey:一对多 将字段定义在多的端中
>
>ManyToManyField:多对多 将字段定义在两端中
>
>OneToOneField:一对一 将字段定义在任意一端中
>
>null 是否为空
>
>**一访问多**
>
>对象.模型小写_set
>
>>**元选项**
>>
>>在模型类中定义Meta类（写在如class Students类里面，用于设置元信息）
>>
>>db_table   定义数据表名 推荐使用小写字母 数据表名默认为数据表_小写
>>
>>ordering  对象的默认排序字段 获取对象列表时可以使用
>>
>>ordering=【‘id’】 升序
>>
>>ordering=【‘-id’】 降序
>
>**模型成员**
>
>>类属性 objects  是Manager类型的一个对象，作用是与数据库进行交互
>>
>>当定义模型类没有指定管理器，则Django为模型创建一个名为objects的管理器
>>
>>**自定义管理器**（没撒用）
>>
>>当自定义模型管理器 objecs就不存在了
>>
>>stuObj=models.Manager()
>>
>>Students.stuObj.all()
>>
>>**自定义Manager类**
>>
>>模型管理器是Django的模型进行与数据库进行交互的接口，一个模型可以有多个模型管理器
>>
>>**作用**
>>
>>想管理器类中添加额外的方法
>>
>>修改管理器返回的原始查询集->重写get_queryset（）方法
>>
>>```python
>>class StudentsManager(models.Manager):
>>def get_queryset(self):
>>return super(StudentsManager, self).get_queryset().filter(isDelete=False)#过滤进来
>>
>>class Students(models.Model):
>>stuObj = StudentsManager()
>>```
>>
>>**创建对象**
>>
>>目的 像数据库中添加数据
>>
>>当创建对象时，Django不会对数据进行读写操作 当调用save（）时才与数据库进行交互
>>
>>>在模型类中添加一个方法
>>>
>>>```python
>>>@classmethod
>>>def createStuden(cls,name,gender,age,contend,grade):
>>>student = cls(sname=name,sgender=gender,sage=age,scontend=contend,sgrade=grade)
>>>return student
>>>
>>>
>>>
>>>def addStudent(request):
>>>stu = Students.createStuden("刘德华",True,34,"我叫刘德华",1)
>>>stu.save()
>>>return HttpResponse("Success")
>>>
>>>
>>>
>>>或者在StudentsManager中写
>>>def createStuden(self,name,gender,age,contend,grade):
>>>stu = self.model()#创建空对象
>>>stu.sname = name
>>>stu.sgender = gender
>>>stu.sage = age
>>>stu.scontend = contend
>>>stu.sgrade = grade
>>>return stu
>>>
>>>
>>>def addStudent(request):
>>>grade = Grades.objects.get(pk=1)
>>>stu = Students.stuObj.createStuden("李建    伟",True,34,"我叫李建伟",grade)
>>>stu.save()
>>>return HttpResponse("Success")
>>>```
>>>
>>>**模型查询**
>>>
>>>>查询集从数据库获取的对象的集合
>>>>
>>>>查询及可以有多个过滤器
>>>>
>>>>过滤器就是一个函数 基于所给的参数限制查询集结果
>>>>
>>>>从sql角度来说 查询集和select等价 过滤器就像where条件
>>>
>>>**查询集**
>>>
>>>>在管理器上条用过滤器方法条用查询集
>>>>
>>>>查询集经过过滤器筛选后返回新查询集 可以链式调用 接多个fliter
>>>>
>>>>创建查询集不会带来任何数据的访问 直到调用数据时 才会访问数据
>>>>
>>>>直接访问数据的情况：迭代 序列化 与if合用
>>>>
>>>>返回查询集的方法为过滤器：all（）
>>>>
>>>>filter（）（返回符合条件的数据）使用方法：filter（键=值，键等于值）或者
>>>>
>>>>filter（键=值）.filter(键=值)
>>>>
>>>>exclude（）过滤掉符合条件的数据
>>>>
>>>>order_by() 排序
>>>>
>>>>values() 一条数据就是一个对象（字典）,返回一个列表 
>>>>
>>>>返回整体是一个列表 列表中是字典
>>>>
>>>>**返回单个数据**
>>>>
>>>>get()  返回一个满足条件的对象
>>>>
>>>>count() 返回当前查询集合中的对象个数
>>>>
>>>>first() 返回查询集中的第一个对象
>>>>
>>>>last()返回查询集中的最后一个对象
>>>>
>>>>exists() 判断查询集合中是否有数据 如果有数据返回True 
>>>>
>>>>限制查询集
>>>>
>>>>Students.objects.all()[0:3]显示3条数据
>>>>
>>>>**分页**
>>>>
>>>>[(page-1)*5:page*5]
>>>>
>>>>**查询集缓存**
>>>>
>>>>每个查询集都会包含一个缓存，来最小化对数据库访问
>>>>
>>>>在新建的查询集中，缓存首次为空，第一次对查询集求值，会发生数据缓存
>>>>
>>>>**字段查询**
>>>>
>>>>属性名称__比较运算符=值（两条下划线）
>>>>
>>>>外键：属性名_id
>>>>
>>>>转义  like语句中使用%是为了匹配占位 匹配数据中的%（where like ‘\%’)
>>>>
>>>>而Django中不需要\
>>>>
>>>>**比较运算符**
>>>>
>>>>exact  判断 大小写敏感
>>>>
>>>>contains 包含 大小写敏感 。。。。。.filter(sname__contains(value))
>>>>
>>>>startwith endwith  以value开头或者结尾
>>>>
>>>>以上四个在前面加上i 就不区分大小写 iexact 。。。。
>>>>
>>>>isnull isnotnull  是否为空
>>>>
>>>>is 是否包含在范围内
>>>>
>>>>gt 大于
>>>>
>>>>gte 大于等于
>>>>
>>>>lt 小于
>>>>
>>>>lte 小于等于
>>>>
>>>>year month day week_day hour minute
>>>>
>>>>second   (日期相关)
>>>>
>>>>**跨关联查询**
>>>>
>>>>处理join查询    模型类名 _ 属性名 _ 比较运算符
>>>>
>>>>描述中带有“ “里面信息的数据是哪个班级的
>>>>
>>>>grade = Grades.objects.filter(students__  scontend__ contains="" )
>>>>
>>>>**查询快捷**
>>>>
>>>>pk  代表主键
>>>
>>>**聚合函数**
>>>
>>>使用	()函数返回聚合函数的值
>>>
>>>Avg
>>>
>>>Count
>>>
>>>Max  
>>>
>>>```python
>>>from django.db.models import Max
>>>maxAge = Students.objects.aggregate(Max('sage'))
>>>```
>>>
>>>
>>>
>>>Min
>>>
>>>Sum
>>
>>**F对象**
>>
>>>可以使用模型的A属性与B属性进行比较
>>>
>>>g = Grades.objects.filter(ggirlnum__gt=F('gboynum')+20)
>>
>>**Q对象**
>>
>>>过滤器的方法中的关键词参数，条件为And模式
>>>
>>>需求：进行or查询
>>>
>>>Students.object.filter(Q(pk__  lte=3)|  Q(sage__  gt=50))
>>>
>>>当只有一个Q对象 就是用于匹配
>>>
>>>~Q(pk__  lte=3)
>>>
>>>加了~表示要取反
>
>**视图**
>
>视图接受WEB请求，并响应web请求
>
>视图就是python中的函数
>
>响应：网页 
>
>重定向
>
>Json数据
>
>URL 配置  指定根级URL  settings.py中的ROOT_URLCONF（默认实现）
>
>URL 匹配正则的注意事项  如果想要在url中获取一个值 需要对正则加小括号、
>
>匹配正则前方不需要加/
>
>正则需要加r表示字符串不转义
>
>url include 中加上 namespace=”myApp“
>
>用途：
>
>**url的反向解析**
>
>```python
>from django.urls import path
>from . import views
>
>urlpatterns = [
>path('', views.index, name="index"),
>]
>#在APP的URL后面加上一个name
>```
>
>
>
>如果在视图 模板中使用了硬编码连接，我们在url配置发生改变时 动态生成连接地址
>
>在使用连接时 通过url配置的名称 动态生成url地址
>
>作用：
>
>使用url模板的时候
>
>**视图函数**
>
>>本质一个函数
>>
>>视图参数：一个HttpResponse的实例 通过url获取的参数
>>
>>位置：一般在views.py中定义
>>
>>settings.py 配置为Debug 为True 不会调用404页面
>>
>>404页面 request_path
>>
>>**HttpRequest对象**
>>
>>概述：服务器接收http请求后 会根据报文创建一个 HttpRequest对象
>>
>>视图第一个参数就是这个对象
>>
>>>**属性**
>>>
>>>path：请求完整路径(不包括域名和接口)
>>>
>>>method：表示请求的方式，常用的有GET,POST
>>>
>>>encoding:表示浏览器提交的编码方式 一般为UTF-8
>>>
>>>GET  类似字典的对象 包含了get请求的所有参数
>>>
>>>POST 类似字典的对象 包含了post请求的所有参数
>>>
>>> FILES 类似字典的对象 包含了所有上传的文件
>>>
>>>COOKIES 字典 包含所有的cookie
>>>
>>>session 类似字典的对象 表示当前会话
>>
>>>is_ajax()  如果是通过xMLHttpRequest发起的 返回True
>>
>>>QueryDict对象  request对象中的GET POST都属于QueryDict对象
>>>
>>>方法：get()  根据键获取值
>>>
>>>getlist() 将键的值以列表的形式返回 可以获取多个值
>>
>>GET属性 获取浏览器传输过来的数据 GRT.get(’‘)
>>
>>注释CSRF中间件
>>
>>POST属性 使用表单实现 
>>
>>**HttpResponse对象**
>>
>>用法:不调用模板 return HttpResponse
>>
>>调用模板 使用render
>>
>>>render(request,templateName,内容)
>>>
>>>作用
>>>
>>>结合数据和模板返回完整的HTML页面
>>
>>参数：
>>
>>>requet  请求体对象
>>>
>>>templateName： 模板路径
>>>
>>>context：传递给需要渲染在模板上的数据
>>
>>属性
>>
>>>content  表示返回的内容的类型
>>>
>>>charset  编码格式
>>>
>>>status_code 响应代码
>>>
>>>content- type 指定输出的MIME类型
>>
>>init : 使用页面内容实例化HttpRequest对象
>>
>>write(content):以文件的形式写入
>>
>>flush()：以文件的形式输出缓冲区
>>
>>set_cookie（key，value=“ ”，max_age=None, exprise = None)
>>
>>delete_cookie【key】  ：删除cookie   如果删除一个不存在的key 就当什么都没发生
>
>
>
>>**HTTPResponseRedirect**
>>
>>>功能：重定向 服务器端跳转
>>>
>>> 简写  redirect
>>>
>>>return redirect（“ ”）
>>>
>>>路径推荐使用反向解析
>>
>>**JsonResponse**
>>
>>返回JSON数据 一般用于异步请求 
>>
>>__ init __(self,data)
>>
>>```python
>>if request.is_ajax():
>>    a = JsonResponse({})#大致过程
>>```
>>
>>data  字典对象
>>
>>注意：Content-type类型为application/json
>
>**存储方式**
>
>>cookie:所有的数据存储在客户端 不要存敏感数据
>>
>>session: 所有的数存储在服务端，在客户端用cookie存储
>
>```python
>username = request.POST.get('username')
>request.session['username'] = username
>
>
>
>取出session
>username = request.session.get("username","游客")#后面的值的意思是如果session中没有取到username 则取游客
>
>退出登录引用logout
>logout(request)清除缓存
>request.session.clear()
>requset.session.flush()
>
>
>```
>
>>设置session过期时间
>>set_expiry(value) 如果不设置两个星期过期
>>
>>时间对象
>>
>>0 关闭浏览器是失效
>>
>>None 永不过期
>
>用redis缓存session
>
>```python
>pip install django-redis-sessions
>```
>
>SESSION_ENGINE = 'redis_sessions.session'
>
>SESSION_REDIS_HOST='localhost'
>
>SESSION_REDIS_PORT=6379
>
>SESSION_REDIS_DB=0
>
>SESSION_REDIS_PASSWORD=''
>
>SESSION_REDIS_PREFIX='session'
>
>**模板**
>
>>在模板中使用点语法 如{{stu.name}}
>>
>>在模板中调用对象方法  注意：不能传递参数
>>
>>>标签
>>>
>>>语法：{% tag %}
>>>
>>>作用：在输出中创建文本
>>>
>>>控制逻辑和循环
>>>
>>>```python
>>>if
>>>'''
>>>格式：   {%if 表达式%}
>>>		{%endif%}
>>>		
>>>		{%if 表达式%}
>>>		{%elif 表达式%}
>>>		....
>>>		{%endif%}	
>>>		
>>>		{%if 表达式%}
>>>		{%else 表达式%}
>>>		{%endif%}	
>>>'''
>>>for
>>>'''
>>>{% for 变量 in 列表 %}
>>>
>>>{% endfor%}
>>>{% for 变量 in 列表 %}
>>>
>>>{% empty %}
>>>语句2 #当列表为空的时候调用语句2
>>>{% endfor%}
>>>
>>>{{forloop.counter}} 显示当前是第几次循环
>>>'''
>>>comment
>>>'''
>>>{%comment%}
>>>注释内容
>>>{% endcomment %}
>>>'''
>>>ifequal,ifnotequa
>>>'''
>>>判断是否相等或者不相等
>>>{%ifequal 值1 值2 %}
>>>值相等就执行
>>>{%endifequal %}
>>>后面一个同类
>>>'''
>>>include
>>>'''
>>>加载模板并以标签内的参数渲染
>>>{% include ’模板目录‘ 参数1 参数2  %}
>>>'''
>>>url
>>>'''
>>>作用：反向解析
>>>格式：{%url ‘namespace：name’ p1 p2 %}
>>>'''
>>>csrf_token
>>>'''
>>>用于跨站请求伪造保护
>>>{% csrf_token  %}
>>>'''
>>>block,extends
>>>'''
>>>用于模板继承
>>>'''
>>>autoescape
>>>'''
>>>用于html转义
>>>'''
>>>
>>>```
>>>
>>>过滤器
>>>
>>>{{var|过滤器}}
>>>
>>>作用  在变量被显示前修改过
>>>
>>>lower(小写)
>>>
>>>upper(大写)  {{str|upper}}
>>>
>>>过滤器可以传递参数，参数用引号引起来  
>>>
>>>join  {{列表|join:'#'}}将列表里面的值用引号引起来
>>>
>>>如果一个变量没有被提供或者值为false，空 可以使用默认值
>>>
>>>default  {{var|dn efault : '  '}}
>>>
>>>根据给定格式转换日期为字符串 
>>>
>>>date  格式  {{dateVal|date:'  '}}
>>>
>>>HTML转义  escape
>>>
>>>加减乘除
>>>
>>>{{var|add:10}}加
>>>
>>>{{var|add:-5}}减
>>>
>>>{% widthratio num 1 5 %}乘5
>>>
>>>{%  widthratio num 5 1 %}除5
>>>
>>>{% if forloop.counter|divisibleby:2 %}
>>>
>>>divisibleby标签的意义是用后面的参数去除，
>>>
>>>除尽为True，否则为False。
>>>
>>>>注释 
>>>>
>>>>单行注释  
>>>>
>>>>语法：{# 注释内容  #}
>>>>
>>>>多行注释
>>>
>>>>反向解析
>>>>
>>>>项目中的url里面定义 namespace
>>>>
>>>>app中定义 name
>>>
>>>>模板继承
>>>>
>>>>作用 ：模板继承可以减少页面内容的定义 减少页面的重用
>>>>
>>>>block标签 在父模板中预留区域 子模版去填充
>>>>
>>>>//父模板在不需要继承的div中写入
>>>>
>>>>{% block 标签名%}
>>>>
>>>>{% endblock 标签名%}
>>>>
>>>>extends标签 继承模板，需要卸载模板文件的第一行
>>>>
>>>>//子模版写法
>>>>
>>>>{%extends  '父模板路径'%}
>>>>
>>>>{%block 标签名%}
>>>>
>>>>//调用刚才的父模板并在在block标签中填东西
>>>>
>>>>{% endblock 标签名%}
>>>>
>>>>>HTML 转义
>>>>>
>>>>>将接受到的字符串当成HTML代码渲染 {{code|safe}}
>>>>>
>>>>>{{%  autoescape off   %}}
>>>>>
>>>>>
>>>>>
>>>>>{{%  endautoescape %}}
>>>>
>>>>>CSRF
>>>>>
>>>>>跨站请求伪造
>>>>>
>>>>>某些恶意的网站包含链接，表单，按钮，会利用登陆用户在浏览器中认证，从而攻击服务
>>>>>
>>>>>防止CSRF
>>>>>
>>>>>1<form>
>>>>>
>>>>>在表单中{% csrf_token %}
>>>>>
>>>>></form>
>>>>>
>>>>>验证码
>>>>>
>>>>>作用： 在用户注册 登录页面的时候使用 防止暴力请求 减轻服务器的压力
>>>>>
>>>>>防止csrf的一种方式
>>>>>
>>>>>```python
>>>>>def verifyCode(request):
>>>>>	# 引入绘图模块
>>>>>	from PIL import Image, ImageDraw, ImageFont
>>>>>	# 引入随机函数模块
>>>>>	import random
>>>>>	# 定义变量，用于画面的背景色，宽，高
>>>>>	bgcolor = (random.randrange(20, 100), random.randrange(20, 100), random.randrange(20, 100))
>>>>>	width = 100
>>>>>	height = 50
>>>>>	# 创建画布对象
>>>>>	im = image.new('RGB', (width, height), bgcolor)#创建了一个画布
>>>>>	# 创建画笔对象
>>>>>	draw = ImageDraw.Draw(im)
>>>>>	# 调用画笔的point()函数绘制噪点
>>>>>	for i in range(0, 100):
>>>>>		xy = (random.randrange(0, width), random.randrange(0, height))
>>>>>		fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
>>>>>		draw.point(xy, fill=fill)#画实心的点
>>>>>	# 定义验证码的备选值
>>>>>	str = '1234567890QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm'
>>>>>	# 随机选取四个值作为验证码
>>>>>	rand_str = ''
>>>>>	for i in range(0,4):
>>>>>		rand_str += str[random.randrange(0, len(str))]
>>>>>	# 构造字体
>>>>>	font = ImageFont.truetype(r'C:\Windows\Fonts\AdobeArabic-Bold.otf', 40)
>>>>>	# 构造字体颜色
>>>>>	fontcolor1 = (255, random.randrange(0, 255), random.randrange(0, 255))
>>>>>	fontcolor2 = (255, random.randrange(0, 255), random.randrange(0, 255))
>>>>>	fontcolor3 = (255, random.randrange(0, 255), random.randrange(0, 255))
>>>>>	fontcolor4 = (255, random.randrange(0, 255), random.randrange(0, 255))
>>>>>	# 绘制四个子
>>>>>	draw.text((5, 2), rand_str[0], font=font, fontcolor=fontcolor1)
>>>>>	draw.text((25, 2), rand_str[1], font=font, fontcolor=fontcolor2)
>>>>>	draw.text((50, 2), rand_str[2], font=font, fontcolor=fontcolor3)
>>>>>	draw.text((75, 2), rand_str[3], font=font, fontcolor=fontcolor4)
>>>>>
>>>>>	# 释放画笔
>>>>>	del draw
>>>>>	# 存入session 用于做进一步验证
>>>>>	request.session['verifyCode'] = rand_str
>>>>>	# 内存文件操作
>>>>>	import io
>>>>>	buf = io.BytesIO()
>>>>>	# 将图片保存在内存中 文件类型为png
>>>>>	im.save(buf, 'png')
>>>>>	# 将内存中的图片数据返回给客户端 MIME类型为图片png
>>>>>	return HttpResponse(buf.getvalue(), 'image/png')
>>>>>```
>>>
>>>## Django高级扩展
>>>
>>>**静态文件**
>>>
>>>css, js, 图片， json文件， 字体文件
>>>
>>>配置 settings.py  
>>>
>>>STATIC_URL = ‘ ’ 静态图片用
>>>
>>>#普通文件用
>>>
>>>STATICFULES_DIRS=[
>>>
>>>​	os.path.join(BASE_DIR, ‘static’)
>>>
>>>   os.path.join(BASE_DIR, 'static')
>>>
>>>]
>>>
>>>{%load static (from staticfiles)%}括号内可有可无
>>>
>>>{%static 'static/css/..'%}
>>>
>>>**中间件**
>>>
>>>概述：一个轻量级 底层的插件 可以介入Django的请求和响应
>>>
>>>本质： 一个Python类
>>>
>>>方法：
>>>
>>>__ init __: 不需要传参数 服务器响应第一个请求的时候 自动调用 用于确定是否启用中间件
>>>
>>>process_request(self.request)  在执行我们的视图之前被调用(分配url匹配视图之前就是调用url之前),每个请求上都要调用，返回None或者HttpResponse对象
>>>
>>>process_view(self.request,view_func,view_args,view_kwargs)调用视图之前执行，每个请求都要调用，返回None或者HttpResponse对象
>>>
>>>process_template_response(self.request,reponse)在视图刚好执行完后调用，每个请求都要调用，返回None或者HttpResponse对象
>>>
>>>使用render
>>>
>>>过程介于调用view view开始去找render中的模板之间
>>>
>>>process_response(self.request,reponse) 所有响应返回浏览器之前调用，每个请求都要调用，返回HttpResponse对象
>>>
>>>process_exception(self.request,exception)当视图抛出异常的时候调用
>>>
>>>![中间件](D:\笔记\图片\中间件.PNG)
>>>
>>>自定义中间件
>>>
>>>工程目录下创建同级目录
>>>
>>>创建一个Python文件
>>>
>>>使用自定义中间件
>>>
>>>配置setting
>>>
>>>MIDDLEWARE中添加：
>>>
>>>’目录文件夹.文件名.类名‘
>>>
>>>**上传图片**
>>>
>>>文件上传时 文件数据存储在request.FILES属性中
>>>
>>>新建一个media用于图片上传并配置MEDIA_ROOT
>>>
>>>上传文件一定要时POST请求
>>>
>>>if request.method == "POST"
>>
>>**分页**
>>
>>>Paginator
>>>
>>>创建对象：
>>>
>>>Paginator(列表，整数)
>>>
>>>返回值  返回的分页对象
>>>
>>>属性：count  对象总数
>>>
>>>num_pages  页面总数
>>>
>>>page_range 页码列表 页码从1开始
>>>
>>>方法：page(num) 获得一个Page对象 如果提供的页码不存在会抛出“InvalidPage”异常
>>>
>>>异常：
>>>
>>>InvalidPage:当向page()传递的是一个无效的页码的时候抛出
>>>
>>>PageNotAnInteger：当向page()传递的是一个无效的页码时抛出
>>>
>>>EmptyPage：当向page()传递一个有效值 但是该页面时没有数据时抛出
>>>
>>>Page对象:
>>>
>>>创建对象：Paginator对象的page()方法返回得到的Page对象
>>>
>>>不需要手动创建
>>>
>>>属性：object_list  当前页上所有的数据(对象)列表
>>>
>>>number  当前的页码值
>>>
>>>paginator  当前page对象关联的paginator对象
>>>
>>>方法：has_next()  判断是否有下一页 如果有返回True
>>>
>>>has_previous()  判断是否有上一页 如果有返回True
>>>
>>>has_other_pages 判断是否有上一页或者下一页 如果有返回True
>>>
>>>next_page_number() 返回下一页的页码 如果下一页不存在 抛出InvalidPage
>>>
>>>previous_page_number() 返回上一页的页码 如果上一页不存在 抛出InvalidPage
>>>
>>>len() 返回当前页的数据（对象）个数
>>>
>>>Paginator对象和Page对象的关系:
>>>
>>>![Pageinator](D:\笔记\图片\Pageinator.PNG)
>>
>>**ajax**
>>
>>>需要动态生成，请求JSON数据
>>
>>**富文本**
>>
>>>pip install django-tinymce
>>>
>>>在站点中使用：
>>>
>>>配置settings
>>>
>>>INSTALLED_APPS添加 ‘tinymce’
>>>
>>>TINYMCE_DEFAULT_CONFIG={
>>>
>>>​	'theme':'advanced',
>>>
>>>​	'width':600,
>>>
>>>​	'height':400,
>>>
>>>}
>>>
>>>创建一个模型类
>>>
>>>在admin中设置
>>>
>>>在自定义视图中使用
>>
>>**celery**(没会 视频没讲 以后用到再看)
>>
>>>问题：
>>>
>>>1.用户发起request，并且要等待response返回 但是在视图中有一些
>>>
>>>耗时的操作 导致用户可能会等待很长的时间才能接受到response
>>>
>>>2.网站每隔一段时间要同步一次数据,但是http请求时需要触发的
>>>
>>>解决：
>>>
>>>celery来解决  将耗时的操作放到celery中执行
>>>
>>>使用celery定时执行
>>>
>>>安装:
>>>
>>>pip install celery
>>>
>>>pip install celery-with-redis
>>>
>>>pip install django-celery
>>>
>>>配置settings.py
>>>
>>>INSTALLED_APPS中添加'djcelery'
>>>
>>>import djcelery
>>>
>>>djcelery.setup_loader()#初始化
>>>
>>>BROKER_URL = 'redis://:sunck@127.0.0.1:6379/0(这个0是第几个库的意思)'
>>>
>>>CELERY_IMPORTS=('项目名.task')
>>>
>>>在app目录下创建task.py
>>>
>>>迁移数据库生成celery所需要的表
>>>
>>>在工程目录下的project目录下创建celery.py文件中添加
>>>
>>>在工程目录下的project目录下__ init.py __文件中添加
>>>
>>>见代码
