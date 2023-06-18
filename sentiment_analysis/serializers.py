from rest_framework import serializers

class SentimentAnalysisSerializer(serializers.Serializer):
    text = serializers.CharField()

    def validate(self, attrs):
        if text := attrs.get('text'):
            return attrs
        else:
            raise serializers.ValidationError("Text field is required.")
