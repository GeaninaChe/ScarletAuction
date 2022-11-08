from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.sites import requests
from django.shortcuts import render
from django.views.generic import DetailView
from rest_framework.views import APIView

from artobjects.models import ArtObjects


# Create your views here.


class ArtObjectsApi(APIView):
    def get_external_call(self, request):
        # fie requests fie http library
        response = requests.get(
            "https://api.gsa.gov/assets/gsaauctions/v2/auctions?api_key=DEMO_KEY&format=JSON")  # response este o lista de dictionare
        response_list_model = []


# for i in response:
#     model = ExternalData(name=i['name'],age=i['age'])
#     response_list_model.append(model)
#
# return HttpResponse('template_name',response_list_model)


class ArtObjectsView(DetailView):
    template_name = 'artobjects/artobjects.html'
    model = ArtObjects

# class StudentApi(APIView):
#
#     def get(self, request):
#         queryset = Student.objects.all()
#         serializer = StudentSerializer(queryset, many=True)
#         return Response(serializer.data)
