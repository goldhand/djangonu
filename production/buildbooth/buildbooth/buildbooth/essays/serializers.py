from rest_framework import serializers

from users.models import User

from .models import Intro, Body, Conclusion, Essay



class IntroSerializer(serializers.HyperlinkedModelSerializer):
    essay = serializers.HyperlinkedRelatedField(many=False, view_name='essay-detail')

    class Meta:
        model = Intro
        fields = [
            'id', 'url', 'essay',
            'created', 'updated',
            'intro', 'transition', 'thesis', 'conclusion',
            ]


class BodySerializer(serializers.HyperlinkedModelSerializer):
    essay = serializers.HyperlinkedRelatedField(many=False, view_name='essay-detail')
    _next = serializers.SerializerMethodField('get_next')
    _previous = serializers.SerializerMethodField('get_previous')

    class Meta:
        model = Body
        fields = [
            'id', 'url', 'essay',
            'created', 'updated',
            'intro', 'transition', 'body', 'conclusion',
            ]

    def get_next(self, obj):
        try:
            return obj.get_next_by_created().get_display_url()
        except Body.DoesNotExist:
            return Body.objects.reverse().latest('created').get_display_url()
        except AttributeError:
            return None

    def get_previous(self, obj):
        try:
            return obj.get_previous_by_created().get_display_url()
        except Body.DoesNotExist:
            return Body.objects.latest('created').get_display_url()
        except AttributeError:
            return None

class ConclusionSerializer(serializers.HyperlinkedModelSerializer):
    essay = serializers.HyperlinkedRelatedField(many=False, view_name='essay-detail')

    class Meta:
        model = Conclusion
        fields = [
            'id', 'url', 'essay',
            'created', 'updated',
            'intro', 'transition', 'thesis', 'body', 'conclusion',
            ]


class EssaySerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.Field(source='owner.username')
    _next = serializers.SerializerMethodField('get_next')
    _previous = serializers.SerializerMethodField('get_previous')
    intro = serializers.HyperlinkedRelatedField(many=True, view_name='intro-detail', read_only=True)
    body = serializers.HyperlinkedRelatedField(many=True, view_name='body-detail', read_only=True)
    conclusion = serializers.HyperlinkedRelatedField(many=True, view_name='conclusion-detail', read_only=True)

    class Meta:
        model = Essay
        fields = [
            'id', 'url', 'owner',
            'created', 'updated',
            'title',
            'intro', 'body', 'conclusion',
            ]

    def get_next(self, obj):
        try:
            return obj.get_next_by_created().get_display_url()
        except Essay.DoesNotExist:
            return Essay.objects.reverse().latest('created').get_display_url()
        except AttributeError:
            return None

    def get_previous(self, obj):
        try:
            return obj.get_previous_by_created().get_display_url()
        except Essay.DoesNotExist:
            return Essay.objects.latest('created').get_display_url()
        except AttributeError:
            return None


class UserSerializer(serializers.HyperlinkedModelSerializer):
    essays = serializers.HyperlinkedRelatedField(many=True, view_name='essay-detail', read_only=True)

    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'essays')



