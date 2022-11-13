from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import task
from .serializers import TaskSerializer
from rest_framework import status

from rest_framework import generics

# Create your views here.
class getAllTasks(APIView):
  def get(self, request):
    print("LLegó un get!!!")
    response = {"msg": "Hola! API online!"}
    tasks= task.objects.all()
    serializer=TaskSerializer(tasks, many=True)
    print(tasks)
    return Response(serializer.data) 

class getTaskById(APIView):
  def get(self, request, pk):
    oneTask =task.objects.get(id=pk)
    serializer=TaskSerializer(oneTask)
    return Response(serializer.data) 

class updateTaskById(APIView):
  def put(self, request, pk):
    putTask = task.objects.get(id=pk)
    serializer = TaskSerializer(putTask, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class deleteTaskById(APIView):
  def delete(self, request, pk, format=None):
    try: 
      deleteTask = task.objects.get(id=pk)
      deleteTask.delete()
      response = {"msg": "Tarea borrada exitosamente"}
      return Response(response)
    except:
      return Response( {"msg": "Error al borrar registro"}, status=status.HTTP_204_NO_CONTENT)
      

'''class GetTasks(generics.ListAPIView):
  queryset=task.objects.all()
  serializer_class = TaskSerializer'''