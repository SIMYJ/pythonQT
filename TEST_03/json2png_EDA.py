import os , glob
import cv2
import numpy as np
from PIL import Image
import math
import json


# 파이썬 디렉토리 처리 총정리
# https://ddolcat.tistory.com/654


class Json2Png:

    def __init__(self):
        os.chdir("../")
        self.path =os.getcwd()
        print("기본경로: {} ".format(self.path))

        self.label_dict = {}

        #json 폴더 경로
        self.path_json_dir = self.path + "/토지_피복지도_항공위성_이미지_강원_및_충청/1.라벨링데이터/2.항공사진_Fine_1024픽셀/2.Ground_Truth_JSON_전체/"
        print("json 폴더경로 : {}".format(self.path_json_dir))

        # 메타데이터 폴더경로
        path_meta_dir = self.path + "/토지_피복지도_항공위성_이미지_강원_및_충청/1.라벨링데이터/2.항공사진_Fine_1024픽셀/4.메타데이터/"

        ## 메타데이터 경로+ 파일명
        self.list_meta_files = glob.glob(path_meta_dir + '*.json')# 모든 json파일 목록 수집
        print('self.list_meta_files: {}'.format(self.list_meta_files))
        self.list_meta_files.sort()

        #read json folder
        list_file = os.listdir(self.path_json_dir)
        self.list_file_name = [ file for file in list_file if file.endswith(".json")]
        self.list_file_name.sort() # 정렬
        print("JSON파일명 리스트출력 : {}".format(self.list_file_name))


        # 체크박스 체크 여부 True, False
        self.ann_cd_check=[False,False,False,False,False,False,False,False,False,False,False]



    def json2polygon(self,json_file, list_selected,meta_coordinatesXY):
    #def parse_json(self,json_file, list_selected):

        polygon_double_list = [[], [], [], [], [], [], [], [], []] #초기화

        for i, info in enumerate(json_file['features']):
            # print(i)
            ann_cd = json_file['features'][i]['properties']['ANN_CD']

            if (ann_cd == 10 and list_selected[0] == True):
                polygon_double_list[0].append(self.makePolygon(json_file['features'], i,meta_coordinatesXY))
                self.ann_cd_check[0]= True
                print("10실행{}".format(10))
            if (ann_cd == 20 and list_selected[1] == True):
                polygon_double_list[1].append(self.makePolygon(json_file['features'], i,meta_coordinatesXY))
                self.ann_cd_check[1]= True
                print("10실행{}".format(20))
            if (ann_cd == 30 and list_selected[2] == True):
                polygon_double_list[2].append(self.makePolygon(json_file['features'], i,meta_coordinatesXY))
                self.ann_cd_check[2]= True
                print("10실행{}".format(30))
            if (ann_cd == 40 and list_selected[3] == True):
                polygon_double_list[3].append(self.makePolygon(json_file['features'], i,meta_coordinatesXY))
                self.ann_cd_check[3]= True
                print("10실행{}".format(40))
            if (ann_cd == 50 and list_selected[4] == True):
                polygon_double_list[4].append(self.makePolygon(json_file['features'], i,meta_coordinatesXY))
                self.ann_cd_check[4]= True
                print("10실행{}".format(50))
            if (ann_cd == 60 and list_selected[5] == True):
                polygon_double_list[5].append(self.makePolygon(json_file['features'], i,meta_coordinatesXY))
                self.ann_cd_check[5]= True
                print("10실행{}".format(60))
            if (ann_cd == 70 and list_selected[6] == True):
                polygon_double_list[6].append(self.makePolygon(json_file['features'], i,meta_coordinatesXY))
                self.ann_cd_check[6]= True
                print("10실행{}".format(70))
            if (ann_cd == 80 and list_selected[7] == True):
                polygon_double_list[7].append(self.makePolygon(json_file['features'], i,meta_coordinatesXY))
                self.ann_cd_check[7]= True
                print("10실행{}".format(80))
            if (ann_cd == 100 and list_selected[8] == True):
                polygon_double_list[8].append(self.makePolygon(json_file['features'], i,meta_coordinatesXY))
                self.ann_cd_check[8]= True
                print("10실행{}".format(100))


                # 숫자
                #label = int(feature['properties']['ANN_CD'])
                #label_list.append(label)


                #if label not in self.label_dict:
                    #self.label_dict[label] = feature['properties']['ANN_NM']



        return polygon_double_list #, label_list

    def makePolygon(self, json_file_features, num,meta_coordinatesXY):
        polygon=[]

        for list_xy in json_file_features[num]['geometry']['coordinates']:
            for x_y in list_xy:
                # ­ 이미지 좌표계 EPSG(European Petroleum Survey Group) 코드는 전세계 좌표계 정의에
                # 대한 고유 명칭을 뜻하며, 그 중 EPSG:5186는 GRS80 타원체의 한국 중부원점, X축으로
                # 200,000미터, Y축으로 600,000미터만큼 이동시킨 좌표계를 나타냄
                # ­ 좌상단 좌표는 학습용 이미지 데이터의 좌상단 X, Y 좌표를 나타냄

                metaX = meta_coordinatesXY[0]
                metaY = meta_coordinatesXY[1]

                polygon.append((x_y[0] - float(metaX))*2)
                polygon.append((float(metaY) - x_y[1])*2 )
                #print("polygon_double_list값:({},{}), ({},{}):".format(x_y[0],x_y[1] , metaX,metaY))

        polygon = list(map(math.floor, polygon))
        polygon = np.array(polygon, np.int32).reshape(-1, 1, 2)
        #print(polygon_list)
        return polygon


    def draw_label(self, polygon_double_list,filename,class_color,list_selected ):

        savepath = self.get_savepath()
        image = np.zeros((1024, 1024, 3), np.uint8)

        if (list_selected[0] == True and self.ann_cd_check[8] == True):
            image = cv2.fillPoly(image, polygon_double_list[8], self.hex_to_rgb(class_color[8]))
        if(list_selected[0]== True and self.ann_cd_check[0] == True):
            image = cv2.fillPoly(image, polygon_double_list[0], self.hex_to_rgb(class_color[0]))
            print("polygon_double_list값{}:".format(polygon_double_list))
        if (list_selected[0] == True and self.ann_cd_check[1] == True):
            image = cv2.fillPoly(image, polygon_double_list[1], self.hex_to_rgb(class_color[1]))
        if (list_selected[0] == True and self.ann_cd_check[2] == True):
            image = cv2.fillPoly(image, polygon_double_list[2], self.hex_to_rgb(class_color[2]))
        if (list_selected[0] == True and self.ann_cd_check[3] == True):
            image = cv2.fillPoly(image, polygon_double_list[3], self.hex_to_rgb(class_color[3]))
        if (list_selected[0] == True and self.ann_cd_check[4] == True):
            image = cv2.fillPoly(image, polygon_double_list[4], self.hex_to_rgb(class_color[4]))
        if (list_selected[0] == True and self.ann_cd_check[5] == True):
            image = cv2.fillPoly(image, polygon_double_list[5], self.hex_to_rgb(class_color[5]))
        if (list_selected[0] == True and self.ann_cd_check[6] == True):
            image = cv2.fillPoly(image, polygon_double_list[6], self.hex_to_rgb(class_color[6]))
        if (list_selected[0] == True and self.ann_cd_check[7] == True):
            image = cv2.fillPoly(image, polygon_double_list[7], self.hex_to_rgb(class_color[7]))



        img = Image.fromarray(image)

        # json확장자 제거
        filename, _ = filename.split(".")
        img.save(f'{savepath}{filename}.png')
        print(f'{savepath}{filename}.png saved!')



    def make_json2png(self, list_selected, class_color):


        for i,filename in enumerate(self.list_file_name):

            print('self.list_meta_files[i]{}'.format(self.list_meta_files[i]))
            with open(self.list_meta_files[i],'r', encoding='cp949') as f01:
                meta_file = json.load(f01)
                meta_coordinatesXY=meta_file[0]["coordinates"].split(',')


                print("meta_coordinatesXY: {}{} :출력".format(meta_coordinatesXY[0],meta_coordinatesXY[1]))

            json_path = self.path_json_dir + filename
            with open(json_path) as f02:
                # print(f)
                json_file = json.load(f02)
                # k=k+1
                # print(k)

                (polygon_double_list) = self.json2polygon(json_file, list_selected, meta_coordinatesXY)
            self.draw_label(polygon_double_list, filename,  class_color, list_selected)



    def get_savepath(self):
        return self.path + '/토지_피복지도_항공위성_이미지_강원_및_충청/1.라벨링데이터/2.항공사진_Fine_1024픽셀/5.Ground_Truth_PNG_전체/'

    # (180, 251, 184) RGB 값 <-> : # B4FBB8(16 진 코드) 변환하기
    def hex_to_rgb(self, value):
        value = value.lstrip('#')
        lv = len(value)
        return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

    #원천데이터 실제
    def get_realpng_path(self):
        return self.path + "/토지_피복지도_항공위성_이미지_강원_및_충청/2.원천데이터/2.항공사진_Fine_1024픽셀/"



