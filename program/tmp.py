import re

# str = "110   login"
# if re.search(r'\d{1,4}\s+[a-z]+', str) and len(str) > 0 and len(str)<20:
#     print("aaaaaaaaaa")
# else:
#     print("error")

# def Singleton(cls):
#     _instance = {}

#     def _Singleton(*args, **kwargs):
#         if cls not in _instance:
#             _instance[cls] = cls(*args, **kwargs)
#         return _instance[cls]

#     return _Singleton

# @Singleton
# class Tmp1(object):
#     def __init__(self):
#         pass


# if __name__ == "__main__":
#     t1 = Tmp1()
#     t2 = Tmp1()
#     print(id(t1)==id(t2))
    
#     k = {}
#     k[1] = []
#     k[2] = []
#     print(k)
#     k["aa"] = []
#     print(k)
    
#     kk = k["bb"] = "bb"
#     print(kk)



# import sys
# from PyQt5 import QtWidgets
# from PyQt5 import QtCore
# from PyQt5 import QtGui

# class CDemo(QtWidgets.QWidget):
#     def __init__(self):
#         super().__init__()

#         self.o_line_edit_0 = self._gen_line_edit_0()
#         self.o_btn_0 = self._gen_btn_0()

#         self.o_line_edit_1 = self._gen_line_edit_1()
#         self.o_btn_1 = self._gen_btn_1()

#         self.resize(300, 200)
#         self.setLayout(self._gen_layout())

#     def _gen_line_edit_0(self):
#         _o_line_edit = QtWidgets.QLineEdit('line edit 0')
#         _o_line_edit.setSelection(5, 9)
#         return _o_line_edit

#     def _gen_line_edit_1(self):
#         _o_line_edit = QtWidgets.QToolButton()
#         _o_line_edit.setText("line edit 1")
#         #_o_palette = QtGui.QPalette()      # 创建一个新调色板
#         _o_palette = _o_line_edit.palette() # 获取已有调色板，在已有调色板基础上修改
#         _o_palette.setColor(QtGui.QPalette.Base           , QtCore.Qt.yellow) # 文本部件背景色
#         _o_palette.setColor(QtGui.QPalette.Text           , QtCore.Qt.blue)   # 文本部件颜色
#         _o_palette.setColor(QtGui.QPalette.Highlight      , QtCore.Qt.green)  # 文本部件选中的背景色
#         _o_palette.setColor(QtGui.QPalette.HighlightedText, QtCore.Qt.red)    # 文本部件选中的文本颜色

#         _o_line_edit.setPalette(_o_palette)      # 为组件设置调色板
#         _o_line_edit.setAutoFillBackground(True) # 不加这句，则颜色不生效
#         return _o_line_edit

#     def _gen_btn_0(self):
#         _o_btn = QtWidgets.QPushButton('button 0')
#         return _o_btn

#     def _gen_btn_1(self):
#         _o_btn = QtWidgets.QPushButton('button 1')

#         #_o_palette = QtGui.QPalette()
#         _o_palette = _o_btn.palette() # 获取已有调色板，在已有调色板基础上修改
#         _o_palette.setColor(QtGui.QPalette.ButtonText, QtCore.Qt.blue)   # 按钮文本颜色
#         #_o_palette.setColor(QtGui.QPalette.Button   , QtCore.Qt.yellow) # 按钮背景色，不起效
#         # 注意：QPushButton的背景色涉及样式表，所以不能通过QPalette修改.

#         _o_btn.setPalette(_o_palette)      # 为组件设置调色板
#         _o_btn.setAutoFillBackground(True) # 不加这句，则颜色不生效
#         return _o_btn

#     def _gen_layout(self):
#         _o_layout_0 = QtWidgets.QHBoxLayout()
#         _o_layout_0.addWidget(self.o_line_edit_0)
#         _o_layout_0.addWidget(self.o_btn_0)
#         _o_layout_0.addStretch(1)

#         _o_layout_1 = QtWidgets.QHBoxLayout()
#         _o_layout_1.addWidget(self.o_line_edit_1)
#         _o_layout_1.addWidget(self.o_btn_1)
#         _o_layout_1.addStretch(1)

#         _o_layout_main = QtWidgets.QVBoxLayout()
#         _o_layout_main.addLayout(_o_layout_0)
#         _o_layout_main.addLayout(_o_layout_1)

#         return _o_layout_main

# if __name__ == '__main__':
#     app = QtWidgets.QApplication(sys.argv)
#     win = CDemo()
#     win.show()
#     sys.exit(app.exec_())

for i in range(10):
    print(i)
    
if '10 login'.find("log") > 0:
    print("xxxxxxxxxxxxx")
else:
    print("sssssssssssss")

kk = "100|200|300"
print(kk.split("|"))

print(list(map(float, kk.split("|"))))
try:
    k = int("100")
except ValueError as e:
    print(e)

ipre = re.compile("^((?:(2[0-4]\d)|(25[0-5])|([01]?\d\d?))\.){3}(?:(2[0-4]\d)|(255[0-5])|([01]?\d\d?))$")
if ipre.match('127.0.0.1'):
    print("true")
else:
    print('xxxx')