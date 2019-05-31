from rest_framework import serializers


class InputSerializer(serializers.Serializer):
    title = serializers.CharField()
    text = serializers.CharField()
