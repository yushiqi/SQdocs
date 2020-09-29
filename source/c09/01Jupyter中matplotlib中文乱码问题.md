# 9.1 Linux环境下Jupyter中matplotlib中文乱码

**解决方法：**

1. 下载SimHei字体（百度搜一个就可以）
2. 找到matplotlib的文件位置

```python
import matplotlib
matplotlib.matplotlib_fname()
```

查看到matplotlib的文件路径，我的路径是：

```
/apps/home/rd/anaconda3/lib/python3.7/site-packages/matplotlib/mpl-data/matplotlibrc
```

进入到`mpl-data/fonts`路径，把下载好的`SimHei.ttf`文件导入进去

3. 返回到`mpl-data`目录，打开`matplotlibrc`文件，搜索定位到`font.family`
   取消`font.family`、`font.serif`和`font.sans-serif`的注释，并在`font.serif`和`font.sans-serif`后添加`SimHei`，保存
4. 进入到`~/.cache`目录，删除该目录下的`matplotlib`文件夹

```shell
cd ~/.cache
rm -rf  matplotlib
```

5. 重新打开jupyter，可以输入如下代码查看是否导入SimHei字体

```python
from matplotlib import font_manager
a = sorted([f.name for f in font_manager.fontManager.ttflist])
for i in a:
    print(i)
```

6. 在导入matplotlib包之后加一句

```python
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
```

