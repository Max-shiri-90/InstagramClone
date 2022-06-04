from rest_framework import serializers

from .models import PostModel


class PostModelListSerializer(serializers.ModelSerializer):    
    class Meta:
        model = PostModel
        exclude = ['user', 'created_at', 'updated_at']

    def create(self, validated_data):
        return PostModel.objects.create(user=self.context['user'],**validated_data)  


class PostModelDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostModel
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.caption = validated_data.get('caption', instance.caption)
        instance.save()
        return instance   
