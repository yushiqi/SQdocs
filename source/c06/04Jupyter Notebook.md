## 6.4 Jupyter Notebook



> Jupyter Notebook是基于网页的用于交互计算的应用程序。其可被应用于全过程计算：开发、文档编写、运行代码和展示结果。——[Jupyter Notebook官方介绍](https://link.jianshu.com/?t=https%3A%2F%2Fjupyter-notebook.readthedocs.io%2Fen%2Fstable%2Fnotebook.html)



### 1. Jupyter Notebook特点

- 编程时具有**语法高亮**、*缩进*、*tab补全*的功能。

- 可直接通过浏览器运行代码，同时在代码块下方展示运行结果。

- 以富媒体格式展示计算结果。富媒体格式包括：HTML，LaTeX，PNG，SVG等。

- 对代码编写说明文档或语句时，支持Markdown语法。

- 支持使用LaTeX编写数学性说明。



### 2. 安装 Jupyter Notebook

推荐使用 Anaconda，内置了Jupyter NoteBook工具

#### 2.1 什么是Anaconda？

##### 1. 简介

Anaconda（[官方网站](https://link.jianshu.com?t=https%3A%2F%2Fwww.anaconda.com%2Fdownload%2F%23macos)）就是可以便捷获取包且对包能够进行管理，同时对环境可以统一管理的发行版本。Anaconda包含了conda、Python在内的超过180个科学包及其依赖项。



##### 2. 特点

Anaconda具有如下特点：

- 开源
- 安装过程简单
- 高性能使用Python和R语言
- 免费的社区支持

其特点的实现主要基于Anaconda拥有的：

- conda包
- 环境管理器
- 1,000+开源库

如果日常工作或学习并不必要使用1,000多个库，那么可以考虑安装Miniconda（[图形界面下载及命令行安装请戳](https://link.jianshu.com?t=https%3A%2F%2Fconda.io%2Fminiconda.html)），这里不过多介绍Miniconda的安装及使用。



##### 3. Anaconda、conda、pip、virtualenv的区别

###### ① Anaconda

- Anaconda是一个包含180+的科学包及其依赖项的发行版本。其包含的科学包包括：conda, numpy, scipy, ipython notebook等。

###### ② conda

- conda是包及其依赖项和环境的管理工具。

- 适用语言：Python, R, Ruby, Lua, Scala, Java, JavaScript, C/C++, FORTRAN。

- 适用平台：Windows, macOS, Linux

- 用途：

  1. 快速安装、运行和升级包及其依赖项。
  2. 在计算机中便捷地创建、保存、加载和切换环境。

  > 如果你需要的包要求不同版本的Python，你无需切换到不同的环境，因为conda同样是一个环境管理器。仅需要几条命令，你可以创建一个完全独立的环境来运行不同的Python版本，同时继续在你常规的环境中使用你常用的Python版本。——[conda官方网站](https://link.jianshu.com?t=https%3A%2F%2Fconda.io%2Fdocs%2F)

- conda为Python项目而创造，但可适用于上述的多种语言。

- conda包和环境管理器包含于Anaconda的所有版本当中。

###### ③ pip

- pip是用于安装和管理软件包的包管理器。
- pip编写语言：Python。
- Python中默认安装的版本：
  - Python 2.7.9及后续版本：默认安装，命令为`pip`
  - Python 3.4及后续版本：默认安装，命令为`pip3`
- pip名称的由来：pip采用的是**递归缩写**进行命名的。其名字被普遍认为来源于2处：
  - “Pip installs Packages”（“pip安装包”）
  - “Pip installs Python”（“pip安装Python”）



###### ④ virtualenv

- virtualenv：用于创建一个**独立的**Python环境的工具。
- 解决问题：
  1. 当一个程序需要使用Python 2.7版本，而另一个程序需要使用Python 3.6版本，如何同时使用这两个程序？
  2. 如果将所有程序都安装在系统下的默认路径，如：`/usr/lib/python2.7/site-packages`，当不小心升级了本不该升级的程序时，将会对其他的程序造成影响。
  3. 如果想要安装程序并在程序运行时对其库或库的版本进行修改，都会导致程序的中断。
  4. 在共享主机时，无法在全局`site-packages`目录中安装包。
- virtualenv将会为它自己的安装目录创建一个环境，这并**不与**其他virtualenv环境共享库；同时也可以**选择性**地不连接已安装的全局库。



###### ⑤ pip 与 conda 比较

**依赖项检查**

- pip：
  - **不一定**会展示所需其他依赖包。
  - 安装包时**或许**会直接忽略依赖项而安装，仅在结果中提示错误。
- conda：
  - 列出所需其他依赖包。
  - 安装包时自动安装其依赖项。
  - 可以便捷地在包的不同版本中自由切换。

**环境管理**

- pip：维护多个环境难度较大。
- conda：比较方便地在不同环境之间进行切换，环境管理较为简单。

**对系统自带Python的影响**

- pip：在系统自带Python中包的**更新/回退版本/卸载将影响其他程序。
- conda：不会影响系统自带Python。

**适用语言**

- pip：仅适用于Python。
- conda：适用于Python, R, Ruby, Lua, Scala, Java, JavaScript, C/C++, FORTRAN。

###### ⑥ conda与pip、virtualenv的关系

- conda**结合**了pip和virtualenv的功能。



#### 2.2 Anaconda的适用平台及安装条件

##### 1. 适用平台

Anaconda可以在以下系统平台中安装和使用：

- Windows
- macOS
- Linux（x86 / Power8）



##### 2. 安装条件

- 系统要求：32位或64位系统均可
- 下载文件大小：约500MB
- 所需空间大小：3GB空间大小（Miniconda仅需400MB空间即可）



#### 2.3 Anaconda的安装步骤

##### 1. macOS系统安装Anaconda

###### ① 图形界面安装

前往[官方下载页面](https://link.jianshu.com?t=https%3A%2F%2Fwww.anaconda.com%2Fdownloads%23macos)下载。

###### ② 命令行安装

1. 前往[官方下载页面](https://link.jianshu.com?t=https%3A%2F%2Fwww.anaconda.com%2Fdownloads%23macos)下载。有两个版本可供选择：Python 3.6 和 Python 2.7，我下载的是前者。选择版之后点击“64-Bit Command-Line Installer”进行下载。
2. 完成下载之后，在mac的Launchpad中找到“其他”并打开“终端”。
   - 安装Python 3.6：`bash ~/Downloads/Anaconda3-5.0.1-MacOSX-x86_64.sh`
   - 安装Python 2.7：`bash ~/Downloads/Anaconda2-5.0.1-MacOSX-x86_64.sh`

- **注意**：
  1. 首词bash也需要输入，无论是否用的Bash shell。
  2. 如果你的下载路径是自定义的，那么把该步骤路径中的`~/Downloads`替换成你自己的下载路径。
  3. 如果你将第1步下载的`.sh`文件重命名了，那么把该步骤路径中的`Anaconda3-5.0.1-MacOSX-x86_64.sh`或`Anaconda2-5.0.1-MacOSX-x86_64.sh`替换成你重命名后的文件名。
     - 强烈建议：**不要**修改文件名。如果重命名，使用**英文**进行命名。

1. 安装过程中，看到提示“In order to continue the installation process, please review the license agreement.”（“请浏览许可证协议以便继续安装。”），点击“Enter”查看“许可证协议”。
2. 在“许可证协议”界面将屏幕滚动至底，输入“yes”表示同意许可证协议内容。然后进行下一步。
3. 安装过程中，提示“Press Enter to confirm the location, Press CTRL-C to cancel the installation or specify an alternate installation directory.”（“按回车键确认安装路径，按'CTRL-C'取消安装或者指定安装目录。”）如果接受默认安装路径，则会显示“PREFIX=/home/<user>/anaconda<2 or 3>”并且继续安装。安装过程大约需要几分钟的时间。

- **建议**：直接接受默认安装路径。

1. 安装器若提示“Do you wish the installer to prepend the Anaconda install location to PATH in your /home/<user>/.bash_profile ?”（“你希望安装器添加Anaconda安装路径在`/home/<user>/.bash_profile`文件中吗？”），建议输入“yes”。

- **注意**：
  1. 路径`/home/<user>/.bash_profile`中“<user>”即进入到家目录后你的目录名。
  2. 如果输入“no”，则需要手动添加路径。添加`export PATH="/<path to anaconda>/bin:$PATH"`在“.bashrc”或者“.bash_profile”中。其中，“<path to anaconda>”替换为你真实的Anaconda安装路径。

1. 当看到“Thank you for installing Anaconda!”则说明已经成功完成安装。

2. 关闭终端，然后再打开终端以使安装后的Anaconda启动。

3. 验证安装结果。可选用以下任意一种方法：

   1. 在终端中输入命令`condal list`，如果Anaconda被成功安装，则会显示已经安装的包名和版本号。

   2. 在终端中输入`python`。这条命令将会启动Python交互界面，如果Anaconda被成功安装并且可以运行，则将会在Python版本号的右边显示“Anaconda custom (64-bit)”。退出Python交互界面则输入`exit()`或`quit()`即可。

   3. 在终端中输入`anaconda-navigator`。如果Anaconda被成功安装，则Anaconda Navigator的图形界面将会被启动。



##### 2. Windows系统安装Anaconda

1. 前往[官方下载页面](https://anaconda.en.softonic.com/)下载。
2. 完成下载之后，双击下载文件，启动安装程序。



##### 3. Linux系统安装Anaconda

1. 前往[官方下载页面](https://anaconda.en.softonic.com/)下载。
2. 启动终端，在终端中输入命令`md5sum /path/filename`或`sha256sum /path/filename`

- 注意：将该步骤命令中的`/path/filename`替换为文件的实际下载路径和文件名。其中，path是路径，filename为文件名。
- **强烈建议**：
  1. 路径和文件名中不要出现空格或其他特殊字符。
  2. 路径和文件名最好以英文命名，不要以中文或其他特殊字符命名。

1. 根据Python版本的不同有选择性地在终端输入命令：
   - Python 3.6：`bash ~/Downloads/Anaconda3-5.0.1-Linux-x86_64.sh`
   - Python 2.7：`bash ~/Downloads/Anaconda2-5.0.1-Linux-x86_64.sh`

- **注意**：
  1. 首词bash也需要输入，无论是否用的Bash shell。
  2. 如果你的下载路径是自定义的，那么把该步骤路径中的`~/Downloads`替换成你自己的下载路径。
  3. 除非被要求使用root权限，否则均选择“Install Anaconda as a user”。

1. 安装过程中，看到提示“In order to continue the installation process, please review the license agreement.”（“请浏览许可证协议以便继续安装。”），点击“Enter”查看“许可证协议”。
2. 在“许可证协议”界面将屏幕滚动至底，输入“yes”表示同意许可证协议内容。然后进行下一步。
3. 安装过程中，提示“Press Enter to accept the default install location, CTRL-C to cancel the installation or specify an alternate installation directory.”（“按回车键确认安装路径，按'CTRL-C'取消安装或者指定安装目录。”）如果接受默认安装路径，则会显示“PREFIX=/home/<user>/anaconda<2 or 3>”并且继续安装。安装过程大约需要几分钟的时间。

- **建议**：直接接受默认安装路径。

1. 安装器若提示“Do you wish the installer to prepend the Anaconda<2 or 3> install location to PATH in your /home/<user>/.bashrc ?”（“你希望安装器添加Anaconda安装路径在`/home/<user>/.bashrc`文件中吗？”），建议输入“yes”。

- **注意**：
  1. 路径`/home/<user>/.bash_rc`中“<user>”即进入到家目录后你的目录名。
  2. 如果输入“no”，则需要手动添加路径，否则conda将无法正常运行。

1. 当看到“Thank you for installing Anaconda<2 or 3>!”则说明已经成功完成安装。
2. 关闭终端，然后再打开终端以使安装后的Anaconda启动。或者直接在终端中输入`source ~/.bashrc`也可完成启动。
3. 验证安装结果。可选用以下任意一种方法：
   1. 在终端中输入命令`condal list`，如果Anaconda被成功安装，则会显示已经安装的包名和版本号。
   2. 在终端中输入`python`。这条命令将会启动Python交互界面，如果Anaconda被成功安装并且可以运行，则将会在Python版本号的右边显示“Anaconda custom (64-bit)”。退出Python交互界面则输入`exit()`或`quit()`即可。
   3. 在终端中输入`anaconda-navigator`。如果Anaconda被成功安装，则Anaconda Navigator将会被启动。



#### 2.4 管理conda

接下来均是以命令行模式进行介绍，Windows用户请打开“Anaconda Prompt”；macOS和Linux用户请打开“Terminal”（“终端”）进行操作。



##### 1. 验证conda已被安装

```shell
$ conda --version
```

终端上将会以`conda 版本号`的形式显示当前安装conda的版本号。如：`conda 3.11.0`

- **注意**：如果出现错误信息，则需核实是否出现以下情况：
  1. 使用的用户是否是安装Anaconda时的账户。
  2. 是否在安装Anaconda之后重启了终端。



##### 2. 更新conda至最新版本

```shell
$ conda update conda
```

执行命令后，conda将会对版本进行比较并列出可以升级的版本。同时，也会告知用户其他相关包也会升级到相应版本。

当较新的版本可以用于升级时，终端会显示`Proceed ([y]/n)?`，此时输入`y`即可进行升级。



##### 3. 查看conda帮助信息

```bash
$ conda --help
```

或

```bash
$ conda -h
```



##### 4. 卸载conda

###### ① Linux 或 macOS

```shell
$  rm -rf ~/anaconda2
```

或

```shell
$  rm -rf ~/anaconda3
```

即删除Anaconda的安装目录。根据安装的Anaconda版本选择相应的卸载命令。



###### ② Windows

```css
控制面板 → 添加或删除程序 → 选择“Python X.X (Anaconda)” → 点击“删除程序”
```

- **注意**：
  1. Python X.X：即Python的版本，如：Python 3.6。
  2. Windows 10的删除有所不同。



#### 2.5 管理环境

接下来均是以命令行模式进行介绍，Windows用户请打开“Anaconda Prompt”；macOS和Linux用户请打开“Terminal”（“终端”）进行操作。



##### 1. 创建新环境

```shell
$  conda create --name <env_name> <package_names>
```

- **注意**：
  - `<env_name>`即创建的环境名。建议以英文命名，且不加空格，名称两边不加尖括号“<>”。
  - `<package_names>`即安装在环境中的包名。名称两边不加尖括号“<>”。
    1. 如果要安装指定的版本号，则只需要在包名后面以`=`和版本号的形式执行。如：`conda create --name python2 python=2.7`，即创建一个名为“python2”的环境，环境中安装版本为2.7的python。
    2. 如果要在新创建的环境中创建多个包，则直接在`<package_names>`后以**空格**隔开，添加多个包名即可。如：`conda create -n python3 python=3.5 numpy pandas`，即创建一个名为“python3”的环境，环境中安装版本为3.5的python，同时也安装了numpy和pandas。
  - `--name`同样可以替换为`-n`。
- **提示**：默认情况下，新创建的环境将会被保存在`/Users/<user_name>/anaconda3/env`目录下，其中，`<user_name>`为当前用户的用户名。



##### 2. 切换环境

###### ① Linux 或 macOS

```bash
$  source activate <env_name>
```

###### ② Windows

```shell
$ activate <env_name>
```

###### ③ 提示

1. 如果创建环境后安装Python时没有指定Python的版本，那么将会安装与Anaconda版本相同的Python版本，即如果安装Anaconda第2版，则会自动安装Python 2.x；如果安装Anaconda第3版，则会自动安装Python 3.x。
2. 当成功切换环境之后，在该行行首将以“(env_name)”或“[env_name]”开头。其中，“env_name”为切换到的环境名。如：在macOS系统中执行`source active python2`，即切换至名为“python2”的环境，则行首将会以(python2)开头。



##### 3. 退出环境至root

###### ① Linux 或 macOS

```bash
$ source deactivate
```



###### ② Windows

```shell
$ deactivate
```



###### ③ 提示

当执行退出当前环境，回到root环境命令后，原本行首以“(env_name)”或“[env_name]”开头的字符将不再显示。



##### 4. 显示已创建环境

```shell
$ conda info --envs
```

或

```shell
$ conda info -e
```

或

```shell
$ conda env list
```



##### 5. 复制环境

```shell
$ conda create --name <new_env_name> --clone <copied_env_name>
```

- **注意**：
  1. `<copied_env_name>`即为被复制/克隆环境名。环境名两边不加尖括号“<>”。
  2. `<new_env_name>`即为复制之后新环境的名称。环境名两边不加尖括号“<>”。
  3. 如：`conda create --name py2 --clone python2`，即为克隆名为“python2”的环境，克隆后的新环境名为“py2”。此时，环境中将同时存在“python2”和“py2”环境，且两个环境的配置相同。



##### 6. 删除环境

```shell
$ conda remove --name <env_name> --all
```

- **注意**：`<env_name>`为被删除环境的名称。环境名两边不加尖括号“<>”。



#### 2.6 管理包

##### 1. 查找可供安装的包版本

###### ① 精确查找

```shell
$ conda search --full-name <package_full_name>
```

- **注意**：
  1. `--full-name`为精确查找的参数。
  2. `<package_full_name>`是被查找包的**全名**。包名两边不加尖括号“<>”。
- **例如**：`conda search --full-name python`即查找全名为“python”的包有哪些版本可供安装。



###### ② 模糊查找

```shell
$ conda search <text>
```

- **注意**：`<text>`是查找含有**此字段**的包名。此字段两边不加尖括号“<>”。
- **例如**：`conda search py`即查找含有“py”字段的包，有哪些版本可供安装。



##### 2. 获取当前环境中已安装的包信息

```shell
$ conda list
```

执行上述命令后将在终端显示当前环境已安装包的包名及其版本号。



##### 3. 安装包

###### ① 在指定环境中安装包

```shell
$ conda install --name <env_name> <package_name>
```

- **注意**：
  1. `<env_name>`即将包安装的指定环境名。环境名两边不加尖括号“<>”。
  2. `<package_name>`即要安装的包名。包名两边不加尖括号“<>”。
- **例如**：`conda install --name python2 pandas`即在名为“python2”的环境中安装pandas包。



###### ② 在当前环境中安装包

```shell
$ conda install <package_name>
```

- **注意**：
  1. `<package_name>`即要安装的包名。包名两边不加尖括号“<>”。
  2. 执行命令后在当前环境中安装包。
- **例如**：`conda install pandas`即在当前环境中安装pandas包。



###### ③ 使用pip安装包

**使用场景**

当使用`conda install`无法进行安装时，可以使用pip进行安装。例如：see包。

**命令**

```shell
$ pip install <package_name>
```

- **注意**：<package_name>为指定安装包的名称。包名两边不加尖括号“<>”。
- **例如**：`pip install see`即安装see包。

**注意**

1. pip只是包管理器，无法对环境进行管理。因此如果想在指定环境中使用pip进行安装包，则需要先切换到指定环境中，再使用pip命令安装包。
2. pip无法更新python，因为pip并不将python视为包。
3. pip可以安装一些conda无法安装的包；conda也可以安装一些pip无法安装的包。因此当使用一种命令无法安装包时，可以尝试用另一种命令。



##### 4. 卸载包

###### ① 卸载指定环境中的包

```shell
$ conda remove --name <env_name> <package_name>
```

- **注意**：
  1. `<env_name>`即卸载包所在指定环境的名称。环境名两边不加尖括号“<>”。
  2. `<package_name>`即要卸载包的名称。包名两边不加尖括号“<>”。
- **例如**：`conda remove --name python2 pandas`即卸载名为“python2”中的pandas包。



###### ② 卸载当前环境中的包

```shell
$ conda remove <package_name>
```

- **注意**：
  1. `<package_name>`即要卸载包的名称。包名两边不加尖括号“<>”。
  2. 执行命令后即在当前环境中卸载指定包。
- **例如**：`conda remove pandas`即在当前环境中卸载pandas包。



##### 5. 更新包

###### ① 更新所有包

```shell
$ conda update --all
```

或

```shell
$ conda upgrade --all
```

- **建议**：在安装Anaconda之后执行上述命令更新Anaconda中的所有包至最新版本，便于使用。



###### ② 更新指定包

```shell
$ conda update <package_name>
```

或

```shell
$ conda upgrade <package_name>
```

- **注意**：
  1. `<package_name>`为指定更新的包名。包名两边不加尖括号“<>”。
  2. 更新多个指定包，则包名以**空格**隔开，向后排列。如：`conda update pandas numpy matplotlib`即更新pandas、numpy、matplotlib包。



### 3. Jupyter Notebook配置

#### 3.1. 生成配置文件

如果服务器上你的账户下已有默认 jupyter 用户的配置文件，可以直接拷贝一份，改个名字，比如：

```shell
$ cd /root/.jupyter

$ cp jupyter_notebook_config.py jupyter_my_config.py
```

或者，直接自己找个任意目录，比如 /root/my_configs，直接创建一个新文件作为配置文件：

```shell
$ mkdir /root/my_configs

$ cd /root/my_configs

$ touch jupyter_notebook_config.py
```

再或者，账户下未建立默认 jupyter 配置文件的情况下，可以自动生成：

```shell
$ jupyter notebook --generate-config
```



#### 3.2. 编辑配置文件

打开 jupyter_notebook_config.py 文件：

```shell
$ vim jupyter_notebook_config.py
```

可以看到全是注释的配置说明，比较复杂，也不是都用得上，这里我们自己写一些重要的配置即可，在文件开头写入：

```xml
c = get_config()

c.IPKernelApp.pylab = "inline"

c.NotebookApp.ip = "*"

c.NotebookAPp.open_browser = False

c.NotebookApp.password = 'sha1:b39d2445079f:9b9ab99f65150e113265cb99a841a6403aa52647'

c.NotebookApp.certfile = u'/root/.jupyter/mycert.pem'

c.NotebookApp.port= 8888

c.NotebookApp.notebook_dir = "/root/ipython"
```



**注意1**：第五行 password 填入的是<登录密码的 sha1 加密版>，通过以下方式生成：

```shell
[root@VM_157_11_centos .jupyter]# python

Python 2.7.5 (default, Aug 4 2017, 00:39:18)

[GCC 4.8.5 20150623 (Red Hat 4.8.5-16)] on linux2

Type "help", "copyright", "credits" or "license" for more information.

>>> from IPython.lib import passwd

>>> passwd()

Enter password:

Verify password:

'sha1:175e8efe8974:eacef02a2e3f959d6efdf6c93d142c7f4712f5cc'

>>> exit()
```

**注意2**：第六行的 certfile 证书文件可以通过下面这行命令生成（中间的交互信息可以随便填），注意路径要对应上：

```shell
$ openssl req -x509 -nodes -days 365 -newkey rsa:1024 -keyout mycert.pem -out mycert.pem
```

**注意3**：第七行的 port 应该是一个未被占用的、被防火墙允许的端口（在上面的步骤我们已经打开了 8888 端口），这里再强调一遍（同样的，腾讯云等服务器需要在官网修改安全策略）：

```shell
$ firewall-cmd --zone=public --add-port=8888/tcp --permanent

success # 系统反馈信息

$ systemctl restart firewalld.service
```

**注意4**：第八行的 notebook_dir 是你的文档目录，需要自行选择并创建（否则运行时会报错）：

```shell
$ mkdir /root/ipython
```

**运行**

```shell
$ jupyter notebook *--config jupyter_notebook_config.py --allow-root*
```

**关于参数**：–config 是可选的，默认会用 jupyter_notebook_config.py 文件，如果有多个用户配置文件（给多个用户分别提供 jupyter notebook），就必须要用这个命令了。–allow-root 是 root 用户启动 jupyter notebook 时的必须参数，实际上不建议使用 root 启动 jupyter notebook，最好还是用其他用户启动，这样在 浏览器端 cmd 窗口就不至于直接暴露 root 权限。

**后台运行：** 实际使用的时候我们当然会让 jupyter notebook 在后台一直运行着，即使我断开 ssh 连接之后也要可以通过浏览器访问。那也简单，用 nohup 命令就可以了：

```shell
$ nohup jupyter notebook --config jupyter_notebook_config.py --allow-root 2>&1 > my.log &
```

用该命令启动 jupyter notebook 之后，原先打印在屏幕上行的日志会写入到 my.log 文本文件中（该文件路径可以替换，当然完全不想要日志的话也可以重定向到 /dev/null）。



### 4. 主题字体设置及自动代码补全

github上发现了一个[jupyter-themes](https://github.com/dunovank/jupyter-themes)工具，可以通过pip安装，非常方便使用。

首先是主题下载，命令行如下所示：

```shell
$ pip install --no-dependencies jupyterthemes==0.18.2
```

安装好了，有的电脑可能会提示缺少 **lesscpy**，继续 pip 安装

```shell
$ pip install lesscpy
```

然后是对主题选择、字体大小进行设置，我总结了一个我最喜欢的

```shell
$ jt --lineh 140 -f consolamono -tf ptmono -t grade3 -ofs 14 -nfs 14 -tfs 14 -fs 14 -T -N
```

 命令行的格式的解释如下表所示

| **cl options**        | **arg** | **default** |
| --------------------- | ------- | ----------- |
| Usage help            | -h      | --          |
| List Themes           | -l      | --          |
| Theme Name to Install | -t      | --          |
| Code Font             | -f      | --          |
| Code Font-Size        | -fs     | 11          |
| Notebook Font         | -nf     | --          |
| Notebook Font Size    | -nfs    | 13          |
| Text/MD Cell Font     | -tf     | --          |
| Text/MD Cell Fontsize | -tfs    | 13          |
| Pandas DF Fontsize    | dfs     | 9           |
| Output Area Fontsize  | -ofs    | 8.5         |
| Mathjax Fontsize (%)  | -mathfs | 100         |
| Intro Page Margins    | -m      | auto        |
| Cell Width            | -cellw  | 980         |
| Line Height           | -lineh  | 170         |
| Cursor Width          | -cursw  | 2           |
| Cursor Color          | -cursc  | --          |
| Alt Prompt Layout     | -altp   | --          |
| Alt Markdown BG Color | -altmd  | --          |
| Alt Output BG Color   | -altout | --          |
| Style Vim NBExt*      | -vim    | --          |
| Toolbar Visible       | -T      | --          |
| Name & Logo Visible   | -N      | --          |
| Reset Default Theme   | -r      | --          |
| Force Default Fonts   | -dfonts | --          |

 接着让 jupyter notebook 实现自动代码补全，首先安装 **nbextensions**

```shell
$ pip install jupyter_contrib_nbextensions

$ jupyter contrib nbextension install --user
```

然后安装 **nbextensions_configurator**

```shell
$ pip install jupyter_nbextensions_configurator
```

如果提示缺少依赖，就使用pip安装对应依赖即可。

最后重启jupyter，在弹出的主页面里，能看到增加了一个Nbextensions标签页，在这个页面里，勾选Hinterland即启用了代码自动补全，如图所示：

![1330952-20180911211947213-1976856179](/Users/bjhl/Documents/1330952-20180911211947213-1976856179.png)



### 5. JupyterLab

#### 5.1 简介

JupyterLab是Jupyter主打的最新数据科学生产工具，某种意义上，它的出现是为了取代Jupyter Notebook。

JupyterLab有以下特点：

- **交互模式：**Python交互式模式可以直接输入代码，然后执行，并立刻得到结果，因此Python交互模式主要是为了调试Python代码用的
- **内核支持的文档：**使你可以在可以在Jupyter内核中运行的任何文本文件（Markdown，Python，R等）中启用代码
- **模块化界面：**可以在同一个窗口同时打开好几个notebook或文件（HTML, TXT, Markdown等等），都以标签的形式展示，更像是一个IDE
- **镜像notebook输出：**让你可以轻易地创建仪表板
- **同一文档多视图：**使你能够实时同步编辑文档并查看结果
- **支持多种数据格式：**你可以查看并处理多种数据格式，也能进行丰富的可视化输出或者Markdown形式输出
- **云服务：**使用Jupyter Lab连接Google Drive等服务，极大得提升生产力



#### 5.2 安装Jupyter Lab

你可以使用`pip`、`conda`安装Jupyter Lab

**pip**
`pip`可能是大多数人使用包管理工具，如果使用`pip`安装，请在命令行执行：

```text
pip install jupyterlab
```

**conda**
如果你是Anaconda用户，那么可以直接用`conda`安装，请在命令行执行：

```text
conda install -c conda-forge jupyterlab
```



#### 5.3 运行Jupyter Lab

在安装Jupyter Lab后，接下来要做的是运行它。
你可以在命令行使用`jupyter-lab`或`jupyter lab`命令，然后默认浏览器会自动打开Jupyter Lab。



---

### 推荐链接

[15个好用到爆炸的Jupyter Lab插件](https://zhuanlan.zhihu.com/p/101070029)

[GitHub JupyterLab](https://github.com/jupyterlab/jupyterlab)

