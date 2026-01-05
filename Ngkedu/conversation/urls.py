from django.urls import path
from . import views

app_name = 'conversation'

urlpatterns = [
    path('', views.inbox, name='inbox'),
    path('new/<int:item_id>/', views.new_conversation, name='new_conversation'),
    path('<int:pk>/', views.detail, name='detail'),
]