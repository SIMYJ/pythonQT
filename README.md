# PythonQT

---
##[가상환경 설정 및 개발환경 설치 바로가기(파이참)](https://github.com/SIMYJ/pythonQT/tree/syj/%ED%8C%8C%EC%9D%B4%EC%B0%B8-%EA%B0%80%EC%83%81%ED%99%98%EA%B2%BD%20%EC%84%A4%EC%A0%95)
---
## 1. PythonQT(PyQt) 소개
- PythonQT는 Qt의 레이아웃에 Python의 코드를 연결하여 GUI 프로그램을 만들 수 있게 해주는 프레임워크이다.
- PyQt는 C++의 Cross Platform GUI Framework인 Qt를 영국의 Riverbank Computing에서 Python 모듈로 변환해주는 툴을 만들어주며 시작되었습니다. 현재는 PyQt4버전과 PyQt5버전이 주로 사용되고 있습니다.
- 파이썬에는 여러가지 GUI 프레임워크가 존재한다.(PyGTK, PySide, Tkinter등) 이런 GUI프레임워크는 사용하기 어렵고, 시각적으로 예쁘지 않다.
- GPL과 상업용 라이센스 중 하나를 선택할 수 있다.
- 윈도우, 리눅스, macOS, 안드로이드, iOS를 지원한다.

```
리눅스 PythonQT(PyQt) 설치
$ pip3 install pyqt5  
$ sudo apt install python3-pyqt5  
$ sudo apt install pyqt5-dev-tools
$ sudo apt install qttools5-dev-tools

https://reason1241.tistory.com/32


qtdesigner실행 명령어 :  $designer

```



PyQt5가 현재 있는 최신 버전이고, PyQt4와 조금 차이가 있을 수 있으므로, PyQt5를 설치하시는 것을 권장합니다. 그리고 참고로, 파이썬[Python]의 경우 3.4이상 버전을 사용하셔야 합니다. 
```

QT는 무엇인가??
Qt는 컴퓨터 프로그래밍에서 GUI 프로그램 개발에 널리 쓰이는 크로스 플랫폼 프레임워크이다. 
```
QT정의 : https://ko.wikipedia.org/wiki/Qt_(%EC%86%8C%ED%94%84%ED%8A%B8%EC%9B%A8%EC%96%B4)

## 2. 개발환경

### 1). Qt Designer
- PyQt는 다른 Framework들과 다르게 시각적으로도 괜찮은 디자인을 보여주면서 **Qt Designer**라는 프로그램을 이용하여 프로그램을 손쉽게 설계할 수 있다는 장점이 있습니다.


### 2). 파이참(PyCharm)
- 파이썬 개발에 가장 널리 사용되는 통합 개발 환경(IDE, Integrated Development Environment) 또는 개발 도구 이다.
- 통합 개발 환경(IDE)은 코드 편집기, 디버거, 컴파일러, 인터프리터 등을 포함한다. 또한 자동 완성, 검색 등의 다양한 기능을 제공한다.
- 체코 회사인 jetbrains(젯브레인즈)에서 개발되었다.

```
리눅스 파이참 설치 : https://enant.tistory.com/10
윈도우 파이참 설치 : https://www.crocus.co.kr/1659

리눅스 파이참 실행 명령어 : $pycharm-community

```
### 3). 아나콘다(Ananconda)
- 가상환경을 만들어 필요한 패키지들을 설치하고, 가상환경 안에서 자기 입맛에 맞게 개발환경을 조성할 수 있다.
- 아나콘다에서는 파이썬에서 중요 사용되는 라이브러리가 자동으로 설치 되어 있다.
- 데이터사이언스(수학과 과학 분야)에서 사용되는 여러 패키지(넘파이,사이파이)들을 가지고 있는 종합적인 플랫폼( 패키지를 묶어 놓은 파이썬 배포판)


### 4). 프로젝트 가상환경
#### Python에서의 가상 환경이란?
파이썬에서는 한 라이브러리에 대해 하나의 버전만 설치가 가능하다.여러개의 프로젝트를 진행하게 되면 이는 문제가 된다. 작업을 바꿀때마다 다른 버전의 라이브러리를 설치해야된다..이를 방지하기 위한 격리된 독립적인 가상환경을 제공한다.일반적으로 프로젝트마다 다른 하나의 가상환경을 생성한 후 작업을 시작한다.
#### 가상환경의 대표적인 모듈은 3가지
- <del>venv : Python 3.3 버전 이후 부터 기본모듈에 포함됨</del>
        - venv 모듈은 pyenv의처 버그로 인해, 제가 현재 작성할 환경 제공 안함
- virtualenv : Python 2 버전부터 사용해오던 가상환경 라이브러리, Python 3에서도 사용가능
- conda : Anaconda Python을 설치했을 시 사용할 수있는 모듈
- pyenv : pyenv의 경우 Python Version Manger임과 동시에 가상환경 기능을 플러그인 형태로 제공      

파이썬 가상환경 : https://wikidocs.net/16402

