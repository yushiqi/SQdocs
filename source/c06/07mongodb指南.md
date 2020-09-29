## 6.7 mongodb指南



### 1. 简介

MongoDB 是一个基于分布式文件存储的数据库。MongoDB 是一个介于关系数据库和非关系数据库之间的产品，是非关系数据库当中功能最丰富，最像关系数据库的。它支持的数据结构非常松散，是类似json的bson格式，因此可以存储比较复杂的数据类型。Mongo最大的特点是它支持的查询语言非常强大，其语法有点类似于面向对象的查询语言，几乎可以实现类似关系数据库单表查询的绝大部分功能，而且还支持对数据建立索引。



通过对比SQL，可以对mongodb中的文档、集合、数据库有一个基本了解：

| SQL术语/概念 | MongoDB术语/概念 | 解释/说明                           |
| :----------- | :--------------- | :---------------------------------- |
| database     | database         | 数据库                              |
| table        | collection       | 数据库表/集合                       |
| row          | document         | 数据记录行/文档                     |
| column       | field            | 数据字段/域                         |
| index        | index            | 索引                                |
| table joins  |                  | 表连接,MongoDB不支持                |
| primary key  | primary key      | 主键,MongoDB自动将_id字段设置为主键 |



**MongoDB的特点**

- 面向集合存储，易存储对象类型的数据。
- 模式自由
- 支持动态查询
- 可通过网络访问
- 支持查询
- 支持复制和故障恢复
- 支持完全索引，包含内部对象
- 文件存储格式为BSON（一种JSON的扩展）
- 自动处理碎片，以支持云计算层次的扩展性
- 使用高效的二进制数据存储，包括大型对象（如视频等）
- 支持 **Golang**，**RUBY**，**PYTHON**，**JAVA**，**C++**，**PHP**，**C#** 等多种语言
- MongoDB安装简单。



**MongoDB 的适用场景**

MongoDB 的主要目标是在键/值存储方式（提供了高性能和高度伸缩性）和传统的RDBMS 系统（具有丰富的功能）之间架起一座桥梁，它集两者的优势于一身。根据官方网站的描述，Mongo 适用于以下场景。

- 网站数据：Mongo 非常适合实时的插入，更新与查询，并具备网站实时数据存储所需的复制及高度伸缩性。
- 缓存：由于性能很高，Mongo 也适合作为信息基础设施的缓存层。在系统重启之后，由Mongo 搭建的持久化缓存层可以避免下层的数据源过载。
- 高伸缩性的场景：Mongo 非常适合由数十或数百台服务器组成的数据库，Mongo 的路线图中已经包含对MapReduce 引擎的内置支持。
- 用于对象及JSON 数据的存储：Mongo 的BSON 数据格式非常适合文档化格式的存储及查询。

MongoDB 的使用也会有一些限制，例如，它不适合于以下几个地方。

- 高度事务性的系统：例如，银行或会计系统。传统的关系型数据库目前还是更适用于需要大量原子性复杂事务的应用程序。
- 传统的商业智能应用：针对特定问题的BI 数据库会产生高度优化的查询方式。对于此类应用，数据仓库可能是更合适的选择。
- 需要SQL 的问题。





### 2. 创建、删除、更新

#### 2.1 创建

文档的数据结构和JSON基本一样。

所有存储在集合中的数据都是BSON格式。

BSON是一种类json的一种二进制形式的存储格式,简称Binary JSON。

MongoDB 使用 `insert()` 或 `save()` 方法向集合中插入文档，语法如下：

```powershell
db.COLLECTION_NAME.insert(document)

db.COLLECTION_NAME.save(document)
```

- `save()`：如果 _id 主键存在则更新数据，如果不存在就插入数据。该方法新版本中已废弃，可以使用 **db.collection.insertOne()** 或 **db.collection.replaceOne()** 来代替。
- `insert()`: 若插入的数据主键已经存在，则会抛 **org.springframework.dao.DuplicateKeyException** 异常，提示主键重复，不保存当前数据。

**3.2 版本之后新增了 db.collection.insertOne() 和 db.collection.insertMany()。**

db.collection.insertOne() 用于向集合插入一个新文档，语法格式如下：

```powershell
db.collection.insertOne(
   <document>,
   {
      writeConcern: <document>
   }
)
```

db.collection.insertMany() 用于向集合插入一个多个文档，语法格式如下：

```powershell
db.collection.insertMany(
   [ <document 1> , <document 2>, ... ],
   {
      writeConcern: <document>,
      ordered: <boolean>
   }
)
```

参数说明：

- document：要写入的文档。
- writeConcern：写入策略，默认为 1，即要求确认写操作，0 是不要求。
- ordered：指定是否按顺序写入，默认 true，按顺序写入。



#### 2.2 删除

`remove()`函数是用来移除集合中的数据

```powershell
db.collection.remove(
   <query>,
   <justOne>
)
```

**参数说明：**

- **query** :（可选）删除的文档的条件。

- **justOne** : （可选）如果设为 true 或 1，则只删除一个文档。

- **writeConcern** :（可选）抛出异常的级别。

  

#### 2.3 更新

使用 `update()` 和 `save()` 方法来更新集合中的文档



**update() 方法**

`update()` 方法用于更新已存在的文档。语法格式如下：

```powershell
db.collection.update(
   <query>,
   <update>,
   {
     upsert: <boolean>,
     multi: <boolean>,
     writeConcern: <document>
   }
)
```

**参数说明：**

- **query** : update的查询条件，类似sql update查询内where后面的。

- **update** : update的对象和一些更新的操作符（如$,$inc...）等，也可以理解为sql update查询内set后面的

- **upsert** : 可选，这个参数的意思是，如果不存在update的记录，是否插入objNew,true为插入，默认是false，不插入。

- **multi** : 可选，mongodb 默认是false,只更新找到的第一条记录，如果这个参数为true,就把按条件查出来多条记录全部更新。

- **writeConcern** :可选，抛出异常的级别。

  

**save() 方法**

`save()` 方法通过传入的文档来替换已有文档，_id 主键存在就更新，不存在就插入。语法格式如下：

```powershell
db.collection.save(
   <document>,
   {
     writeConcern: <document>
   }
)
```

**参数说明：**

- **document** : 文档数据。
- **writeConcern** :可选，抛出异常的级别。





### 3. 查询

#### 3.1 find查询

MongoDB 查询数据的语法格式如下：

```powershell
>db.collection.find(query, projection)
```

- **query** ：可选，使用查询操作符指定查询条件
- **projection** ：可选，使用投影操作符指定返回的键。查询时返回文档中所有键值， 只需省略该参数即可（默认省略）。

如果你需要以易读的方式来读取数据，可以使用 pretty() 方法，语法格式如下：

```powershell
>db.col.find().pretty()
```

pretty() 方法以格式化的方式来显示所有文档。除了 find() 方法之外，还有一个 findOne() 方法，它只返回一个文档。



#### 3.2 查询条件

##### 1. 条件查询

MongoDB中条件操作符有：

- (>) 大于 - $gt
- (<) 小于 - $lt
- (>=) 大于等于 - $gte
- (<= ) 小于等于 - $lte

**MongoDB 与 RDBMS Where 语句比较**

| 操作       | 格式                     | 范例                                        | RDBMS中的类似语句     |
| :--------- | :----------------------- | :------------------------------------------ | :-------------------- |
| 等于       | `{<key>:<value>`}        | `db.col.find({"name":"lisi"}).pretty()`     | `where name = 'lisi'` |
| 小于       | `{<key>:{$lt:<value>}}`  | `db.col.find({"likes":{$lt:50}}).pretty()`  | `where likes < 50`    |
| 小于或等于 | `{<key>:{$lte:<value>}}` | `db.col.find({"likes":{$lte:50}}).pretty()` | `where likes <= 50`   |
| 大于       | `{<key>:{$gt:<value>}}`  | `db.col.find({"likes":{$gt:50}}).pretty()`  | `where likes > 50`    |
| 大于或等于 | `{<key>:{$gte:<value>}}` | `db.col.find({"likes":{$gte:50}}).pretty()` | `where likes >= 50`   |
| 不等于     | `{<key>:{$ne:<value>}}`  | `db.col.find({"likes":{$ne:50}}).pretty()`  | `where likes != 50`   |



##### 2. OR查询

MongoDB中有两种方式进行OR查询：

`$in`可以用来查询一个键的多个值；

`$or`更通用一些，可以在多个键中查询任意的给定值。



如果一个键需要和多个值进行匹配的话，就要有`$in`操作符

```powershell
>db.descinfo.find({"views":{"$in":[143, 23, 444]}})
```

`$in`非常灵活，可以指定不用类型的条件和值

```powershell
>db.descinfo.find({"user_id":{"$in":[143, "tom", 444]}})
```

如果`$in`对应的数组只有一个值，那么和直接匹配这个值的效果是一样的

```powershell
>db.descinfo.find({"user_id":{"$in":[143]}})
等价于
>db.descinfo.find({"user_id":143})
```

与`$in`相对的是`$nin`，`$nin`返回与数组中所有条件都不匹配的文档

```powershell
>db.descinfo.find({"views":{"$in":[143, 23, 444]}})
```

查询结果返回views值不是143、23、444的所有文档



