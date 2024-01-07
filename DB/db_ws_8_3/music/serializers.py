from rest_framework import serializers
from .models import Music, Comment


class MusicListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ("id", "title")


class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = "__all__"

class CommentSerializer(serializers.ModelSerializer):
    class MusicSerializer(serializers.ModelSerializer):
        class Meta:
            model = Music
            fields = "__all__"
    
    music = MusicSerializer(read_only=True)
    
    class Meta:
        model = Comment
        fields = '__all__'
