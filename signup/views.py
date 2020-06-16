from django.shortcuts import render, redirect
# from django.contrib.auth.models import User, auth
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.views import generic
from django.http import JsonResponse,HttpResponse
import json
from django.contrib import messages
from django.core.serializers import serialize

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
                return redirect('/sign_in/')
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
        
    
def user_lsit(request):
    json_Customer = Customer.objects.all().order_by('date_created')
    print(json_Customer)
    data = json.loads(serialize('json', json_Customer))
    # render(request, 'Customer_list.html')
    return JsonResponse({'items': data})

# class c_list(generic.ListView):
#     model = Customer

def signIn(request):
    alert =0
    if request.method == "POST":
        id = request.POST["your_name"]
        password = request.POST["your_pass"]
        querySet = Customer.objects.filter(id = id).values()
        print(querySet[0]['password'])

        if querySet[0]['id'] != id:
            alert =1
            context = {
                "alert": alert
            }
            print("존재하지 않는 아이디")
            return render(request, 'sign_in.html', context)
        elif querySet[0]['password'] != password:
            alert = 2
            context = {
                "alert": alert
            }
            print("비밀번호 불일치")
            return render(request, 'sign_in.html', context)
        else:
            return

        return  render(request, 'sign_in.html')

    return render(request, 'sign_in.html')
