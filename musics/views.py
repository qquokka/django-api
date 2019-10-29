from django.shortcuts import render, get_object_or_404
from .models import Music
from rest_framework.decorators import api_view
from .serializers import MusicSerializers
from rest_framework.response import Response


@api_view(['GET'])  # http method의 GET요청을 의미
def index(request):
    musics = Music.objects.all()
    serializer = MusicSerializers(musics, many=True)
    # 쿼리 셋이라 many=True 안 하면 어트리뷰트가 없다고 에러남 그래서 많이 가지고 있다고 붙여주는 거임(?)
    return Response(serializer.data)

@api_view(['GET'])
def detail(request, music_pk):
    music = get_object_or_404(Music, pk=music_pk)
    serializer = MusicSerializers(music)
    # 쿼리셋이 아니라 단이 ㄹ오브젝트라 매니는트류 필요없ㅇ므
    return Response(serializer.data)