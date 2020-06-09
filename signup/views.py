from django.shortcuts import render, redirect
# from django.contrib.auth.models import User, auth
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.views import generic
from django.http import JsonResponse,HttpResponse
import json
from django.contrib import messages

# Create your views here.
# @csrf_exempt

    # def post(self,request):
    #         data = json.loads(request.body)

def signup(request):
    alert =0
    if request.method == 'POST':
        id = request.POST["name"]
        email = request.POST["email"]
        password = request.POST["pass"]
        password2 = request.POST["re_pass"]
            
        if password == password2:
            if Customer.objects.filter(id = id).exists():
                # messages.info(request, 'ID is Taken')
                alert =1
                context = {
                    "alert": alert,
                }
                return render(request, 'index2.html', context)
            else:
                Customers = Customer(
                    id = id, email = email, password = password
                )
                Customers.save()
                context = {
                    "alert": alert,
                }
                render(request, 'Customer_list.html', context)
        else:
            # messages.info(request, 'Password is Not Matching')
            alert = 2
            context = {
                "alert": alert,
            }
            return render(request, 'index2.html', context)

        return redirect('/')
    else:
        return render(request, "index2.html")
        
    
        

# class c_list(generic.ListView):
#     model = Customer
    
