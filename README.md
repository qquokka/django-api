덤프뜬다: 복제한다

```
python manage.py dumpdata musics > musics.json
python manage.py dumpdata --indent 2 musics > musics.json
```

로드데이터: 데이터 로드한다(가져온다?)

픽스쳐스 폴더안에 제이슨 파일을 넣는다.

우리가 가진 오브젝트를 제이슨으로 만들어주는ㅇ ㅐ 시리얼라이저

many=True 많은 애임

포스트맨 가장 기본적이 ㄴgui 툴

리뷰 쓰고 포스트맨으로 확인할 거임

래스트??

아래와 같은 구조를 restful architecture

자원 uri 행위 http method 표현 representaions(json, html, ...)

GET reviews/ 리뷰 목록

POST reviews/  리뷰 등록

GET reviews/1/ 1번 리뷰 가져오기

PUT reviews/1/ 1번 리뷰 수정하기

DELETE reivews/1/ 1번 리뷰 삭제하기



gui 대표적인거 윈도우 그래픽 유저 인터페이스

폴더를 열고 들어가고 이런 게 다 그래픽으로 이루어지기 때문

cli(command line interface)와 반대 개념

GUI - 그래픽으로 유저랑 상호작용하는 인터페이스

CLI - 명령어 인터페이스

API(Application Programming Interface) - 프로그래밍으로 하는 인터페이스. 프로그래밍으로 어떤 정보를 가져갈 수 있는 어떤.. 방법...??? 정도?



다음과 같이 validator를 이용하면 입력받을 때 검증할 수 있다. (시험에는 나오지 않음)

```
# models.py

from django.db import models
from django.core.validators import MinValueValidator, EmailValidator

class Person(models.Model):
	name = models.CharField(max_length=10)
    age = models.IntegerField(
        validators=[MinValueValidator(20, message='미성년자 출입금지')]
    )
    email = models.CharField(
    	max_length=20,
    	validators=[EmailValidator(message='이메일 형식이 아닙니다.')]
    )
```

