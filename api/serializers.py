from rest_framework import serializers

from .models import Team, TeamMember


class TeamSerializer(serializers.ModelSerializer):
    members = serializers.StringRelatedField(many=True)
    class Meta:
        model = Team
        fields = ['name', 'members']
