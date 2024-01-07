accounts -> 유저와 인증
articles -> 게시판 구현 
1. articles 모델에서 새로운 댓글 모델 생성 
2. N:1 관계에서는 모델은 참조하는 소문자 단수형(articles->article) 
만들어지는 필드는 article_id가 되므로 article_id로 만들면  article_id_id가 되요 조심 
3. Foriegnkey는 (참조할 클래스 모델 이름, on_delete=~)
- 1. cascade - 참조하는 객체도 삭제
- 2. protect - 댓글 달린 게시글 삭제 금지  

1번 댓글의 내용 -> 
comment.article_id
comment.article.pk

N ->1 (참조)
- 댓글이 어떤 게시글에 작성 되었는지를 조회 가능 

1 -> N (역참조)
- 게시글에 작성된 모든 댓글을 조회 -> all() 사용 
- article.comment_set.all() -> comment 는 지금 comment로 만들어서 임니다 

-----------------------------------------------------------------------

1. models.py에서 Comment model 만들어 주구요 
2. forms.py에서 CommentForm을 만들어 주구요 -> content만 표시되면 되구요
3. views.py -> main.html에서 댓글 제출 창 꾸며 주구요 
4. 댓글 제출하면 넘어가지는 페이지 만들기위해서 url 가주구요 view에서 함수 만들어주구요 
5. view 만들 때 임시로 인스턴스를 받아온 다음에 다시 저장?

6. 역참조로 댓글 읽기
7. 댓글 삭제 