# PythonQT-TEST01


## 위키독스 참조 소스
 - [02.15 Pixmap](https://github.com/SIMYJ/pythonQT/tree/syj/%5B%EC%9C%84%ED%82%A4%EB%8F%85%EC%8A%A4%5DPyQt5_for_Beginner/02.15%20Pixmap) 
 - [02.18 List Widget](https://github.com/SIMYJ/pythonQT/tree/syj/%5B%EC%9C%84%ED%82%A4%EB%8F%85%EC%8A%A4%5DPyQt5_for_Beginner/02.18%20List%20Widget)

## 간략한 설명
- 그레이스케일 이미지에서 roads,buildings 따로 추출해서 저장하고, 각 이미지 화면에 출력한다.

## UI 
<img src = "https://i.imgur.com/vc4IHnG.png" width="500px">     

<img src = "https://i.imgur.com/C4yb6El.gif" width="500px">



## 프로젝트 구성

- 0.KD_hackathon/Preprocessing-main 은 제공하지 않음
- TEST/~ 만 업로드함

```txt
/0.KD_hackathon
	/Preprocessing-main
		/sample
		/gtFine
			/train
				/LC_AP_37607046_004_1024.png 대량
			/val
				/LC_AP_37714010_023_1024.png 소량
		/make_label
			/kor_buildings
				/전치리된 파일.png
			/kor_roads
				/전치리된 파일.png
			/kor_multi
				/X -> 아직 구현 안함
				
	/TEST
		/listwidgetTest.py
		/listwidgetTest.ui
		/Preprocessing.py
```






