## 7.4 nohup命令

nohup 英文全称 no hang up（不挂起），用于在系统后台不挂断地运行命令，退出终端不会影响程序的运行。



### 1. 基本使用

**语法格式**

```shell
 nohup Command [ Arg … ] [　& ]
```

**参数说明：**

**Command**：要执行的命令。

**Arg**：一些参数，可以指定输出文件。

**&**：让命令在后台执行，终端退出后命令仍旧执行。



**实例**

```
nohup /root/test.sh &
```

查看运行的后台进程

1. `jobs -l`
2. `ps -ef` 
3. 如果某个进程起不来，可能是某个端口被占用，查看端口进程：

```shell
lsof -i:8090

netstat -ap|grep 8090
```

4. 终止后台运行的进程

```shell
kill -9 8090
```



### 2. 输出文件

以下命令在后台执行test.sh 脚本，并重定向输入到 mylog.log 文件：

```shell
nohup test.sh > mylog.log 2>&1 &
```

操作系统中有三个常用的流：
	0 - 标准输入流 stdin
　1 - 标准输出流 stdout
　2 - 标准错误流 stderr

一般当我们用 > console.txt，实际是 1>console.txt的省略用法；< console.txt ，实际是 0 < console.txt的省略用法。

**2>&1 &** 解释：

1. 带**&**的命令行，即使terminal（终端）关闭，或者电脑死机程序依然运行（前提是你把程序递交到服务器上)； 

2. **2>&1**的意思是把标准错误2重定向到标准输出中1，而标准输出又导入文件output里面，所以结果是标准错误和标准输出都导入文件output里面了。至于为什么需要将标准错误重定向到标准输出的原因，那就归结为标准错误没有缓冲区，而stdout有。这就会导致 >output 2>output 文件output被两次打开，而stdout和stderr将会竞争覆盖，这肯定不是我门想要的。这就是为什么有人会写成： nohup ./command.sh >output 2>output出错的原因了



### 3. 不输出日志文件

**/dev/null**（参见dd命令章节）文件的作用，这是一个无底洞，任何东西都可以定向到这里，但是却无法打开。

所以一般很大的stdou和stderr当你不关心的时候可以利用stdout和stderr定向到这里

```shell
>./command.sh >/dev/null 2>&1 
```



### 4. 日志按天输出

输出日志在当前目录：

```shell
nohup command.sh >> nohup`date +%Y-%m-%d`.out 2>&1 &
```

 

指定输出到当前目录log文件夹中

```shell
nohup command.sh >> ./log/nohup`date +%Y-%m-%d`.out 2>&1 &
```

