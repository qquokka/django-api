from rest_framework import serializers
from .models import Music

# serializer: 우리가 가진 데이터를 json 파일로 만들어주는 것

class MusicSerializers(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ('id', 'title', 'artist_id')