from rest_framework import serializers

from .models import Lead, Agent


class LeadSerializer(serializers.ModelSerializer):
    """ API для добавления Лида в базу данных. """

    class Meta:
        model = Lead
        fields = ('name', 'email', 'phone')


class AgentSerializer(serializers.ModelSerializer):
    """ API для вывода всех агентов. """

    class Meta:
        model = Agent
        fields = ('id', 'first_name', 'last_name',
                  'email', 'phone', 'date_of_birth', 'is_staff')
