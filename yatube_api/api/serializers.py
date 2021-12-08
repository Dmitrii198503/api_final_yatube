from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField


from posts.models import Comment, Post, Group, Follow, User


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Comment


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Group


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )
    following = serializers.SlugRelatedField(
        queryset=User.objects.all(), slug_field='username'
    )
    class Meta:
        model = Follow
        fields = '__all__'

    def validate(self, data):
        user = get_object_or_404(User, username=self.context['request'].user)
        following = get_object_or_404(User, username=data['following'].username)
        check = Follow.objects.filter(user=user, following=following).exists()
        if user == following:
            raise serializers.ValidationError('Нельзя подписаться на самого себя!')
        if check is True:
            raise serializers.ValidationError('Подписка уже существует!')
        return data



