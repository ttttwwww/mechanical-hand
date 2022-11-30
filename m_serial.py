import serial
import setting
import serial.tools.list_ports
import copy

FRAME_HEAD = [0x55,0x55,0x00]
CMD_MULT_SERVO_MOVE = 0x03
CMD_FULL_ACTION_RUN = 0x06
CMD_FULL_ACTION_STOP = 0x07
CMD_FULL_ACTION_ERASE = 0x08
CMD_ACTION_DOWNLOAD = 0x19

class MySerial:
    def __init__(self):
        super(MySerial, self).__init__()
        self.bps=setting.bps
        self.port=setting.portx
        self.timex=setting.timex
        self.m_serial =serial.Serial()
        self.port_list = list(serial.tools.list_ports.comports())

    def port_connect(self):
        print(self.port,self.bps)
        self.m_serial = serial.Serial(self.port ,self.bps,timeout=self.timex)

    def port_close(self):
        self.m_serial.close()
    '''
        用于直接控制手势姿势
        串口通信的格式为
        [0x55,0x55,length,cmd_parameter,cnt,time_low,time_high,idx,posx_l,posx_h,...]
        参数：
            cnt 调控手指数量
            time 动作用时，用于调整速度 最小为0，最大还没试
            ids 调控手指的编号
            pos 调控手指的位置参数，从900到2000，为对应舵机的pwm参数
    '''
    def gesture_set(self,cnt,time,ids,pos):
        # 设命令内容
        print("parameter")
        print(cnt,time,ids,pos)
        temp = []
        length = 5
        time_high = time & 0xff00>>8# 将时间拆分为高低八位
        time_low = time & 0xff
        for i in range(cnt):
            temp.append(ids[i])
            temp.append(pos[i] & 0xff)
            temp.append((pos[i] & 0xff00)>>8)
            length += 3

        # 填装命令
        cmd = copy.deepcopy(FRAME_HEAD)
        cmd[2] = length
        cmd.append(CMD_MULT_SERVO_MOVE)
        cmd.append(cnt)
        cmd.append(time_low)
        cmd.append(time_high)
        cmd.extend(temp)
        # 串口发送命令
        self.m_serial.write(cmd)
    '''
        用于将手势预设为目标姿势
        参数：
            idx 手势对应编号
                0 全部收紧
                1 全部张开
                其他待定
    '''
    def gesture_default(self,idx):
        #格式[0x55, 0x55, length, cmd_parameter, cnt, time_low, time_high, idx, posx_l, posx_h, ...]
        cmd0 = [0x55,0x55,0x17,0x03,0x05,0x00,0x00,0x00,0x84,0x03,0x01,0x84,0x03,0x02,0x84,0x03,0x03,0x84,0x03,0x04,
                0x84,0x03,0x05,0x84,0x03]
        cmd1 = [0x55,0x55,0x17,0x03,0x05,0x00,0x00,0x00,0xD0,0x07,0x01,0xD0,0x07,0x02,0xD0,0x07,0x03,0xD0,0x07,0x04,
                0xD0,0x07,0x05,0xD0,0x07]
        cmd = {
            0: cmd0,
            1: cmd1
        }
        if cmd.get(idx) == None:
            print("default gesture doesn't exist")
        self.m_serial.write(cmd.get(idx))






