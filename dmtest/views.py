from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import DatamodelSerializer
from .models import Datamodel
from rest_framework import filters
# Create your views here.

class DatamodelAPIView(APIView):
  # whatever serializer class

  def get_queryset(self):
    query_params = self.request.query_params
    first_object = query_params.get('firstobject', None)
    second_object = query_params.get('secondobject', None)
    third_object = query_params.get('thirdobject', None)
    print(first_object)

    # create an empty list for parameters to be filters by 
    firstobjectParams = []
    secondobjectParams = []
    thirdobjectParams = []

    # create the list based on the query parameters
    if first_object is not None:
      for arg in first_object.split('|'):
        firstobjectParams.append(int(arg))
    if second_object is not None:
      for arg in second_object.split('|'):
        secondobjectParams.append(int(arg))
    if third_object is not None:
      for arg in third_object.split('|'):
        thirdobjectParams.append(int(arg))

    if first_object and second_object and third_object is not None:
      
      queryset_list = Datamodel.objects.all()
      queryset_list = queryset_list.filter(first_object_id__in=firstobjectParams)
      queryset_list = queryset_list.filter(second_object_id__in=secondobjectParams)
      queryset_list = queryset_list.filter(third_object__in=thirdobjectParams) 
    return queryset_list


"""  If we need to add DB :


@api_view(['GET'])

def dmtestOverview(request):
    dmtest_urls = {
		'List':'/name-list/',
		'Detail View':'/name-detail/<str:pk>/',
		'Create':'/name-create/',
		'Update':'/name-update/<str:pk>/',
		'Delete':'/name-delete/<str:pk>/',
		}
    return Response(dmtest_urls)



@api_view(['GET'])
def namelist(request):
    names = Datamodel.objects.all()
    serializer = DatamodelSerializer(names, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def namedetail(request, pk):
    names = Datamodel.objects.get(id=pk)
    serializer = DatamodelSerializer(names, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def namecreate(request, pk):
    
    serializer = DatamodelSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def nameupdate(request, pk):
    
    names = Datamodel.objects.get(id=pk)
    serializer = DatamodelSerializer(instance=names, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)  

@api_view(['DELETE'])
def namedelete(request, pk):
	name = Datamodel.objects.get(id=pk)
	name.delete()

	return Response('Item succsesfully delete!') 



def special(request):
	

	return JsonResponse("Item succsesfully delete!", safe=False)     


def special2(request):
	

	return JsonResponse("Item succsesfully delete!", safe=False)    
    
       """










     