`$in`能对**单个键**做OR查询，如果需要查询类似于"age"为20或"name"为"张三"的文档，就需要用`$or`。`$or`接受一个包含所有可能条件的数组作为参数。

```powershell
>db.student.find({"$or":[{"age":20},{"name":"张三"}]})
```

**使用普通的AND型查询时，总是希望尽可能用最少的条件来限定结果的范围。OR型查询正相反：第一个条件应该尽可能匹配更多的文档，这样才是最为高效的。**

`$or`在任何情况下都会正常工作。如果查询优化器可以更高效地处理`$in​`，那就选择使用它。



##### 3. $not

`$not`是元条件句，即可以用在任何其他条件之上。

就拿取模运算符`$mod`来说。`$mod`会将查询的值除以第一个给定值，若余数等于第二个给定值则匹配成功:

```powershell
>db.users.find({"id_num":{"$mod":[5,1]}})
```

上面的查询会返回"id_num"值为1、6、11、16等的用户。但要是想返回"id_num"为2、3、4、5、7、8、9、10、12等的用户，就要用`$not`了：

```powershell
>db.users.find({"id_num":{"not":{"$mod":[5,1]}}})
```





### 4. 特定类型查询

#### 4.1 null

null不仅会匹配某个键的值为null的文档，而且还会匹配不包含这个键的文档。所以，这种匹配还会返回缺少这个键的所有文档：

如果仅想匹配键值为null的文档，既要检查该键的值是否为null，还要通过"$exists"条件判定键值已存在：

```powershell
>db.c.find({"z":{"$in":[null],"$exists":true}}) 
```

**注意：**MongoDB中没有`$eq`操作符，但是使用只有一个元素的`$in`操作符效果是一样的。



#### 4.2 查询数组

查询数组元素与查询标量值是一样的。例如，有一个水果列表，如下所示：

```powershell
>db.food.insert({"fruit":["apple","banana","peach"]})
```

下面的查询：

```powershell
>db.food.find({"fruit":"banana"})
```

会成功匹配该文档。这个查询好比我们对一个这样的（不合法）文档进行查询：**{"fruit":"apple","fruit":"banana","fruit":"peach"}**。



**$all**

如果需要通过多个元素来匹配数组，就要用`$all`了。这样就会匹配一组元素。例如，假设创建了一个包含3个元素的集合：

```powershell
>db.food.insert({"_id":1,"fruit":["apple","banana","peach"]})

>db.food.insert({"_id":2,"fruit":["apple","kumquat","orange"]})

>db.food.insert({"_id":3,"fruit":["cherry","banana","apple"]})
```

要找到既有"apple"又有"banana"的文档，可以使用`$all`来

```powershell
>db.food.find({fruit:{$all:["apple","banana"]}})

{"_id":1,"fruit":["apple","banana","peach"]}
{"_id":3,"fruit":["cherry","banana","apple"]}
```

