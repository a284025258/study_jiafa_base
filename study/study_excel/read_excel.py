import openpyxl


class ReadExcel(object):
    def __init__(self, file, sheet_name):
        """

        :param file: 文件路径及文件名
        :param sheet_name:
        """
        self.file = file
        self.sheet_name = sheet_name

    def open(self):
        """
        打开Excel文档指定sheet
        :return:
        """
        self.workbook = openpyxl.load_workbook(self.file)
        self.sheet = self.workbook[self.sheet_name]

    def read_data(self):
        """

        :return:
        """
        self.open()
        # 获取sheet所有数据
        rows = list(self.sheet.rows)
        # 获取表头数据
        title = [row.value for row in rows[0]]
        # 获取其他行数据
        cases = []
        for row in rows[1:]:
            data = [r.value for r in row]
            # title与每行数据打包并转化为字典类型
            case = dict(zip(title, data))
            cases.append(case)
        return cases



if __name__ == '__main__':
    read_excel1 = ReadExcel('cases.xlsx', 'login')
    cases = read_excel1.read_data()
    print(cases)