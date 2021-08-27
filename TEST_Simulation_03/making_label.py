import os
import cv2
import numpy as np
from PIL import Image


# 파이썬 디렉토리 처리 총정리
# https://ddolcat.tistory.com/654
class Preprocessing:



    def __init__(self,path=None,list_files_name = None,png_dir_path =None):
        os.chdir("../")
        #path = os.getcwd()
        print("기본경로: {} ".format(path))
        self.path =os.getcwd()

        self.png_dir_path =self.path+ "/Preprocessing-main/sample/gtFine/train/train/"
        print("label_PNG파일 폴더경로 : {}".format(self.png_dir_path))

        list_file = os.listdir(self.png_dir_path)
        self.list_files_name = [ file for file in list_file if file.endswith(".png")]
        print("label_PNG파일 리스트출력 : {}".format(self.list_files_name))





    ## image_
    def kor_make_label(self):

        png_dir_path = self.path + "/Preprocessing-main/sample/gtFine/train/train/"
        save_dir_building_path = self.path + "/Preprocessing-main/sample/make_label/kor_buildings/"
        save_dir_road_path = self.path + "/Preprocessing-main/sample/make_label/kor_roads/"
        save_dir_multi_path = self.path + "/Preprocessing-main/sample/make_label/kor_multi/"

        for filename in self.list_files_name :
            path = png_dir_path + filename
            #path값 : /home/aiffel/0.KD_hackathon/Preprocessing-main/sample/gtFine/train/train/LC_AP_37607046_004_1024.png
            print("path값 : {} ".format(path))
            #filename = os.path.splitext(os.path.basename(name))[0]
            img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
            # change label
            # building 128(회색)
            img[img == 10] = 128
            # road  255(흰색)
            img[img == 30] = 255
            # else
            img[img < 128] = 0

            # building 128(회색)
            if img in np.array(128):
                image = np.array(img)
                img2 = Image.fromarray(image)
                img2.save(f'{save_dir_building_path}{filename}')
                # img2.save(f'{save_dir_building_path}{filename}.png')

            # road  255(흰색)
            if img in np.array(255):
                image = np.array(img)
                img3 = Image.fromarray(image)
                img3.save(f'{save_dir_road_path}{filename}')
                #img3.save(f'{save_dir_road_path}{filename}.png')
            # multi
            if img in np.array(128) and img in np.array(255):
                image = np.array(img)
                img4 = Image.fromarray(image)
                img4.save(f'{save_dir_multi_path}{filename}.png')





"""
os.chdir("../")
path = os.getcwd()
print("기본경로: {} ".format(path))

png_dir_path = getPngFolder(path)
list_files_name = getPngList(png_dir_path)
list_files_name.sort()
print("sort된 파일리스트 : {}".format(list_files_name))

##kor_make_label(path,list_files_name)


 # Png 폴더경로 반환함수
    def getPngFolder(path):
        png_path = path

        png_path += "/Preprocessing-main/sample/gtFine/train/train/"
        print("label_PNG파일 폴더경로 : {}".format(png_path))
        return png_path

    # 인자로 폴더경로를 받아 폴더안에 png확장자 파일명 리스트로 반환함수
    def getPngList(path):
        image_folder = path
        file_list = os.listdir(image_folder)
        image_files = [file for file in file_list if file.endswith(".png")]
        print("label_PNG파일 리스트출력 : {}".format(image_files))
        return image_files



"""
