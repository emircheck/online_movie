from rest_framework import serializers
from applications.genre.models import Genre


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        if not instance.parent:
            rep.pop('parent')
        return rep
