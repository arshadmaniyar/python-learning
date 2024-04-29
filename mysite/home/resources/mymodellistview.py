from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from home.models import User
import json

class MyModelListView(View):
    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request):
        user = User.objects.all().values()
        #return self.arshad()
        #print(type(user))
        data = {"data": list(user),"status_code":200}
        return JsonResponse(data)

    def post(self, request):
        #print(type(user))
        data = {"data": "post","status_code":"data inserted succefully"}
        return JsonResponse(data)

    def put(self, request):
        #print(type(user))
        data = {"data": "put","status_code":200}
        return JsonResponse(data)
    
    def delete(self, request):
        #print(type(user))
        data = {"data": "delete","status_code":200}
        return JsonResponse(data)
    
    def arshad(self):
        #print(type(user))
        data = {"data": "arshaad","status_code":200}
        return JsonResponse(data)
    