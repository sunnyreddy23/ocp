from rest_framework import serializers
from rest_framework.utils import model_meta

from .models import Topic, Preference, Medium

class TopicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Topic
        fields = ('id', 'name', 'description')
        extra_kwargs = {
            'name': {
                'validators': [],
            },
        }

class MediumSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Medium
        fields = ('id', 'medium', 'medium_value', 'status', 'preference')


class PreferenceMediumSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Medium
        fields = ('id', 'medium', 'medium_value', 'status')

class PreferenceSerializers(serializers.ModelSerializer):

    topic = TopicSerializer()
    mediums = PreferenceMediumSerializer(many=True, required=False)
    #created_at = serializers.SerializerMethodField(method_name='get_created_at')
    #updated_at = serializers.SerializerMethodField(method_name='get_updated_at')

    class Meta:
        model = Preference
        #fields = ('uuid', 'mediums', 'user_ref', 'opted_in', 'entity', 'entity_id', 'topic', 'updated_at', 'created_at')
        fields = ('id', 'user_ref', 'opted_in', 'entity', 'entity_id', 'topic', 'mediums')

    def create(self, validated_data):
        data = validated_data
        mediums = validated_data.pop('mediums', [])
        topic = validated_data.pop('topic')

        topic_instance = Topic.objects.get(name=topic.get('name'))
        
        preference = Preference.objects.create(**validated_data, topic=topic_instance)
        for medium in mediums:
            preference.mediums.create(**medium)

        return preference

    def get_created_at(self, instance):
        return instance.created_at.isoformat()

    def get_updated_at(self, instance):
        return instance.updated_at.isoformat()

    def update(self, instance, validated_data):
        topic = validated_data.pop('topic')
        mediums = validated_data.pop('mediums', [])

        topic_instance = Topic.objects.get(name=topic.get('name'))

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        instance.topic = topic_instance 
        instance.save()

        return instance