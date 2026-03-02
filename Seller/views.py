from django.http import HttpResponse
from django.shortcuts import render,redirect
from Seller.models import*
from Guest.models import*
from Admin.models import*
from User.models import*
from django.db.models import Sum



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
        # productdata=tbl_product.objects.all() 

        # recent_products = tbl_product.objects.filter(
        #     seller=sellerdata
        # ).order_by('-id')[:5]
        productdata = tbl_product.objects.filter(seller=sellerdata)
        total_value = productdata.aggregate(total=Sum('product_price'))['total'] or 0
        recent_products = productdata.order_by('-id')[:5]
        
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
                return render(request,"Seller/Product.html",{'subcategorydata':subcategorydata,'categorydata':categorydata,'branddata':branddata,'sellerdata':sellerdata,'productdata':productdata,'recent_products':recent_products,'total_value':total_value})

def Ajaxproduct(request):
        categoryid=request.GET.get('did')
        subcategorydata=tbl_subcategory.objects.filter(category=categoryid)
        return render(request,"Seller/Ajaxproduct.html",{'subcategorydata':subcategorydata})



def delproduct(request,pid):
        tbl_product.objects.get(id=pid).delete()
        return render(request,"Seller/Product.html",{'msg':"Data Deleted"})
        # return redirect("Seller:Product")


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
        return render(request,"Seller/Gallery.html",{'msgDelete':"Data Deleted Successfully",'pid':pid})
        # return redirect("Seller:Gallery",pid)

# def ViewBookings(request):
#     if 'sid' not in request.session:
#         return redirect('Guest:Login')
#     else:
#        bookings = tbl_booking.objects.filter(tbl_cart__product__seller_id=request.session['sid']).distinct()
#        return render(request, 'Seller/ViewBookings.html', {'bookings': bookings})


def ViewBookings(request):
    if 'sid' not in request.session:
        return redirect('Guest:Login')

    bookings = tbl_booking.objects.filter(
        tbl_cart__product__seller_id=request.session['sid']
    ).distinct().order_by('-booking_date')

    from_date = request.GET.get('from_date')
    to_date = request.GET.get('to_date')

    # Apply date filtering safely
    if from_date:
        bookings = bookings.filter(booking_date__gte=from_date)

    if to_date:
        bookings = bookings.filter(booking_date__lte=to_date)

    context = {
        'bookings': bookings,
        'from_date': from_date,
        'to_date': to_date
    }

    return render(request, 'Seller/ViewBookings.html', context)

# def UpdateCartStatus(request, cid, status):
#     cart = tbl_cart.objects.get(id=cid)
#     cart.cart_status = status
#     cart.save()
#     booking = cart.booking
#     total_items = tbl_cart.objects.filter(booking=booking).count()
# #     shipped_item=tbl_cart.objects.filter(booking=booking,cart_status=4).count()
#     delivered_items = tbl_cart.objects.filter(booking=booking,cart_status=6).count()
    
#     if total_items == delivered_items:
#         booking.booking_status = 4
#         booking.save()
#     return redirect("Seller:ViewBookings")


def UpdateCartStatus(request, cid, status):
    cart = tbl_cart.objects.get(id=cid)
    cart.cart_status = status
    cart.save()

    booking = cart.booking

    total_items = tbl_cart.objects.filter(booking=booking).count()

    shipped_items = tbl_cart.objects.filter(
        booking=booking,
        cart_status__gte=4   # shipped or beyond
    ).count()

    delivered_items = tbl_cart.objects.filter(
        booking=booking,
        cart_status=6
    ).count()

    # If ALL items shipped → booking ready for delivery
    if total_items == shipped_items:
        booking.booking_status = 3

    # If ALL items delivered → booking completed
    if total_items == delivered_items:
        booking.booking_status = 4

    booking.save()

    return redirect("Seller:ViewBookings")





def Logout(request):
       del request.session['sid']
       return redirect("Guest:Login")



































# def AssignDelivery(request, bid):
#     if 'sid' not in request.session:
#         return redirect('Guest:Login')

#     deliveryboys = tbl_deliveryboy.objects.all()

#     return render(request, 'Seller/AssignDelivery.html', {
#         'deliveryboys': deliveryboys,
#         'bid': bid
#     })


# def ConfirmAssign(request, bid, did):
#     if 'sid' not in request.session:
#         return redirect('Guest:Login')

#     booking = tbl_booking.objects.get(id=bid)
#     deliveryboy = tbl_deliveryboy.objects.get(id=did)

#     # Only store delivery person in booking table
#     booking.deliveryboy = deliveryboy
#     booking.booking_status = 3  # Assigned
#     booking.save()

#     return redirect('Seller:ViewBookings')








































