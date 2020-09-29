# 前言



## 关于博客

这个博客



## 搭建教程

搭建这个博客的时候，我使用了如下工具：

- Markdown：书写文档

- Pandoc：格式转化工具
- Sphinx：中文检索及生成静态网页
- Github：项目托管
- ReadtheDocs：网页发布



### 1. 安装Sphnix

- 安装

可参照[Sphnix官网文档](https://pandoc.org/installing.html)



- 初始化

创建一个工程目录，执行 `sphinx-quickstart` 命令

```python
sphinx-quickstart
```



- 执行完成会看到如下文件

```css
.
├── build
├── make.bat
├── Makefile
└── source
    ├── conf.py
    └──index.rst
```

> build：这是触发特定输出后用来存放所生成的文件的目录。

> make.bat：bat脚本

> Makefile：使用 make 命令，可以构建文档输出。

> source：这是存放.rst文件的目录。

> > conf.py：\用于存放 Sphinx 的配置值

> > index.rst：文档项目的 root 目录



### 2.配置及拓展

对Sphinx做了如下拓展：

- 配置主题
- 支持LaTex
- 支持中文检索

配置文件及拓展文件，都可以在Github上找到



### 3.编写文章及生成静态html

Sphinx默认支持rst文件。在source目录下，新增`preface.rst`

内容如下：

```rst
前言
====

关于博客
--------

这个博客

搭建教程
--------

搭建这个博客的时候，我使用了如下工具：

-  Markdown：书写文档
-  Pandoc：格式转化工具
-  Sphinx：中文检索及生成静态网页
-  Github：项目托管
-  ReadtheDocs：网页发布
```

然后写进排版配置文件`source/index.rst`中

```rst
Python学习笔记
==========================================

.. toctree::
   :maxdepth: 2
   :glob:

   preface
```

执行`make html`生成html静态文件

```
$ make html
Running Sphinx v3.2.1
loading translations [zh_CN]... done
making output directory... done
WARNING: multiple files found for the document "aboutme": ['aboutme.rst', 'aboutme.md']
Use '/Users/bjhl/PycharmProjects/mkdocs/source/aboutme.rst' for the build.
WARNING: multiple files found for the document "preface": ['preface.md', 'preface.rst']
Use '/Users/bjhl/PycharmProjects/mkdocs/source/preface.rst' for the build.
building [mo]: targets for 0 po files that are out of date
building [html]: targets for 9 source files that are out of date
updating environment: [new config] 9 added, 0 changed, 0 removed
reading sources... [100%] preface 
build succeeded.
The HTML pages are in build/html.
```

在build文件夹下可以找到`index.html`文件，用浏览器打开，可以看到效果

![image-20200904174442779](/Users/bjhl/Library/Application Support/typora-user-images/image-20200904174442779.png)

因为我习惯使用MarkDown写文章，可以使用Pandoc([官方文档](https://pandoc.org/installing.html))这个工具转换文档格式。转换命令如下：

```
pandoc -V mainfont="SimSun" -f markdown -t rst hello.md -o hello.rst
```



### 4.托管项目

我把项目托管在`GitHub`上，具体方法就不介绍了，`.gitignore`内容如下：

```
build/
.idea/
*.pyc
```



### 5.发布上线

代码托管后，我使用Read the Docs来发布。

首先在Read the Docs注册账号，关联GitHub。

![image-20200904183643011](/Users/bjhl/Library/Application Support/typora-user-images/image-20200904183643011.png)

导入代码库，填好对应的信息，构建网页后，可以看到发布后的在线地址。



![image-20200904181900385](/Users/bjhl/Library/Application Support/typora-user-images/image-20200904181900385.png)