这里的顺序无关紧要。注意，第二个结果中**"banana"**在**"apple"**之前。要是对只有一个元素的数组使用`$all`，就和不用`$all`一样了。例如，**{fruit:{$all:['apple']}**和**{fruit:'apple'}**的查询结果完全一样。

也可以使用整个数组进行精确匹配。但是，精确匹配对于缺少元素或者元素冗余的情况就不大灵了。例如，下面的方法会匹配之前的第一个文档：

```powershell
>db.food.find({"fruit":["apple","banana","peach"]})
```

但是下面这个就不会匹配：

```powershell
>db.food.find({"fruit":["apple","banana"]})
```

这个也不会匹配：

```powershell
>db.food.find({"fruit":["banana","apple","peach"]})
```

要是想查询数组特定位置的元素，需使用key.index语法指定下标：

```powershell
>db.food.find({"fruit.2":"peach"})
```

数组下标都是从0开始的，所以上面的表达式会用数组的第3个元素和"peach"进行匹配。



**$size**

`$size`对于查询数组来说也是非常有用的，顾名思义，可以用它查询特定长度的数组。例如：

```powershell
>db.food.find({"fruit":{"$size":3}})
```

得到一个长度范围内的文档是一种常见的查询。`$size`并不能与其他查询条件（比如`$gt`）组合使用，但是这种查询可以通过在文档中添加一个**"size"**键的方式来实现。这样每一次向指定数组添加元素时，同时增加**"size"**的值。比如，原本这样的更新：

```powershell
>db.food.update(criteria,{"$push":{"fruit":"strawberry"}}) 
```

就要变成下面这样：

```powershell
>db.food.update(criteria,{"$push":{"fruit":"strawberry"},"$inc":{"size":1}})
```

自增操作的速度非常快，所以对性能的影响微乎其微。这样存储文档后，就可以像下面这样查询了：

```powershell
>db.food.find({"size":{"$gt":3}})
```



**$slice操作符**

find的第二个参数是可选的，可以指定需要返回的键。这个特别的`$slice`操作符可以返回某个键匹配的数组元素的一个子集。

假设现在有一个博客文章的文档，我们希望返回前10条评论，可以这样做：

```powershell
>db.blog.posts.findOne(criteria,{"comments":{"$slice":10}})
```

也可以返回后10条评论:

```powershell
>db.blog.posts.findOne(criteria,{"comments":{"$slice":-10}})
```

`$slice`也可以指定偏移值以及希望返回的元素数量，来返回元素集合中间位置的某些结果：

```powershell
>db.blog.posts.findOne(criteria,{"comments":{"$slice":[23,10]}})
```

这个操作会跳过前23个元素，返回第24~33个元素。如果数组不够33个元素，则返回第23个元素后面的所有元素。

除非特别声明，否则使用`$slice`时将返回文档中的所有键。别的键说明符都是默认不返回未提及的键，这点与`$slice`不太一样。例如，有如下博客文章文档：

```json
{
	"_id": ObjectId("4b2d75476cc613d5ee930164"),
	"title": "Ablogpost",
	"content": "...",
	"comments": [{
			"name": "joe",
			"email": "joe@example.com",
			"content": "nicepost."
		},
		{
			"name": "bob",
			"email": "bob@example.com",
			"content": "goodpost."
		}
	]
}
```

用`$slice`来获取最后一条评论，可以这样：

```powershell
>db.blog.posts.findOne(criteria,{"comments":{"$slice":1}})

{
	"_id": ObjectId("4b2d75476cc613d5ee930164"),
	"title": "Ablogpost",
	"content": "...",
	"comments": [{
		"name": "bob",
		"email": "bob@example.com",
		"content": "goodpost."
	}]
}
```

**"title"**和**"content"**都返回了，即便是并没有显式地出现在键说明符中。



**返回一个匹配的数组元素**

如果知道元素的下标，那么`$slice`非常有用。但有时我们希望返回与查询条件相匹配的任意一个数组元素。可以使用$操作符得到一个匹配的元素。对于上面的博客文章示例，可以用如下的方式得到Bob的评论：

```powershell
>db.blog.posts.find({"comments.name":"bob"},{"comments.$":1})

{
	"_id": ObjectId("4b2d75476cc613d5ee930164"),
	"comments": [{
		"name": "bob",
		"email": "bob@example.com",
		"content": "goodpost."
	}]
}
```

注意，这样只会返回第一个匹配的文档。如果Bob在这篇博客文章下写过多条评论，只有**"comments"**数组中的第一条评论会被返回。



#### 4.3 正则表达式

MongoDB 使用 `$regex` 操作符来设置匹配字符串的正则表达式。MongoDB使用PCRE (Perl Compatible Regular Expression) 作为正则表达式语言。不同于全文检索，我们使用正则表达式不需要做任何配置。

考虑以下**profile**集合的文档结构，该文档包含了文章内容和标签：

```json
{
    "_id" : "xinhuashefabu1",
    "aliasName" : "xinhuashefabu1",
    "logo_url" : "http://wx.qlogo.cn/mmhead/Q3auHgzwzM6CRL0IbOnOf9n66mYHko2JPHX9GCPqPkSlHzibCHnua3w/96",
    "detail" : "新华通讯社官方账号。新华社是中国国家通讯社，现场新闻、原创新闻报道的大本营。",
    "wxId" : "gh_6651e07e4b2d",
    "name" : "新华社",
    "register" : "新华新媒文化传播有限公司",
    "biz" : "MzA4NDI3NjcyNA==",
    "links" : [ 
        {
            "url" : "https://xhpfmapi.zhongguowangshi.com/vh512/sceneList/9",
            "word" : "现场云"
        }, 
        {
            "url" : "https://xhpfmapi.zhongguowangshi.com/vh512/fasttheme/25367",
            "word" : "AI主播"
        }, 
        {
            "userName" : "gh_345c5d37f42f@app",
            "weappUrl" : "/pages/home-page/index.html?p=63",
            "word" : "掌上高铁"
        }
    ],
  	"tags": [
      "新闻",
      "新闻资讯",
      "热门"
    ]
}
```

**使用正则表达式**

以下命令使用正则表达式查找包含 "新华社" 字符串的文章：

```shell
>db.profile.find({register:{$regex:"新华社"}})
```

以上查询也可以写为：

```powershell
>db.profile.find({post_text:/新华社/})
```

**不区分大小写的正则表达式**

如果检索需要不区分大小写，我们可以设置 `$options` 为 `$i`。

以下命令将查找不区分大小写的字符串 xinhua：

```powershell
>db.profile.find({aliasName:{$regex:"xinhua",$options:"$i"}})
```

**数组元素使用正则表达式**

我们还可以在数组字段中使用正则表达式来查找内容。 这在标签的实现上非常有用，如果需要查找包含以**新闻**开头的标签数据，使用以下代码：

```powershell
>db.profile.find({tags:{$regex:"新闻"}})
```

**优化正则表达式查询**

- 如果对文档中字段设置了索引，那么使用索引相比于正则表达式匹配查找所有的数据查询速度更快。
- 如果正则表达式是前缀表达式，所有匹配的数据将以指定的前缀字符串为开始。例如： 如果正则表达式为 **^tut** ，查询语句将查找以 tut 为开头的字符串。

**这里面使用正则表达式有两点需要注意：**

正则表达式中使用变量。一定要使用eval将组合的字符串进行转换，不能直接将字符串拼接后传入给表达式。否则没有报错信息，只是结果为空！实例如下：

```js
var name=eval("/" + 变量值key +"/i"); 
```

以下是模糊查询包含title关键词, 且不区分大小写:

```js
title:eval("/"+title+"/i")    // 等同于 title:{$regex:title,$Option:"$i"}  
```



#### 4.4 $where

键/值对是一种表达能力非常好的查询方式，但是依然有些需求它无法表达。其他方法都败下阵时，就轮到`$where`子句登场了，用它可以在查询中执行任意的JavaScript。这样就能在查询中做（几乎）任何事情。

**注意：**为安全起见，应该严格限制或者消除`$where`语句的使用。应该禁止终端用户使用任意的`$where`语句。

`$where`语句最常见的应用就是比较文档中的两个键的值是否相等。假如我们有如下文档：

```powershell
>db.foo.insert({"apple":1,"banana":6,"peach":3})

>db.foo.insert({"apple":8,"spinach":4,"watermelon":4})
```

我们希望返回两个键具有相同值的文档。第二个文档中，**"spinach"**和**"watermelon"**的值相同，所以需要返回该文档。

MongoDB似乎从来没有提供过一个条件语句来做这种查询，所以只能用`$where`子句借助JavaScript来完成了：

```powershell
>db.foo.find({"$where":function(){
    for(varcurrentinthis){
        for(varotherinthis){
            if(current!=other&&this[current]==this[other]){
                return true;
            }
        }
    }
    return false;
    }});
```

如果函数返回true，文档就做为结果集的一部分返回；如果为false，就不返回。

不是非常必要时，一定要避免使用`$where`查询，因为它们在速度上要比常规查询慢很多。每个文档都要从BSON转换成JavaScript对象，然后通过`$where`表达式来运行。而且`$where`语句不能使用索引，所以只在走投无路时才考虑`$where`这种用法。先使用常规查询进行过滤，然后再使用`$where`语句，这样组合使用可以降低性能损失。如果可能的话，使用`$where`语句前应该先使用索引进行过滤，`$where`只用于对结果进行进一步过滤。





### 5. 游标

#### 5.1 limit、skip和sort

`limit()`方法接受一个数字参数，该参数指定从MongoDB中读取的记录条数。

```powershell
>db.COLLECTION_NAME.find().limit(NUMBER)
```



`skip()`方法来跳过指定数量的数据，skip方法同样接受一个数字参数作为跳过的记录条数。

```powershell
>db.COLLECTION_NAME.find().limit(NUMBER).skip(NUMBER)
```

**避免使用skip()跳过大量数据**

跳过数量过多会导致`skip()`查询变得很慢，因为要先找到需要被略过的数据，然后再抛弃这些数据。大多数数据库都会在索引中保存更多的元数据，用于处理skip，但是MongoDB目前还不支持，所以要尽量避免略过太多的数据。通常可以利用上次的结果来计算下一次查询条件。



`sort() `方法可以通过参数指定排序的字段，并使用 1 和 -1 来指定排序的方式，其中 1 为升序排列，而 -1 是用于降序排列。

```powershell
>db.COLLECTION_NAME.find().sort({KEY:1})
```



#### 5.2 游标生命周期

看待游标有两种角度：客户端的游标以及客户端游标表示的数据库游标。

在服务器端，游标消耗内存和其他资源。游标遍历尽了结果以后，或者客户端发来消息要求终止，数据库将会释放这些资源。释放的资源可以被数据库另作他用，这是非常有益的，所以要尽量保证尽快释放游标（在合理的前提下）。

还有一些情况导致游标终止（随后被清理）。首先，游标完成匹配结果的迭代时，它会清除自身。另外，如果客户端的游标已经不在作用域内了，驱动程序会向服务器发送一条特别的消息，让其销毁游标。最后，即便用户没有迭代完所有结果，并且游标也还在作用域中，如果一个游标在10分钟内没有使用的话，数据库游标也会自动销毁。这样的话，如果客户端崩溃或者出错，MongoDB就不需要维护这上千个被打开却不再使用的游标。

这种“超时销毁”的行为是我们希望的：极少有应用程序希望用户花费数分钟坐在那里等待结果。然而，有时的确希望游标持续的时间长一些。若是如此的话，多数驱动程序都实现了一个叫immortal的函数，或者类似的机制，来告知数据库不要让游标超时。如果关闭了游标的超时时间，则一定要迭代完所有结果，或者主动将其销毁，以确保游标被关闭。否则它会一直在数据库中消耗服务器资源。





### 6. 索引

#### 6.1 索引简介

索引是对数据库表中一列或多列的值进行排序的一种结构。数据库可以直接在索引中查找，在索引中找到条目以后，就可以直接跳转到目标文档的位置，这能使查找速度提高几个数量级。

举个例子，我们创建一个很大的文档集合：

```js
for(i=0;i<1000000;i++){
    db.users.insert(
    {
        "i":i,
        "username":"user"+i,
        "age":Math.floor(Math.random()*100 + 1)
        }
    );
}
```

查询一个随机的username，需要知道的是，可以使用[explain()](https://docs.mongodb.com/manual/reference/method/cursor.explain/#cursor.explain)返回查询过程的详细描述

```shell
db.users.find({username:'user1003'}).explain('executionStats')
```

执行结果：

```json
{
    "queryPlanner" : {
        "plannerVersion" : 1,
        "namespace" : "users",
        "indexFilterSet" : false,
        "parsedQuery" : {
            "username" : {
                "$eq" : "user1003"
            }
        },
        "winningPlan" : {
            "stage" : "COLLSCAN",
            "filter" : {
                "username" : {
                    "$eq" : "user1003"
                }
            },
            "direction" : "forward"
        },
        "rejectedPlans" : []
    },
    "executionStats" : {
        "executionSuccess" : true,
        "nReturned" : 1,
        "executionTimeMillis" : 337,
        "totalKeysExamined" : 0,
        "totalDocsExamined" : 1000000,
        "executionStages" : {
            "stage" : "COLLSCAN",
            "filter" : {
                "username" : {
                    "$eq" : "user1003"
                }
            },
            "nReturned" : 1,
            "executionTimeMillisEstimate" : 290,
            "works" : 1000002,
            "advanced" : 1,
            "needTime" : 1000000,
            "needYield" : 0,
            "saveState" : 7812,
            "restoreState" : 7812,
            "isEOF" : 1,
            "invalidates" : 0,
            "direction" : "forward",
            "docsExamined" : 1000000
        }
    },
    "ok" : 1.0
}
```

可以看到执行整个查询共计扫描文档数1000000，耗时337毫秒。虽然返回结果只有一个，但是由于不知道集合中的username字段是否唯一，MongoDB不得不查看集合中的每一个文档。



类似于此类查询，索引可以根据给定的字段组织数据，让MongoDB更快地找到目标文档，下面我们创建一个索引：

```shell
db.users.ensureIndex({'username':1})
```

再次执行上面的查询，用explain()查看详细描述

```json
{
    "queryPlanner" : {
        "plannerVersion" : 1,
        "namespace" : "users",
        "indexFilterSet" : false,
        "parsedQuery" : {
            "username" : {
                "$eq" : "user1003"
            }
        },
        "winningPlan" : {
            "stage" : "FETCH",
            "inputStage" : {
                "stage" : "IXSCAN",
                "keyPattern" : {
                    "username" : 1.0
                },
                "indexName" : "username_1",
                "isMultiKey" : false,
                "multiKeyPaths" : {
                    "username" : []
                },
                "isUnique" : false,
                "isSparse" : false,
                "isPartial" : false,
                "indexVersion" : 2,
                "direction" : "forward",
                "indexBounds" : {
                    "username" : [ 
                        "[\"user1003\", \"user1003\"]"
                    ]
                }
            }
        },
        "rejectedPlans" : []
    },
    "executionStats" : {
        "executionSuccess" : true,
        "nReturned" : 1,
        "executionTimeMillis" : 0,
        "totalKeysExamined" : 1,
        "totalDocsExamined" : 1,
        "executionStages" : {
            "stage" : "FETCH",
            "nReturned" : 1,
            "executionTimeMillisEstimate" : 0,
            "works" : 2,
            "advanced" : 1,
            "needTime" : 0,
            "needYield" : 0,
            "saveState" : 0,
            "restoreState" : 0,
            "isEOF" : 1,
            "invalidates" : 0,
            "docsExamined" : 1,
            "alreadyHasObj" : 0,
            "inputStage" : {
                "stage" : "IXSCAN",
                "nReturned" : 1,
                "executionTimeMillisEstimate" : 0,
                "works" : 2,
                "advanced" : 1,
                "needTime" : 0,
                "needYield" : 0,
                "saveState" : 0,
                "restoreState" : 0,
                "isEOF" : 1,
                "invalidates" : 0,
                "keyPattern" : {
                    "username" : 1.0
                },
                "indexName" : "username_1",
                "isMultiKey" : false,
                "multiKeyPaths" : {
                    "username" : []
                },
                "isUnique" : false,
                "isSparse" : false,
                "isPartial" : false,
                "indexVersion" : 2,
                "direction" : "forward",
                "indexBounds" : {
                    "username" : [ 
                        "[\"user1003\", \"user1003\"]"
                    ]
                },
                "keysExamined" : 1,
                "seeks" : 1,
                "dupsTested" : 0,
                "dupsDropped" : 0,
                "seenInvalidated" : 0
            }
        }
    },
    "ok" : 1.0
}
```

可以看到，查询过程瞬间完成。

**但是要注意，使用索引是有代价的：对于添加的每一个索引，每次写操作（插入、更新、删除）都将耗费更多的时间。这是因为，当数据发生变动时，MongoDB不仅要更新文档，还要更新集合上的所有索引。因此，MongoDB限制每个集合上最多只能有64个索引。通常，在一个特定的集合上，不应该拥有两个以上的索引。于是，挑选合适的字段建立索引非常重要。**



#### 6.2 复合索引简介

索引的值是按一定顺序排列的，因此，使用索引键对文档进行排序非常快。然而，只有在首先使用索引键进行排序时，索引才有用。例如，在下面的排序里，"username"上的索引没什么作用：

```shell
db.users.find({}).sort({'age':1, 'username':1})
```

这里先根据"age"排序再根据"username"排序，所以"username"在这里发挥的作用并不大。为了优化这个排序，可能需要在"age"和"username"上建立索引：

```shell
db.users.ensureIndex({'age':1, 'username':1})
```

这就建立了一个复合索引



#### 6.3 复合索引键的方向

如果需要在两个（或者更多）查询条件上进行排序，可能需要让索引键的方向不同。例如，假设我们要根据年龄从小到大，用户名从Z到A对上面的集合进行排序。对于这个问题，之前的升序索引变得不再高效：每一个年龄分组内都是按照"username"升序排列的，是A到Z，不是Z到A。对于按"age"升序排列按"username"降序排列这样的需求来说，用上面的索引得到的数据的顺序没什么用。为了在不同方向上优化这个复合排序，需要使用与方向相匹配的索引。在这个例子中，可以使用{"age":1，"username":-1}，它会以下面的方式组织数据：

```json
[21,"user999977"]>0xe57bf737
[21,"user999954"]>0x8bffa512
[21,"user999902"]>0x9e1447d1
[21,"user999900"]>0x3a6a8426
[21,"user999874"]>0xc353ee06
...
[30,"user999936"]>0x7f39a81a
[30,"user999850"]>0xa979e136
[30,"user999775"]>0x5de6b77a
...
[30,"user100324"]>0xe14f8e4d
[30,"user100140"]>0x0f34d446
[30,"user100050"]>0x223c35b1
```

年龄按照从年轻到年长顺序排列，在每一个年龄分组中，用户名是从Z到A排列的（对于我们的用户名来说，也可以说是按照"9"到"0"排列的）。

如果应用程序同时需要按照{"age":1，"username":1}优化排序，我们还需要创建一个这个方向上的索引。至于索引使用的方向，与排序方向相同就可以了。注意，相互反转（在每个方向都乘以1）的索引是等价的：{"age":1，"username":-1}适用的查询与{"age":-1，"username":1}是完全一样的。

只有基于多个查询条件进行排序时，索引方向才是比较重要的。如果只是基于单一键进行排序，MongoDB可以简单地从相反方向读取索引。例如，如果有一个基于{"age":-1}的排序和一个基于{"age":1}的索引，MongoDB会在使用索引时进行优化，就如同存在一个{"age":-1}索引一样（所以不要创建两个这样的索引！）。只有在基于多键排序时，方向才变得重要。



#### 6.4 索引对象和数组

MongoDB允许深入文档内部，对嵌套字段和数组建立索引。嵌套对象和数组字段可以与复合索引中的顶级字段一起使用，虽然它们比较特殊，但是大多数情况下与“正常”索引字段的行为是一致的。

##### 1. 索引嵌套文档

可以在嵌套文档的键上建立索引，方式与正常的键一样。如果有这样一个集合，其中的第一个文档表示一个用户，可能需要使用嵌套文档来表示每个用户的位置：

```json
{"username":"sid",
   "loc":{
     "ip":"1.2.3.4",
     "city":"Springfield",
     "state":"NY"
   }
}
```

需要在"loc"的某一个子字段（比如"loc.city"）上建立索引，以便提高这个字段的查询速度：

```shell
db.users.ensureIndex({"loc.city":1})
```

可以用这种方式对任意深层次的字段建立索引，比如你可以在"x.y.z.w.a.b.c"上建立索引。

**注意：对嵌套文档本身（"loc"）建立索引，与对嵌套文档的某个字段（"loc.city"）建立索引是不同的。对整个子文档建立索引，只会提高整个子文档的查询速度。**



##### 2. 索引数组

也可以对数组建立索引，这样就可以高效地搜索数组中的特定元素。假如有一个博客文章的集合，其中每个文档表示一篇文章。每篇文章都有一个"comments"字段，这是一个数组，其中每个元素都是一个评论子文档。如果想要找出最近被评论次数最多的博客文章，可以在博客文章集合中嵌套的"comments"数组的"date"键上建立索引：

```shell
db.blog.ensureIndex({"comments.date":1})
```

对数组建立索引，实际上是对数组的每一个元素建立一个索引条目，所以如果一篇文章有20条评论，那么它就拥有20个索引条目。因此数组索引的代价比单值索引高：对于单次插入、更新或者删除，每一个数组条目可能都需要更新（可能有上千个索引条目）。

与上面说到的"loc"的例子不同，无法将整个数组作为一个实体建立索引：对数组建立索引，实际上是对数组中的每个元素建立索引，而不是对数组本身建立索引。在数组上建立的索引并不包含任何位置信息：无法使用数组索引查找特定位置的数组元素，比如"comments.4"。

少数特殊情况下，可以对某个特定的数组条目进行索引，比如：

```shell
db.blog.ensureIndex({"comments.10.votes":1})
```

然而，只有在精确匹配第11个数组元素时这个索引才有用（数组下标从0开始）。一个索引中的数组字段最多只能有一个。这是为了避免在多键索引中索引条目爆炸性增长：每一对可能的元素都要被索引，这样导致每个文档拥有n*m个索引条目。假如有一个{"x":1，"y":1}上的索引：

```shell
>//x是一个数组——这是合法的
>db.multi.insert({"x":[1,2,3],"y":1})
>
>//y是一个数组——这也是合法的
>db.multi.insert({"x":1,"y":[4,5,6]})
>
>//x和y都是数组——这是非法的！
>db.multi.insert({"x":[1,2,3],"y":[4,5,6]})
cannotindexparallelarrays[y][x]
```

如果MongoDB要为上面的最后一个例子创建索引，它必须要创建这么多索引条目：{"x":1，"y":4}、{"x":1，"y":5}、{"x":1，"y":6}、{"x":2，"y":4}、{"x":2，"y":5}，{"x":2，"y":6}、{"x":3，"y":4}、{"x":3，"y":5}和{"x":3，"y":6}。尽管这些数组只有3个元素。



#### 6.5 索引基数

基数（cardinality）就是集合中某个字段拥有不同值的数量。有一些字段，比如"gender"或者"newsletteroptout"，可能只拥有两个可能的值，这种键的基数就是非常低的。另外一些字段，比如"username"或者"email"，可能集合中的每个文档都拥有一个不同的值，这类键的基数是非常高的。当然也有一些介于两者之间的字段，比如"age"或者"zipcode"。



通常，一个字段的基数越高，这个键上的索引就越有用。这是因为索引能够迅速将搜索范围缩小到一个比较小的结果集。对于低基数的字段，索引通常无法排除掉大量可能的匹配。



假设我们在"gender"上有一个索引，需要查找名为Susan的女性用户。通过这个索引，只能将搜索空间缩小到大约50%，然后要在每个单独的文档中查找"name"为"Susan"的用户。反过来，如果在"name"上建立索引，就能立即将结果集缩小到名为"Susan"的用户，这样的结果集非常小，然后就可以根据性别从中迅速地找到匹配的文档了。



**一般说来，应该在基数比较高的键上建立索引，或者至少应该把基数较高的键放在复合索引的前面（低基数的键之前）。**





#### 6.6 索引管理

**1. 创建索引**

```shell
db.col.createIndex({"索引名称":1})
```

**2. 查看集合索引**

```
db.col.getIndexes()
```

**3. 查看集合索引大小**

```
db.col.totalIndexSize()
```

**4. 删除集合所有索引**

```
db.col.dropIndexes()
```

**5. 删除集合指定索引**

```
db.col.dropIndex("索引名称")
```



### 7. 聚合

#### 7.1 管道操作aggregate

MongoDB中聚合(aggregate)主要用于处理数据(诸如统计平均值,求和等)，并返回计算后的数据结果。有点类似sql语句中的 count(*)。



MongoDB中聚合的方法使用aggregate()。

```powershell
>db.COLLECTION_NAME.aggregate(AGGREGATE_OPERATION)
```

**实例**

集合中的数据如下：

```json
{
   _id: ObjectId(7df78ad8902c)
   title: 'MongoDB Overview', 
   description: 'MongoDB is no sql database',
   by_user: 'w3cschool.cn',
   url: 'http://www.w3cschool.cn',
   tags: ['mongodb', 'database', 'NoSQL'],
   likes: 100
},
{
   _id: ObjectId(7df78ad8902d)
   title: 'NoSQL Overview', 
   description: 'No sql database is very fast',
   by_user: 'w3cschool.cn',
   url: 'http://www.w3cschool.cn',
   tags: ['mongodb', 'database', 'NoSQL'],
   likes: 10
},
{
   _id: ObjectId(7df78ad8902e)
   title: 'Neo4j Overview', 
   description: 'Neo4j is no sql database',
   by_user: 'Neo4j',
   url: 'http://www.neo4j.com',
   tags: ['neo4j', 'database', 'NoSQL'],
   likes: 750
},
```

现在我们通过以上集合计算每个作者所写的文章数，使用aggregate()计算结果如下：

```powershell
> db.mycol.aggregate([{$group : {_id : "$by_user", num_tutorial : {$sum : 1}}}])
{
   "result" : [
      {
         "_id" : "w3cschool.cn",
         "num_tutorial" : 2
      },
      {
         "_id" : "Neo4j",
         "num_tutorial" : 1
      }
   ],
   "ok" : 1
}

```

以上实例类似sql语句： ***select by_user, count(\*) from mycol group by by_user***

在上面的例子中，我们通过字段by_user字段对数据进行分组，并计算by_user字段相同值的总和。

下表展示了一些聚合的表达式:

| 表达式    | 描述                                           |
| :-------- | :--------------------------------------------- |
| $sum      | 计算总和。                                     |
| $avg      | 计算平均值                                     |
| $min      | 获取集合中所有文档对应值得最小值。             |
| $max      | 获取集合中所有文档对应值得最大值。             |
| $push     | 在结果文档中插入值到一个数组中。               |
| $addToSet | 在结果文档中插入值到一个数组中，但不创建副本。 |
| $first    | 根据资源文档的排序获取第一个文档数据。         |
| $last     | 根据资源文档的排序获取最后一个文档数据         |

------

**管道的概念**

管道在Unix和Linux中一般用于将当前命令的输出结果作为下一个命令的参数。

MongoDB的聚合管道将MongoDB文档在一个管道处理完毕后将结果传递给下一个管道处理。管道操作是可以重复的。

表达式：处理输入文档并输出。表达式是无状态的，只能用于计算当前聚合管道的文档，不能处理其它的文档。

这里我们介绍一下聚合框架中常用的几个操作：

- `$project`：修改输入文档的结构。可以用来重命名、增加或删除域，也可以用于创建计算结果以及嵌套文档。
- `$match`：用于过滤数据，只输出符合条件的文档。$match使用MongoDB的标准查询操作。
- `$limit`：用来限制MongoDB聚合管道返回的文档数。
- `$skip`：在聚合管道中跳过指定数量的文档，并返回余下的文档。
- `$unwind`：将文档中的某一个数组类型字段拆分成多条，每条包含数组中的一个值。
- `$group`：将集合中的文档分组，可用于统计结果。
- `$sort`：将输入文档排序后输出。
- `$geoNear`：输出接近某一地理位置的有序文档。

  

**管道操作符实例**

1、$project实例

```
db.article.aggregate(
    { $project : {
        title : 1 ,
        author : 1 ,
    }}
 );
```

这样的话结果中就只还有_id,tilte和author三个字段了，默认情况下_id字段是被包含的，如果要想不包含_id话可以这样:

```
db.article.aggregate(
    { $project : {
        _id : 0 ,
        title : 1 ,
        author : 1
    }});
```

2.$match实例

```
db.articles.aggregate( [
                        { $match : { score : { $gt : 70, $lte : 90 } } },
                        { $group: { _id: null, count: { $sum: 1 } } }
                       ] );
```

$match用于获取分数大于70小于或等于90记录，然后将符合条件的记录送到下一阶段$group管道操作符进行处理。

3.$skip实例

```
db.article.aggregate(
    { $skip : 5 });
```

经过$skip管道操作符处理后，前五个文档被"过滤"掉。



#### 7.2 MapReduce

MapReduce基本语法

```powershell
db.runCommand( {
     mapReduce: <string>,
     map: <string or JavaScript>,
     reduce: <string or JavaScript>,
     finalize: <string or JavaScript>,
     out: <output>,
     query: <document>,
     sort: <document>,
     limit: <number>,
     scope: <document>,
     jsMode: <boolean>,
     verbose: <boolean>,
     bypassDocumentValidation: <boolean>,
     collation: <document>,
     writeConcern: <document>,
     comment: <any>
} )
```

**参数说明：**

- Mapreduce：要操作的目标集合
- Map：映射函数（生成键值对序列，作为reduce函数参数）
- Reduce：统计函数
- Query：目标记录过滤
- Sort：目标记录排序
- Limit：限制目标记录数量
- Out：统计结果存放集合（不指定使用临时集合，在客户端断开后自动删除）
- Keeptemp：是否保留临时集合
- Finalize：最终处理函数（对reduce返回结果进行最终整理后存入结果集合）
- Scope：向map、reduce、finalize导入外部变量
- jsMode说明:为false时 BSON-->JS-->map-->BSON-->JS-->reduce-->BSON,可处理非常大的mapreduce,为true时 BSON-->js-->map-->reduce-->BSON
- Verbose：显示详细的时间统计信息

**行查询的步骤**

- MapReduce对指定的集合Collection进行查询
- 对A的结果集进行mapper方法采集
- 对B的结果执行finalize方法处理
- 最终结果集输出到临时Collection中
- 断开连接，临时Collection删除或保留



**插入样例数据**

```shell
db.orders.insertMany([
   { _id: 1, cust_id: "Ant O. Knee", ord_date: new Date("2020-03-01"), price: 25, items: [ { sku: "oranges", qty: 5, price: 2.5 }, { sku: "apples", qty: 5, price: 2.5 } ], status: "A" },
   { _id: 2, cust_id: "Ant O. Knee", ord_date: new Date("2020-03-08"), price: 70, items: [ { sku: "oranges", qty: 8, price: 2.5 }, { sku: "chocolates", qty: 5, price: 10 } ], status: "A" },
   { _id: 3, cust_id: "Busby Bee", ord_date: new Date("2020-03-08"), price: 50, items: [ { sku: "oranges", qty: 10, price: 2.5 }, { sku: "pears", qty: 10, price: 2.5 } ], status: "A" },
   { _id: 4, cust_id: "Busby Bee", ord_date: new Date("2020-03-18"), price: 25, items: [ { sku: "oranges", qty: 10, price: 2.5 } ], status: "A" },
   { _id: 5, cust_id: "Busby Bee", ord_date: new Date("2020-03-19"), price: 50, items: [ { sku: "chocolates", qty: 5, price: 10 } ], status: "A"},
   { _id: 6, cust_id: "Cam Elot", ord_date: new Date("2020-03-19"), price: 35, items: [ { sku: "carrots", qty: 10, price: 1.0 }, { sku: "apples", qty: 10, price: 2.5 } ], status: "A" },
   { _id: 7, cust_id: "Cam Elot", ord_date: new Date("2020-03-20"), price: 25, items: [ { sku: "oranges", qty: 10, price: 2.5 } ], status: "A" },
   { _id: 8, cust_id: "Don Quis", ord_date: new Date("2020-03-20"), price: 75, items: [ { sku: "chocolates", qty: 5, price: 10 }, { sku: "apples", qty: 10, price: 2.5 } ], status: "A" },
   { _id: 9, cust_id: "Don Quis", ord_date: new Date("2020-03-20"), price: 55, items: [ { sku: "carrots", qty: 5, price: 1.0 }, { sku: "apples", qty: 10, price: 2.5 }, { sku: "oranges", qty: 10, price: 2.5 } ], status: "A" },
   { _id: 10, cust_id: "Don Quis", ord_date: new Date("2020-03-23"), price: 25, items: [ { sku: "oranges", qty: 10, price: 2.5 } ], status: "A" }
])
```



**计算每个客户的总消费**

对**orders**集合进行**map-reduce**操作，对**cust_id**进行分组，并计算每个**cust_id**对应的**price**总和

1. 定义**map**函数来处理每个输入文档：

- 在函数中，**this**指的是**map-reduce**正在处理的文档
- 该函数将映射**price**到**cust_id**每个文档，并生成**cust_id**和**price**对

```js
var mapFunction1 = function() {
   emit(this.cust_id, this.price);
};
```

2. 定义对应的**reduce**函数，包含两个参数**keyCustId**和**valuesPrices**：

- **valuesPrices**是一个数组，其元素是由**map**函数处理后，根据**cust_id**分组的**price**序列
- 该函数处理**valuesPrices**数组，计算出总和

```js
var reduceFunction1 = function(keyCustId, valuesPrices) {
   return Array.sum(valuesPrices);
};
```

3. 在**orders**集合执行**map-reduce**操作，**mapFunction1**作为map函数，**reduceFunction1**作为reduce函数

```js
db.orders.mapReduce(
   mapFunction1,
   reduceFunction1,
   { out: "map_reduce_example" }
)
```

操作将结果输出到名为 `map_reduce_example`的集合。如果`map_reduce_example`集合已经存在，则该操作将用此map-reduce操作的结果替换。

4. 查询**map_reduce_example**集合，验证结果

```js
db.map_reduce_example.find().sort({ _id: 1 })
```

操作返回以下文档：

```json
{ "_id" : "Ant O. Knee", "value" : 95 }
{ "_id" : "Busby Bee", "value" : 125 }
{ "_id" : "Cam Elot", "value" : 60 }
{ "_id" : "Don Quis", "value" : 155 }
```

**聚集替代**

使用管道操作符也可以实现上述map-reduce功能

```js
db.orders.aggregate([
   { $group: { _id: "$cust_id", value: { $sum: "$price" } } },
   { $out: "agg_alternative_1" }
])
```



**用每个项目的平均数量计算订单和总数量**

1. 定义**map**函数

```js
var mapFunction2 = function() {
    for (var idx = 0; idx < this.items.length; idx++) {
       var key = this.items[idx].sku;
       var value = { count: 1, qty: this.items[idx].qty };

       emit(key, value);
    }
};
```

2. 定义**reduce**函数

```js
var reduceFunction2 = function(keySKU, countObjVals) {
   reducedVal = { count: 0, qty: 0 };

   for (var idx = 0; idx < countObjVals.length; idx++) {
       reducedVal.count += countObjVals[idx].count;
       reducedVal.qty += countObjVals[idx].qty;
   }

   return reducedVal;
};
```

3. 定义**finalize**函数，对**reduce**的返回值做最后处理

```js
var finalizeFunction2 = function (key, reducedVal) {
  reducedVal.avg = reducedVal.qty/reducedVal.count;
  return reducedVal;
};
```

4. 执行**map-reduce**操作

```js
db.orders.mapReduce(
   mapFunction2,
   reduceFunction2,
   {
     out: { merge: "map_reduce_example2" },
     query: { ord_date: { $gte: new Date("2020-03-01") } },
     finalize: finalizeFunction2
   }
 );
```

此操作使用**query**字段选择仅**ord_date**大于等于**new Date("2020-03-01")**的文档。然后将结果输出到`map_reduce_example2`集合。

5. 查询**map_reduce_example2**集合，验证结果

```js
db.map_reduce_example2.find().sort({ _id: 1 })
```

操作返回以下文档：

```json
{ "_id" : "apples", "value" : { "count" : 3, "qty" : 30, "avg" : 10 } }
{ "_id" : "carrots", "value" : { "count" : 2, "qty" : 15, "avg" : 7.5 } }
{ "_id" : "chocolates", "value" : { "count" : 3, "qty" : 15, "avg" : 5 } }
{ "_id" : "oranges", "value" : { "count" : 6, "qty" : 58, "avg" : 9.666666666666666 } }
{ "_id" : "pears", "value" : { "count" : 1, "qty" : 10, "avg" : 10 } }
```

**聚集替代**

使用管道操作符也可以实现上述map-reduce功能

```js
db.orders.aggregate( [
   { $match: { ord_date: { $gte: new Date("2020-03-01") } } },
   { $unwind: "$items" },
   { $group: { _id: "$items.sku", qty: { $sum: "$items.qty" }, orders_ids: { $addToSet: "$_id" } }  },
   { $project: { value: { count: { $size: "$orders_ids" }, qty: "$qty", avg: { $divide: [ "$qty", { $size: "$orders_ids" } ] } } } },
   { $merge: { into: "agg_alternative_3", on: "_id", whenMatched: "replace",  whenNotMatched: "insert" } }
] )
```





### 8. 副本集

#### 8.1 主从复制

主从复制是 MongoDB 最早使用的复制方式， 该复制方式易于配置，并且可以支持任意数量的从节点服务器，与使用单节点模式相比有如下优点：

- 在从服务器上存储数据副本，提高了数据的可用性， 并可以保证数据的安全性
- 可配置读写分离,主节点负责写操作,从节点负责读操作,将读写压力分开,提高系统的稳定性

MongoDB 的主从复制至少需要两个服务器或者节点。其中一个是主节点，负责处理客户端请求，其它的都是从节点，负责同步主节点的数据。

主节点记录在其上执行的所有写操作，从节点定期轮询主节点获取这些操作，然后再对自己的数据副本执行这些操作。由于和主节点执行了相同的操作，从节点就能保持与主节点的数据同步。

主节点的操作记录称为oplog(operation log)，它被存储在 MongoDB 的 local 数据库中。oplog 中的每个文档都代表主节点上执行的一个操作。需要重点强调的是**oplog只记录改变数据库状态的操作**。比如，查询操作就不会被存储在oplog中。这是因为oplog只是作为从节点与主节点保持数据同步的机制。

然而，**主从复制并非生产环境下推荐的复制方式**，主要原因如下：

- **灾备都是完全人工的：**如果主节点发生故障失败，管理员必须关闭一个从服务器，然后作为主节点重新启动它。然后应用程序必须重新配置连接新的主节点。

- **数据恢复困难：**因为oplog只在主节点存在，故障失败需要在新的服务器上创建新的oplog，这意味着任意存在的节点需要重新从新的主节点同步oplog。

因此，在新版本的MongoDB中已经不再支持使用主从复制这种复制方式了，取而代之的是使用副本集复制方式。



#### 8.2 MongoDB副本集

MongoDB副本集（Replica Set）其实就是具有自动故障恢复功能的主从集群，和主从复制最大的区别就是在副本集中没有固定的**主节点**；整个副本集会选出一个节点作为**主节点**，当其挂掉后，再在剩下的从节点中选举一个节点成为新的**主节点**，在副本集中总有一个主节点(primary)和一个或多个备份节点(secondary)。

客户端连接到整个副本集，不关心具体哪一台机器是否挂掉。主服务器负责整个副本集的读写，副本集定期同步数据备份，一但主节点挂掉，副本节点就会选举一个新的主服务器，这一切对于应用服务器不需要关心。

除了primary和secondary之外，副本集中的节点还可以是以下角色：

|                | 成为primary | 对客户端可见 | 参与投票 | 延迟同步 | 复制数据 |
| -------------- | ----------- | ------------ | -------- | -------- | -------- |
| Default        | √           | √            | √        | ∕        | √        |
| Secondary-Only | ∕           | √            | √        | ∕        | √        |
| Hidden         | ∕           | ∕            | √        | ∕        | √        |
| Delayed        | ∕           | √            | √        | √        | √        |
| Arbiters       | ∕           | ∕            | √        | ∕        | ∕        |
| Non-Voting     | √           | √            | ∕        | ∕        | √        |

- **主节点（Primary）**
  接收所有的写请求，然后把修改同步到所有Secondary。一个Replica Set只能有一个Primary节点，当Primary挂掉后，其他Secondary或者Arbiter节点会重新选举出来一个主节点。
  默认读请求也是发到Primary节点处理的，可以通过修改客户端连接配置以支持读取Secondary节点。
- **副本节点（Secondary）**
  与主节点保持同样的数据集。当主节点挂掉的时候，参与选主。

- **仲裁者（Arbiter）**
  不保有数据，不参与选主，只进行选主投票。使用Arbiter可以减轻数据存储的硬件需求，Arbiter几乎没什么大的硬件资源需求，但重要的一点是，在生产环境下它和其他数据节点不要部署在同一台机器



#### 8.3 副本集和主从复制的区别

其实副本集（Replica Set）是主从复制的高级形式。主从复制实现了数据备份+读扩展，但是master一旦down掉，需要手动启动slave。副本集在此基础上实现了备份自动重启的功能，也就是某一台slave会挺身而出，担当起master的职责。所以有三个角色:**Primary**，**Secondary**，**Arbiter**。



**副本集特征：**

- N 个节点的集群
- 任何节点可作为主节点
- 所有写入操作都在主节点上
- 自动故障转移
- 自动恢复



#### 8.4 副本集架构

官方推荐的副本集最小配置需要有三个节点：一个主节点接收和处理所有的写操作，两个备份节点通过复制主节点的操作来对主节点的数据进行同步备份。

当开发一个副本集架构时要注意下面的因素：

1. 确保副本集的成员总能选出一个primary。运行奇数个成员或者运行一个仲裁者（arbiter）+偶数个成员。
2. 分布在不同地理位置的成员，知道“群体”的成员在任意网络分区中的情况。试图确保在主数据中心的成员中选举出primary。
3. 考虑副本集中包含hidden或者delayed成员用于支持专用功能，如备份、reporting和测试。
4. 考虑保留一或者两个位于其他数据中心的成员，同时通过配置确保其不会成为primary。
5. 使用replica set tags创建定制的写规则以确保应用能够控制写操作成功的门限值。使用写规则确保操作在返回成功之前将操作传递给指定的数据中心或不同功能的机器。



#### 8.5 部署策略

如果副本集中的成员多于三个，则需要遵照下面的架构条件：

- 集合中有奇数个参与投票的成员。如果有偶数个投票成员，则部署一个仲裁者将个数变为奇数。
- 集合中同一时刻不多于7个参与投票的成员
- 如果不想让某些成员在故障切换时成为primary，则将它们的优先级设为0。
- 集合的多数成员运行在主要的数据中心



#### 8.6 副本集常见操作

```shell
rs.status()   //查看成员的运行状态等信息

rs.config()    //查看配置信息

rs.slaveOk()  //允许在SECONDARY节点上进行查询操作，默认从节点不具有查询功能

rs.isMaster()  //查询该节点是否是主节点

rs.add({})   //添加新的节点到该副本集中

rs.remove()   //从副本集中删除节点
```





### 9. 分片

MongoDB的分片机制允许创建一个包含许多台机器（分片）的集群，将数据子集分散在集群中，每个分片维护着一个数据集合的子集。与单机服务器和副本集相比，使用集群架构可以使应用程序具有更大的数据处理能力。

和MySQL分区方案相比，MongoDB的最大区别在于它几乎能自动完成所有事情，只要告诉MongoDB要分配数据，它就能自动维护数据在不同服务器之间的均衡。

> **注意：**分片与副本集（复制）是不同的。复制是让多台服务器都拥有同样的数据副本，每一台服务器都是其他服务器的镜像，而每一个分片都有其他分片拥有不同的数据子集。



#### 9.1 分片的目的

高数据量和吞吐量的数据库应用会对单机的性能造成较大压力，大的查询量会将单机的CPU耗尽，大的数据量对单机的存储压力较大，最终会耗尽系统的内存而将压力转移到磁盘IO上。

为了解决这些问题,有两个基本的方法: 

- **垂直扩展：**增加更多的CPU和存储资源来扩展容量。

- **水平扩展：**将数据集分布在多个服务器上。水平扩展即分片。



#### 9.2 分片的时机

决定何时分片是一个值得权衡的问题。通常不必太早分片，因为分片不仅会增加部署的操作复杂度，还要求做出设计决策，而该决策以后很难再改。另外最好也不要在系统运行太久之后再分片，因为在一个过载的系统上不停机进行分片是非常困难的。

通常，分片用来：

- 增加可用RAM

- 增加可用磁盘空间

- 减轻单台服务器的负载

- 处理单个mongod无法承受的吞吐量

因此，良好的监控对于决定应何时分片是十分重要的，必须认真对待其中每一项。由于人们往往过于关注改进其中一个指标，所以应弄明白到底哪一项指标对自己的部署最为重要，并提前做好何时分片以及如何分片的计划。随着不断增加分片数量，系统性能大致会呈线性增长。但是，如果从一个未分片的系统转换为只有几个分片的系统，性能通常会有所下降。由于迁移数据、维护元数据、路由等开销，少量分片的系统与未分片的系统相比，通常延迟更大，吞吐量甚至可能会更小。因此，至少应该创建3个或以上的分片。



#### 9.3 分片的原理

MongoDB通过配置分片集群来支持分片，一个分片集群包括以下几个组件：

![img](https://www.runoob.com/wp-content/uploads/2013/12/sharding.png)

- Shard:

  用于存储实际的数据块，实际生产环境中一个shard server角色可由几台机器组个一个replica set承担，防止主机单点故障

- Config Server:

  mongod实例，存储了整个 ClusterMetadata，其中包括 chunk信息。

- mongos:

  前端路由，客户端由此接入，且让整个集群看上去像单一数据库，前端应用可以透明使用。

Mongos本身并不持久化数据，Sharded cluster所有的元数据都会存储到Config Server，而用户的数据会分散存储到各个Shard。Mongos启动后，会从配置服务器加载元数据，开始提供服务，将用户的请求正确路由到对应的碎片。



#### 9.4 分片的优势

1. mongos对集群进行抽象，让集群“不可见”

   对于一个读写操作，mongos 需要知道应该将其路由到哪个复制集上，mongos通过将片键空间划分为若干个区间，计算出一个操作的片键的所属区间对应的复制集来实现路由。

2. 保证集群总是可读写

   MongoDB通过多种途径来确保集群的可用性和可靠性。将MongoDB的分片和复制功能结合使用，在确保数据分片到多台服务器的同时，也确保了每分数据都有相应的备份，这样就可以确保有服务器换掉时，其他的从库可以立即接替坏掉的部分继续工作。

3. 使集群易于扩展

   当系统需要更多的空间和资源的时候，MongoDB使我们可以按需方便的扩充系统容量。





### 10.身份验证

#### 10.1 启用访问控制

在MongoDB部署时启用访问控制会强制执行身份验证，要求用户表明身份。当MongoDB部署时启用了访问控制后，用户只能执行由其角色限定的操作。



在启用访问控制之前，应该创建一个用户，该用户可以在启用访问控制后创建用户并为用户分配角色。然后，这个用户管理员将用于创建和维护其他用户和角色，因此需要分配一个合适的角色（具有 `userAdmin`或`userAdminAnyDatabase`角色）来支持。如果你不创建此管理用户，则在启用访问控制时将无法登录或创建新用户和角色。



以下过程首先将用户管理员添加到没有访问控制的情况下运行的MongoDB实例，然后启用访问控制。

**1. 在没有访问控制的情况下启动MongoDB实例**

```shell
mongod --port 27017 --dbpath /var/lib/mongodb
```



**2. 连接到实例**

```shell
mongo --port 27017
```



**3. 创建用户管理员**

```shell
use admin
db.createUser(
  {
    user: "myUserAdmin",
    pwd: passwordPrompt(), // or cleartext password
    roles: [ { role: "userAdminAnyDatabase", db: "admin" }, "readWriteAnyDatabase" ]
  }
)
```


**4. 使用访问控制重启MongoDB实例**

- 使用命令行启动，添加`--auth`命令

```shell
mongod --auth --port 27017 --dbpath /var/lib/mongodb
```

- 使用配置文件，添加 `security.authorization`配置

```shell
security:
    authorization: enabled
```



**5. 以用户管理员身份连接并进行身份验证**

- 使用命令行验证方式

```shell
mongo --port 27017  --authenticationDatabase "admin" -u "myUserAdmin" -p
```

- 连接后身份验证

```shell
mongo --port 27017
use admin
db.auth("myUserAdmin", passwordPrompt()) // or cleartext password
```



**6. 根据部署需要，创建其他用户**

以下操作是在**test**数据库，创建一个**myTester**用户。该用户具有对**test**数据库的`readWrite`权限以及**reporting**数据库的`read`权限

```shell
use test
db.createUser(
  {
    user: "myTester",
    pwd:  passwordPrompt(),   // or cleartext password
    roles: [ { role: "readWrite", db: "test" },
             { role: "read", db: "reporting" } ]
  }
)
```



**7. 以myTester身份连接到MongoDB实例**

- 连接过程中验证

```shell
mongo --port 27017 -u "myTester" --authenticationDatabase "test" -p
```

- 连接后验证

```shell
mongo --port 27017
use test
db.auth("myTester", passwordPrompt())  // or cleartext password
```



#### 10.2 内置角色

##### 1. 数据库用户角色

- read:只读数据权限
- readWrite:读写数据权限



##### 2. 数据库管理角色

- dbAdmin: 在当前db中执行管理操作的权限
- dbOwner: 在当前db中执行任意操作
- userAdmin: 在当前db中管理user的权限



##### 3. 备份和还原角色

- backup
- restore



##### 4. 所有数据库角色

- readAnyDatabase: 在所有数据库上都有读取数据的权限
- readWriteAnyDatabase: 在所有数据库上都有读写数据的权限
- userAdminAnyDatabase: 在所有数据库上都有管理user的权限
- dbAdminAnyDatabase: 管理所有数据库的权限



##### 5. 集群管理

- clusterAdmin: 管理机器的最高权限
- clusterManager: 管理和监控集群的权限
- clusterMonitor: 监控集群的权限
- hostManager: 管理Server



##### 6. 超级权限

- root: 超级用户



#### 10.3 用户管理

| Name                                                         | Description                                                  |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| [db.auth()](https://docs.mongodb.com/manual/reference/method/db.auth/#db.auth) | Authenticates a user to a database.                          |
| [db.changeUserPassword()](https://docs.mongodb.com/manual/reference/method/db.changeUserPassword/#db.changeUserPassword) | Changes an existing user’s password.                         |
| [db.createUser()](https://docs.mongodb.com/manual/reference/method/db.createUser/#db.createUser) | Creates a new user.                                          |
| [db.dropUser()](https://docs.mongodb.com/manual/reference/method/db.dropUser/#db.dropUser) | Removes a single user.                                       |
| [db.dropAllUsers()](https://docs.mongodb.com/manual/reference/method/db.dropAllUsers/#db.dropAllUsers) | Deletes all users associated with a database.                |
| [db.getUser()](https://docs.mongodb.com/manual/reference/method/db.getUser/#db.getUser) | Returns information about the specified user.                |
| [db.getUsers()](https://docs.mongodb.com/manual/reference/method/db.getUsers/#db.getUsers) | Returns information about all users associated with a database. |
| [db.grantRolesToUser()](https://docs.mongodb.com/manual/reference/method/db.grantRolesToUser/#db.grantRolesToUser) | Grants a role and its privileges to a user.                  |



#### 10.4 权限管理

| Name                                                         | Description                                                  |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| [db.createRole()](https://docs.mongodb.com/manual/reference/method/db.createRole/#db.createRole) | Creates a role and specifies its privileges.                 |
| [db.dropRole()](https://docs.mongodb.com/manual/reference/method/db.dropRole/#db.dropRole) | Deletes a user-defined role.                                 |
| [db.dropAllRoles()](https://docs.mongodb.com/manual/reference/method/db.dropAllRoles/#db.dropAllRoles) | Deletes all user-defined roles associated with a database.   |
| [db.getRole()](https://docs.mongodb.com/manual/reference/method/db.getRole/#db.getRole) | Returns information for the specified role.                  |
| [db.getRoles()](https://docs.mongodb.com/manual/reference/method/db.getRoles/#db.getRoles) | Returns information for all the user-defined roles in a database. |
| [db.grantPrivilegesToRole()](https://docs.mongodb.com/manual/reference/method/db.grantPrivilegesToRole/#db.grantPrivilegesToRole) | Assigns privileges to a user-defined role.                   |
| [db.revokePrivilegesFromRole()](https://docs.mongodb.com/manual/reference/method/db.revokePrivilegesFromRole/#db.revokePrivilegesFromRole) | Removes the specified privileges from a user-defined role.   |
| [db.grantRolesToRole()](https://docs.mongodb.com/manual/reference/method/db.grantRolesToRole/#db.grantRolesToRole) | Specifies roles from which a user-defined role inherits privileges. |
| [db.revokeRolesFromRole()](https://docs.mongodb.com/manual/reference/method/db.revokeRolesFromRole/#db.revokeRolesFromRole) | Removes inherited roles from a role.                         |
| [db.updateRole()](https://docs.mongodb.com/manual/reference/method/db.updateRole/#db.updateRole) | Updates a user-defined role.                                 |





### 11. 服务器管理

#### 11.1 常用配置项

执行mongod程序即可启动MongoDB服务器，mongod在启动时可使用许多可配置选项，在命令行中运行`mongod --help`可列出这些选项。下列选项十分常用，需着重注意。

- **--dbpath**

  使用此选项可指定一个目录为数据目录。其默认值为/data/db/（在Windows中则为MongoDB可执行文件所在磁盘卷中的\data\db目录）。机器上的每个mongod进程都需要属于自己的数据目录，即若在同一机器上运行三个mongod实例，则需三个独立的数据目录。mongod启动时，会在其数据目录中创建一个mongod.lock文件，以阻止其他mongod进程使用此数据目录。若尝试启动另一个使用相同数据目录的MongoDB服务器，则会出现错误提示：`"Unabletoacquirelockforlockfilepath:/data/db/mongod.lock."`

  

- **--port**

  此选项用以指定服务器监听的端口号。mongod默认占用27017端口，除其他mongod进程外，其余程序不会使用此端口。若要在同一机器上运行多个mongod进程，则需为它们指定不同的端口。若尝试在已被占用的端口启动mongod，则会出现错误提示：`"Addressalreadyinuseforsocket:0.0.0.0:27017"`

  

- **--fork**

  启用此选项以调用fork创建子进程，在后台运行MongoDB。

  首次启动mongod而数据目录为空时，文件系统需几分钟时间分配数据库文件。预分配结束，mongod可接收连接后，父进程才会继续运行。因此，**fork**可能会发生挂起。可查看日志中的最新记录得知正在进行的操作。启用`--fork`选项时，必须同时启用`--logpath`选项。

  

- **--logpath**

  使用此选项，所有输出信息会被发送至指定文件，而非在命令行上输出。假设我们拥有该目录的写权限，若指定文件不存在，启用该选项后则会自动生成一个文件。若指定日志文件已存在，选项启用后则会覆盖掉该文件，并清除所有旧的日志条目。如需保留旧日志，除`--logpath`选项外，强烈建议使用`--logappend`选项。

  

- **--directoryperdb**

  启用该选项可将每个数据库存放在单独的目录中。我们可由此按需将不同的数据库挂载到不同的磁盘上。该选项一般用于将本地数据库或副本放置于单独的磁盘上，或在磁盘空间不足时将数据库移动至其他磁盘。也可将频繁操作的数据库挂载到速度较快的磁盘上，而将不常用的数据库放到较慢的磁盘上。总之该选项能使我们在今后更加灵活地操作数据库。

  

- **--config**

  额外加载配置文件，未在命令行中指定的选项将使用配置文件中的参数。该选项通常用于确保每次重新启动时的选项都是一样的。

  

- **--bind_ip**

  指定MongoDB监听的接口。我们通常将其设置为一个内部IP地址，从而保证应用服务器和集群中其他成员的访问，同时拒绝外网的访问。如MongoDB与应用服务器运行于同一台机器上，则可将其设为localhost。但配置服务器和分片需要其他机器的访问，所以不应设为localhost。

  

- **--nohttpinterface**

  MongoDB启动时，默认在端口1000启动一个微型的HTTP服务器。该服务器可提供一些系统信息，但这些信息均可在其他地方找到。对于一个可能只需通过SSH访问的机器，没有必要将这些信息暴露在外网上。

  **除非正在进行开发，否则请关闭此选项。**

  

- **--nounixsocket**

  如不打算使用UNIXsocket来进行连接，则可禁用此选项。只有在本地，即应用服务器和MongoDB运行在同一台机器上时，才能使用socket进行连接。

  

- **--noscripting**

  该选项完全禁止服务器端JavaScript脚本的运行。大多数报告的MongoDB安全问题都与JavaScript有关。如程序允许的话，禁止JavaScript通常会更安全一些。

  一些shell中的辅助函数依赖于服务器端的JavaScript，尤其是`sh.status()`。在一台禁止了JavaScript的服务器上运行这些辅助函数时，会出现错误提示。



MongoDB支持从文件中读取配置信息。当使用的选项很多，或自动化启动任务时，使用配置文件就十分实用。使用`-f`或`-config`标记，告知服务器使用配置文件。例如，运行`mongod --config ~/.mongodb.conf`，从而使用~/.mongodb.conf作为配置文件。





#### 11.2 备份与恢复

##### 1. 备份

在Mongodb中我们使用mongodump命令来备份MongoDB数据。该命令可以导出所有数据到指定目录中。

mongodump命令可以通过参数指定导出的数据量级转存的服务器。

**语法**

mongodump命令脚本语法如下：

```shell
>mongodump -h dbhost -d dbname -o dbdirectory
```

- -h：

  MongDB所在服务器地址，例如：127.0.0.1，当然也可以指定端口号：127.0.0.1:27017

- -d：

  需要备份的数据库实例，例如：test

- -o：

  备份的数据存放位置，例如：`c:\data\dump`，当然该目录需要提前建立，在备份完成后，系统自动在dump目录下建立一个test目录，这个目录里面存放该数据库实例的备份数据。



mongodump 命令可选参数列表如下：

| 语法                                              | 描述                           | 实例                                             |
| :------------------------------------------------ | :----------------------------- | :----------------------------------------------- |
| mongodump --host HOST_NAME --port PORT_NUMBER     | 该命令将备份所有MongoDB数据    | mongodump --host runoob.com --port 27017         |
| mongodump --dbpath DB_PATH --out BACKUP_DIRECTORY |                                | mongodump --dbpath /data/db/ --out /data/backup/ |
| mongodump --collection COLLECTION --db DB_NAME    | 该命令将备份指定数据库的集合。 | mongodump --collection mycol --db test           |



##### 2.恢复

**语法**

mongorestore命令脚本语法如下：

```shell
>mongorestore -h <hostname><:port> -d dbname <path>
```

- `--host <:port>, -h <:port>`：

  MongoDB所在服务器地址，默认为： localhost:27017

- `--db , -d` ：

  需要恢复的数据库实例，例如：test，当然这个名称也可以和备份时候的不一样，比如test2

- `--drop`：

  恢复的时候，先删除当前数据，然后恢复备份的数据。就是说，恢复后，备份后添加修改的数据都会被删除，慎用哦！

- `<path>`：

  mongorestore 最后的一个参数，设置备份数据所在位置，例如：`c:\data\dump\test`。

  你不能同时指定 `<path>` 和 `--dir` 选项，`--dir`也可以设置备份目录。

- `--dir`：

  指定备份的目录

  你不能同时指定 `<path>` 和 `--dir` 选项。





#### 11.3 监控

MongoDB中提供了mongostat 和 mongotop 两个命令来监控MongoDB的运行情况。



##### 1. mongostat 命令

mongostat是mongodb自带的状态检测工具，在命令行下使用。它会间隔固定时间获取mongodb的当前运行状态，并输出。如果你发现数据库突然变慢或者有其他问题的话，你第一手的操作就考虑采用mongostat来查看mongo的状态。



##### 2. mongotop 命令

mongotop也是mongodb下的一个内置工具，mongotop提供了一个方法，用来跟踪一个MongoDB的实例，查看哪些大量的时间花费在读取和写入数据。 mongotop提供每个集合的水平的统计数据。默认情况下，mongotop返回值的每一秒。



---

**参考地址**

MongoDB 官网地址：https://www.mongodb.com/

MongoDB官方文档：https://docs.mongodb.com/manual/

w3cschool：https://www.w3cschool.cn/mongodb/