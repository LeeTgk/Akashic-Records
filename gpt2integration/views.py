from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
import requests
import json
import os

API_URL_SmallPortuguese = "https://api-inference.huggingface.co/models/pierreguillou/gpt2-small-portuguese"
headers = {"Authorization": f"Bearer {os.getenv('API_TOKEN')}"}

class AjaxHandlerView(View):
    def get(self,request):
        text = request.GET.get('textbox_text')
        queryRes = query(text)
        if request.is_ajax():
            print(queryRes[0])
            return JsonResponse(queryRes[0], status=200)

        return render(request, 'Gpt2Integration/home.html')
    
    def post(self,request):
        return


def home(request):
    return render(request, 'Gpt2Integration/home.html')

def query(payload):
	response = requests.post(API_URL_SmallPortuguese, headers=headers, json=payload)
	return response.json()

#output = query("Can you please let us know more details about your ")