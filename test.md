[toc]
# 正文
### Markdown是什么？
**Markdown**是一种轻量级**标记语言**，它以纯文本形式(*易读、易写、易更改*)编写文档，并最终以HTML格式发布。    
**Markdown**也可以理解为将以MARKDOWN语法编写的语言转换成HTML内容的工具。    

### 谁创造了它？
它由[**Aaron Swartz**](http://www.aaronsw.com/)和**John Gruber**共同设计，**Aaron Swartz**就是那位于去年（*2013年1月11日*）自杀,有着**开挂**一般人生经历的程序员。维基百科对他的[介绍](http://zh.wikipedia.org/wiki/%E4%BA%9A%E4%BC%A6%C2%B7%E6%96%AF%E6%B2%83%E8%8C%A8)是：**软件工程师、作家、政治组织者、互联网活动家、维基百科人**。    

他有着足以让你跪拜的人生经历：    
+ **14岁**参与RSS 1.0规格标准的制订。     
+ **2004**年入读**斯坦福**，之后退学。   
+ **2005**年创建[Infogami](http://infogami.org/)，之后与[Reddit](http://www.reddit.com/)合并成为其合伙人。   
+ **2010**年创立求进会（Demand Progress），积极参与禁止网络盗版法案（SOPA）活动，最终该提案被撤回。   
+ **2011**年7月19日，因被控从MIT和JSTOR下载480万篇学术论文并以免费形式上传于网络被捕。     
+ **2013**年1月自杀身亡。    

天才都有早逝的归途。

### 为什么要使用它？
+ 它是易读（看起来舒服）、易写（语法简单）、易更改**纯文本**。处处体现着**极简主义**的影子。
+ 兼容HTML，可以转换为HTML格式发布。
+ 跨平台使用。
+ 越来越多的网站支持Markdown。
+ 更方便清晰地组织你的电子邮件。（Markdown-here, Airmail）
+ 摆脱Word（我不是认真的）。

### 怎么使用？
如果不算**扩展**，Markdown的语法绝对**简单**到让你爱不释手。

Markdown语法主要分为如下几大部分：
**标题**，**段落**，**区块引用**，**代码区块**，**强调**，**列表**，**分割线**，**链接**，**图片**，**反斜杠 `\`**，**符号'`'**。

#### 标题
两种形式：  
1）使用`=`和`-`标记一级和二级标题。
> 一级标题   
> `=========`   
> 二级标题    
> `---------`

效果：
> 一级标题   
> =========   
> 二级标题
> ---------  

2）使用`#`，可表示1-6级标题。
> \# 一级标题   
> \## 二级标题   
> \### 三级标题   
> \#### 四级标题   
> \##### 五级标题   
> \###### 六级标题    

效果：
> # 一级标题   
> ## 二级标题   
> ### 三级标题   
> #### 四级标题   
> ##### 五级标题   
> ###### 六级标题

#### 段落
段落的前后要有空行，所谓的空行是指没有文字内容。若想在段内强制换行的方式是使用**两个以上**空格加上回车（引用中换行省略回车）。

#### 区块引用
在段落的每行或者只在第一行使用符号`>`,还可使用多个嵌套引用，如：
> \> 区块引用  
> \>> 嵌套引用  

效果：
> 区块引用  
>> 嵌套引用

#### 代码区块
代码区块的建立是在每行加上4个空格或者一个制表符（如同写代码一样）。如    
普通段落：

void main()    
{    
    printf("Hello, Markdown.");    
}    

代码区块：

    void main()
    {
        printf("Hello, Markdown.");
    }

**注意**:需要和普通段落之间存在空行。

#### 强调
在强调内容两侧分别加上`*`或者`_`，如：
> \*斜体\*，\_斜体\_    
> \*\*粗体\*\*，\_\_粗体\_\_

效果：
> *斜体*，_斜体_    
> **粗体**，__粗体__

#### 列表
使用`·`、`+`、或`-`标记无序列表，如：
> \-（+\*） 第一项
> \-（+\*） 第二项
> \- （+\*）第三项

**注意**：标记后面最少有一个_空格_或_制表符_。若不在引用区块中，必须和前方段落之间存在空行。

效果：
> + 第一项
> + 第二项
> + 第三项

有序列表的标记方式是将上述的符号换成数字,并辅以`.`，如：
> 1 . 第一项   
> 2 . 第二项    
> 3 . 第三项    

效果：
> 1. 第一项
> 2. 第二项
> 3. 第三项

#### 分割线
分割线最常使用就是三个或以上`*`，还可以使用`-`和`_`。

#### 链接
链接可以由两种形式生成：**行内式**和**参考式**。    
**行内式**：
> \[younghz的Markdown库\]\(https:://github.com/younghz/Markdown "Markdown"\)。

效果：
> [younghz的Markdown库](https:://github.com/younghz/Markdown "Markdown")。

**参考式**：
> \[younghz的Markdown库1\]\[1\]    
> \[younghz的Markdown库2\]\[2\]    
> \[1\]:https:://github.com/younghz/Markdown "Markdown"    
> \[2\]:https:://github.com/younghz/Markdown "Markdown"    

效果：
> [younghz的Markdown库1][1]    
> [younghz的Markdown库2][2]

[1]: https:://github.com/younghz/Markdown "Markdown"
[2]: https:://github.com/younghz/Markdown "Markdown"

**注意**：上述的`[1]:https:://github.com/younghz/Markdown "Markdown"`不出现在区块中。

#### 图片
添加图片的形式和链接相似，只需在链接的基础上前方加一个`！`。
#### 反斜杠`\`
相当于**反转义**作用。使符号成为普通符号。
#### 符号'`'
起到标记作用。如：
>\`ctrl+a\`

效果：
>`ctrl+a`    

#### *谁*在用？
Markdown的使用者：
+ GitHub
+ 简书
+ Stack Overflow
+ Apollo
+ Moodle
+ Reddit
+ 等等

#### 尝试一下
+ **Chrome**下的插件诸如`stackedit`与`markdown-here`等非常方便，也不用担心平台受限。
+ **在线**的dillinger.io评价也不错   
+ **Windowns**下的MarkdownPad也用过，不过免费版的体验不是很好。    
+ **Mac**下的Mou是国人贡献的，口碑很好。
+ **Linux**下的ReText不错。    

**当然，最终境界永远都是笔下是语法，心中格式化 :)。**

****
**注意**：不同的Markdown解释器或工具对相应语法（扩展语法）的解释效果不尽相同，具体可参见工具的使用说明。
虽然有人想出面搞一个所谓的标准化的Markdown，[没想到还惹怒了健在的创始人John Gruber]
(http://blog.codinghorror.com/standard-markdown-is-now-common-markdown/ )。
****
以上基本是所有traditonal markdown的语法。

### 其它：
列表的使用(非traditonal markdown)：

用`|`表示表格纵向边界，表头和表内容用`-`隔开，并可用`:`进行对齐设置，两边都有`:`则表示居中，若不加`:`则默认左对齐。

|代码库                              |链接                                |
|:------------------------------------:|------------------------------------|
|MarkDown                              |[https://github.com/younghz/Markdown](https://github.com/younghz/Markdown "Markdown")|
|MarkDownCopy                              |[https://github.com/younghz/Markdown](https://github.com/younghz/Markdown "Markdown")|


关于其它扩展语法可参见具体工具的使用说明。

# :sparkles: vue3-markdown-it demo :sparkles:

> Welcome to the <b>demo</b> Feel free to type anything in the textarea!
> > *Psst, enable the `html` option!* :P

https://github.com/JanGuillermo/vue3-markdown-it (*Enable the `linkify` option!~*)

___

## This is a h2 tag

Freaky, right? Oh yeah, have you seen this ~~horrible~~ **amazing** repository [here](https://github.com/JanGuillermo/vue3-markdown-it)?!

So far, it supports the following plugins:
- [markdown-it-abbr](https://github.com/markdown-it/markdown-it-abbr) - Add abbreviations
- [markdown-it-anchor](https://github.com/valeriangalliat/markdown-it-anchor) - Add anchors
- [markdown-it-deflist](https://github.com/markdown-it/markdown-it-deflist) - Add definition lists
- [markdown-it-emoji](https://github.com/markdown-it/markdown-it-emoji) - Add emojis
- [markdown-it-footnote](https://github.com/markdown-it/markdown-it-footnote) - Add footnotes
- [markdown-it-highlightjs](https://github.com/valeriangalliat/markdown-it-highlightjs) - Add highlighting for code blocks
- [markdown-it-ins](https://github.com/markdown-it/markdown-it-ins) - Add `<ins>` tags
- [markdown-it-mark](https://github.com/markdown-it/markdown-it-mark) - Add marking/highlighting
- [markdown-it-sub](https://github.com/markdown-it/markdown-it-sub) - Add subscript
- [markdown-it-sup](https://github.com/markdown-it/markdown-it-sup) - Add superscript
- [markdown-it-task-lists](https://github.com/revin/markdown-it-task-lists) - Add task lists
- [markdown-it-toc-done-right](https://github.com/nagaozen/markdown-it-toc-done-right) - Add table of contents

### This is a h3 tag

#### This is a h^4^ tag.

Enable the `typographer` option to see the magic.

(c) (C) (r) (R) (tm) (TM) (p) (P) +-

---

## Basic stuff

## Lists

Sometimes you want numbered lists:

1. One
2. Two
3. Three

Sometimes you want bullet points:

* Start a line with a star
* Profit!

Alternatively,

- Dashes work just as well
- And if you have sub points, put two spaces before the dash or star:
  - Like this
  - And this

## Blockquotes

As Abraham Lincoln once said:

> vue3-markdown-it is pretty amazing!

## Tables
First Header | Second Header
------------ | -------------
Content from cell 1 | Content from cell 2
Content in the first column | Content in the second column
Content in the first column | Content in the second column
Content in the first column | Content in the second column
Content in the first column | Content in the second column
Content in the first column | Content in the second column

---

# Anyway, guess what?!

![pog](https://cdn.frankerfacez.com/emoticon/305343/4)

We support plugging in external `markdown-it` plugins! [markdown-it-icons](https://github.com/tylingsoft/markdown-it-icons) was added as an external plugin. Let's test it out!

A :fa-car: runs!

# Ok, plugin showcase time!

## [markdown-it-abbr](https://github.com/markdown-it/markdown-it-abbr)

*[HTML]: Hyper Text Markup Language
*[W3C]:  World Wide Web Consortium
The HTML specification
is maintained by the W3C.

## [markdown-it-anchor](https://github.com/valeriangalliat/markdown-it-anchor)

Hard to display this, but if you view the source, you can see that all headings have an id generated from this plugin!

## [markdown-it-deflist](https://github.com/markdown-it/markdown-it-deflist)

First Term
: This is the definition of the first term.

Second Term
: This is one definition of the second term.
: This is another definition of the second term.

## [markdown-it-emoji](https://github.com/markdown-it/markdown-it-emoji)

:O :) :sparkles: 8-)

## [markdown-it-footnote](https://github.com/markdown-it/markdown-it-footnote)

Here is a footnote reference,[^1] and another.[^longnote]

## [markdown-it-highlightjs](https://github.com/valeriangalliat/markdown-it-highlightjs)
```python
print('Hello World! This is Python.')
```

```js
console.log("Hello World! This is JavaScript.");
```

## [markdown-it-ins](https://github.com/markdown-it/markdown-it-ins)

++this is inserted++

## [markdown-it-mark](https://github.com/markdown-it/markdown-it-mark)

==Oh hi, Mark.==

## [markdown-it-sub](https://github.com/markdown-it/markdown-it-sub)

C~7~H~14~O~2~

## [markdown-it-sup](https://github.com/markdown-it/markdown-it-sup)

Friday the 13^th^

## [markdown-it-task-lists](https://github.com/revin/markdown-it-task-lists)

- [ ] Homework
- [x] Procrastinating

## [markdown-it-toc-done-right](https://github.com/nagaozen/markdown-it-toc-done-right)

[^1]: Here is the footnote.

[^longnote]: Here's one with multiple blocks.

    Subsequent paragraphs are indented to show that they
belong to the previous footnote.