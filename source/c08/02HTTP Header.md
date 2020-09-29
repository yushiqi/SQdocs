## 8.2 HTTP Header

**HTTP Header** 大体分为**Request**和**Response**两部分。



### 1. Requests

**Accept：**

- **解释：**指定客户端能够接收的内容类型
- **示例：**`Accept: text/plain, text/html`



**Accept-Charset：**:

- **解释：**浏览器可以接受的字符编码集
- **示例：**`Accept-Charset: iso-8859-5`



**Accept-Encoding：**

- **解释：**指定浏览器可以支持的web服务器返回内容压缩编码类型
- **示例：**`Accept-Encoding: compress, gzip`



**Accept-Language：**

- **解释：**浏览器可接受的语言
- **示例：**`Accept-Language: en,zh`



**Accept-Ranges：**

- **解释：**可以请求网页实体的一个或者多个子范围字段
- **示例：**`Accept-Ranges: bytes`



**Authorization：**

- **解释：**HTTP授权的授权证书
- **示例：**`Authorization: Basic QWxhZGRpbjpvcGVuIHNlc2FtZQ==`



**Cache-Control：**

- **解释：**指定请求和响应遵循的缓存机制
- **示例：**`Cache-Control: no-cache`



**Connection：**

- **解释：**表示是否需要持久连接。（HTTP 1.1默认进行持久连接）
- **示例：**`Connection: close`



**Cookie：**

- **解释：**HTTP请求发送时，会把保存在该请求域名下的所有cookie值一起发送给web服务器

- **示例：**`Cookie: $Version=1; Skin=new;`

  

**Content-Length：**

- **解释：**请求的内容长度 
- **示例：**`Content-Length: 348` 



**Content-Type：** 

- **解释：**请求的与实体对应的MIME信息 
- **示例：**`Content-Type: application/x-www-form-urlencoded` 



**Date：**

- **解释：**请求发送的日期和时间 
- **示例：**`Date: Tue, 15 Nov 2010 08:12:31 GMT`



**Expect：**

- **解释：**请求的特定的服务器行为
- **示例：**`Expect: 100-continue`



**From：**

- **解释：**发出请求的用户的Email
- **示例：**`From: https://www.xxx.com/mailto:user@email.com` 



**Host：**

- **解释：**指定请求的服务器的域名和端口号
- **示例：**`Host: http://www.xxx.com`


**If-Match：**

- **解释：**只有请求内容与实体相匹配才有效 
- **示例：**`If-Match: “737060cd8c284d8af7ad3082f209582d”` 



**If-Modified-Since：**

- **解释：**如果请求的部分在指定时间之后被修改则请求成功，未被修改则返回304代码 
- **示例：**`If-Modified-Since: Sat, 29 Oct 2010 19:43:31 GMT`



**If-None-Match：**

- **解释：**如果内容未改变返回304代码，参数为服务器先前发送的Etag，与服务器回应的Etag比较判断是否改变 
- **示例：**`If-None-Match: “737060cd8c284d8af7ad3082f209582d”`



**If-Range：**

- **解释：**如果实体未改变，服务器发送客户端丢失的部分，否则发送整个实体。参数也为Etag 
- **示例：**`If-Range: “737060cd8c284d8af7ad3082f209582d”`



**If-Unmodified-Since： **

- **解释：**只在实体在指定时间之后未被修改才请求成功 
- **示例：**`If-Modified-Since: Sat, 29 Oct 2010 19:43:31 GMT`



**Max-Forwards： **

- **解释：**限制信息通过代理和网关传送的时间 
- **示例：**`Max-Forwards: 10` 



**Pragma：**

- **解释：**用来包含实现特定的指令
- **示例：**`Pragma: no-cache` 



**Proxy-Authorization：**

- **解释：**连接到代理的授权证书
- **示例：**`Proxy-Authorization: Basic QWxhZGRpbjpvcGVuIHNlc2FtZQ==`



**Range：**

- **解释：**只请求实体的一部分，指定范围 
- **示例：**`Range: bytes=500-999`



**Referer：**

- **解释：**先前网页的地址，当前请求网页紧随其后,即来路
- **示例：**`Referer: http://www.xxx.com/a.html`



**TE：**

- **解释：**客户端愿意接受的传输编码，并通知服务器接受接受尾加头信息 
- **示例：**`TE: trailers,deflate;q=0.5`



**Upgrade： **

- **解释：**向服务器指定某种传输协议以便服务器进行转换（如果支持）
- **示例：**`Upgrade: HTTP/2.0, SHTTP/1.3, IRC/6.9, RTA/x11` 



**User-Agent： **

