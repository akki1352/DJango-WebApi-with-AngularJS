from django.shortcuts import render, redirect, HttpResponse
from django.http import Http404, HttpResponseNotFound
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
from django.views.generic import TemplateView
from django.views import View
import json
from app.models import employee
from app.forms import userRegister, userLogin
from django.contrib.auth import authenticate, login, logout
import pdb

def index(request):
    return render(request, 'home.html')

def login_view(request):
    # print(request.user)
    # print(request.user.is_authenticated)
    if 'login' not in request.session:
        form = userLogin(request.POST or None)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            # user = authenticate(username=username,password=password)
            user_name = employee.objects.filter(username = username)
            print(user_name.count())
            if user_name.count() == 1:
                user_object = employee.objects.get(username = username)
                if user_object.username == username and user_object.password == password:
                    # user = authenticate(username=user_object.username,password=user_object.password)
                    # login(request,user)
                    # print(request.user.is_authenticated)
                    print("username and password matched")
                    request.session['login'] = user_object.username
                    return redirect('/')
            
        return render(request,'login.html',{'form':form})
    else:
        name = request.session['login']
        print(name)
        return render(request,'login.html',{'user':name})

        

def logout_view(request):
	# logout(request)
    del request.session['login']
    return render(request, 'home.html')

def register(request):
	print(request.user.is_authenticated)
	form = userRegister(request.POST or None)
	if form.is_valid():
		user = form.save(commit=False)
		name = form.cleaned_data.get('name')
		email = form.cleaned_data.get('email')
		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password')
		user.save()

		# new_user = authenticate(username = user.username, password = user.password)
		# login(request,user)
		# print(request.user.is_authenticated)
		return redirect('/login')

	return render(request,'register.html',{'form':form})

class gp(APIView):

    def get(self, request):
        users = employee.objects.all().values()
        return JsonResponse(list(users), safe=False)

    def post(self, request):
        employee.objects.create(name=request.POST.get('fname'),
        email=request.POST.get('email'),
        username=request.POST.get('user'),
        password=request.POST.get('pwd'))
        return HttpResponse(status=201)

class gud(APIView):

    def get(self, request, pk):
        if employee.objects.filter(id=pk):
            users = employee.objects.get(id = pk)
            userlist = [{'id':users.id, 'name':users.name, 'email':users.email, 'username':users.username, 'password':users.password}]
            return JsonResponse(list(userlist),safe=False)
        else:
            return HttpResponseNotFound('<h1>Details Not Found</h1>')

    def put(self, request, pk):
        if employee.objects.filter(id=pk):
            users = employee.objects.get(id = pk)
            users.name = request.POST.get('fname')
            users.email = request.POST.get('email')
            users.password = request.POST.get('pwd')
            users.save()
            return HttpResponse(status=202)
        else:
            return HttpResponseNotFound('<h1>Details Not Found</h1>')  
        
    def delete(self, request, pk):
        if employee.objects.filter(id=pk):
            employee.objects.get(id=pk).delete()
            return HttpResponse(status=202)
        else:
            return HttpResponseNotFound('<h1>Details Not Found</h1>')

def ang_login(request):
    return render(request,'angularlogin.html')