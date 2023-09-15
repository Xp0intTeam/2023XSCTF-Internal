本文主要说明如何在 Google Cloud Platform 上创建、配置、维护用作比赛平台和靶机的虚拟机。

最后更新：2021/11/6

## 网络拓扑

下面是比赛平台和靶机虚拟机的网络拓扑。

```
                                                    Google Cloud Platform
                                          +----------------------------------------+
  +----------------+                      |                                        |
  |                |       CTF Payload    |                           SSH          |
  |                |  <-------------------|--------->  [dockervm]  <------+        |
  |   (players)    |                      |                               |        |
  |                |       HTTP / HTTPS   |                           SSH |        |
  |                |  <-------------------|--------->   [ctfdvm]   <------+        |
  +----------------+                      |                               |        |
                              SSH         |                               |        |
       (Xp0int)  <------------------------|-------------------------------+        |
                                          |                                        |
                                          +----------------------------------------+
```

| 序号 | 名称 | 开放端口（不含 SSH） | 描述 |
| :----: | :---- | :---- | :---- |
| 1 | **ctfdvm** | `TCP/80`</br> `TCP/443` | **Web 服务器**<br/>运行 CTFd 平台 |
| 2 | **dockervm**| `TCP/10000-20000` | **靶机**<br/>部署 Pwn / Web 题目 Docker 容器 |

## 简介

