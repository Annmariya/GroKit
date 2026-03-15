from django.db import models
from Admin.models import*
from Seller.models import*
from Guest.models import*
from User.models import*


# Create your models here.

class tbl_product(models.Model):
    UNIT= [
    ('kg', 'Kilogram'),   # weight
    ('g', 'Gram'),        # weight
    ('l', 'Litre'),       # volume
    ('ml', 'Millilitre'), # volume
]
    product_name=models.CharField(max_length=50)
    product_details=models.CharField(max_length=60)
    product_price=models.IntegerField(max_length=50)
    product_photo=models.FileField(upload_to ='Assets/ProductDocs')
    product_weight = models.IntegerField(null=True)
    weight_unit = models.CharField(max_length=10, choices=UNIT,null=True,blank=True)
    subcategory=models.ForeignKey(tbl_subcategory,on_delete=models.CASCADE)
    brand=models.ForeignKey(tbl_brand,on_delete=models.CASCADE)
    seller=models.ForeignKey(tbl_seller,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

class tbl_stock(models.Model):
    stock_date=models.DateField(auto_now_add=True)
    stock_count=models.IntegerField(max_length=20)
    product=models.ForeignKey(tbl_product,on_delete=models.CASCADE)

class tbl_gallery(models.Model):
    gallery_photo=models.FileField(upload_to ='Assets/GalleryDocs')
    product=models.ForeignKey(tbl_product,on_delete=models.CASCADE)
    