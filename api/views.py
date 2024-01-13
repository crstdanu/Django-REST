from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import TaskSerializer
from myapp.models import Task


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': 'task-list/',
        'Detailed View': 'task-detail/<str:pk>',
        'Create': 'task-create/',
        'Update': 'task-update/<str:pk>',
        "Delete": 'task-delete/<str:pk>'
    }
    return Response(api_urls)


@api_view(['GET'])
def taskList(request):
    items = Task.objects.all()
    serializer = TaskSerializer(items, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def detailedView(request, pk):
    item = Task.objects.get(id=pk)
    serializer = TaskSerializer(item, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def taskCreate(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def taskUpdate(request, pk):
    item = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=item, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def taskDelete(request, pk):
    item = Task.objects.get(id=pk)
    item.delete()
    return Response("Item successfully deleted!")
