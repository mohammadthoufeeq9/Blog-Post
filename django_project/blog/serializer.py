#A serializer converts complex Python/Django data into simple data types that can be rendered as JSON through api 
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import post

class postserializer(serializers.ModelSerializer):
    # title=serializers.CharField(max_length=100)
    # content=serializers.CharField()
    # date_posted =serializers.DateField()
    # author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    # modelserailizer
    class Meta:
        model =post
        fields='__all__'
    def validate_title(self,value):
        if len(value)<5:
            raise serializers.ValidationError("The title should contain at least 5 charaters")
        return value
    
    def validate(self, data):
        title=data.get('title')
        content=data.get('content')

        if title is not None and content is not None and title == content:
            raise serializers.ValidationError('title and content cannot be same')
        return data

    