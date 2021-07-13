# PythonQT-TEST_Simulation_02


## 간략한 설명
-   json → png(라벨) 변환 기능
-   png 색상 선택 기능
-   json annotation 클래스별 선택 기능


## 0. 3종기능 
<img src = "https://i.imgur.com/bSzUcyI.gif" width="400">      



## 1.DATA SPOON

<img src = "https://i.imgur.com/oPhMYA3.png" width="500">      

## 2. Simulation settings
       
<img src = "https://i.imgur.com/wAW3GAo.png" width="500">           


## 2. Visualization
      
<img src = "https://i.imgur.com/nSQ79uh.png" width="500">           






## 프로젝트 구성


```txt
/pythonQT
	/토지_피복지도_항공위성_이미지_강원_및_충청
		      
          /1.라벨링데이터 
	  	/2.항공사진_Fine_1024픽셀
                    /1.Ground_Truth_Tiff                  # 원래 tif파일만 존재했음 + 원본이미지에 대한 png파일 임의로  만듬
	            /2.Ground_Truth_JSON_전체              # 전처리에 사용할 JSON파일 디렉토리
                    /3.Ground_Truth_JSON_항목별              # 시용 안함
                    /4.메타데이터                           # 메타데이터 (coordinates 계산을 위해 사용됨)
                    /5.Ground_Truth_PNG_전체               # 전처리 작업 후 저장경로 디렉토리
				
	/TEST_Simulation_02
		/json2png_EDA.py          # JSON-> PNG전처리 파일
		/Sim2data.ui              # UI파일
		/Sim2data.ui.py           # UI구현 코드
		/making_label.py          # 사용안함(전 TEST_01코드)
```




