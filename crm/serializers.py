from rest_framework import serializers

from .models import Lead


class LeadSerializer(serializers.ModelSerializer):
    """ Сериализатор для мождели Lead """

    class Meta:
        model = Lead
        fields = ('name', 'email', 'phone')