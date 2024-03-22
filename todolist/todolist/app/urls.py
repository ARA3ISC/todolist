from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name="home"),
	path('itemDetails/<int:id>/', views.itemDetails),
	path('addingItem/', views.addingForm, name="addingItem"),
	path('createTask/', views.createTask, name="createTask"),
	path('setAsFinished/<int:id>', views.setAsFinished, name="setAsFinished"),
	path('deleteItem/<int:id>', views.deleteItem, name="deleteItem"),

]

