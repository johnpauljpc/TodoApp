from django.urls import path
from .views import home, update, delete 

urlpatterns = [
	
	path('', home, name = 'home'),
	path('update/<int:pk>/', update, name ="update"),
	path('delete/<int:pk>/', delete, name = "delete")
]