import os
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
        self.path_json_dir = self.path + "/json2png_sample/building_and_road_label_json_val/"
        print("json 폴더경로 : {}".format(self.path_json_dir))

        #read json folder
        list_file = os.listdir(self.path_json_dir)
        self.list_file_name = [ file for file in list_file if file.endswith(".json")]
        self.list_file_name.sort() # 정렬
        print("JSON파일명 리스트출력 : {}".format(self.list_file_name))

    #
    # 'building_imcoords'
    def parse_json(self,json_file, num_class):

        if(num_class==0):
            imcoords='building_imcoords'
        elif(num_class==1):
            imcoords = 'road_imcoords'
        polygon_list = []
        label_list = []
        for feature in json_file['features']:
            if feature['properties'][imcoords] and feature['properties'][imcoords]!='EMPTY':

                polygon = list(map(float, feature['properties'][imcoords].split(',')))
                polygon = list(map(math.floor, polygon))
                polygon = np.array(polygon, np.int32).reshape(-1, 1, 2)
                polygon_list.append(polygon)

                label = int(feature['properties']['type_id'])
                label_list.append(label)

                if label not in self.label_dict:
                    self.label_dict[label] = feature['properties']['type_name']

        return polygon_list, label_list


    def draw_label(self, polygon_list,filename,num_class,class_color ):

        savepath = self.get_savepath()
        image = np.zeros((1024, 1024, 3), np.uint8)

        if(num_class==0):
            img = cv2.fillPoly(image, polygon_list, self.hex_to_rgb(class_color[0]))
        elif(num_class==1):
            img = cv2.fillPoly(image, polygon_list, self.hex_to_rgb(class_color[1]))


        img = Image.fromarray(img)

        # json확장자 제거
        filename, _ = filename.split(".")
        img.save(f'{savepath}{filename}.png')
        print(f'{savepath}{filename}.png saved!')


    # list_selected[0] =>T/F buiding
    # list_selected[1] =>T/F road
    def make_json2png(self, list_selected, class_color):

        for i,v in enumerate(list_selected):
            if(v == True):
                # 현재는 단일 클래스 표현
                # num_class 0 => 빌딩
                # num_class 1 => 로드
                num_class = i
                for filename in self.list_file_name:
                    json_path = self.path_json_dir + filename
                    with open(json_path) as f:
                        # print(f)
                        json_file = json.load(f)
                        # k=k+1
                        # print(k)

                        # 현재는 단일 클래스 표현이여서 num_class 한개만 넘겨준다.
                        (polygon_list, a) = self.parse_json(json_file,num_class)
                    self.draw_label(polygon_list, filename,num_class,class_color)



    def get_savepath(self):
        return self.path + '/json2png_sample/building_and_road_save_png/label/'

    # (180, 251, 184) RGB 값 <-> : # B4FBB8(16 진 코드) 변환하기
    def hex_to_rgb(self, value):
        value = value.lstrip('#')
        lv = len(value)
        return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))
