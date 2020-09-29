6.1 包管理工具pip
-----------------

1. 安装
~~~~~~~

通常情况，pip是默认安装的，如果没有我们可以按照如下方式安装：

-  使用easy_install安装：
   各种进入到easy_install脚本的目录下，然后运行\ ``easy_inatall pip``

-  使用get-pip.py安装： 下载get-pip.py脚本
   ``curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py``
   然后运行：\ ``python get-pip.py``
   这个脚本会同时安装setuptools和wheel工具。

-  在linux下使用包管理工具安装pip：

   ubuntu下：\ ``sudo apt-get install python-pip``

   Fedora系下：\ ``sudo yum install python-pip``

-  在windows下安装pip：
   在C::raw-latex:`\python`27:raw-latex:`\scirpts下运行easy`\_install
   pip进行安装。

刚安装完毕的pip可能需要先升级一下自身： 在Linux或masOS中：

.. code:: shell

   $ pip install -U pip

在windows中：

.. code:: shell

   $ python -m pip install -U pip

2. 查询软件包
~~~~~~~~~~~~~

查询当前环境安装的所有软件包

.. code:: shell

   $ pip list

查询 pypi 上含有某名字的包

.. code:: shell

   $ pip search pkg

查询当前环境中可升级的包

.. code:: shell

   $ pip list --outdated

查询一个包的详细内容

.. code:: shell

   $ pip show pkg

3. 下载软件包
~~~~~~~~~~~~~

在不安装软件包的情况下下载软件包到本地

.. code:: shell

   $ pip download --destination-directory /local/wheels -r requirements.txt

下载完，总归是要安装的，可以指定这个目录中安装软件包，而不从 pypi
上安装。

.. code:: shell

   $ pip install --no-index --find-links=/local/wheels -r requirements.txt

当然你也从你下载的包中，自己构建生成 wheel 文件

.. code:: shell

   $ pip install wheel
   $ pip wheel --wheel-dir=/local/wheels -r requirements.txt

4. 安装软件包
~~~~~~~~~~~~~

使用 ``pip install <pkg>`` 可以很方便地从 pypi 上搜索下载并安装 python
包。

如下所示

.. code:: shell

   $ pip install requests

这是安装包的基本格式，我们也可以为其添加更多参数来实现不同的效果。

**4.1 只从本地安装，而不从 pypi 安装**

.. code:: shell

   # 前提你得保证你已经下载 pkg 包到 /local/wheels 目录下
   $ pip install --no-index --find-links=/local/wheels pkg

**4.2 限定版本进行软件包安装**

以下三种，对单个 python 包的版本进行了约束

.. code:: shell

   # 所安装的包的版本为 2.1.2
   $ pip install pkg==2.1.2

   # 所安装的包必须大于等于 2.1.2
   $ pip install pkg>=2.1.2

   # 所安装的包必须小于等于 2.1.2
   $ pip install pkg<=2.1.2

以下命令用于管理/控制整个 python 环境的包版本

.. code:: shell

   # 导出依赖包列表
   pip freeze >requirements.txt

   # 从依赖包列表中安装
   pip install -r requirements.txt

   # 确保当前环境软件包的版本(并不确保安装)
   pip install -c constraints.txt

**4.3 限制不使用二进制包安装**

由于默认情况下，wheel 包的平台是运行 pip download 命令
的平台，所以可能出现平台不适配的情况。

比如在 MacOS 系统下得到的 pymongo-2.8-cp27-none-macosx_10_10_intel.whl
就不能在 linux_x86_64 安装。

使用下面这条命令下载的是 tar.gz 的包，可以直接使用 pip install 安装。

比 wheel 包，这种包在安装时会进行编译，所以花费的时间会长一些。

.. code:: shell

   # 下载非二进制的包
   $ pip download --no-binary=:all: pkg

   #　安装非二进制的包
   $ pip install pkg --no-binary

**4.4 指定代理服务器安装**

当你身处在一个内网环境中时，无法直接连接公网。这时候你使用\ ``pip install``
安装包，就会失败。

面对这种情况，可以有两种方法：

1. 下载离线包拷贝到内网机器中安装
2. 使用代理服务器转发请求

第一种方法，虽说可行，但有相当多的弊端

-  步骤繁杂，耗时耗力
-  无法处理包的依赖问题

这里重点来介绍，第二种方法：

.. code:: shell

   $ pip install --proxy [user:passwd@]http_server_ip:port pkg

每次安装包就发输入长长的参数，未免有些麻烦，为此你可以将其写入配置文件中：\ ``$HOME/.config/pip/pip.conf``

对于这个路径，说明几点

-  不同的操作系统，路径各不相同

.. code:: shell

   # Linux/Unix:
   /etc/pip.conf
   ~/.pip/pip.conf
   ~/.config/pip/pip.conf

   # Mac OSX:
   ~/Library/Application Support/pip/pip.conf
   ~/.pip/pip.conf
   /Library/Application Support/pip/pip.conf

   # Windows:
   %APPDATA%\pip\pip.ini
   %HOME%\pip\pip.ini
   C:\Documents and Settings\All Users\Application Data\PyPA\pip\pip.conf (Windows XP)
   C:\ProgramData\PyPA\pip\pip.conf (Windows 7及以后)

-  若在你的机子上没有此文件，则自行创建即可

如何配置，这边给个样例：