**[Google Cloud Platform (GCP)](https://cloud.google.com/)** 是 Google 推出的云计算平台，类似于 AWS、Azure 和阿里云。GCP 提供相应的 VPS 产品 (**[Compute Engine](https://cloud.google.com/compute/)**)，支持按秒计费，可以选择多种虚拟机类型、多种网络区域等。

选择 GCP 的理由：

* **新用户赠金：** [USD $300 / 90 天](https://cloud.google.com/free)
  * [AWS](https://aws.amazon.com/cn/free/)：每个月一台免费 t2.micro / t3.micro 虚拟机（最高 2 vCPU / 1 GB 内存）
  * [Azure](https://azure.microsoft.com/zh-cn/free/)：USD $200 / 30 天 （+ USD $100 [学生额度](https://azure.microsoft.com/zh-cn/free/students/)）
  * 阿里云：?
* **自定义机器配置：** 可以设置任意的 vCPU 数量和内存大小，节省费用
* **注册方便：** 只需 Google 帐号

***

### 注册 GCP

要求：

* 一个 Google 帐号
* 一张国际信用卡 / 借记卡

具体操作请参考网上教程。

### 添加协助者

**管理员：**

1. 登录已注册好的 Google 帐号；
2. 打开 [GCP 控制台](https://console.cloud.google.com/)，进入 “IAM 和管理” ->  “IAM” ；
3. 点击 “添加” ，输入协助者的 Google 邮箱地址，并选择角色：  
  * Viewer：只能查看、不能编辑，不能使用浏览器 SSH
  * Editor：允许查看和编辑，可以使用浏览器 SSH
  * Owner：管理员
4. 将项目名称 / ID 告诉给协助者。

**协助者：**

1. 将 Google 邮箱地址告诉项目管理员；
2. 登录 Google 帐号，打开 [GCP 控制台](https://console.cloud.google.com/)；
3. 点击网页上方的 “选择项目” （位于 `Google Cloud Platform` 文字的右边）
4. 在 “全部” 子标签中选择管理员告知的项目。

## 虚拟机创建指南

本节记载如何在 GCP 上创建带有静态 IP 的 Linux 虚拟机。

#### 1. 创建实例    
地址：[https://console.cloud.google.com/compute/instances](https://console.cloud.google.com/compute/instances)  
* **区域：** asia-east1  (台湾)*（原因：延迟低）*
* **可用区：** *（所有虚拟机位于同一个可用区即可）*
* **启动磁盘：**
  * （注意：实例创建后，不可更改启动磁盘，除非销毁重建）
  * **启动磁盘类型：** SSD *（原因：性能较好）*
  * **大小：**
    * **dockervm：** 20 GB *（原因：储存 Docker 容器）*
    * **ctfdvm：** 10 GB
  * **操作系统：** *（一般 Ubuntu 系列）*
* **机器配置：**
  * （注意：实例创建后，机器配置可以随时更改）
  * **系列：** `N2D` *（原因：性价比较好）*
  * **机器类型：** 自定义 *（原因：可以自选 vCPU 数量和内存大小）*
* **网络：** *（参见“防火墙配置指南”->“虚拟机”这节）*

#### 2. 预留公网 IP 地址  
地址：[https://console.cloud.google.com/networking/addresses/list](https://console.cloud.google.com/networking/addresses/list)  

找到刚创建的虚拟机，点击 “预留”。

注意：若不预留 IP 地址，每次重启虚拟机，公网 IP 地址会发生变化。

#### 3. 修改 SSH 端口

地址：[https://console.cloud.google.com/compute/instances](https://console.cloud.google.com/compute/instances)  

1. 打开 GCP 控制台，登录虚拟机  
  * “SSH” -> “ 在浏览器窗口中打开 ”   
2. 编辑`/etc/ssh/sshd_config`  
  * ```$ sudo vim /etc/ssh/sshd_config```
    * 将 `#Port 22` 改成 `Port _CUSTOM_SSH_PORT_`，`_CUSTOM_SSH_PORT_` 为自定义的 SSH 端口。
    * 添加`PermitRootLogin no`
3. 重启 SSH 服务
  * ```$ sudo service ssh restart```

## 连接虚拟机

本节记载如何通过 SSH 连接到虚拟机。

#### （方式一）浏览器 SSH

地址：[https://console.cloud.google.com/compute/instances](https://console.cloud.google.com/compute/instances)  

1. 打开 GCP 控制台，找到需要连接的虚拟机，点击 “SSH” -> “  通过自定义端口在浏览器窗口中打开 ”
2. 输入自定义 SSH 端口`_CUSTOM_SSH_PORT_`
3. 点击 “打开” 即可

浏览器 SSH [支持上传和下载文件](https://cloud.google.com/compute/docs/instances/transfer-files#transferbrowser)。

#### （方式二）本地 SSH 客户端

<del>
1. 添加 SSH 公钥
  1. 生成一对 SSH 密钥
  2. 通过方式一登录虚拟机，将 SSH 公钥添加到`~/.ssh/authorized_keys`  
    * `$ echo "ssh-rsa AAAA......." >> ~/.ssh/authorized_keys`
</del>

原方法有误。VPS 中的`~/.ssh/authorized_keys`由 Google agent 管理，任何自行添加的 SSH 公钥会被自动删除。

正确的方法是：

1. 生成一对 SSH 密钥
2. 登录到 GCP 控制台的[ SSH 密钥页面](https://console.cloud.google.com/compute/metadata/sshKeys)。添加 SSH 公钥，修改 SSH 公钥最后一个部分（以空格分割），使 “用户名” 一栏与浏览器 SSH 中使用的用户名一致。
3. 本地使用 SSH 客户端登录虚拟机
```
Hostname ：<虚拟机的公网 IP 地址>
Port     ：_CUSTOM_SSH_PORT_
Username ：<浏览器 SSH 中使用的用户名>
认证方式 ：SSH 私钥
```

## 虚拟机计费规则

**一台虚拟机所花费的费用 = 虚拟机实例费用 + 其他费用**

注意：虚拟机处于停止状态时，不收取虚拟机实例费用，只收取其他费用。

***

**虚拟机实例费用：**

创建虚拟机实例的页面上可以计算实例运行一个月的费用（包含启动磁盘费用）。

相同系列下，实例费用主要取决于 vCPU 数量。

**其他费用：**  
（以`asia-east1` 台湾的价格为例）
* 网络流量费用  
  * 出站至香港等地区：`USD$0.12/GB`
  * 出站至中国大陆：`USD$0.23/GB`
  * 入站流量免费
  * 同区域虚拟机之间的出站流量免费
  * 参见[这个页面](https://cloud.google.com/vpc/network-pricing)
* 静态公网 IP 地址费用
  * `USD$1.44/Month`（常规实例）
  * 若静态 IP 地址没有附加到虚拟机实例上，收费更高
  * 参见[这个页面](https://cloud.google.com/vpc/network-pricing#ipaddress)
* 启动磁盘费用
  * 10 GB SSD：`USD$1.87/Month`
  * 20 GB SSD：`USD$3.40/Month`

理想情况下，其他费用总和一般不超过`USD$10`。

## 防火墙配置指南

地址：[https://console.cloud.google.com/networking/firewalls/list](https://console.cloud.google.com/networking/firewalls/list)

所有虚拟机属于同一个 VPC 网络 **default**，通过**标记**来决定哪些防火墙规则应用于哪些虚拟机。

举个例子：带有 ctfdvm 标记的防火墙规则生效于所有带有 ctfdvm 标记的虚拟机。

**目前可用标记**：ctfdvm / dockervm

**目前正在使用的防火墙规则：**

| 防火墙规则名称 | 标记 | IP 地址 | 开放端口 | 描述 |
| :----: | :----: | :----: | :---- | :---- |
| **ctfdvm-allow-http-https** | `ctfdvm` | `0.0.0.0/0` | `TCP/80`<br/>`TCP/443` | 开放 **ctfdvm** 的 Web 服务端口 |
| **dockervm-allow-docker-ports** | `dockervm` | `0.0.0.0/0` | `TCP/10000-20000` | 开放 **dockervm** 的 Pwn / Web 题目端口 |
| **default-allow-ssh** | 无 | `0.0.0.0/0` | `TCP/22`<br/>`TCP/_CUSTOM_SSH_PORT_` | 开放 SSH 端口<br/>22 端口应只在初次连接虚拟机的时候使用

***

### 防火墙规则

创建新的防火墙规则时，请填写以下字段：

* **网络：** default
* **目标标记：** ctfdvm / dockervm（请根据虚拟机用选择其一）
* **来源 IPv4 范围：**
  * `0.0.0.0/0`：允许公网和内网访问
  * `10.128.0.0/9`：仅允许内网访问
* （可选）次要来源过滤条件：
  * 选择“来源标记”，填写标记名称

注意：GCP [默认](https://cloud.google.com/vpc/docs/firewalls?hl=zh-cn#default_firewall_rules)允许所有出站流量、拒绝所有入站流量。

### 虚拟机

创建新的虚拟机时，请填写以下字段：

  * **网络接口：** default
  * **网络标记**：ctfdvm / dockervm（请根据虚拟机用途选择其一）
    * 路径：“网络、磁盘、安全、管理、单租户”-> “网络”
