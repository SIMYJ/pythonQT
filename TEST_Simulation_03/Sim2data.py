import os
import sys

from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from TEST_Simulation_03.json2png_EDA import Json2Png

form_class = uic.loadUiType("Sim2data.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Sim2Data')
        # 현재는 클래스 빌딩과 로드가 있다.
        self.list_selected_class = [True, True, True, True, True, True, True, True, False]

        #클래스에 표현 될 색 리스트
        self.class_color =[QColor(205, 92, 92).name(),
                           QColor(0, 255, 0).name(),
                           QColor(199, 21, 133).name(),
                           QColor(32, 178, 170).name(),
                           QColor(233, 150, 122).name(),
                           QColor(0, 0, 255).name(),
                           QColor(128, 0, 0).name(),
                           QColor(255, 0, 0).name(),
                           QColor(0,0,0).name()
                           ]

        ##########################################
        ## listWidget_Test에 label 데이터 넣기
        self.listWidget_Test.clear()
        for name in json2png_object.list_file_name:
             self.listWidget_Test.addItem(name)
        ################################################################################################################

        # UI 성능지표 (label_visualization)
        #path_label_visualization = os.getcwd()
        #path_label_visualization += "/image/label_visualization.png"

        #print("path_label_visualizationpath_label_visualization:::{}".format(path_label_visualization))
        #self.qPixmapVar_visualization = QPixmap()
        #self.qPixmapVar_visualization.load(path_label_visualization)
        #self.label_visualization.setPixmap(self.qPixmapVar_visualization.scaled(850,630))

        # 성능지표 gif 시각화하는법
       # movie = QMovie("/home/aiffel-dj60/aiffel/0.PythonQT_STUDY/image/simtodata/성능지표_영상.gif")
        #self.setStyleSheet("background:blue;")
       # self.label_visualization.move(0, 0)
       # self.label_visualization.resize(850, 650)
       # self.label_visualization.setMovie(movie)
       # self.label_visualization.setScaledContents(True)
       # movie.start()

        # 성능 지표 버튼
        self.pushButton_2.clicked.connect(self.clickableBtn2)



        #################################################################################################################

        #ListWidget의 시그널
        self.listWidget_Test.itemClicked.connect(self.chkItemClicked)
        self.listWidget_Test.itemDoubleClicked.connect(self.chkItemDoubleClicked)
        self.listWidget_Test.currentItemChanged.connect(self.chkCurrentItemChanged)

        #버튼에 기능 연결
        self.btn_addItem.clicked.connect(self.addListWidget)
        self.btn_insertItem.clicked.connect(self.insertListWidget)

        self.btn_printItem.clicked.connect(self.printCurrentItem)
        self.btn_printMultiItems.clicked.connect(self.printMultiItems)
        self.btn_removeItem.clicked.connect(self.removeCurrentItem)
        self.btn_clearItem.clicked.connect(self.clearItem)

        ################################################################
        # 이미지 전처리 버튼
        self.btn_Preprocessing.clicked.connect(self.preprocessingImage)

        # GroupBox안에 있는 CheckBox에 기능 연결
        self.groupchk_1.stateChanged.connect(self.groupchkFunction)
        self.groupchk_2.stateChanged.connect(self.groupchkFunction)
        self.groupchk_3.stateChanged.connect(self.groupchkFunction)
        self.groupchk_4.stateChanged.connect(self.groupchkFunction)
        self.groupchk_5.stateChanged.connect(self.groupchkFunction)
        self.groupchk_6.stateChanged.connect(self.groupchkFunction)
        self.groupchk_7.stateChanged.connect(self.groupchkFunction)
        self.groupchk_8.stateChanged.connect(self.groupchkFunction)
        self.groupchk_9.stateChanged.connect(self.groupchkFunction)

        # 클래스 색
        self.frame_1.setStyleSheet('QWidget { background-color: %s }' % self.class_color[0]) # class_color[0]는#4e9a06 이런꼴
        self.frame_2.setStyleSheet('QWidget { background-color: %s }' % self.class_color[1])
        self.frame_3.setStyleSheet('QWidget { background-color: %s }' % self.class_color[2])
        self.frame_4.setStyleSheet('QWidget { background-color: %s }' % self.class_color[3])
        self.frame_5.setStyleSheet('QWidget { background-color: %s }' % self.class_color[4])
        self.frame_6.setStyleSheet('QWidget { background-color: %s }' % self.class_color[5])
        self.frame_7.setStyleSheet('QWidget { background-color: %s }' % self.class_color[6])
        self.frame_8.setStyleSheet('QWidget { background-color: %s }' % self.class_color[7])
        self.frame_9.setStyleSheet('QWidget { background-color: %s }' % self.class_color[8])



        # 클래스 색 선택하기
        self.clickable(self.frame_1).connect(self.showDialog01)
        self.clickable(self.frame_2).connect(self.showDialog02)
        self.clickable(self.frame_3).connect(self.showDialog03)
        self.clickable(self.frame_4).connect(self.showDialog04)
        self.clickable(self.frame_5).connect(self.showDialog05)
        self.clickable(self.frame_6).connect(self.showDialog06)
        self.clickable(self.frame_7).connect(self.showDialog07)
        self.clickable(self.frame_8).connect(self.showDialog08)
        self.clickable(self.frame_9).connect(self.showDialog08)



    def clickableBtn2(self):
        movie = QMovie("/home/aiffel-dj60/aiffel/0.PythonQT_STUDY/image/simtodata/성능지표_영상.gif")
        # self.setStyleSheet("background:blue;")
        self.label_visualization.move(0, 50)
        self.label_visualization.resize(850, 600)
        self.label_visualization.setMovie(movie)
        self.label_visualization.setScaledContents(True)
        movie.start()

    def showDialog01(self):
        col = QColorDialog.getColor()
        if col.isValid():
            self.frame_1.setStyleSheet('QWidget { background-color: %s }' % col.name())
            self.class_color[0] = col.name()

    def showDialog02(self):
        col = QColorDialog.getColor()
        if col.isValid():
            self.frame_2.setStyleSheet('QWidget { background-color: %s }' % col.name())
            self.class_color[1] = col.name()
    def showDialog03(self):
        col = QColorDialog.getColor()
        if col.isValid():
            self.frame_3.setStyleSheet('QWidget { background-color: %s }' % col.name())
            self.class_color[2] = col.name()
    def showDialog04(self):
        col = QColorDialog.getColor()
        if col.isValid():
            self.frame_4.setStyleSheet('QWidget { background-color: %s }' % col.name())
            self.class_color[3] = col.name()
    def showDialog05(self):
        col = QColorDialog.getColor()
        if col.isValid():
            self.frame_5.setStyleSheet('QWidget { background-color: %s }' % col.name())
            self.class_color[4] = col.name()
    def showDialog06(self):
        col = QColorDialog.getColor()
        if col.isValid():
            self.frame_6.setStyleSheet('QWidget { background-color: %s }' % col.name())
            self.class_color[5] = col.name()
    def showDialog07(self):
        col = QColorDialog.getColor()
        if col.isValid():
            self.frame_7.setStyleSheet('QWidget { background-color: %s }' % col.name())
            self.class_color[6] = col.name()
    def showDialog08(self):
        col = QColorDialog.getColor()
        if col.isValid():
            self.frame_8.setStyleSheet('QWidget { background-color: %s }' % col.name())
            self.class_color[7] = col.name()
    def showDialog09(self):
        col = QColorDialog.getColor()
        if col.isValid():
            self.frame_9.setStyleSheet('QWidget { background-color: %s }' % col.name())
            self.class_color[8] = col.name()

    # 클래스 체크박스
    def groupchkFunction(self):
        if self.groupchk_1.isChecked():
            self.list_selected_class[0] = True
            print("groupchk_1 isChecked")
        else:
            self.list_selected_class[0] = False

        if self.groupchk_2.isChecked():
            self.list_selected_class[1] = True
            print("groupchk_2 isChecked")
        else:
            self.list_selected_class[1] = False

        if self.groupchk_3.isChecked():
            self.list_selected_class[2] = True
            print("groupchk_3 isChecked")
        else:
            self.list_selected_class[2] = False

        if self.groupchk_4.isChecked():
            self.list_selected_class[3] = True
            print("groupchk_4 isChecked")
        else:
            self.list_selected_class[3] = False
        if self.groupchk_5.isChecked():
            self.list_selected_class[4] = True
            print("groupchk_5 isChecked")
        else:
            self.list_selected_class[4] = False
        if self.groupchk_6.isChecked():
            self.list_selected_class[5] = True
            print("groupchk_6 isChecked")
        else:
            self.list_selected_class[5] = False
        if self.groupchk_7.isChecked():
            self.list_selected_class[6] = True
            print("groupchk_7 isChecked")
        else:
            self.list_selected_class[6] = False
        if self.groupchk_8.isChecked():
            self.list_selected_class[7] = True
            print("groupchk_8 isChecked")
        else:
            self.list_selected_class[7] = False
        if self.groupchk_9.isChecked():
            self.list_selected_class[8] = True
            print("groupchk_9 isChecked")
        else:
            self.list_selected_class[8] = False


    # 전치리 버튼 클릭시 josn -> png
    def preprocessingImage(self):


        # 선택된 클래스 리스트, 선택된 클래스의 달
        json2png_object.make_json2png(self.list_selected_class,self.class_color)

        #for i,v in enumerate(self.list_selected):
        #    dic_list_selected[i]=v
        print("10:{}, 20:{} 30:{} 40:{} 50:{} 60:{} 70:{} 80:{} 100:{}".format(self.list_selected_class[0], self.list_selected_class[1],
                                                                               self.list_selected_class[2],self.list_selected_class[3],
                                                                               self.list_selected_class[4],self.list_selected_class[5],
                                                                               self.list_selected_class[6],self.list_selected_class[7],
                                                                               self.list_selected_class[8]))



    #ListWidget의 시그널에 연결된 함수들
    def chkItemClicked(self) :
        print(self.listWidget_Test.currentItem().text())


    ######################################################################################
    def chkItemDoubleClicked(self) :
        text = self.listWidget_Test.currentItem().text()
        text,_ = text.split(".")
        text += ".png"
        #print(str(self.listWidget_Test.currentRow()) + " : " +text )

        josn2png_path = json2png_object.get_savepath() + text

        #print("chkItemClicked 테스트 : {}".format(josn2png_path))


        ## ui 보여주기 코드(원천데이터)
        text, _ = text.split("_FGT_1024")
        text += "_1024.png"
        #LC_AP_36603093_026_FGT_1024를  아래와 같이 변환해준다.
        # 'LC_AP_36603093_026_1024'.png


        #원본이미지
        self.qPixmapVar01 = QPixmap()
        self.qPixmapVar01.load(json2png_object.get_realpng_path() + text)
        self.label_picture01.setPixmap(self.qPixmapVar01.scaledToWidth(400))
        print("원천이미지 경로: {}".format(json2png_object.get_realpng_path() + text))

        #전처리된 이미지
        self.qPixmapVar02 = QPixmap()
        self.qPixmapVar02.load(josn2png_path)
        self.label_picture02.setPixmap(self.qPixmapVar02.scaledToWidth(400))
        print("save_dir_path: {}".format(josn2png_path))
        print("save_file_Exist?: {}".format(os.path.isfile(josn2png_path)))


        #LC_AP_36603093_026_1024
        #LC_AP_36603093_026_FGT_1024.png

        #save_dir_building_path = a.path + "/Preprocessing-main/sample/make_label/kor_buildings/"+text
        #save_dir_road_path = a.path + "/Preprocessing-main/sample/make_label/kor_roads/"+text
        #print("save_dir_building_path: {}".format(save_dir_building_path))
        #print("save_dir_road_path: {}".format(save_dir_road_path))
        #print("save_dir_building_path: {}".format(os.path.isfile(save_dir_building_path)))
        #print("save_dir_road_path: {}".format(os.path.isfile(save_dir_road_path)))

        """
        if(os.path.isfile(save_dir_building_path)):
            png_path = save_dir_building_path
            self.qPixmapVar02.load(png_path)
            self.label_picture02.setPixmap(self.qPixmapVar02)

        elif(os.path.isfile(save_dir_road_path)):
            png_path = save_dir_road_path
            self.qPixmapVar02.load(png_path)
            self.label_picture02.setPixmap(self.qPixmapVar02)
        else:
            print("전치리된 이미지 없다.")
            self.label_picture02.setText("전치리된 이미지 없다.")
        """
    def chkCurrentItemChanged(self) :
        print("Current Row : " + str(self.listWidget_Test.currentRow()))

    #항목을 추가, 삽입하는 함수들
    def addListWidget(self) :
        self.addItemText = self.line_addItem.text()
        self.listWidget_Test.addItem(self.addItemText)

    def insertListWidget(self) :
        self.insertRow = self.spin_insertRow.value()
        self.insertText = self.line_insertItem.text()
        self.listWidget_Test.insertItem(self.insertRow, self.insertText)

    #Button Function
    def printCurrentItem(self) :
        print(self.listWidget_Test.currentItem().text())

    def printMultiItems(self) :
        #여러개를 선택했을 때, selectedItems()를 이용하여 선택한 항목을 List의 형태로 반환받습니다.
        #그 후, for문을 이용하여 선택된 항목을 출력합니다.
        #출력할 때, List안에는 QListWidgetItem객체가 저장되어 있으므로, .text()함수를 이용하여 문자열로 변환해야 합니다.
        self.selectedList = self.listWidget_Test.selectedItems()
        for i in self.selectedList :
            print(i.text())

    def removeCurrentItem(self) :
        #ListWidget에서 현재 선택한 항목을 삭제할 때는 선택한 항목의 줄을 반환한 후, takeItem함수를 이용해 삭제합니다. 
        self.removeItemRow = self.listWidget_Test.currentRow()
        self.listWidget_Test.takeItem(self.removeItemRow)

    def clearItem(self) :
        self.listWidget_Test.clear()

    #https://developer-mistive.tistory.com/55
    # 클릭할수 없었던 위젯 클릭하는법
    def clickable(self,widget):

        class Filter(QObject):

            clicked = pyqtSignal()  # pyside2 사용자는 pyqtSignal() -> Signal()로 변경

            def eventFilter(self, obj, event):

                if obj == widget:
                    if event.type() == QEvent.MouseButtonRelease:
                        if obj.rect().contains(event.pos()):
                            self.clicked.emit()
                            # The developer can opt for .emit(obj) to get the object within the slot.
                            return True

                return False

        filter = Filter(widget)
        widget.installEventFilter(filter)
        return filter.clicked

if __name__ == "__main__" :
    json2png_object = Json2Png()
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
