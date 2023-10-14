* **题目名称：**

* **题目类型：** MISC

* **题目难度：** 困难

* **出题人：** Silenter

* **考点：**  

1. 流量分析

2. 信息搜集

3. Minecraft

* **描述：**

偷偷加入朋友的世界想要下载他的地图，可是被发现然后赶走了……

没有关系！我还偷偷抓了他电脑的包……

* **Hints：**

[WIKI.VG](http://wiki.vg)

* **flag：**

XSCTF{MYWORLD}

* **Writeup：**

使用重放把地图显示出来（当然直接对着数据解析也是可以的，但是我喜欢直观一点的）

代码实现在MapStealer.zip

放入到支持BukkitAPI的服务端的plugins文件夹中，前置插件为ProtocolLib

同时在plugins中创建MapStealer文件夹，把服务器到客户端数据流放入data.bin（追踪流→TCP流→左下角选择服务端到客户端，show data as原始数据→另存为）

启动服务端并用客户端加入，服务端将会把所有区块覆盖为数据包中的区块

本题所使用的版本为1.20.2。

（截止WP更新的时候ProtocolLib没有出对应的正式版，可以通过Dev Builds获取。）
