1. user 모델을 직접 참조하는건 좋지 않음
accounts에 user를 아직 만들지 못했을 때 불러오려고 하면 문제가 생길 수 있음
from django.conf import settings -> settings.AUTH_USER_MODEL으로 사용

2. model에 user도 같이 출력되기 때문에 form에서 user 제외시킴
fields = ('content', 'title') or exclude('user')

3. create view 함수 수정 
article = form.save(commit=False)
article.user = requset.user
form.save()