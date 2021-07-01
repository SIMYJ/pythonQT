# 02.07 Input - QLineEdit
- QLineEdit이란, 한줄짜리 글자를 입력받을 수 있는 입력위젯입니다. 위젯을 더블클릭하여 기본적으로 입력될 글자를 미리 입력해놓을 수도 있습니다. 다른 위젯들과 마찬가지로 Widget Window에서 끌어와 사용할 수 있습니다. LineEdit을 추가한 후 Property Editor에서 반드시 ObjectName을 본인이 기억하기 쉬운 이름으로 바꿔주시기 바랍니다.

## QLineEdit의 시그널과 활용예시
- QLineEdit의 시그널에 대해서 알아보도록 하겠습니다. QLineEdit에서는 LineEdit의 글자가 바뀔 때 마다 기능을 수행하는 시그널과 Return키(Enter키)가 눌렸을 때 기능을 수행하는 시그널이 있습니다

``` python
LineEdit의 글자가 바뀔 때 기능 실행
 - self.LineEdit이름.textChanged.connect(함수)

LineEdit에서 Return키(Enter키)가 눌렸을 때 기능 실행
- self.LineEdit이름.returnPressed.connect(함수)


```

