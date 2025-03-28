from rest_framework import serializers

from .models import Conversation, ConversationMessage

from useraccount.serializers import UserDetailSerializer


class ConversationListSerializer(serializers.ModelSerializers):
    users = UserDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Conversation
        fields = ('id', 'users', 'modified_at', )