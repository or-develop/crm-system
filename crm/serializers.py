from rest_framework import serializers

from .models import Lead, AbstractModelDateTime


class AddLeadSerializer(serializers.ModelSerializer):
    """ API для добавления Лида в базу данных. """

    class Meta:
        model = Lead
        fields = ('name', 'email', 'phone')


class LeadListSerializer(serializers.ModelSerializer):
    """ API для вывода списка Лидов. """

    class Meta:
        model = Lead
        fields = ('name', 'email', 'phone')


class LatestApplicationsSerializer(serializers.ModelSerializer):
    """ API для заявок последних 30-ти дней """

    class Meta:
        model = AbstractModelDateTime
        fields = ('created', )
