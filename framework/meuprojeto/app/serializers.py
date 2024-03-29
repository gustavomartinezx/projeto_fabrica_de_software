from rest_framework import serializers
from app.models import ToDo

class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = ["id", "atividade", "status"]