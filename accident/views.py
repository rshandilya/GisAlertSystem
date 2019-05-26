from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Accident
from .serializers import AccidentSerializer

# Create your views here.

@api_view(['GET', 'POST'])
def accident_list(request):
	if request.method == 'GET':
		accidents = Accident.objects.all()
		accident_serializer = AccidentSerializer(accidents, many=True)
		return Response(accident_serializer.data)
	elif request.method == 'POST':
		accident_serializer = AccidentSerializer(data=request.data)
		if accident_serializer.is_valid():
			accident_serializer.save()
			return Response(accident_serializer.data,
			                status=status.HTTP_201_CREATED)
		return Response(accident_serializer.errors,
		                status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE'])
def accident_detail(request, pk):
	try:
		accident = Accident.objects.get(pk=pk)
	except Accident.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)
	if request.method == 'GET':
		accident_serializer = AccidentSerializer(accident)
		return Response(accident_serializer.data)
	elif request.method == 'DELETE':
		accident.delete()