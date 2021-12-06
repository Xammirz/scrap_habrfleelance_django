
from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Follower
from .models import Information
from django.contrib import messages
from datetime import datetime
class PostList(ListView):
    def post(self, request):
            email = request.POST.get('email')
            f = Follower.objects.filter(email=email)
            if f:
                messages.error(request, 'Error updating your profile')
                return redirect ("index")
            if email:
                f = Follower(email=email)
                f.save()
                messages.success(request, 'Profile updated successfully')               
            return redirect('index')       
    def get(self, request):
        jobs = Information.objects.all()[:10]
        return render(request, 'index.html', {'jobs': jobs})

# Create your views here.
