# from django.shortcuts import render
from rest_framework import viewsets
from .models import Post, Toy
from .serializers import PostSerializer, ToySerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class ToyViewSet(viewsets.ModelViewSet):
    queryset = Toy.objects.all()
    serializer_class = ToySerializer

    # override the queryset to get only sound making animals
    def get_queryset(self):
        return Toy.objects.get_sound_making_animals()