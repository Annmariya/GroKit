from django.db import models
from Admin.models import*
from Seller.models import*
from Guest.models import*
from User.models import*


# Create your models here.

class tbl_product(models.Model):
    product_name=models.CharField(max_length=50)
    product_details=models.CharField(max_length=60)
    product_price=models.IntegerField(max_length=50)
    product_photo=models.FileField(upload_to ='Assets/ProductDocs')
    subcategory=models.ForeignKey(tbl_subcategory,on_delete=models.CASCADE)
    brand=models.ForeignKey(tbl_brand,on_delete=models.CASCADE)
    seller=models.ForeignKey(tbl_seller,on_delete=models.CASCADE)

class tbl_stock(models.Model):
    stock_date=models.DateField(auto_now_add=True)
    stock_count=models.IntegerField(max_length=20)
    product=models.ForeignKey(tbl_product,on_delete=models.CASCADE)

class tbl_gallery(models.Model):
    gallery_photo=models.FileField(upload_to ='Assets/GalleryDocs')
    product=models.ForeignKey(tbl_product,on_delete=models.CASCADE)
    