from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Wish
# Create your views here.

def home(request):
  wishlist = Wish.objects.all()
  return render(request, 'home.html', {'wishlist': wishlist})

def create(request):
  if request.method == 'POST':
      item = Wish(description=request.POST['description'])
      item.save()
      return redirect('home')

  return render(request, 'create.html')


def delete(request, item_id):
    item = Wish.objects.get(id=item_id)
    item.delete()
    return redirect('home')