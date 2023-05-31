import socket
import os



# ----------------客户端---------------------
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2.在发送数据前，必须要跟对方建立连接
client_socket.connect('192.168.1.673', 9090)

# 3.输入下载文件名，进行发送
file_name = input('请输入要下载的文件名')
client_socket.sendto(file_name.encode('utf8'))

# 4.接受服务器返回的内容
service_content = client_socket.recv(1024)
with open(file_name, 'w', encoding='utf8') as file:
    file.write(service_content)

# 5. 关闭socket
client_socket.close()



# ----------------服务端---------------------
# 1.创建一个基于tcp的网络socket连接
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2.监听数据
server_socket.bind(('192.168.1.673', 9090))
server_socket.listen(673)  # 设置极限监听队列数

# 3.接收内容(接收到的数据是元组，第0个是客户端的socket连接，第1个是客户端的ip地址和端口号)
recv_client_socket, client_addr = server_socket.accept() 
recv_data = client_socket.recv(2014).decode('utf8') # buffersize为1024


# 4.处理下载请求
if os.path.isfile(recv_data):
    print('读取文件，返回给客户端')
    while True:
        with open(recv_data, 'r', encoding='utf8') as file:
            file_content = file.read()
            print(file_content)
            # 使用客户端的socket返回回去
            recv_client_socket.send(file_content.encode('utf8'))
else:
    print('文件不存在')

# 5.关闭连接
server_socket.close()

