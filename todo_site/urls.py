from django.contrib import admin
from django.urls import path
from todo import views

urlpatterns = [
    path('', views.index, name='index'),  
    path('del/<str:item_id>/', views.remove, name='delete_todo'),  
    path('edit/<int:item_id>/', views.edit, name='edit_todo'),
    path('add/', views.add, name='add_todo'),  
    path('admin/', admin.site.urls),
]
