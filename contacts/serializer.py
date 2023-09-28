from rest_framework import serializers

from contacts.models import Contacts


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = [
            "id", "user", "email", "subject", "message"
        ]
