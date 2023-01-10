import os 
import pandas as pd
import numpy as np
import matplotlib as mtp
import matplotlib.pyplot as plt
import csv
import copy


class DataSetProcess():
    def __init__(self,raw_path):
        super(DataSetProcess,self).__init__()

        #region parameter
        self.MODE_SLICE = 0
        self.MODE_DIRECT_FRE = 1
        self.MODE_SLICE_FRE = 2
        self.NUMBER_SLICE = 6

        self.PATH_DATA_SLICED = r'.\slice'
        #endregion

        self.csv_list = []
        self.leaf_dir_list = []
        self.raw_path = raw_path
        self.path = None
        self.mode = self.MODE_SLICE

    def run(self, mode=None):
        if mode is None:
            if self.mode == self.MODE_SLICE:
                print(1)
            elif self.mode == self.MODE_DIRECT_FRE:
                print(1)
            elif self.mode == self.MODE_SLICE_FRE:
                print(1)
            else:
                raise ValueError("work mode is not assigned")
        else:
            if self.mode == self.MODE_SLICE:
                print(1)
            elif self.mode == self.MODE_DIRECT_FRE:
                print(1)
            elif self.mode == self.MODE_SLICE_FRE:
                print(1)
            else:
                raise ValueError("Wrong set for mode parameter")

    def slice_raw_data(self, plot=False):
        self.m_get_csv()
        for file in self.csv_list:
            with open(file,'r',encoding='utf-8') as f:
                reader = csv.reader(f)
                t = []  # 时间戳
                v0 = []  # 第一组电压
                v1 = []  # 第二组电压
                cnt = 0  # 计数，跳过前十行
                flag_islow = False  # 用于标记现在电位是否为低
                flag_start = False  # 用于标记是否已经进入了发放
                index_start = -1
                index_end = -1

                for row in reader:
                    if cnt > 10:
                        t.append(float(row[0] if row[0] != "" else 0))
                        v0.append(float(row[1] if row[1] != "" else 0))
                        v1.append(float(row[2] if row[2] != "" else 0))
                    cnt += 1

                if max(v0) > 1:
                    v2 = copy.deepcopy(v1)
                    v1 = copy.deepcopy(v0)
                    v0 = copy.deepcopy(v2)

                for i in range(len(t)):
                    if v0[i] < 0.06:
                        flag_islow = True
                    if v0[i] > 0.08 and flag_islow:
                        if flag_start is False:
                            flag_start = True
                            index_start = i
                        index_end = i

                length = index_end - index_start
                len_slice = length // self.NUMBER_SLICE
                for i in range(self.NUMBER_SLICE):

                    slice = [t[i * len_slice + index_start: (i + 1) * len_slice + index_start],
                             v0[i * len_slice + index_start: (i + 1) * len_slice + index_start],
                             v1[i * len_slice + index_start: (i + 1) * len_slice + index_start],
                             ]
                    if plot == True:
                        plt.plot(slice[1])
                        plt.show()
                    self.save_slice(slice,file,i)

    # region parameter_fun
    def m_get_csv(self):
        self.csv_list = self.get_csv()
        print(self.csv_list)

    def m_get_leaf_dir(self):
        self.leaf_dir_list = self.get_leaf_dir()
        print(self.leaf_dir_list)

    def m_set_raw_path(self,path):
        self.raw_path = path

    def m_set_path(self,path):
        self.path = path

    # endregion
    # region bottom_fun

    def get_csv(self, raw_path=None):
        if raw_path is None:
            raw_path = self.raw_path
        dir_list = os.listdir(raw_path)
        if dir_list is None:
            raise ValueError("empty dir {}".format(raw_path))
        csv_list = []
        for item in dir_list:
            path = os.path.join(raw_path, item)
            if os.path.splitext(path)[1] == ".csv":
                csv_list.append(path)
            if os.path.isdir(path):
                temp_list = self.get_csv(raw_path=path)
                csv_list.extend(temp_list)

        return csv_list

    def get_leaf_dir(self,raw_path=None):
        if raw_path is None:
            raw_path = self.raw_path
        dir_list = os.listdir(raw_path)
        if dir_list is None:
            raise ValueError("empty dir {}".format(raw_path))
        leaf_dir_list = []
        for item in dir_list:
            if '副本' in item:
                leaf_dir_list.append(raw_path)
                return leaf_dir_list

        for item in dir_list:
            path = os.path.join(raw_path, item)
            if os.path.isdir(path):
                temp_list = self.get_leaf_dir(raw_path=path)
                leaf_dir_list.extend(temp_list)

        return leaf_dir_list
    '''传入原始数据的数组，切分为指定段数后传回'''
    def save_slice(self, slice, raw_file,slice_index):
        slice = np.array(slice)
        dataframe = pd.DataFrame({"t": slice[0], "v0": slice[1], "v1": slice[2]})
        (path, file_name) = os.path.split(raw_file)
        path = os.path.relpath(path)
        path = os.path.join(self.PATH_DATA_SLICED, path)
        print(path)

        file_name = os.path.splitext(file_name)[0]
        print(file_name)
        file_name = file_name + "_slice_" + str(slice_index) + ".csv"
        file_path = os.path.join(path, file_name)
        print(file_path)
        os.makedirs(path, exist_ok=True)
        dataframe.to_csv(file_path, index=False)
    #endregion


if __name__ == "__main__":
    dataset = DataSetProcess(r'F:\Study\打工\温度压力双模态频率处理\温度压力双模态频率处理\raw')
    dataset.slice_raw_data(plot=True)