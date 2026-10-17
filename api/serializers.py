
from rest_framework import serializers
from members.models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
        read_only_fields = [
            "id",
            "student_id",
            "registration_no",
            "roll",
            "created_at",
            "updated_at",
        ]
