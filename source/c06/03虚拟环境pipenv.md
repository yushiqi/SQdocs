

## 6.3 虚拟环境pipenv



### 1.pipenv解决的问题

**1.1 requirements.txt依赖管理的局限**

如果我要使用 flask, 我会在requirements.txt里面写上

```tex
flask
```

不过由于没有指定版本，因此在另一个环境通过pip install -r requirements.txt安装依赖模块时，会默认安装最新版本的flask，如果新版本向后兼容，这当然是没问题的。但是如果新版本不兼容旧的接口，那么就出问题了：代码无法在该环境运行。因此测试环境和生产环境的不一致出现了，同一份requirement.txt，结果出来2份不同的环境，这叫做不确定构建 (the build isn’t deterministic) 问题。

这时候，可以考虑加上版本号，requirements.txt这么写

```tex
flask==0.12.1
```

这么写肯定可以了吧？因为以后在新环境安装pip install -r requirements.txt的时候，用的是该指定版本，就不会发生跑不起来的情况。

是这样吗？不一定哟，我们再分析一下：因为flask本身还依赖于其他模块，因此执行pip install -r requirements.txt的时候，flask使用的是0.12.1版本，但是它的依赖模块可不一定相同。比如说flask依赖Werkzeug模块，而Werkzeug模块的新版本有bug！

这时候，传统的解决方式是使用pip freeze， 它能给出当前环境下第三方模块和所有依赖子模块的版本号，因此在生产环境就可以确保使用与开发环境相同的模块了。这样我就可以把pip freeze的输出写入到requirement.txt：

```tex
click==6.7

Flask==0.12.1

itsdangerous==0.24

Jinja2==2.10

MarkupSafe==1.0

Werkzeug==0.14.1
```

这或许解决了生产与开发环境不一致的问题，可是它又引入了一大坨新问题！

因为，也许Werkzeug==0.14.1隐藏了一个漏洞，官方发布了0.14.2版本修复了该问题，那么我不仅需要及时下载更新模块，还得去更新requirememts.txt文件。但是那么多模块，我难道要把所有更新版本都记录下来？事实上，我本不需要记录那么多我不关心的模块的版本，我只想记录自己关心的核心模块版本。

这就出现了一个矛盾：<确定构建>与<不记录所有模块版本>之间的矛盾。



**1.2 多个项目依赖不同版本的子模块**

假如我有2个项目A和B，A依赖django==1.9，B依赖django==1.10。linux默认使用全局共享的依赖包，因此当我在A和B项目间切换时，需要检测--卸载--安装django。

