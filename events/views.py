from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Item
from django.template import loader
from .forms import ItemForm
from django.core.paginator import Paginator
from django.db.models import Count

# Create your views here.

def index(request):
    item_list = Item.objects.all()

    item_name = request.GET.get('item_name')
    item_category = request.GET.get('item_category')
    item_location = request.GET.get('item_location')
    item_date = request.GET.get('item_date')

    if item_name:
        item_list = item_list.filter(item_name__icontains=item_name)
    
    if item_category:
        item_list = item_list.filter(item_category=item_category)

    if item_location:
        item_list = item_list.filter(item_location=item_location)

    if item_date:
        item_list = item_list.filter(item_date=item_date)


    categories = Item.objects.values('item_category').annotate(count=Count('item_category'))
    locations = Item.objects.values_list('item_location', flat=True).distinct()
    dates = Item.objects.values_list('item_date', flat=True).distinct()

    paginator = Paginator(item_list,6)
    page = request.GET.get('page')
    item_list = paginator.get_page(page)
    
    context ={
        'item_list':item_list,
        'categories': [category['item_category'] for category in categories],
        'locations': locations,
        'dates': dates,
    }
    return render(request,'events/index.html',context)

def item(request):
    return HttpResponse('<h1>This is an item view<h1>')

def detail(request,item_id):
    item = Item.objects.get(pk=item_id)
    context ={
        'item':item,
    }
    return render(request,'events/detail.html',context)

def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('events:index')

    return render(request,'events/item-form.html',{'form':form})