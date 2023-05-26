from rest_framework import serializers
from .models import Post, Toy


class PostSerializer(serializers.ModelSerializer):
    # post_age is not a model field so it needs to be added explicitly
    post_age = serializers.ReadOnlyField()
    class Meta:
        model = Post
        fields = ('title', 'content', 'post_age')


class ToySerializer(serializers.ModelSerializer):
    class Meta:
        model = Toy
        fields = '__all__'
        