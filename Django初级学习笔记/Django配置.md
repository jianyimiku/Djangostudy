## 服务器配置环境

> 1：重置系统16.04->18.04

## Ubuntun 18.04安装Python 3.7.4

>1:**下载安装包**
>
>wget https://www.python.org/ftp/python/3.7.4/Python-3.7.4.tgz
>
>2：**配置libreadline-dev等依赖文件**
>
>sudo apt-get update    //将软件源更新为最新版
>sudo apt-get install gcc patch
>sudo apt-get install libreadline-dev    //直接运行python中支持换行
>sudo apt-get install libmysqlclient-dev libffi-dev libssl-dev openssl zlib1g-dev libsqlite3-dev tk-dev build-essential python-dev python-setuptools python-pip python-smbus libncursesw5-dev libgdbm-dev libc6-dev
>
>3：**解压 配置** 
>
>tar -xvf ..... 
>
>cd Python-3.7.4
>
>cd Modules
>
>ls
>
>sudo vim Setup.dist
>
>/ssl
>
>从SSL=/url/local/ssl开始四行取消注释
>
>wq
>
>cd ..
>
>./configure --enable-optimizations
>
>make
>
>make install
>
>pip3 install virtualenv
>
>pip3 --upgrade pip
>
>pip3 install virtualenvwrapper
>
>sudo vim .bashrc
>
>export WORKON_HOME=~/my_env
>
>export VIRTUALENVWRAPPER_PYTHON=/usr/local/bin/python3.7
>
>source /usr/local/bin/virtualenvwrapper.sh
>
>source ~/.bashrc
>
>mkvirtualenv yqqsb	
>
>deactivate(退出虚拟环境)
>
>workon yqqsb(进入虚拟环境)











>在虚拟环境中运行
>
>mkvirtualenv -p python3.6 nsb 指定版本的虚拟环境
>
>sudo apt-get install lrzsz
>
>pip install django