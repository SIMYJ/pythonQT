import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("lineeditTest.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        #버튼에 기능을 할당하는 코드
        self.lineedit_Test.textChanged.connect(self.lineeditTextFunction)# LineEdit의 글자가 바뀔 때 기능 실행
        self.lineedit_Test.returnPressed.connect(self.printTextFunction)#LineEdit에서 Return키(Enter키)가 눌렸을 때 기능 실행
        self.btn_changeText.clicked.connect(self.changeTextFunction)

    # 라벨이 lineedit텍스트값 가져온다.
    def lineeditTextFunction(self) :
        self.lbl_textHere.setText(self.lineedit_Test.text())

    def printTextFunction(self) :
        #self.lineedit이름.text()
        #Lineedit에 있는 글자를 가져오는 메서드
        print(self.lineedit_Test.text())

    def changeTextFunction(self) :
        #self.lineedit이름.setText("String")
        #Lineedit의 글자를 바꾸는 메서드
        self.lineedit_Test.setText("Change Text")

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()