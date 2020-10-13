# NetworkProgramming

### 1. 网络、计算机网络的构成

在计算领域中，网络是传输信息、接受、共享的虚拟的平台。

通过它可以把各个点、面、体的信息联系到一起，从而实现这些资源的共享。


### 2. 什么是网络编程

网络编程从大的方面就是说对信息的发送接收。

通过操作相应API调度计算机资源硬件，并且利用管道（网线）进行数据交互的过程。

更为具体的涉及：网络模型、套接字、数据包


### 3. 7层网络模型 - OSI

基础层：物理层（Physical）、数据链路层（Datalink）、网络层（Network）

传输层（Transport）：TCP-UDP 协议层、Socket

高级层：会话层（Session）、表示层（Presentation）、应用层（Application）


### 4. 网络模型 - 对应关系


### 5. Socket 与 TCP UDP

Socket: 简单来说是 ip 地址与端口的结合协议（RFC 793）

    一种地址与端口的结合描述协议

    TCP/IP 协议的相关 API 的总称；是网络 API 的集合实现

    涵盖了 Stream Socket / Datagram Socket 

 Socket 的组成与作用：

    在网络传输中用于唯一标识两个端点的链接

    端点：包括（ip+port）

    4个要素：客户端的地址、客户端的端口、服务器的地址、服务器端口
              

### 6. Socket 的传输原理

Socket 之 TCP:

    TCP 是面向连接的通讯协议。

    通过三次握手建立连接，通讯完成时要拆除连接。

    由于 TCP 是面向连接的，所以只能用于端到端的通信。

Socket 之 UDP:

    UDP 是面向无连接进行通讯的。

    UDP 数据包括目的端口号和源端口号信息。

    由于通讯时是不需要连接，所以可以是实现广播发送，并不局限于端到端。


### 7. Client-Server Application

### 8. 报文段

### 9. 传输协议
