from rest_framework import status, mixins, viewsets
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.permissions import (
    IsAuthenticated,
    AllowAny
)

from .models import Topic, Preference, Medium
from .serializers import TopicSerializer, PreferenceSerializers, MediumSerializer
from .renderers import TopicRenderer, PreferenceRenderer, MediumRenderer


class TopicViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet):

    lookup_field = 'name'
    queryset = Topic.objects.all()
    permission_classes = (AllowAny, )
    renderer_classes = (TopicRenderer, )
    serializer_class = TopicSerializer

    def create(self, request, *args, **kwargs):
    
        serializer_context = {
            'request': request,
        }

        serializer_data = request.data.get('topic', {})
        
        serializer = self.serializer_class(
            data = serializer_data,
            context = serializer_context
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, name):
        #investigate
        
        serializer_context = {'request': request}

        try:
            serializer_instance = self.queryset.get(name=name)
        except:
            raise NotFound('Topic with this name does not exist.')

        serializer_data = request.data.get('topic', {})

        serializer = self.serializer_class(
            serializer_instance,
            context=serializer_context,
            data=serializer_data
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)

class PreferenceViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet):

    permission_classes = (AllowAny,)
    renderer_classes = (PreferenceRenderer,)
    serializer_class = PreferenceSerializers
    queryset = Preference.objects.all()

    def retrieve(self, request, *args, **kwargs):
        serializer_context = {'request': request}

        try:
            serializer_instance = self.queryset.get(pk=kwargs.get('pk'))
        except Preference.DoesNotExist:
            raise NotFound('Preference with this id does not exist.')

        serializer = self.serializer_class(serializer_instance, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        
        serializer_context = {
            'request': request,
        }

        serializer_data = request.data.get('preference', {})
        
        serializer = self.serializer_class(
            data = serializer_data,
            context = serializer_context
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        serializer_context = {'request': request}

        try:
            serializer_instance = self.queryset.get(pk=kwargs.get('pk'))
        except: 
            raise NotFound('Preference with this id does not exist.')

        serializer_data = request.data.get('preference', {})

        serializer = self.serializer_class(
            serializer_instance,
            context=serializer_context,
            data=serializer_data
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)

class MediumViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet):

    permission_classes = (AllowAny,)
    renderer_classes = (MediumRenderer,)
    serializer_class = MediumSerializer
    queryset = Medium.objects.filter(status=True)

    def create(self, request, *args, **kwargs):
        
        serializer_context = {
            'request': request,
        }

        serializer_data = request.data.get('medium', {})
        
        serializer = self.serializer_class(
            data = serializer_data,
            context = serializer_context
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        serializer_context = {'request': request}

        try:
            serializer_instance = self.queryset.get(pk=kwargs.get('pk'))
        except: 
            raise NotFound('Medium with this id does not exist.')

        serializer_data = request.data.get('medium', {})

        serializer = self.serializer_class(
            serializer_instance,
            context=serializer_context,
            data=serializer_data
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)