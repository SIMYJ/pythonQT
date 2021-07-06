# PythonQT-TEST_02


##  참조 자료
 - https://codetorial.net/pyqt5/dialog/qcolordialog.html

## 간략한 설명
-   json → png(라벨) 변환 기능
-   png 색상 선택 기능
-   json annotation 클래스별 선택 기능

## UI 
<img src = "https://i.imgur.com/lowUCK0.gif">     





## 프로젝트 구성


```txt
/0.PythonQT_STUDY
	/json2png_sample
		/building_and_road_label_json_val # 빌딩과 로드이미지 이 폴더에 넣음(아래 2개의 파일을)
		/building_label_and_json_val      # 사용안함
		/road_label_json_val              # 사용안함
		/building_and_road_save_png
			/label                    # 전처리된 파일 저장

				
	/TEST_02
		/json2png_EDA.py          # JSON-> PNG전처리 class
		/listwidgetTest.ui        # UI파일
		/listwidgetTest.py        # UI구현 코드
		/making_label.py          # 사용안함(전 TEST_01코드)
```


## 생각할 부분

### 1.여러가지 데이터셋으로 돌린다.
- 라벨 클래스종류와 숫자가 다르다.(변수가 유동적이다.)
- 문제점: UI표현시 클래스 종류와 수 유동적으로 변화되어야됨

### 2. JSON→ PNG 변화 UI구현시

- 원본,뎁스,전처리된 세그멘테이션 3가지 이미지를 화면에 출력할것인가?    
(원본이미지출력시 JSON이 아닌 다른PNG로 출력/ 뎁스랑 세그멘테이션은 전처리파일 출력)

### 3.제공된 샘플JSON파일은 도로정보만,혹은 빌딩정보만 가지고 있다. 
- 하나의 JSON파일에 도로,빌딩 모두 넣어도 되는가?




