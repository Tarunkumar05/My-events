from . import views
from django.urls import path

app_name = 'events'
urlpatterns = [
    #/events/
    path('',views.index,name='index'),
    #/events/1
    path('<int:item_id>/',views.detail,name='detail'),
    path('item/',views.item,name='item'),
    # add items
    path('add',views.create_item,name='create_item'),
]

