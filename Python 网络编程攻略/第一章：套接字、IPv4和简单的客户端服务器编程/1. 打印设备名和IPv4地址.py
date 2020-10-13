# 要快速查看设备的某些信息，例如主机名、IP地址和网络接口的数量等

import socket


def print_machine_info():
    host_name = socket.gethostname()
    ip_address = socket.gethostbyname(host_name)

    print("Host name:%s" % host_name)
    print("IP address:{}".format(ip_address))


if __name__ == '__main__':
    print_machine_info()

    
'''
  gethostname(),没有参数，返回所在主机或本地主机的名字
  gethostbyname(host_name),接收一个参数 hostname，返回对应的IP地址
'''
    
'''
  __name__是python的一个内置类属性，它天生就存在于一个 python 程序中，代表对应程序名称

  我们要在常用的__main__代码块中调用这个函数
  运行时，Python会为某些内部变量赋值，例如__name__。在这里，__name__表示调用程序的进程名
  如果在命令行中运行脚本（如后面 的命令所示），__name__的值是__main__。
  如果在命令行中调用这个模块，会自动运行print_machine_info()函数；
  如果在其他脚本中导入，用户就要手动调用这个函数。
'''
