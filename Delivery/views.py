from django.shortcuts import render,redirect
from Seller.models import*
from Guest.models import*
from User.models import*
from Admin.models import*

# Create your views here.
def Homepage(request):
        # print(request.session['uid'])
        deliverydata=tbl_deliveryboy.objects.get(id=request.session['delid'])
        return render(request,"Delivery/Homepage.html",{'deliverydata':deliverydata})
def Myprofile (request):
     deliverydata=tbl_deliveryboy.objects.get(id=request.session['delid'])
     return render(request,"Delivery/Myprofile.html",{'deliverydata':deliverydata})

def Editprofile (request):
    deliverydata=tbl_deliveryboy.objects.get(id=request.session['delid'])
    if request.method=="POST":
         name=request.POST.get('txt_name')
         email=request.POST.get('txt_email')
         contact=request.POST.get('txt_contact')
         address=request.POST.get('txt_address')
         photo=request.FILES.get('txt_photo')
         deliverydata.delivery_name=name
         deliverydata.delivery_email=email
         deliverydata.delivery_contact=contact
         deliverydata.delivery_address=address
         if photo:  # update only if new image selected
            deliverydata.delivery_photo = photo
         deliverydata.save()
         return render(request,"Delivery/Editprofile.html",{'msg':'Data Updated'})
    else:
        return render(request,"Delivery/Editprofile.html",{'deliverydata':deliverydata})
    
def Changepassword (request):
    deliverydata=tbl_deliveryboy.objects.get(id=request.session['delid'])
    dbpass=deliverydata.delivery_password
    if request.method=="POST":
        oldpass=request.POST.get('txt_oldpass')
        newpass=request.POST.get('txt_newpass')
        retypepass=request.POST.get('txt_retypepass')
        if oldpass==dbpass: 
             if newpass==retypepass:
                  deliverydata.delivery_password=newpass
                  deliverydata.save()
                  return render(request,"Delivery/Changepassword.html",{'msg':'Password updated successfully'})
             else:
                return render(request,"Delivery/Changepassword.html",{'msg':'New password and confirm password do not match'})
        else:
            return render(request,"Delivery/Changepassword.html",{'msg':'Old password is incorrect'})
        
    else:
          return render(request,"Delivery/Changepassword.html",{'deliverydata':deliverydata})
 
# def Mydelivery(request):
#     if 'delid' not in request.session:
#         return redirect('Guest:Login')
#     else:
       
#        bookings = tbl_booking.objects.filter(tbl_cart__product__deliveryboy_id=request.session['delid'],booking_status__gte=2).distinct().order_by('-booking_date')
#        return render(request, 'Delivery/Mydelivery.html', {'bookings': bookings})

# def Mydelivery(request):
#     if 'delid' not in request.session:
#         return redirect('Guest:Login')

#     delid = request.session['delid']

#     available_orders = tbl_booking.objects.filter(
#         deliveryboy__isnull=True,
#         tbl_cart__cart_status__gte=4,
#         booking_status__gte=2
#     ).distinct()

#     my_orders = tbl_booking.objects.filter(
#         deliveryboy_id=delid,
#         tbl_cart__cart_status__gte=4,
#         booking_status__gte=3
#     ).distinct()

#     bookings = (available_orders | my_orders).distinct()

#     return render(request, 'Delivery/Mydelivery.html', {'bookings': bookings})




def Mydelivery(request):
    if 'delid' not in request.session:
        return redirect('Guest:Login')

    delid = request.session['delid']

    available_orders = tbl_booking.objects.filter(
        deliveryboy__isnull=True,
        tbl_cart__cart_status__gte=4,
        booking_status__gte=2
    ).distinct()

    my_orders = tbl_booking.objects.filter(
        deliveryboy_id=delid,
        tbl_cart__cart_status__gte=4,
        booking_status__gte=3
    ).distinct()

    bookings = (available_orders | my_orders).distinct().order_by('-booking_date')

    # Date Filter
    from_date = request.GET.get('from_date')
    to_date = request.GET.get('to_date')

    if from_date:
        bookings = bookings.filter(booking_date__gte=from_date)

    if to_date:
        bookings = bookings.filter(booking_date__lte=to_date)

    context = {
        'bookings': bookings,
        'from_date': from_date,
        'to_date': to_date
    }

    return render(request, 'Delivery/Mydelivery.html', context)
    

# def UpdateCartStatus(request, cid, status):
#     cart = tbl_cart.objects.get(id=cid)
#     cart.cart_status = status
#     cart.save()
#     booking = cart.booking
#     total_items = tbl_cart.objects.filter(booking=booking).count()
#     delivered_items = tbl_cart.objects.filter(booking=booking,cart_status=7).count()
#     if total_items == delivered_items:
#         booking.booking_status = 3
#         booking.save()
#     return redirect("Delivery:Mydelivery")



def UpdateCartStatus(request, cid, status):
    cart = tbl_cart.objects.get(id=cid)
    cart.cart_status = status
    cart.save()

    booking = cart.booking

    # Assign delivery boy when item is collected
    if status == 5:
        booking.deliveryboy_id = request.session['delid']
        booking.save()

    total_items = tbl_cart.objects.filter(booking=booking).count()
    delivered_items = tbl_cart.objects.filter(booking=booking, cart_status=7).count()

    if total_items == delivered_items:
        booking.booking_status = 4
        booking.save()

    return redirect("Delivery:Mydelivery")


def Logout(request):
       del request.session['delid']
       return redirect("Guest:Login")



def Deliveryorder(request):
    if 'delid' not in request.session:
        return redirect('Guest:Login')

    delid = request.session['delid']

    deliveryorder = tbl_booking.objects.filter(
        deliveryboy_id=delid,
        tbl_cart__cart_status__gte=6,
        booking_status__gte=4
    ).distinct()

    return render(request, 'Delivery/Deliveryorder.html', {'deliveryorder': deliveryorder})
