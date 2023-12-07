from django.shortcuts import render
from django.http import JsonResponse

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Employee, Student
from .serializers import StudentSerializer

def employeeView(request):
    empleados = Employee.objects.all()
    data = {
        'employees' : list(empleados.values('name', 'salary'))
    }
    return JsonResponse(data)

@api_view(['GET', 'POST'])
def student_list(request):
    match request.method:
        case 'GET':
            students = Student.objects.all()
            serializer = StudentSerializer(students, many=True)
            return Response(serializer.data)
        case 'POST':
            serializer = StudentSerializer(data=request.data)
            if(serializer.is_valid()):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def student_detail(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    match request.method:
        case 'GET':
            serializer = StudentSerializer(student)
            return Response(serializer.data)
        case 'PUT':
            serializer = StudentSerializer(student, data=request.data)
            if(serializer.is_valid()):
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        case 'DELETE':
            student.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
