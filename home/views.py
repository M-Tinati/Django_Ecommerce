from django.shortcuts import render , redirect
from django.views import View
from .models import Product
class HomeView(View):
    def get(self,request):
        product = Product.objects.all()
        
        return render(request,'home.html',{'product':product})
    def post(self,request):
        return render(request,'home.html',{})
