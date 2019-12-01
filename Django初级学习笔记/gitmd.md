```git
配置用户名 git config --global user.name '用户名'
配置邮箱 git config --global user.email '邮箱'
使用 git init 命令把空目录变成git可以管理的仓库
把文件添加到版本库
在仓库目录中移入文件
把文件添加到仓库 git add 文件名
把文件提交到仓库 git commit -m "第一次提交（注释信息）"
git status 查看仓库状态
git diff 查看修改的内容
git log 查看曾经提交过的日志
git log --pretty=oneline 只查看一行
git reset --hard HEAD^ 回退一个版本
git reset --hard HEAD^^ 回退2个版本
git reset --hard HEAD~n 回退N个版本
git reset --hard 版本号
git reflog 记录每一次命令
git checkout --filename 撤销到最后一次的commit或者add的状态
#以上是本地仓库管理
## 远程仓库操作
ssh-keygen -t rsa -C "邮箱"#获取密钥只有带有密钥的电脑才可以上传文件
复制id_rsa.pub公钥
ssh -T git@github.com

关联远程仓库
git remote add origin  地址
删除关联
git remote rm origin
推送本地库内容到远程库 
git push origin master
拉取远程库的内容
git pull origin master(注意先拉后推送)
```

