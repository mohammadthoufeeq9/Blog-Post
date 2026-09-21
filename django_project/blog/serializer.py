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
