from .models import Music
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import MusicSerializer, MusicListSerializer
from django.shortcuts import get_object_or_404
from rest_framework import status

@api_view(['GET', 'POST'])
def music_list(request):
    musics = Music.objects.all()
    if request.method == 'GET':
        serializers = MusicListSerializer(musics, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializers = MusicListSerializer(data=request.data)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        

@api_view(['GET', 'PUT', 'DELETE'])
def music_detail(request, music_pk):

    music = get_object_or_404(Music, pk=music_pk)
    if request.method == 'GET':
        serializers = MusicSerializer(music)
        return Response(serializers.data, status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        serializers = MusicSerializer(music, data=request.data)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)

    elif request.method == 'DELETE':
        music.delete()
        data = {
            'delete': f'음악 {music_pk}번이 삭제되었습니다.',
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)