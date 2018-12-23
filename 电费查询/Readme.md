### 电费爬取的流程

+ 由于学校的网站是aspx站点,难点在于
  **VIEWSTATE**和**EVENTVALIDATION**这两个变量的获取问题。(难的是default.aspx页面的)

+ **已知**:
    + **VIEWSTATE**和**EVENTVALIDATION**
    值,这两个值都隐藏在网页源码中

    + 由于default.aspx页面的**VIEWSTATE**和**EVENTVALIDATION**会变化，导致每次需要重新去获取这两个值。

    + 同时发现login.aspx的**VIEWSTATE**和**EVENTVALIDATION**两个变量不会变化

+ 获取的方法:
    + 首先模拟登录查询平台, 获取登录后的cookie
        + login.aspx的**VIEWSTATE**和**EVENTVALIDATION**两个变量直接在手动登录时的requests headers中找到
        
        + 模拟登录后从response headers中获取set-cookie,做字符串处理得到cookie值

    + 获得cookie值后再用get方法请求default.aspx页面，
      用正则表达式获取**VIEWSTATE**和**EVENTVALIDATION**

    + 获取完两个变量，携带cookie一起post上去即可获得电费

---
### 使用方法

+ 先新建一个PowerQuery(DormNum)对象
+ 再调用 PowerQuery(DormNum).Query()函数即可