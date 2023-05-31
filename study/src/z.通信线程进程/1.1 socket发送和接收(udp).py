# socket可以在不同的电脑问通信;还可以在同一个电脑的不同程序之问通信
import socket



# ----------------发送数据(电脑A的应用aaa)---------------------
# 1.创建一个基于udp的网络socket连接
# AF_INET:表示这个socket是用来进行网络连接
# SOCK_DGRAM:表示连接是一个udp连接
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 2.绑定端口号：使对方能够正确的回复
s.bind('192.168.1.111', 8080)

# 3．发送数据
# data：要发送的数据，它是二进制的数据
# address：发送给谁，参数是一个元组，元组里有两个元素,第0个表示目标的i口地址，第1个表示程序的端口号

# 给 192.168.1.199 这台主机的9090端口上发送了hello
# 端口号范围：0-65536 (注意0-1024不要用，是系统一些重要的务在使用)
s.sendto('hello'.encode('utf8'), ('192.168.1.673', 9090))

# 4. 关闭socket
s.close()



# ----------------接收数据(电脑B的应用bbb)---------------------
# 1.创建一个基于udp的网络socket连接
recSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 2.绑定端口号和ip地址
recSocket.bind('192.168.1.673', 9090)

# 3.接收内容(接收到的数据是元组，第0个是接收到的数据，第1个是发送方的ip地址和端口号)
data, addr = recSocket.recvfrom(1024) # buffersize为1024
# data= recSocket.recvfrom(1024)[0] 
# addr = recSocket.recvfrom(1024)[1] 

# b'\xe4\xb8\x8b\xe5\x8d\x88\xe5\xa5\xbd',('192.168.1.199', 8080)
print(r'从ip地址{}端口{}接收到了消息，内容是：{}'.format(addr[0], addr[1], data))

# 4.关闭连接
recSocket.close()




# 绑定端口号的意义：如果不绑定的话，每次发送消息后，端口都会被重置，所以发送方和接收方都需要bing端口号