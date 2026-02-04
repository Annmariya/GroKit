from django.db import models
from Admin.models import*
from Guest.models import*
from Seller.models import tbl_product

# Create your models here.

class tbl_Complaint(models.Model):
    complaint_title=models.CharField(max_length=50)
    complaint_content=models.CharField(max_length=50)
    complaint_date=models.DateField(auto_now_add=True)
    complaint_replay=models.CharField(max_length=50 ,null=True)
    complaint_status=models.IntegerField(default=0)
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)
   

class tbl_booking(models.Model):
    booking_status=models.IntegerField(default=0)
    booking_date=models.DateField(auto_now_add=True)
    booking_amount = models.DecimalField(max_digits=10,decimal_places=2,null=True)
    deliveryboy=models.ForeignKey(tbl_deliveryboy,on_delete=models.CASCADE,null=True)
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)

class tbl_cart(models.Model):
    cart_quantity=models.IntegerField(default=1)
    cart_status=models.IntegerField(default=0)
    product=models.ForeignKey(tbl_product,on_delete=models.CASCADE)
    booking=models.ForeignKey(tbl_booking,on_delete=models.CASCADE)



class tbl_wishlist(models.Model):
    product=models.ForeignKey(tbl_product,on_delete=models.CASCADE)
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)  