# coding:utf-8
import xlrd
from parse_interface.BaseParse import BaseParse
from TraceLog import TraceLog

class ExcelParse(BaseParse):
    def __init__(self, file_path):
        super(ExcelParse, self).__init__(file_path)
        self.__flag_index = 0

    def open_excel(self):
        file_path = self.get_file_path()
        file_data = None
        try:
            file_data = xlrd.open_workbook(file_path)
        except Exception:
            TraceLog.log_error("parse excel error")
            raise
        finally:
            return file_data

    def get_specified_table(self, parse_type = "BY_INDEX", parse_val = 0):
        file_data = self.open_excel()

        if file_data is None:
            return None

        if parse_type == "BY_INDEX":
            table = file_data.sheets()[parse_val]
        else:
            table = file_data.sheet_by_name(parse_val)

        return table

    def get_table_col_data(self, parse_type = "BY_INDEX", parse_val = 0):
        table = self.get_specified_table(parse_type, parse_val)
        if table is None:
            return {}
        row_num = table.nrows
        col_flag =  table.row_values(self.get_flag_index())
        flag_data_dict = {}
        for index in range(1, row_num):
             row = table.row_values(index)
             if row:
                for i in range(len(col_flag)):
                    if col_flag[i] not in flag_data_dict:
                        flag_data_dict[col_flag[i]] = []
                    flag_data_dict[col_flag[i]].append(row[i])

        return flag_data_dict

    def set_flag_index(self, flag_index):
        self.__flag_index = flag_index

    def get_flag_index(self):
        return self.__flag_index

    def parse(self, conf):
        if len(conf) != 1 or ("BY_INDEX" not in conf and "BY_NAME" not in conf):
            return None

        for type, val in conf.items():
            return  self.get_table_col_data(type, val)

        return None
