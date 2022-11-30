'''
串口设置
'''
#端口名
portx = "COM3"
#波特率
bps = 9600
bps_list = [4800,9600,14400,19200,38400,57600,115200]
#超时时间
timex = 5


#预设姿势
default_pos =[[900, 2000, 900, 900, 900, 900],
              [900, 900, 900, 900, 900, 900],
              [900, 2000, 2000, 900, 900, 900],
              [900, 2000, 900, 2000, 900, 900],
              [900, 2000, 900, 900, 2000, 900],
              [900, 2000, 900, 900, 900, 2000]
              ]

ids = [6,1,2,3,4,5]
'''
网络控制部分
'''
#本机ip
net_address = "192.168.137.1"
#本机服务端端口
net_port = 8080