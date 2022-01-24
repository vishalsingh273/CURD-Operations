
from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
path('', views.add_show, name='create'),
    path('delete/<int:id>/',views.delete,name="delete"),
    path('update/<int:id>/', views.update, name="update"),
]


