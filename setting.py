
# region 工作模式
MODE_SERIAL = 0
MODE_NET = 1
mode_list = {
    MODE_SERIAL: "self.ser.gesture_set",
    MODE_NET: "self.tcp_server.gesture_set"
}
# endregion

# region 串口设置
# 端口名
portx = "COM3"
# 波特率
bps = 9600
bps_list = [4800, 9600, 14400, 19200, 38400, 57600, 115200]
# 超时时间
timex = 5


# 预设姿势
default_pos =[[900, 2000, 900, 900, 900, 900],
              [900, 900, 900, 900, 900, 900],
              [900, 2000, 2000, 900, 900, 900],
              [900, 2000, 900, 2000, 900, 900],
              [900, 2000, 900, 900, 2000, 900],
              [900, 2000, 900, 900, 900, 2000]
              ]

ids = [6, 1, 2, 3, 4, 5]
# endregion

# region 网络设置
# 本机ip
net_address = "192.168.137.1"
# 本机服务端端口
net_port = 8080
# endregion

# region 图形显示

# SPOTS_POS = [
#     [50, 160, 51, 41],
#     [140, 30, 31, 31],
#     [180, 20, 31, 31],
#     [220, 40, 31, 31],
#     [260, 60, 31, 31],
#     [150, 150, 81, 71]
# ]

SPOTS_POS = [[147,35,5,5],
[149,48,5,5],
[152,63,5,5],
[156,78,5,5],
[159,91,5,5],
[159,107,5,5],
[159,34,5,5],
[163,48,5,5],
[167,64,5,5],
[169,78,5,5],
[172,93,5,5],
[173,107,5,5],
[189,32,5,5],
[189,46,5,5],
[190,59,5,5],
[188,76,5,5],
[188,88,5,5],
[186,106,5,5],
[199,32,5,5],
[202,48,5,5],
[203,62,5,5],
[203,76,5,5],
[199,92,5,5],
[198,107,5,5],
[229,48,5,5],
[227,60,5,5],
[224,73,5,5],
[221,86,5,5],
[219,99,5,5],
[218,112,5,5],
[240,49,5,5],
[239,62,5,5],
[237,76,5,5],
[234,88,5,5],
[233,101,5,5],
[230,115,5,5],
[272,72,5,5],
[269,83,5,5],
[265,93,5,5],
[260,106,5,5],
[257,118,5,5],
[250,132,5,5],
[282,74,5,5],
[280,86,5,5],
[275,99,5,5],
[271,112,5,5],
[267,124,5,5],
[261,138,5,5],
[53,157,5,5],
[69,160,5,5],
[87,163,5,5],
[103,165,5,5],
[118,167,5,5],
[132,171,5,5],
[52,168,5,5],
[67,173,5,5],
[85,174,5,5],
[102,178,5,5],
[116,182,5,5],
[130,187,5,5],
[165,153,5,5],
[180,154,5,5],
[192,157,5,5],
[208,161,5,5],
[221,162,5,5],
[235,166,5,5],
[249,167,5,5],
[152,153,5,5],
[151,166,5,5],
[166,169,5,5],
[183,170,5,5],
[196,172,5,5],
[208,174,5,5],
[224,177,5,5],
[239,178,5,5],
[253,179,5,5],
[150,182,5,5],
[164,183,5,5],
[181,186,5,5],
[195,186,5,5],
[208,188,5,5],
[225,191,5,5],
[238,192,5,5],
[251,193,5,5],
[151,197,5,5],
[162,199,5,5],
[179,202,5,5],
[194,203,5,5],
[208,206,5,5],
[222,208,5,5],
[237,209,5,5],
[250,210,5,5],
[169,217,5,5],
[185,219,5,5],
[200,221,5,5],
[217,223,5,5],
[177,140,5,5],
[194,144,5,5],
[210,148,5,5],
[231,150,5,5]
]

SPOTS_NUMBER = len(SPOTS_POS)

default_opacity = [0,0.25,0.5,0.75,1]

DATA_SET_PATH = "./test.xlsx"
# endregion

# region 数据集参数
DATA_LEN = 500
MAX_PRESSURE_FRE = 46.21489
#