import sys
import os
from PySide2 import QtWidgets, QtCore, QtUiTools


class MyApp(QtWidgets.QMainWindow):
    """
    계산기 입니다
    """
    def __init__(self):
        super().__init__()

        ui_path = os.path.expanduser('~/calc.ui')
        ui_file = QtCore.QFile(ui_path)
        ui_file.open(QtCore.QFile.ReadOnly)
        loader = QtUiTools.QUiLoader()
        self.ui = loader.load(ui_file)
        ui_file.close()
        self.ui.show()

        self.temp = 0
        self.first_num = 0
        self.second_num = 0
        self.float_count = 0
        self.func = 'none'
        self.sum_count = False
        self.input_min_toggle = False

        for child in self.ui.findChildren(QtWidgets.QPushButton):
            child.clicked.connect(self.apply_value)

    def apply_value(self):
        button = self.sender()
        if button.objectName().startswith('num_'):
            num = int(button.objectName()[-1:])
            self.input_num(num, self.func)
        if button.objectName().startswith('func_'):
            self.input_func(button.objectName())
        if button.objectName().startswith('efunc_'):
            self.ect_func(button.objectName())
        if button.objectName().startswith('sum_'):
            self.sum()
        if button.objectName().startswith('clear_'):
            self.clear_num()
        if button.objectName().startswith('point_'):
            self.make_float()

    def input_num(self, num, func):
        self.sum_count = False
        if self.input_min_toggle is True:
            num *= -1
        qnum = self.float_check(num)
        if func == 'none':
            if self.float_count == 0:
                self.first_num *= 10
            self.first_num += qnum
            self.num_formatting_and_display(self.first_num, 'main_display')
        else:
            if self.float_count == 0:
                self.second_num *= 10
            self.second_num += qnum
            self.num_formatting_and_display(self.second_num, 'main_display')

    def input_func(self, func):
        # if func == "none":
        #     pass
        # else:
        #     self.sum(self.func)
        self.func = func
        self.float_count = 0
        self.input_min_toggle = False
        self.num_formatting_and_display(self.first_num, 'sub_display')
        self.num_formatting_and_display(self.second_num, 'main_display')

    def sum(self):
        if self.sum_count is True:
            execute_num = self.temp
        else:
            execute_num = self.second_num
            self.temp = self.second_num
        if self.func == 'func_add':
            self.first_num += execute_num
        if self.func == 'func_sub':
            self.first_num -= execute_num
        if self.func == 'func_mul':
            self.first_num *= execute_num
        if self.func == 'func_div':
            self.first_num /= execute_num
        self.second_num = 0
        self.float_count = 0
        self.sum_count = True
        self.input_min_toggle = False
        formatted_a = format(self.first_num, '.12g')
        formatted_b = format(execute_num, '.12g')
        self.ui.disp_main.display(formatted_a)
        self.ui.disp_sub.display(formatted_b)

    def clear_num(self):
        self.func = 'none'
        self.first_num = 0
        self.second_num = 0
        self.float_count = 0
        self.ui.disp_main.display(self.first_num)
        self.ui.disp_sub.display(self.second_num)

    def ect_func(self, func):
        execute_num = 0
        if func == 'efunc_perc':
            execute_num = 0.01
        elif func == 'efunc_min':
            self.input_min_toggle = not self.input_min_toggle
            execute_num = -1
        if self.func == 'none' or self.sum_count is True:
            self.first_num *= execute_num
            self.ui.disp_main.display(self.first_num)
        else:
            self.second_num *= execute_num
            self.ui.disp_main.display(self.second_num)

    def float_check(self, num):
        for i in range(self.float_count):
            num *= 0.1
        else:
            pass
        if self.float_count > 0:
            self.float_count += 1
        return num

    def make_float(self):
        if self.float_count == 0:
            self.float_count = 1
        else:
            pass

    def num_formatting_and_display(self, num, status):
        num = format(num, '.12g')
        if status == 'main_display':
            self.ui.disp_main.display(num)
        if status == 'sub_display':
            self.ui.disp_sub.display(num)
        if status == 'format_first_num':
            self.first_num = num
        if status == 'format_second_num':
            self.second_num = num


def main():
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)
    app = QtWidgets.QApplication()
    aapp = MyApp()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
