from django.urls import path
from .views import home, update, delete, complete

urlpatterns = [
	
	path('', home, name = 'home'),
	path('update/<int:pk>/', update, name ="update"),
	path('delete/<int:pk>/', delete, name = "delete"),
	path('complete/<int:pk>/', complete, name = "complete"),
]