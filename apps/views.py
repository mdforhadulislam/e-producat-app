from django.shortcuts import render
from apps.models import *

# Create your views here.
def home(request):
   slider_section_data = Slider.objects.all()
   propuler_categories_data = Propuler_categories.objects.all()
   producat = Producat.objects.all()
   review_ss = Testimonial.objects.all()
   context = {
      'slider':slider_section_data,
      'propuler_categories':propuler_categories_data,
      'producats':producat,
      'reviews':review_ss
   }
   return render(request,'home.html',context)



def shops(request):
   producat = Producat.objects.all()
   context = {
      'producats':producat,
   }
   return render(request,'shops.html',context)



def single_producat(request,producat_id):
   producat = Producat.objects.get(id=producat_id)
   producats = Producat.objects.all()
   print(producat)
   context = {
      'producat':producat,
      'producats':producats
   }
   return render(request,'single-producat.html',context)
   