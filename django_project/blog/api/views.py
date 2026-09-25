from django.shortcuts import get_object_or_404
from blog.models import post
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import postserializer
from .serializers import PostSerializerV2
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAdminUser
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from blog.api.permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

class TestApi(APIView):
    def get(self, request, pk=None, *args, **kwargs):
    #Get a specific post
    #/api/v1/test/1/
        if pk:

            post_object = get_object_or_404(post, pk=pk)

            if request.version == 'v1':
                serializer = postserializer(post_object)

            elif request.version == 'v2':
                serializer = PostSerializerV2(post_object)

            return Response({
                'version': request.version,
                'Message': f'The data is from {request.version}',
                'data': serializer.data
            })
        #Get all posts
        #/api/v1/test/

        posts = post.objects.all()

        if request.version == 'v1':
            serializer = postserializer(posts, many=True)

        elif request.version == 'v2':
            serializer = PostSerializerV2(posts, many=True)

        return Response({
            'version': request.version,
            'Message': f'The data is from {request.version}',
            'data': serializer.data
        })
    def post(self,request,*args,**kwargs):
        serializer=postserializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def put(self,request,pk=None,*args,**kwargs):
           post_object=get_object_or_404(post,pk=pk)
           serializer=postserializer(post_object, data=request.data)

           if serializer.is_valid():
               serializer.save()
               return Response(serializer.data)
           return Response(serializer.errors)

    def patch(self,request,pk=None,*args,**kwargs):
        post_object=get_object_or_404(post,pk=pk)
        serializer=postserializer(post_object, data=request.data, partial=True)#The client is only sending some fields, so don't require all fields

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self,request,pk=None,*args,**kwargs):
        post_object=get_object_or_404(post,pk=pk)
        post_object.delete()
        return Response({'Message': "Post deleted successfully"})


# Create a CRUD ViewSet for my post model, and use postserializer to handle its data.
class PostViewSet(ModelViewSet):
    queryset=post.objects.all()
    serializer_class=postserializer
    permission_classes=[IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]

    filter_backends =[DjangoFilterBackend,SearchFilter]
    filterset_fields =['author']
    search_fields = ['title', 'content']
