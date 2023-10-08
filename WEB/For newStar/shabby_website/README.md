- **题目名称：** shabby_website
- **题目类型：** WEB
- **题目难度：** 中等
- **出题人：** Rieß
- **考点：**

1. 原型链污染
2. ssti

- **描述：** 快来尝试一下简单的代码审计，代码量很少，毕竟出题人连前端都懒得写。
- **flag：** 动态flag
- **Writeup：** 

拿到源码后先进行简单审计，/login路由接收传入的数据，修改session进行身份识别，但admin被过滤无法直接传递。/render路由直接对数据进行pugjs渲染。由于给了package.json因此可以直接在本地用npm起环境。
![[Pasted image 20231008084304.png]]
发现json5.parse方法存在原型链污染漏洞，/login路由在对输入进行处理时刚好使用了该方法，因此可以直接通过原型链污染将admin污染为true。（没有接触过原型链污染漏洞的建议先学习一下，在node.js中较常见）
![[Pasted image 20231008084938.png]]
拿到admin的session后再去访问/render路由，通过信息搜集发现pugjs也会存在ssti漏洞，直接使用相应的payload进行注入。
![[Pasted image 20231008085125.png]]
