# PythonQT-TEST_03


## 간략한 설명
-   json → png(라벨) 변환 기능
-   png 색상 선택 기능
-   json annotation 클래스별 선택 기능

## 1.원천이미지 출력 
<img src = "https://i.imgur.com/4xD2NJr.gif" width="400">      

## 2.json → png(라벨) 어노테이션 전처리       
### 2.1. 어노테이션 전처리시( 로그출력)       
<img src = "https://i.imgur.com/DI9maF0.gif" width="400">           

### 2.2. 어노테이션 전처리 시(파일 생성)       

<img src = "https://i.imgur.com/2wwW4Oc.gif" width="400">            


### 2.3. 어노테이션 8종에 대한 전처리된 파일 출력     

<img src = "https://i.imgur.com/jgFIRZ2.gif" width="400">     


### 2.4. 어노테이션 3종(건물, 가로수, 논)에 대한 전처리된 파일 출력      
<img src = "https://i.imgur.com/sfTkV4E.gif" width="400">        


## 3. 어노테이션 색 선택하기       
<img src = "https://i.imgur.com/Fiu2iZ1.gif" width="400">     





## 프로젝트 구성


```txt
/pythonQT
	/토지_피복지도_항공위성_이미지_강원_및_충청
		      
          /1.라벨링데이터 
	  	/2.항공사진_Fine_1024픽셀
                    /1.Ground_Truth_Tiff                  # 원래 tif파일만 존재했음 + 원본이미지에 대한 png파일 임의로  만듬
	                	/2.Ground_Truth_JSON_전체              # 시용 안함
                    /2.Ground_Truth_JSON_전체              # 전처리에 사용할 JSON파일 디렉토리
                    /4.메타데이터                           # coordinates 계산을 위해 사용됨
                    /5.Ground_Truth_PNG_전체               # 전처리 작업 후 저장경로 디렉토리
				
	/TEST_03
		/json2png_EDA.py          # JSON-> PNG전처리 파일
		/listwidgetTest.ui        # UI파일
		/listwidgetTest.py        # UI구현 코드
		/making_label.py          # 사용안함(전 TEST_01코드)
```




