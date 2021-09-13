from rest_framework import serializers
from .models import Comment
from main.models import Publication


class PublicationsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = ('id', 'title', 'user')


class PublicationDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['comments'] = CommentSerializer(instance.comments.all(), many=True.data)
        return rep


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