.. code:: shell

   [global]
   index-url = http://mirrors.aliyun.com/pypi/simple/

   # 替换出自己的代理地址，格式为[user:passwd@]proxy.server:port
   proxy=http://xxx.xxx.xxx.xxx:8080

   [install]
   # 信任阿里云的镜像源，否则会有警告
   trusted-host=mirrors.aliyun.com

**4.5 安装用户私有软件包**

很多人可能还不清楚，python 的安装包是可以用户隔离的。

如果你拥有管理员权限，你可以将包安装在全局环境中。在全局环境中的这个包可被该机器上的所有拥有管理员权限的用户使用。

如果一台机器上的使用者不只一样，自私地将在全局环境中安装或者升级某个包，是不负责任且危险的做法。

面对这种情况，我们就想能否安装单独为我所用的包呢？

庆幸的是，还真有。

我能想到的有两种方法：

1. 使用虚拟环境
2. 将包安装在用户的环境中

虚拟环境，之前写过几篇文章，这里不再展开讲。

今天的重点是第二种方法，教你如何安装用户私有的包？

命令也很简单，只要加上 ``--user`` 参数，pip 就会将其安装在当前用户的
``~/.local/lib/python3.x/site-packages`` 下，而其他用户的 python
则不会受影响。

.. code:: shell

   $ pip install --user pkg

来举个例子

.. code:: shell

   # 在全局环境中未安装 requests
   [root@localhost ~]# pip list | grep requests
   [root@localhost ~]# su - wangbm
   [root@localhost ~]#

   # 由于用户环境继承自全局环境，这里也未安装
   [wangbm@localhost ~]# pip list | grep requests
   [wangbm@localhost ~]# pip install --user requests
   [wangbm@localhost ~]# pip list | grep requests
   requests (2.22.0)
   [wangbm@localhost ~]#

   # 从 Location 属性可发现 requests 只安装在当前用户环境中
   [wangbm@ws_compute01 ~]$ pip show requests
   ---
   Metadata-Version: 2.1
   Name: requests
   Version: 2.22.0
   Summary: Python HTTP for Humans.
   Home-page: http://python-requests.org
   Author: Kenneth Reitz
   Author-email: me@kennethreitz.org
   Installer: pip
   License: Apache 2.0
   Location: /home/wangbm/.local/lib/python2.7/site-packages
   [wangbm@localhost ~]$ exit
   logout

   # 退出 wangbm 用户，在 root 用户环境中发现 requests 未安装
   [root@localhost ~]$ pip list | grep requests
   [root@localhost ~]$

当你身处个人用户环境中，python
导包时会先检索当前用户环境中是否已安装这个包，已安装则优先使用，未安装则使用全局环境中的包。

验证如下：

.. code:: shell

   >>> import sys
   >>> from pprint import pprint
   >>> pprint(sys.path)
   ['',
    '/usr/lib64/python27.zip',
    '/usr/lib64/python2.7',
    '/usr/lib64/python2.7/plat-linux2',
    '/usr/lib64/python2.7/lib-tk',
    '/usr/lib64/python2.7/lib-old',
    '/usr/lib64/python2.7/lib-dynload',
    '/home/wangbm/.local/lib/python2.7/site-packages',
    '/usr/lib64/python2.7/site-packages',
    '/usr/lib64/python2.7/site-packages/gtk-2.0',
    '/usr/lib/python2.7/site-packages',
    '/usr/lib/python2.7/site-packages/pip-18.1-py2.7.egg',
    '/usr/lib/python2.7/site-packages/lockfile-0.12.2-py2.7.egg']
   >>>

5. 卸载软件包
~~~~~~~~~~~~~

就一条命令，不再赘述

.. code:: shell

   $ pip uninstall pkg

6. 升级软件包
~~~~~~~~~~~~~

想要对现有的 python 进行升级，其本质上也是先从 pypi
上下载最新版本的包，再对其进行安装。所以升级也是使用
``pip install``\ ，只不过要加一个参数 ``--upgrade``\ 。

.. code:: shell

   $ pip install --upgrade pkg

在升级的时候，其实还有一个不怎么用到的选项
``--upgrade-strategy``\ ，它是用来指定升级策略。

它的可选项只有两个：

-  ``eager`` ：升级全部依赖包
-  ``only-if-need``\ ：只有当旧版本不能适配新的父依赖包时，才会升级。

在 pip 10.0 版本之后，这个选项的默认值是
``only-if-need``\ ，因此如下两种写法是一互致的。

.. code:: shell

   $ pip install --upgrade pkg1
   $ pip install --upgrade pkg1 --upgrade-strategy only-if-need

7. 配置文件
~~~~~~~~~~~

由于在使用 pip 安装一些包时，默认会使用 pip
的官方源，所以经常会报网络超时失败。

常用的解决办法是，在安装包时，使用 ``-i``
参数指定一个国内的镜像源。但是每次指定就很麻烦呀，还要打超长的一串字母。

这时候，其实可以将这个源写进 pip
的配置文件里。以后安装的时候，就默认从你配置的这个 源里安装了。

那怎么配置呢？文件文件在哪？

使用\ ``win+r`` 输入 ``%APPDATA%`` 进入用户资料文件夹，查看有没有一个
pip 的文件夹，若没有则创建之。

然后进入这个 文件夹，新建一个 ``pip.ini`` 的文件，内容如下

.. code:: shell

   [global]
   time-out=60
   index-url=https://pypi.tuna.tsinghua.edu.cn/simple/
   [install]
   trusted-host=tsinghua.edu.cn
