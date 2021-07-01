import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import os

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)
## pyinstaller에게 ui파일을 포함하도록 알려 줘야 하는데, spec 파일이다.
## spec 파일은 프로그램 빌드 시 다양한 옵션을 줄 수 있도록 하는 파일이다.
## .py 스크립트만 빌드를 하면 spec 파일이 자동으로 생성된다. 그러면 그걸 수정하고 다시 빌드하면 된다.
###################################################################################


#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
#form_class = uic.loadUiType("listwidgetTest.ui")[0]
form = resource_path("pushbuttonTest.ui")
form_class = uic.loadUiType(form)[0]
# ('listwidgetTest.ui','.')




#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        #test

        # qt designer의 objectName명이 btn_1과 btn_2이다.
        self.btn_1.clicked.connect(self.button1Function)
        self.btn_2.clicked.connect(self.button2Function)

    def button1Function(self) :
        print("btn_1 Clicked")

    def button2Function(self) :
        print("btn_2 Clicked")


if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()