from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, status, authentication

from .models import PostModel
from .serializers import PostModelListSerializer, PostModelDetailSerializer


class PostModelListView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        query_set = PostModel.objects.all().filter(user=request.user)
        serializer = PostModelListSerializer(query_set, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = PostModelListSerializer(data=request.data, context={'user': request.user})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            

class PostModelDetailView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        query_set = PostModel.objects.get(pk=pk)
        serializer = PostModelDetailSerializer(query_set)
        return Response(serializer.data)

    def put(self, request, pk):
        query_set = PostModel.objects.get(pk=pk)
        serializer = PostModelDetailSerializer(query_set, data=request.data, \
            context={'user': request.user}, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        query_set = PostModel.objects.get(pk=pk)
        query_set.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)   
        