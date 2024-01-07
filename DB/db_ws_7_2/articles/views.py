from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Article
from .serializers import ArticleListSerializer, ArticleSerializer

# 조회 & 생성 (pk 필요 없을 때)
@api_view(['GET', 'POST'])
# 전체 조회 한 후에 변환기를 통해서 변환해주고 반환
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        # 단일 데이터가 아닌 경우에는 many = True로 바꿔줘야함
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 조회 & 삭제 & 수정 (pk 필요 할 때)
@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    # NO_CONTENT : 삭제 성공해서 코드가 읍다
    elif request.method == 'DELETE':
        article.delete()
        return Response({'성공적으로 삭제'}, status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)