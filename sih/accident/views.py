from django.shortcuts import render, redirect
from django.urls import reverse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Accident
from account.models import Customer
from .serializers import AccidentSerializer
from django.http import JsonResponse, HttpResponseRedirect

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

def track(request):
	current_accidents = Accident.objects.all().filter(status='DET')
	for a in current_accidents:
		hospital = a.get_nearest_hospital()
		police_st = a.get_nearest_police_station()		
		if hospital.admin == request.user or police_st.admin == request.user:
			accident_info = {'id': a.id,
				             'lon': a.lon, 
		                     'lat': a.lat,
						     'mcc': a.mcc,
						     'mnc': a.mnc,
						     'lac': a.lac,
						     'cell_id': a.cell_id
			                }
			customer = Customer.objects.get(id=a.get_customer()) 
			customer_info = {'phone': customer.phone,
			                 'rel_phone': customer.rel_phone,
							 'address': customer.address,
							 'vehicle_no': customer.vehicle_no}
			d = {'accident': accident_info, 'user': customer_info}
			return JsonResponse(d)
	
	
			
	
	

def acknowledge(request, pk):
	accident = Accident.objects.get(pk=pk)
	accident.status = 'ACK'
	accident.save()
	return HttpResponseRedirect(reverse('accident:log_list'))

def accidents_log_list(request):
	accidents = Accident.objects.all()
	acci_list = [] 
	for a in accidents:
		hospital = a.get_nearest_hospital()
		if hospital.admin == request.user:
			acci_list.append(a)
	return render(request, 'accident/accident_log.html', {'accident_list': acci_list})

def accidents_log_detail(request, pk):
	accident = Accident.objects.get(pk=pk)
	customer_id = accident.get_customer()
	customer = Customer.objects.get(pk=customer_id)
	return render(request, 
	             'accident/accident_log_detail.html',
				 {'accident': accident, 'customer': customer}) 

				