- **解释：**User-Agent的内容包含发出请求的用户信息
- **示例：**`User-Agent: Mozilla/5.0 (Linux; X11)`



**Via：**

- **解释：**通知中间网关或代理服务器地址，通信协议 
- **示例：**`Via: 1.0 fred, 1.1 nowhere.com (Apache/1.1)`



**Warning：**

- **解释：**关于消息实体的警告信息
- **示例：**`Warn: 199 Miscellaneous warning`




### 2. Responses

**Accept-Ranges：**

- **解释：**表明服务器是否支持指定范围请求及哪种类型的分段请求
- **示例：**`Accept-Ranges: bytes` 



**Age：** 

- **解释：**从原始服务器到代理缓存形成的估算时间（以秒计，非负）
- **示例：**`Age: 12`



**Allow：**

- **解释：**对某网络资源的有效的请求行为，不允许则返回405
- **示例：**`Allow: GET, HEAD`



**Cache-Control：**

- **解释：**告诉所有的缓存机制是否可以缓存及哪种类型
- **示例：**`Cache-Control: no-cache` 



**Content-Encoding：** 

- **解释：**web服务器支持的返回内容压缩编码类型
- **示例：**`Content-Encoding: gzip`




**Content-Language：**

- **解释：**响应体的语言
- **示例：**`Content-Language: en,zh`




**Content-Length：**

- **解释：**响应体的长度
- **示例：**`Content-Length: 348`




**Content-Location：** 

- **解释：**请求资源可替代的备用的另一地址
- **示例：**`Content-Location: /index.htm` 



**Content-MD5：**

- **解释：**返回资源的MD5校验值
- **示例：**`Content-MD5: Q2hlY2sgSW50ZWdyaXR5IQ==`




**Content-Range：**

- **解释：**在整个返回体中本部分的字节位置
- **示例：**`Content-Range: bytes 21010-47021/47022`




**Content-Type：**

- **解释：**返回内容的MIME类型
- **示例：**`Content-Type: text/html; charset=utf-8`




**Date：**

- **解释：**原始服务器消息发出的时间
- **示例：**`Date: Tue, 15 Nov 2010 08:12:31 GMT`




**ETag：**

- **解释：**请求变量的实体标签的当前值
- **示例：**`ETag: “737060cd8c284d8af7ad3082f209582d”`



**Expires：** 

- **解释：**响应过期的日期和时间
- **示例：**`Expires: Thu, 01 Dec 2010 16:00:00 GMT`



**Last-Modified：**

- **解释：**请求资源的最后修改时间
- **示例：**`Last-Modified: Tue, 15 Nov 2010 12:45:26 GMT`




**Location：**

- **解释：**用来重定向接收方到非请求URL的位置来完成请求或标识新的资源
- **示例：**`Location: http://www.zcmhi.com/archives/94.html`




**Pragma：**

- **解释：**包括实现特定的指令，它可应用到响应链上的任何接收方
- **示例：**`Pragma: no-cache`




**Proxy-Authenticate：**

- **解释：**它指出认证方案和可应用到代理的该URL上的参数
- **示例：**`Proxy-Authenticate: Basic`




**refresh：**

- **解释：**应用于重定向或一个新的资源被创造，在5秒之后重定向
- **示例：`Refresh: 5; url=http://www.zcmhi.com/archives/94.html`



**Retry-After：**

- **解释：**如果实体暂时不可取，通知客户端在指定时间之后再次尝试
- **示例：**`Retry-After: 120`




**Server：**

- **解释：**web服务器软件名称
- **示例：**`Server: Apache/1.3.27 (Unix) (Red-Hat/Linux)`




**Set-Cookie：** 

- **解释：**设置Http Cookie
- **示例：**`Set-Cookie: UserID=JohnDoe; Max-Age=3600; Version=1`




**Trailer:** 

- **解释：**指出头域在分块传输编码的尾部存在

- **示例：**`Trailer: Max-Forwards`

  

**Transfer-Encoding:**

- **解释：**文件传输编码
- **示例：**`Transfer-Encoding:chunked`



**Vary:**

- **解释：**告诉下游代理是使用缓存响应还是从原始服务器请求
- **示例：**`Vary: *`




**Via:**

- **解释：**告知代理客户端响应是通过哪里发送的
- **示例：**`Via: 1.0 fred, 1.1 nowhere.com (Apache/1.1)`



**Warning:** 

- **解释：**警告实体可能存在的问题
- **示例：**`Warning: 199 Miscellaneous warning` 




**WWW-Authenticate:**

- **解释：**表明客户端请求实体应该使用的授权方案
- **示例：**`WWW-Authenticate: Basic`