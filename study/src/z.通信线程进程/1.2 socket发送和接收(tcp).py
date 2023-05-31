# socket可以在不同的电脑问通信;还可以在同一个电脑的不同程序之问通信
import socket



# ----------------发送数据(电脑A的应用aaa)---------------------
# 1.创建一个基于tcp的网络socket连接
# AF_INET:表示这个socket是用来进行网络连接
# SOCK_STREAM:表示连接是一个TCP连接
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2.在发送数据前，必须要跟对方建立连接
s.connect('192.168.1.673', 9090)

# 3．发送数据
# data：要发送的数据，它是二进制的数据
# address：发送给谁，参数是一个元组，元组里有两个元素,第0个表示目标的i口地址，第1个表示程序的端口号
s.sendto('hello'.encode('utf8'), ('192.168.1.673', 9090))

# 4. 关闭socket
s.close()



# ----------------接收数据(电脑B的应用bbb)---------------------
# 1.创建一个基于tcp的网络socket连接
recSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2.监听数据
recSocket.listen(673)  # 设置极限监听队列数

# 3.接收内容(接收到的数据是元组，第0个是客户端的socket连接，第1个是客户端的ip地址和端口号)
client_socket, client_addr = recSocket.accept() 
recv_data = client_socket.recv(2014).decode('utf8') # buffersize为1024
# client_socket= recSocket.accept()[0] 
# client_addr = recSocket.accept()[1] 

print(r'从ip地址{}端口{}接收到了消息，内容是：{}'.format(client_addr[0], client_addr[1], recv_data))

# 4.关闭连接
recSocket.close()

