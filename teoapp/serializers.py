from rest_framework import serializers
from teoapp.models import PostAuthor, PostContent


class AuthorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostAuthor
        fields = ('nameId','topTen')
        lookup_field = 'nameId'

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret = {ret['nameId']: ret['topTen']}
        return ret

class AuthorsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostAuthor
        fields = ('name','nameId')
        lookup_field = 'nameId'
        extra_kwargs = {
            'url': {'lookup_field': 'nameId'}
        }

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret = {ret['nameId']: ret['name']}
        return ret




class PostContentSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        """Convert `username` to lowercase."""
        ret = super().to_representation(instance)
        #ret['username'] = ret['username'].lower()
        return ret['topTen']

    class Meta:
        model = PostContent
        fields = ('topTen',)



