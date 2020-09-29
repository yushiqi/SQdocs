6.2 虚拟环境 - virtualenv
-------------------------

virtualenv
是一个创建隔绝的Python环境的工具。virtualenv创建一个包含所有必要的可执行文件的文件夹，用来使用Python工程所需的包。

1.安装
~~~~~~

.. code:: shell

   $ pip install virtualenv

2.\ **基本使用**
~~~~~~~~~~~~~~~~

**2.1 为一个工程创建一个虚拟环境**

.. code:: shell

   $ cd my_project_dir
   $ virtualenv venv　　# venv为虚拟环境目录名，目录名自定义

``virtualenv venv``
将会在当前的目录中创建一个文件夹，包含了Python可执行文件，以及 pip
库的一份拷贝，这样就能安装其他包了。虚拟环境的名字（此例中是 venv
）可以是任意的；若省略名字将会把文件均放在当前目录。

在任何你运行命令的目录中，这会创建Python的拷贝，并将之放在叫做 venv
的文件中。

你可以选择使用一个Python解释器：

.. code:: shell

   $ virtualenv -p /usr/bin/python2.7 venv　　　　# -p参数指定Python解释器程序路径

这将会使用 /usr/bin/python2.7 中的Python解释器。

**2.2 要开始使用虚拟环境，其需要被激活**

.. code:: shell

   $ source venv/bin/activate

``现在起，任何你使用pip安装的包将会放在 venv``
文件夹中，与全局安装的Python隔绝开。

可以像平常一样安装包，比如：

.. code:: shell

   $ pip install requests

**2.3 退出虚拟环境，可以使用**

.. code:: shell

   $ . venv/bin/deactivate

这将会回到系统默认的Python解释器，包括已安装的库也会回到默认的。

**2.4 要删除一个虚拟环境，只需删除它的文件夹。（执行 ``rm -rf venv``
）**

这里virtualenv
有些不便，因为virtual的启动、停止脚本都在特定文件夹，可能一段时间后，你可能会有很多个虚拟环境散落在系统各处，你可能忘记它们的名字或者位置。

3. virtualenvwrapper
~~~~~~~~~~~~~~~~~~~~

鉴于virtualenv不便于对虚拟环境集中管理，所以推荐直接使用virtualenvwrapper。
virtualenvwrapper提供了一系列命令使得和虚拟环境工作变得便利。它把你所有的虚拟环境都放在一个地方。

**3.1 安装virtualenvwrapper(确保virtualenv已安装)**

.. code:: shell

   $ pip install virtualenvwrapper

   $ pip install virtualenvwrapper-win　　#Windows使用该命令

安装完成后，在~/.bashrc写入以下内容

.. code:: shell

   export WORKON_HOME=~/Envs
   source /usr/local/bin/virtualenvwrapper.sh　　
   # 查找virtualenvwrapper.sh可以使用：find / -name virtualenvwrapper.sh

　　第一行：virtualenvwrapper存放虚拟环境目录

　　第二行：virtrualenvwrapper会安装到python的bin目录下，所以该路径是python安装目录下bin/virtualenvwrapper.sh

.. code:: shell

   $ source ~/.bashrc　　　　# 读入配置文件，立即生效

　

**3.2 virtualenvwrapper基本使用**

-  创建虚拟环境　\ **mkvirtualenv**

.. code:: shell

   $ mkvirtualenv venv

这样会在WORKON_HOME变量指定的目录下新建名为venv的虚拟环境。

若想指定python版本，可通过“–python”指定python解释器

.. code:: shell

   $ mkvirtualenv --python=/usr/local/python3.5.3/bin/python venv

   $ mkvirtualenv -p python3 虚拟环境名称

-  基本命令

查看当前的虚拟环境目录

.. code:: shell

   $ [root@localhost ~]# workon

   $ py2

   $ py3

-  切换到虚拟环境

.. code:: shell

   $ [root@localhost ~]# workon py3

   $ (py3) [root@localhost ~]#

-  退出虚拟环境

.. code:: shell

   $ (py3) [root@localhost ~]# deactivate

   $ [root@localhost ~]#

-  删除虚拟环境

.. code:: shell

   $ rmvirtualenv venv
