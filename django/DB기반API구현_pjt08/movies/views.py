from django.shortcuts import get_list_or_404, get_object_or_404, render
from movies.serializers.actor import ActorListSerializer, ActorSerializer
from movies.serializers.movie import MovieSerializer, MovieListSerializer
from movies.serializers.review import ReviewSerializer
from .models import Actor, Movie, Review
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET', 'POST'])
def actor_list_or_create(request):
    def create_actor():
        
        return 
    def actor_list():
        actors = Actor.objects.all()
        serializer = ActorListSerializer(actors, many=True)
        return Response(serializer.data)

    if request.method == 'GET':
        return actor_list()
    elif request.method == 'POST':
        return create_actor()


@api_view(['GET', 'PUT', 'DELETE'])
def actor_detail_or_update_or_delete(request, actor_pk):
    actor = get_object_or_404(Actor, pk=actor_pk)
    def actor_detail():
        serializer = ActorSerializer(actor)
        return Response(serializer.data)
    def update_actor():
        return 
    def delete_actor():
        return 
    if request.method == 'GET':
        return actor_detail()
    elif request.method == 'PUT':
        return update_actor()
    if request.method == 'DELETE':
        return delete_actor()


@api_view(['GET', 'POST'])
def movie_list_or_create(request):
    def movie_list():
        movies = Movie.objects.all()
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)
    def create_movie():
        return 
    if request.method == 'GET':
        return movie_list()
    if request.method == 'POST':
        return create_movie()
    

@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail_or_update_or_delete(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    def movie_detail():
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    def update_movie():
        return 
    def delete_movie():
        return 
    if request.method == 'GET':
        return movie_detail()
    elif request.method == 'PUT':
        return update_movie()
    if request.method == 'DELETE':
        return delete_movie()


@api_view(['GET', 'POST'])
def movie_review_list_or_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    def create_review():
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie)
            return Response(serializer.data)
    def review_list():
        reviews = Review.objects.filter(movie=movie)
        # reviews = get_list_or_404(Review) 모든 리뷰 다 나옴
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        return create_review()
    if request.method == 'GET':
        return review_list()


@api_view(['GET', 'POST'])
def review_list_or_create(request):
    def review_list():
        reviews = get_list_or_404(Review)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
    def create_review():
        pass
    if request.method == 'POST':
        return create_review()
    if request.method == 'GET':
        return review_list()


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail_or_update_or_delete(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    def review_detail():
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    def update_movie():
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    def delete_movie():
        review.delete()
        data ={
            'message': '삭제되었습니다.'
        }
        return Response(data)
    if request.method == 'GET':
        return review_detail()
    elif request.method == 'PUT':
        return update_movie()
    if request.method == 'DELETE':
        return delete_movie()