传统的解决方式是使用[virtual environment](https://links.jianshu.com/go?to=https%3A%2F%2Frealpython.com%2Fpython-virtual-environments-a-primer%2F) ，将项目A和B的第三包隔离开。python2目前有virtualenv方案，python3目前有venv方案。

而pipenv也集成了虚拟环境管理的功能。



**1.3 依赖分析**

先解释一下什么叫依赖分析，假如我有一个requirments.txt如下：

```txt
package_a

package_b
```

如果package_a依赖于package_c>=1.0，package_b依赖于同样的package_c<=2.0, 那么在安装a，b模块时，就只能在（1.0，2.0）的中选择package_c的版本，如果安装工具有这种能力，就说它能做依赖分析。

不过pip工具没有这种依赖分析的功能。这时候只能通过在requirement.txt里面添加package_c的版本范围才能解决问题，好傻：

```tex
package_c>=1.0,<=2.0

package_a

package_b
```



### 2. 安装pipenv

```shell
$ pip install pipenv
```

在指定目录下创建虚拟环境, 会使用本地默认版本的python

```shell
$ pipenv install
```

如果要指定版本创建环境，可以使用如下命令，当然前提是本地启动目录能找到该版本的python

```shell
$ pipenv --python 3.6
```

激活虚拟环境

```shell
$ pipenv shell
```

安装第三方模块, 运行后会生成Pipfile和Pipfile.lock文件

```shell
$ pipenv install flask==0.12.1
```

当然也可以不指定版本：

```shell
$ pipenv install numpy
```

如果想只安装在开发环境才使用的包，这么做：

```shell
$ pipenv install pytest --dev
```

无论是生产环境还是开发环境的包都会写入一个Pipfile里面，而如果是用传统方法，需要2个文件：dev-requirements.txt 和 test-requirements.txt。

接下来如果在开发环境已经完成开发，如何构建生产环境的东东呢？这时候就要使用Pipfile.lock了，运行以下命令，把当前环境的模块lock住, 它会更新Pipfile.lock文件，该文件是用于生产环境的，你永远不应该编辑它。

```shell
$ pipenv lock
```

然后只需要把代码和Pipfile.lock放到生产环境，运行下面的代码，就可以创建和开发环境一样的环境咯，Pipfile.lock里记录了所有包和子依赖包的确切版本，因此是确定构建：

```shell
$ pipenv install --ignore-pipfile
```

如果要在另一个开发环境做开发，则将代码和Pipfile复制过去，运行以下命令：

```shell
$ pipenv install --dev
```

由于Pipfile里面没有所有子依赖包或者确定的版本，因此该安装可能会更新未指定模块的版本号，这不仅不是问题，还解决了一些其他问题，我在这里做一下解释：

假如该命令更新了一些依赖包的版本，由于我肯定还会在新环境做单元测试或者功能测试，因此我可以确保这些包的版本更新是不会影响软件功能的；然后我会pipenv lock并把它发布到生产环境，因此我可以确定生产环境也是不会有问题的。这样一来，我既可以保证生产环境和开发环境的一致性，又可以不用管理众多依赖包的版本，完美的解决方案！



### 3. 操作虚拟环境

```shell
# 返回项目的路径
$ pipenv --where

# 返回虚拟环境路径
$ pipenv --venv

# 返回该虚拟环境的解释器
$ pipenv --py

# 进入这个虚拟环境
$ pipenv shell

# 退出这个虚拟环境
$ exit
$ deactivate

# 移除当前目录的虚拟环境
$ pipenv --rm

# 在当前虚拟环境中运行
$ pipenv run python  # 进入交互式,跟直接执行 python 一样
$ pipenv run python 文件名 # 运行文件
$ pipenv run pip ...  # 运行pip
```



### 4. 虚拟环境包管理

```shell
# 安装一个本地包（setup.py）到虚拟环境（Pipfile）
$ pipenv install -e .

# 安装、卸载模块
$ pipenv install requests
$ pipenv uninstall requests
$ pipenv uninstall --all   # 卸载全部包
$ pipenv install -r path/to/requirements.txt


# 安装所有依赖
$ pipenv install --dev

# 更新包
$ pipenv update # 更新所有包
$ pipenv update --outdated # 打印所有要更新的包
$ pipenv update <包名> # 更新指定的包

# 将Pipfile和Pipfile.lock文件里面的包导出为requirements.txt文件
$ pipenv run pip freeze  # 相当于pipenv run pip freeze >requirements.txt

$ pipenv lock -r > requirements.txt
$ pipenv lock -r --dev # 若只想导出开发用的包

# 创建一个包含预发布的锁文件:
$ pipenv lock --pre

# 打印所有包的依赖关系图
$ pipenv graph

# 检查安全漏洞
$ pipenv check
```



###5. 旧项目的requirments.txt转化为Pipfile

使用pipenv install会自动检测当前目录下的requirments.txt, 并生成Pipfile, 我也可以再对生成的Pipfile做修改。

此外以下命令也有同样效果, 可以指定具体文件名：

```shell
$ pipenv install -r requirements.txt
```

如果我有一个开发环境的requirent-dev.txt, 可以用以下命令加入到Pipfile:

```shell
$ pipenv install -r dev-requirements.txt --dev
```

