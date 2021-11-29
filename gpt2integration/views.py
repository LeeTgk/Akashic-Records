from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
import requests
import json
import os

API_URL = {
    "SmallPortuguese" : "https://api-inference.huggingface.co/models/pierreguillou/gpt2-small-portuguese",
    "TolkienMythopoeic" : "https://api-inference.huggingface.co/models/muirkat/tolkien-mythopoeic-gen"
}
headers = {"Authorization": f"Bearer {os.getenv('API_TOKEN')}"}

class AjaxHandlerView(View):
    def get(self,request):
        text = request.GET.get('textbox_text')
        model = request.GET.get('model')
        queryRes = query(text,model)
        if request.is_ajax():
            print(queryRes[0])
            return JsonResponse(queryRes[0], status=200)

        return render(request, 'Gpt2Integration/home.html')
    
    def post(self,request):
        return


def home(request):
    return render(request, 'Gpt2Integration/home.html')

def query(payload,model):
    if model:
        print(model)
        api = API_URL[model]
        response = requests.post(api, headers=headers, json=payload)
        return response.json()
    return

#output = query("Can you please let us know more details about your ")