
from rest_framework.decorators import api_view
from rest_framework.response import Response
from members.models import Student
from rest_framework import status
from .serializers import StudentSerializer


@api_view(["GET"])
def hello_api(request):
    data = {
        "message": "My first REST API is working!",
        "project": "School Management System",
        "status": "success",
    }
    return Response(data)


@api_view(["GET", "POST"])
def student_list_api(request):

    if request.method == "GET":
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = StudentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
