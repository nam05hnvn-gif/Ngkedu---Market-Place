from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from item.models import Item

@login_required
def dashboard(request):
    user_items = Item.objects.filter(created_by=request.user).order_by('-created_at')
    return render(request, 'dashboard/dashboard.html', {
        'user_items': user_items,
    })