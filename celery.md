

# celery使用

>pip install celery[redis]==4.2.0
>
>我下载的4.2.0版本
>
>Python3.6可以正常运行
>
>如果使用的是Python3.7
>
>则会遇到问题 需要使用最新版本直接用github版本更新
>
>pip install --upgrade https://github.com/celery/celery/tarball/master
>
>问题解决
>
>配置代码见celery学习代码
>
>执行celery work -A celery_app [实例化的celery所在的包] -l INFO （日志等级）