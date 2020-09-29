## 7.5 crontab定时任务

Linux crontab是用来定期执行程序的命令。

crond 命令每分钟会定期检查是否有要执行的工作，如果有要执行的工作便会自动执行该工作。

**注意：**新创建的 cron 任务，不会马上执行，至少要过 2 分钟后才可以，可以重启 cron 来马上执行。



### 1. 基本使用

linux 任务调度的工作主要分为以下两类：

- 系统执行的工作：系统周期性所要执行的工作，如备份系统数据、清理缓存
- 个人执行的工作：某个用户定期要做的工作，例如每隔10分钟检查邮件服务器是否有新信，这些工作可由每个用户自行设置

**语法**

```
crontab [ -u user ] file
```

或

```
crontab [ -u user ] { -l | -r | -e }
```

**说明：**

crontab 是用来让使用者在固定时间或固定间隔执行程序之用，换句话说，也就是类似使用者的时程表。

-u user 是指设定指定 user 的时程表，这个前提是你必须要有其权限(比如说是 root)才能够指定他人的时程表。如果不使用 -u user 的话，就是表示设定自己的时程表。

**参数说明**：

- -e : 执行文字编辑器来设定时程表，内定的文字编辑器是 VI，如果你想用别的文字编辑器，则请先设定 VISUAL 环境变数来指定使用那个文字编辑器(比如说 setenv VISUAL joe)
- -r : 删除目前的时程表
- -l : 列出目前的时程表

时间格式如下：

```
f1 f2 f3 f4 f5 program
```

- 其中 f1 是表示分钟，f2 表示小时，f3 表示一个月份中的第几日，f4 表示月份，f5 表示一个星期中的第几天。program 表示要执行的程序。
- 当 f1 为 * 时表示每分钟都要执行 program，f2 为 * 时表示每小时都要执行程序，其馀类推
- 当 f1 为 a-b 时表示从第 a 分钟到第 b 分钟这段时间内要执行，f2 为 a-b 时表示从第 a 到第 b 小时都要执行，其馀类推
- 当 f1 为 */n 时表示每 n 分钟个时间间隔执行一次，f2 为 */n 表示每 n 小时个时间间隔执行一次，其馀类推
- 当 f1 为 a, b, c,... 时表示第 a, b, c,... 分钟要执行，f2 为 a, b, c,... 时表示第 a, b, c...个小时要执行，其馀类推

```
*    *    *    *    *
-    -    -    -    -
|    |    |    |    |
|    |    |    |    +----- 星期中星期几 (0 - 7) (星期天 为0)
|    |    |    +---------- 月份 (1 - 12) 
|    |    +--------------- 一个月中的第几天 (1 - 31)
|    +-------------------- 小时 (0 - 23)
+------------------------- 分钟 (0 - 59)
```

使用者也可以将所有的设定先存放在文件中，用 crontab file 的方式来设定执行时间。

**实例**

每一分钟执行一次 /bin/ls：

```
* * * * * /bin/ls
```

在 12 月内, 每天的早上 6 点到 12 点，每隔 3 个小时 0 分钟执行一次 /usr/bin/backup：

```
0 6-12/3 * 12 * /usr/bin/backup
```

周一到周五每天下午 5:00 寄一封信给 alex@domain.name：

```
0 17 * * 1-5 mail -s "hi" alex@domain.name < /tmp/maildata
```

每月每天的午夜 0 点 20 分, 2 点 20 分, 4 点 20 分....执行 echo "haha"：

```
20 0-23/2 * * * echo "haha"
```

下面再看看几个具体的例子：

```shell
0 */2 * * * /sbin/service httpd restart  意思是每两个小时重启一次apache 

50 7 * * * /sbin/service sshd start  意思是每天7：50开启ssh服务 

50 22 * * * /sbin/service sshd stop  意思是每天22：50关闭ssh服务 

0 0 1,15 * * fsck /home  每月1号和15号检查/home 磁盘 

1 * * * * /home/bruce/backup  每小时的第一分执行 /home/bruce/backup这个文件 

00 03 * * 1-5 find /home "*.xxx" -mtime +4 -exec rm {} \;  每周一至周五3点钟，在目录/home中，查找文件名为*.xxx的文件，并删除4天前的文件。

30 6 */10 * * ls  意思是每月的1、11、21、31日是的6：30执行一次ls命令
```

**注意：**当程序在你所指定的时间执行后，系统会发一封邮件给当前的用户，显示该程序执行的内容，若是你不希望收到这样的邮件，请在每一行空一格之后加上 **> /dev/null 2>&1** 即可，如：

```shell
20 03 * * * . /etc/profile;/bin/sh test.sh > /dev/null 2>&1 
```



### 2. 常用命令

crontab服务操作说明：

```shell
/sbin/service crond start //启动服务
 
/sbin/service crond stop //关闭服务
 
/sbin/service crond restart //重启服务
 
/sbin/service crond reload //重新载入配置
```

查看crontab服务状态：

```shell
service crond status
```

手动启动crontab服务：

```shell
service crond status
```

查看crontab服务是否已设置为开机启动，执行命令：

```shell
方法一： 界面启动   ntsysv 

方法二： 加入开机自动启动：  chkconfig –level 35 crond on
```

查看定时任务列表

```shell
crontab -l
```

编辑定时任务

```shell
crontab –e
或
vim /var/spool/cron/root
```

crontab -r 删除定时任务

```xml
从/var/spool/cron目录中删除用户的crontab文件

如果不指定用户，则默认删除当前用户的crontab文件

crontab –i 在删除用户的crontab 文件时给确认提示
```

备份crontab文件

```shell
crontab -l > $HOME/mycron
```


恢复丢失的crontab文件

> 如果不小心误删了`crontab`文件，假设你在自己的`$HOME`目录下还有一个备份，那么可以将其拷贝到/var/spool/cron/<username>，其中<username>是用户名。如果由于权限问题无法完成拷贝，可以用：crontab <filename> 其中，<filename>是你在`$HOME`目录中副本的文件名。

> 有些`crontab`的变体有些怪异，所以在使用`crontab`命令时要格外小心。如果遗漏了任何选项，`crontab`可能会打开一个空文件，或者看起来像是个空文件。这时敲delete键退出，不要按<Ctrl-D>，否则你将丢失`crontab`文件。



### 3. 脚本无法执行问题

如果我们使用 crontab 来定时执行脚本，无法执行，但是如果直接通过命令（如：./test.sh)又可以正常执行，这主要是因为无法读取环境变量的原因。

**解决方法：**

1. 所有命令需要写成绝对路径形式，如: **/usr/local/bin/docker**。

2. 在 shell 脚本开头使用以下代码：

```
#!/bin/sh

. /etc/profile
. ~/.bash_profile
```

3. 在 **/etc/crontab** 中添加环境变量，在可执行命令之前添加命令 **. /etc/profile;/bin/sh**例如：

```
20 03 * * * . /etc/profile;/bin/sh test.sh
```

