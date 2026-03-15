from django.db import models
from Admin.models import*
# Create your models here.

class tbl_user(models.Model):
    user_name=models.CharField(max_length=50)
    user_gender=models.CharField(max_length=50)
    user_contact=models.CharField(max_length=15)
    user_email=models.CharField(max_length=50)
    user_password=models.CharField(max_length=50)
    user_address=models.CharField(max_length=50)
    user_place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
    user_photo=models.FileField(upload_to ='Assets/UserDocs')
    user_status=models.IntegerField(default=0)

class tbl_seller(models.Model):
    seller_name=models.CharField(max_length=50)
    seller_contact=models.CharField(max_length=15)
    seller_email=models.CharField(max_length=50)
    seller_password=models.CharField(max_length=50)
    seller_establishdate=models.CharField(max_length=50)
    seller_licenseno=models.CharField(max_length=50)
    seller_ownername=models.CharField(max_length=50)
    seller_place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
    seller_licenseproof=models.FileField(upload_to ='Assets/SellerDocs')
    seller_ownerproof=models.FileField(upload_to ='Assets/SellerDocs')
    seller_status=models.IntegerField(default=0)

class tbl_deliveryboy(models.Model):
    delivery_name=models.CharField(max_length=50)
    delivery_gender=models.CharField(max_length=50)
    delivery_email=models.CharField(max_length=50)
    delivery_contact=models.CharField(max_length=15)
    delivery_address=models.CharField(max_length=50)
    delivery_photo=models.FileField(upload_to ='Assets/DeliveryboyDocs')
    delivery_proof=models.FileField(upload_to ='Assets/DeliveryboyDocs')
    delivery_place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
    delivery_status=models.IntegerField(default=0)
    delivery_password=models.CharField(max_length=50)
    delivery_doj=models.DateField(auto_now_add=True)




