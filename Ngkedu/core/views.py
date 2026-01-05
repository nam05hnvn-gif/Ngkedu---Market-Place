from django.shortcuts import redirect, render
from item.models import Category, Item
from .forms import SignUpForm
from django.contrib.auth import logout

def index(request):
    items = Item.objects.filter(is_sold=False).order_by('-created_at')[:9]
    categories = Category.objects.all()
    return render(request, 'core/index.html', {'items': items, 'categories': categories})

def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:login')
    else:
        form = SignUpForm()
    return render(request, 'core/signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('core:index')