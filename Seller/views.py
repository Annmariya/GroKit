from django.shortcuts import render,redirect
from Seller.models import*
from Guest.models import*
from Admin.models import*
from User.models import*


# Create your views here.
def Myprofile (request):
     sellerdata=tbl_seller.objects.get(id=request.session['sid'])
     return render(request,"Seller/Myprofile.html",{'sellerdata':sellerdata})

def Editprofile (request):
    sellerdata=tbl_seller.objects.get(id=request.session['sid'])
    if request.method=="POST":
         name=request.POST.get('txt_name')
         email=request.POST.get('txt_email')
         contact=request.POST.get('txt_contact')
         sellerdata.seller_name=name
         sellerdata.seller_email=email
         sellerdata.seller_contact=contact
         sellerdata.save()
         return render(request,"Seller/Editprofile.html",{'msg':'Data Updated'})
    else:
        return render(request,"Seller/Editprofile.html",{'sellerdata':sellerdata})

def Changepassword (request):
    sellerdata=tbl_seller.objects.get(id=request.session['sid'])
    dbpass=sellerdata.seller_password
    if request.method=="POST":
        oldpass=request.POST.get('txt_oldpass')
        newpass=request.POST.get('txt_newpass')
        retypepass=request.POST.get('txt_retypepass')
        if oldpass==dbpass: 
             if newpass==retypepass:
                  sellerdata.seller_password=newpass
                  sellerdata.save()
                  return render(request,"Seller/Changepassword.html",{'msg':'Password updated successfully'})
             else:
                return render(request,"Seller/Changepassword.html",{'msg':'New password and confirm password do not match'})
        else:
            return render(request,"Seller/Changepassword.html",{'msg':'Old password is incorrect'})
        
    else:
          return render(request,"Seller/Changepassword.html",{'sellerdata':sellerdata})
        
    

def Homepage(request):
        # print(request.session['uid'])
      
        sellerdata=tbl_seller.objects.get(id=request.session['sid'])
        return render(request,"Seller/Homepage.html",{'sellerdata':sellerdata})




def Product(request):
        sellerdata=tbl_seller.objects.get(id=request.session['sid'])
        subcategorydata=tbl_subcategory.objects.all()
        categorydata=tbl_category.objects.all()
        branddata=tbl_brand.objects.all()
        productdata=tbl_product.objects.all()  
        if request.method=="POST":
                brand=tbl_brand.objects.get(id=request.POST.get("sel_brand"))
                subcategory=tbl_subcategory.objects.get(id=request.POST.get("sel_subcategory"))
                # district=tbl_district.objects.get(id=request.POST.get("sel_district"))
                name=request.POST.get("txt_productname")
                details=request.POST.get("txt_productdetails")
                photo=request.FILES.get("txt_photo")
                price=request.POST.get("txt_price")
                tbl_product.objects.create(product_name=name,product_details=details,product_price=price,product_photo=photo,subcategory=subcategory,brand=brand,seller=sellerdata)
                return render(request,"Seller/Product.html",{'msg':"Data inserted"})
        
        else:
                return render(request,"Seller/Product.html",{'subcategorydata':subcategorydata,'categorydata':categorydata,'branddata':branddata,'sellerdata':sellerdata,'productdata':productdata})

def Ajaxproduct(request):
        categoryid=request.GET.get('did')
        subcategorydata=tbl_subcategory.objects.filter(category=categoryid)
        return render(request,"Seller/Ajaxproduct.html",{'subcategorydata':subcategorydata})



def delproduct(request,pid):
        tbl_product.objects.get(id=pid).delete()
        return redirect("Seller:Product")


def Stock(request,pid):
        stockdata=tbl_stock.objects.all() 
        Product=tbl_product.objects.get(id=pid)
        if request.method=="POST":
                stock=request.POST.get("txt_stock")
                tbl_stock.objects.create(stock_count=stock,product=Product)
                return render(request,"Seller/Stock.html",{'msg':"Data inserted",'pid':pid})
        
        else:
               return render(request,"Seller/Stock.html",{'stockdata':stockdata,'pid':pid})
        
        
def delestock(request,soid,pid):
        tbl_stock.objects.get(id=soid).delete()
        return redirect("Seller:Stock",pid)


def Gallery(request,pid):
        gallerydata=tbl_gallery.objects.all() 
        Product=tbl_product.objects.get(id=pid)
        if request.method=="POST":
                photo=request.FILES.get("txt_photo")
                tbl_gallery.objects.create(gallery_photo=photo,product=Product)
                return render(request,"Seller/Gallery.html",{'msg':"Data inserted",'pid':pid})
        else:
               return render(request,"Seller/Gallery.html",{'gallerydata':gallerydata,'pid':pid})




def delegallery(request,gid,pid):
        tbl_gallery.objects.get(id=gid).delete()
        return redirect("Seller:Gallery",pid)

def ViewBookings(request):
    if 'sid' not in request.session:
        return redirect('Guest:Login')
    else:
       bookings = tbl_booking.objects.filter(tbl_cart__product__seller_id=request.session['sid']).distinct()
       return render(request, 'Seller/ViewBookings.html', {'bookings': bookings})

def UpdateCartStatus(request, cid, status):
    cart = tbl_cart.objects.get(id=cid)
    cart.cart_status = status
    cart.save()
    booking = cart.booking
    total_items = tbl_cart.objects.filter(booking=booking).count()
    delivered_items = tbl_cart.objects.filter(booking=booking,cart_status=6).count()
    if total_items == delivered_items:
        booking.booking_status = 3
        booking.save()
    return redirect("Seller:ViewBookings")
def Logout(request):
       del request.session['sid']
       return redirect("Guest:Login")