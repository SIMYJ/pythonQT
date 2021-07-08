
# 가상환경 설정(파이참 설치 전제)


## 가상환경 생성 및 필요 패키지 설치
```
conda create -n 가상환경이름 python=3.7 numpy pillow scikit-learn tqdm matplotlib opencv

```

## 가상환경 접속 및 파이참 실행
```
conda activate 가상환경이름

pycharm-community

```

### 생성된 가상환경 파이참 연결하기
<img src="blob:https://imgur.com/97f5b85d-ef44-4db4-b118-06580469e3ba" width="400px">


### 추가로 설치할 패키지
```
pip install visidom  
pip install torch   
pip install torchvision 
```


## 끝!





## 추가 정보

-matplotlib에 qt패키지 포함되어 있다.      
<img src="blob:https://imgur.com/d3246c08-92fa-476f-8fd6-67fcc99d7d06" width="300px">


- apt-get명령어 : [](https://luckeex.tistory.com/290)
- pip install과 apt-get install의 차이는? pip와 pip3는 뭐가 다르지? : [](https://bskyvision.com/686)
- 리눅스 패키지 설치 : https://daewonyoon.tistory.com/311
```
conda install 로 설치해본다.
conda install -c conda-forge 명령으로 설치해 본다.
인터넷에서 anaconda + 패키지명 으로 검색하여, anaconda.org 사이트 페이지가 검색되면, 검색페이지에서 소개하는 채널을 이용하여 conda install -c <channal> 명령으로 설치한다.
위 모든 것이 실패하였을 때에, pip install 한다.
pip install 시 디펜던시로 설치된 패키지들 중에 conda install 이 가능한 패키지가 있다면, pip uninstall 한 후에 conda install 로 다시 설치한다.
```

