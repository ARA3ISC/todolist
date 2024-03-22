from django.shortcuts import render, redirect
from app.models import Item
from django.http import HttpResponse
from django.forms import ModelForm

class todoListForm(ModelForm):
	class Meta:
		model = Item
		fields = '__all__'


# Create your views here.
def home(request):
	items = Item.objects.all()
	return render(request, 'app/home.html', {'items': items})

def itemDetails(request, id):
	item = Item.objects.get(id=id)
	return render(request, 'app/itemDetails.html', {"item": item})

def addingForm(request):
	form = todoListForm()
	return render(request, 'app/addingItem.html', {'addingForm': form})

def createTask(request):
	form = todoListForm()

	if request.method == "POST":
		form = todoListForm(request.POST)
		if (form.is_valid()):
			form.save()
			return redirect('home')

def setAsFinished(request, id):
	# MyModel.objects.get(pk=1).delete()
	item = Item.objects.get(id=id)
	if item.status != 'D':
		item.status = 'D'
	else:
		item.status = 'P'
	item.save()
	return redirect('home')

def deleteItem(request, id):
	# print("Method -------------------------------------	", request.method)
	# if request.method == "DELETE":
	# print(request.DELETE)
	item = Item.objects.get(id=id)
	item.delete()
	return redirect('home')
