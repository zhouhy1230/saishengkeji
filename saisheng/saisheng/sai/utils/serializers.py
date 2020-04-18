from rest_framework import serializers
from sai.models import ClientName


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientName
        fields = ('ip', 'score')
