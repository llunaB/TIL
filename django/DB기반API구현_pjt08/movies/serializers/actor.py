from rest_framework import serializers
from ..models import Actor, Movie

class ActorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ('pk', 'name', )


class ActorSerializer(serializers.ModelSerializer):
    ##
    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('pk', 'title')
    movies = MovieSerializer(many=True, read_only=True)
        
    class Meta:
        model = Actor
        fields = '__all__'

