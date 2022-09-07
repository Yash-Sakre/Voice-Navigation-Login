from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

import speech_recognition as sr
# Create your views here.

def index(request):
    return render(request, 'home.html')

def home(request):
    return render(request, 'home.html')



def voice(request):
     if request.method == "POST":
          # value=request.POST.get('vr2')
          r = sr.Recognizer()
          while(1):   
               try:
                    with sr.Microphone() as source2:
                         # r.adjust_for_ambient_noise(source2, duration=0.2)
                         audio2 = r.listen(source2)
                         MyText = r.recognize_google(audio2)
                         MyText = MyText.lower()
                         return HttpResponse(MyText)
                         
               except sr.RequestError as e:
                    print("Could not request results; {0}".format(e))
         
               except sr.UnknownValueError:
                    print("unknown error occured")




