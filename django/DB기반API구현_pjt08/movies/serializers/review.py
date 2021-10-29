from rest_framework import serializers
from ..models import Movie, Review, Actor

class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('pk', 'title', )


# class ReviewSerializer(serializers.ModelSerializer):
#     class MovieSerializer(serializers.ModelSerializer):
#         class ActorSerializer(serializers.ModelSerializer):
#             class Meta:
#                 model = Actor
#                 fields = '__all__'
#         actors = ActorSerializer(many=True, read_only=True)

#         class Meta:
#             model = Movie
#             fields = '__all__'

#     movie = MovieSerializer(read_only=True)
#     class Meta:
#         model = Review
#         fields = '__all__'



class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'
        
class ReviewSerializer(serializers.ModelSerializer):

    movie = MovieSerializer(read_only=True)
    class Meta:
        model = Review
        fields = '__all__'