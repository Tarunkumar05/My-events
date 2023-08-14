from django.db import models

# Create your models here.
class Item(models.Model):

    def __str__(self):
        return self.item_name
    
    item_name = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_location = models.CharField(max_length=200)
    item_description = models.CharField(max_length=200)
    item_date = models.DateField(null=True, blank=True)
    item_category = models.CharField(max_length=200)
    item_image = models.CharField(max_length=500,default="https://t3.ftcdn.net/jpg/02/48/42/64/360_F_248426448_NVKLywWqArG2ADUxDq6QprtIzsF82dMF.jpg")


    def formatted_date(self):
        if self.item_date:
            return self.item_date.strftime('%d-%B')  
        return ''
