import os

import numpy as np
import pandas as pd

import setting

92415997


class DataSet():
    def __init__(self, file_path=None):
        self.data_normalized = None
        self.max_pressure_fre = None
        self.raw_lab = None
        self.raw_data = None
        self.file_type = None
        self.raw_data_file = None
        self.file_path = None
        self.raw_array = None

        self.data_len = setting.DATA_LEN

        if file_path is None:
            return
        self.file_path = file_path
        self.read_file()
        self.normalize_raw_data()

    def set_path(self, file_path):
        if os.path.isfile(file_path) is False:
            raise ValueError("file {} doesn't exist".format(file_path))
        self.file_path = file_path

    def read_file(self):
        if os.path.isfile(self.file_path) is False:
            raise ValueError("file {} doesn't exist".format(self.file_path))
        self.file_type = os.path.splitext(self.file_path)[1]
        if self.file_type == ".csv":
            self.read_csv()
        elif self.file_type == ".xlsx":
            self.read_excel()
        else:
            raise ValueError("the format of file {} doesn't match".format(self.file_path))

    def read_csv(self):
        self.raw_data_file = pd.read_csv(self.file_path)

    def read_excel(self):
        self.raw_data_file = pd.read_excel(self.file_path,header=None)
        self.raw_array = self.raw_data_file.values
        self.raw_data = self.raw_array[:, :self.data_len]
        self.raw_lab = self.raw_array[:, self.data_len:]

    # 用于得到最大的频率
    def get_max_pressure_fre(self, mode="static"):
        if mode == "static":
            self.max_pressure_fre = setting.MAX_PRESSURE_FRE
        elif mode == "dynamic":
            self.max_pressure_fre = np.max(self.raw_data)

    def normalize_raw_data(self):
        self.get_max_pressure_fre()
        self.data_normalized = np.divide(self.raw_data, self.max_pressure_fre)


if __name__ == "__main__":
    test = DataSet(setting.DATA_SET_PATH)
    # test.read_file()
