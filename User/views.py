from django.http import JsonResponse
from django.shortcuts import render,redirect,get_object_or_404
from User.models import*
from Guest.models import*
from Admin.models import*
from Seller.models import*
from django.db.models import Sum
from datetime import datetime
from django.utils import timezone
from datetime import date
from django.conf import settings
from django.core.mail import send_mail

from django.utils import timezone
from datetime import timedelta
from .models import tbl_subscription, tbl_plan

# new point

# Create your views here.
def Myprofile (request):
     userdata=tbl_user.objects.get(id=request.session['uid'])
     return render(request,"User/Myprofile.html",{'userdata':userdata})

def Editprofile (request):
    userdata=tbl_user.objects.get(id=request.session['uid'])
    if request.method=="POST":
         name=request.POST.get('txt_name')
         email=request.POST.get('txt_email')
         contact=request.POST.get('txt_contact')
         address=request.POST.get('txt_address')
         photo=request.FILES.get('txt_photo')
         userdata.user_name=name
         userdata.user_email=email
         userdata.user_contact=contact
         userdata.user_address=address
         if photo:  # update only if new image selected
            userdata.user_photo = photo
         userdata.save()
         return render(request,"User/Editprofile.html",{'msg':'Data Updated'})
    else:
        return render(request,"User/Editprofile.html",{'userdata':userdata})

def Changepassword (request):
    userdata=tbl_user.objects.get(id=request.session['uid'])
    dbpass=userdata.user_password
    if request.method=="POST":
        oldpass=request.POST.get('txt_oldpass')
        newpass=request.POST.get('txt_newpass')
        retypepass=request.POST.get('txt_retypepass')
        if oldpass==dbpass: 
             if newpass==retypepass:
                  userdata.user_password=newpass
                  userdata.save()
                  return render(request,"User/Changepassword.html",{'msg':'Password updated successfully'})
             else:
                return render(request,"User/Changepassword.html",{'msg':'New password and confirm password do not match'})
        else:
            return render(request,"User/Changepassword.html",{'msg':'Old password is incorrect'})
        
    else:
          return render(request,"User/Changepassword.html",{'userdata':userdata})
        
def Homepage(request):
        if 'uid' not in request.session:
             return redirect("Guest:Login")
        # print(request.session['uid'])
        userdata=tbl_user.objects.get(id=request.session['uid'])
        productviewdata=tbl_product.objects.all()
        branddata=tbl_brand.objects.all()
        categorydata=tbl_category.objects.all()
        subcategorydata=tbl_subcategory.objects.all()

        new_products = tbl_product.objects.all().order_by('-id')[:8]


        if request.method == "POST":
            productname = request.POST.get('txt_productname')
            category = request.POST.get('sel_category')
            subcategory = request.POST.get('sel_subcategory')
            brand = request.POST.get('sel_brand')

            productviewdata = tbl_product.objects.all()
            if productname:
                productviewdata = productviewdata.filter(product_name__icontains=productname)
            if category:
                productviewdata = productviewdata.filter(subcategory__category_id=category)
            if subcategory:
                productviewdata = productviewdata.filter(subcategory_id=subcategory)
            if brand:
                productviewdata = productviewdata.filter(brand_id=brand)
    
        for i in productviewdata:
            total_stock = tbl_stock.objects.filter(
                product=i.id
            ).aggregate(total=Sum('stock_count'))['total'] or 0

            total_cart = tbl_cart.objects.filter(
                product=i.id,
                cart_status=1
            ).aggregate(total=Sum('cart_quantity'))['total'] or 0

            i.total_stock = total_stock - total_cart

            tot = 0  
        return render(request,"User/Homepage.html",{'new_products':new_products,'userdata':userdata,'productviewdata':productviewdata,'branddata':branddata,'categorydata':categorydata,'subcategorydata':subcategorydata})





     
def Complaint(request): 
       userdata=tbl_user.objects.get(id=request.session['uid'])
       complaintdata=tbl_Complaint.objects.filter(user=request.session['uid'])  
       if request.method=="POST":
                title=request.POST.get("txt_title")
                content=request.POST.get("txt_content")
                tbl_Complaint.objects.create(complaint_title=title,complaint_content=content,user=userdata)
                return render(request,"User/Complaint.html",{'msg':"Data Inserted"})
       else:
            return render(request,"User/Complaint.html",{'complaintdata':complaintdata})

def delecomplaint(request,cid):
        tbl_Complaint.objects.get(id=cid).delete()
        return redirect("User:Complaint")




def Viewproduct(request):
    productviewdata=tbl_product.objects.all()
    branddata=tbl_brand.objects.all()
    categorydata=tbl_category.objects.all()
    subcategorydata=tbl_subcategory.objects.all()

    if request.method == "POST":
         productname = request.POST.get('txt_productname')
         category = request.POST.get('sel_category')
         subcategory = request.POST.get('sel_subcategory')
         brand = request.POST.get('sel_brand')

         productviewdata = tbl_product.objects.all()
         if productname:
            productviewdata = productviewdata.filter(product_name__icontains=productname)
         if category:
              productviewdata = productviewdata.filter(subcategory__category_id=category)
         if subcategory:
            productviewdata = productviewdata.filter(subcategory_id=subcategory)
         if brand:
            productviewdata = productviewdata.filter(brand_id=brand)
    
    
    for i in productviewdata:
        total_stock = tbl_stock.objects.filter(
            product=i.id
        ).aggregate(total=Sum('stock_count'))['total'] or 0

        total_cart = tbl_cart.objects.filter(
            product=i.id,
            cart_status=1
        ).aggregate(total=Sum('cart_quantity'))['total'] or 0

        i.total_stock = total_stock - total_cart
        tot = 0
       
    return render(request,"User/Viewproduct.html",{'productviewdata':productviewdata,'branddata':branddata,'categorydata':categorydata,'subcategorydata':subcategorydata})


def ViewMore(request, pid):

    product = tbl_product.objects.get(id=pid)

    gallery = tbl_gallery.objects.filter(product=product)

    total_stock = tbl_stock.objects.filter(
        product=product
    ).aggregate(total=Sum('stock_count'))['total'] or 0

    total_cart = tbl_cart.objects.filter(
        product=product,
        cart_status=1
    ).aggregate(total=Sum('cart_quantity'))['total'] or 0

    available = total_stock - total_cart

    ratecount = tbl_rating.objects.filter(product=product).count()
    avg = 0

    if ratecount > 0:
        total_rating = tbl_rating.objects.filter(product=product)\
            .aggregate(total=Sum('rating_value'))['total'] or 0
        avg = total_rating // ratecount

    seller = product.seller
    ar = [1, 2, 3, 4, 5]

    simlarproduct = tbl_product.objects.filter(
        subcategory__category=product.subcategory.category
    ).exclude(id=product.id)[:12]

    for sp in simlarproduct:

        sp_stock = tbl_stock.objects.filter(
            product=sp
        ).aggregate(total=Sum('stock_count'))['total'] or 0

        sp_cart = tbl_cart.objects.filter(
            product=sp,
            cart_status=1
        ).aggregate(total=Sum('cart_quantity'))['total'] or 0

        sp.available = sp_stock - sp_cart

        sp_ratecount = tbl_rating.objects.filter(product=sp).count()
        sp.ratecount = sp_ratecount

        if sp_ratecount > 0:
            sp_total_rating = tbl_rating.objects.filter(product=sp)\
                .aggregate(total=Sum('rating_value'))['total'] or 0
            sp.avg = sp_total_rating // sp_ratecount
        else:
            sp.avg = 0

    return render(request, 'User/ViewMore.html', {
        'product': product,
        'gallery': gallery,
        'available': available,
        'avg': avg,
        'ratecount': ratecount,
        'seller': seller,
        'ar': ar,
        'simlarproduct': simlarproduct
    })





def Addtocart(request,pid):
   
    userdata = tbl_user.objects.get(id=request.session['uid'])
    productdata=tbl_product.objects.get(id=pid)
    bookingcount=tbl_booking.objects.filter(user=userdata,booking_status=0).count()
    if bookingcount>0:
        booking=tbl_booking.objects.get(user=userdata,booking_status=0)
        cartcount=tbl_cart.objects.filter(product=productdata,cart_status=0,booking=booking).count()
        
        if cartcount>0:
             return render(request,"User/Viewproduct.html",{'msg':"Already Added in cart"})
        else:
             tbl_cart.objects.create(product=productdata,booking=booking)
             return render(request,"User/Viewproduct.html",{'msg':"Data Added in cart"})
    else:
        bookingdata=tbl_booking.objects.create(user=userdata)
        cartdata=tbl_cart.objects.create(product=productdata,booking=bookingdata)
        return render(request,"User/Viewproduct.hml",{'bookingdata':bookingdata,'cartdata':cartdata,'msg':"Data Added in cart"})



def MyCart(request):
    if request.method=="POST":
        bookingdata=tbl_booking.objects.get(id=request.session["bookingid"])
        bookingdata.booking_amount=request.POST.get("carttotalamt")
        bookingdata.booking_status=1
        bookingdata.save()
        cart = tbl_cart.objects.filter(booking=bookingdata)
        for i in cart:
            i.cart_status = 1
            i.save()
        return redirect("User:Payment")
    else:
        bookcount = tbl_booking.objects.filter(user=request.session["uid"],booking_status=0).count()
        if bookcount > 0:
            book = tbl_booking.objects.get(user=request.session["uid"],booking_status=0)
            request.session["bookingid"] = book.id
            cart = tbl_cart.objects.filter(booking=book)
            for i in cart:
                total_stock = tbl_stock.objects.filter(product=i.product.id).aggregate(total=Sum('stock_count'))['total']
                total_cart = tbl_cart.objects.filter(product=i.product.id, cart_status=1).aggregate(total=Sum('cart_quantity'))['total']
                # print(total_stock)
                # print(total_cart)
                if total_stock is None:
                    total_stock = 0
                if total_cart is None:
                    total_cart = 0
                total =  total_stock - total_cart
                i.total_stock = total
            return render(request,"User/MyCart.html",{'cartdata':cart,'book':book})
        else:
            return render(request,"User/MyCart.html")
   
def DelCart(request,did):
   tbl_cart.objects.get(id=did).delete()
   return redirect("User:MyCart")

def CartQty(request):
   qty=request.GET.get('QTY')
   cartid=request.GET.get('ALT')
   cartdata=tbl_cart.objects.get(id=cartid)
   cartdata.cart_quantity=qty
   cartdata.save()
   return redirect("User:MyCart")

def MyBooking(request):
    bookingdata = tbl_booking.objects.filter(
        user_id=request.session['uid']
    ).order_by('-booking_date')

    from_date = request.GET.get('from_date')
    to_date = request.GET.get('to_date')

    # Apply filters only if value exists
    if from_date:
        bookingdata = bookingdata.filter(
            booking_date__gte=from_date
        )

    if to_date:
        bookingdata = bookingdata.filter(
            booking_date__lte=to_date
        )

    context = {
        'bookingdata': bookingdata,
        'from_date': from_date,
        'to_date': to_date
    }

    return render(request, "User/MyBooking.html", context)



def Payment(request):
        bookingdata=tbl_booking.objects.get(id=request.session['bookingid'])
        # Only this booking's cart items
        cardtdata=tbl_cart.objects.filter(booking=bookingdata, cart_status=1)
        if request.method == "POST":
             bookingdata.booking_status = 1 
             bookingdata.save()
             cart = tbl_cart.objects.filter(booking=bookingdata)
             for i in cart:
                i.cart_status = 2
                i.save()
                email=bookingdata.user.user_email
                send_mail(
            'Respected Sir/Madam ',#subject
            "\rYour request was rejected becacuse of"
            "\r1, You are not identified. "
            "\r2, if you have a proof of id , you will be accepted within two or three days."
            "\r By"
            "\r ecobloom" ,#body
            settings.EMAIL_HOST_USER,
            [email],
        )
                
             return render(request,"User/Homepage.html",{'msg':'Payment Successful'})
        else:
             return render(request,"User/Payment.html",{'bookingdata':bookingdata,'cardtdata':cardtdata})
        
             
def Index(request):
       return render(request,"User/Index.html")


def Logout(request):
       del request.session['uid']
       return redirect("Guest:Login")


def Viewrecipe(request):
     viewrecipedata=tbl_recipe.objects.all()
     return render(request,"User/Viewrecipe.html",{'viewrecipedata':viewrecipedata})
     

def Viewingrediants(request,rid):
      viewingredientdata=tbl_ingredients.objects.filter(recipe=rid)
      return render(request,"User/Viewingrediants.html",{'viewingredientdata':viewingredientdata})
       
def Addwishlist(request,pid):
    if 'uid' not in request.session:
             return redirect("Guest:Login")
    userdata = tbl_user.objects.get(id=request.session['uid'])
    productdata=tbl_product.objects.get(id=pid)
    wishlistcount = tbl_wishlist.objects.filter(user=userdata,product=productdata).count() 
    if wishlistcount > 0:
        return render(request,"User/Homepage.html",{'msg':"Product Already Added in Whishlist"})
    else:
        wishlistdata=tbl_wishlist.objects.create(user=userdata,product=productdata)
        return render(request,"User/Homepage.html",{'wishlistdata':wishlistdata,'msg':"Product Added in Whishlist"})

def Mywishlist(request):
     userdata = tbl_user.objects.get(id=request.session['uid'])
     viewwishlistdata=tbl_wishlist.objects.filter(user=userdata)
     return render(request,"User/Mywishlist.html",{'viewwishlistdata':viewwishlistdata,'userdata':userdata})



def Delwishlist(request,wid):
   tbl_wishlist.objects.get(id=wid).delete()
   return redirect("User:Mywishlist")


def time_based_recipe(request):
    current_time = datetime.now().time()

    mealdata = tbl_mealtype.objects.filter(
        meal_fromtime__lte=current_time,
        meal_totime__gte=current_time
    ).first()

    if mealdata:
        recipedata = tbl_recipe.objects.filter(mealtype=mealdata)
        meal = mealdata.mealtype_name
    else:
        recipedata = tbl_recipe.objects.all()
        meal = "Recommended"

    return render(request,"User/TimeBasedRecipe.html",{
        'recipedata':recipedata,
        'meal':meal
    })

def Addtocart1(request,pid):
   
    userdata = tbl_user.objects.get(id=request.session['uid'])
    productdata=tbl_product.objects.get(id=pid)
    bookingcount=tbl_booking.objects.filter(user=userdata,booking_status=0).count()
    if bookingcount>0:
        booking=tbl_booking.objects.get(user=userdata,booking_status=0)
        cartcount=tbl_cart.objects.filter(product=productdata,cart_status=0,booking=booking).count()
        
        if cartcount>0:
             return render(request,"User/Homepage.html",{'msg':"Already Added in cart"})
        else:
             tbl_cart.objects.create(product=productdata,booking=booking)
             return render(request,"User/Homepage.html",{'msg':"Data Added in cart"})
    else:
        bookingdata=tbl_booking.objects.create(user=userdata)
        cartdata=tbl_cart.objects.create(product=productdata,booking=bookingdata)
        return render(request,"User/Homepage.hml",{'bookingdata':bookingdata,'cartdata':cartdata,'msg':"Data Added in cart"})

def rating(request,mid):
    parray=[1,2,3,4,5]
    mid=mid
    # wdata=tbl_booking.objects.get(id=mid)
    
    counts=0
    counts=stardata=tbl_rating.objects.filter(product=mid).count()
    if counts>0:
        res=0
        stardata=tbl_rating.objects.filter(product=mid).order_by('-rating_datetime')
        for i in stardata:
            res=res+i.rating_value
        avg=res//counts
        # print(avg)
        return render(request,"User/Rating.html",{'mid':mid,'data':stardata,'ar':parray,'avg':avg,'count':counts})
    else:
         return render(request,"User/Rating.html",{'mid':mid})
    
def ajaxstar(request):
    parray=[1,2,3,4,5]
    rating_value=request.GET.get('rating_data')
    
    user_review=request.GET.get('user_review')
    pid=request.GET.get('pid')
    # wdata=tbl_booking.objects.get(id=pid)
    tbl_rating.objects.create(user=tbl_user.objects.get(id=request.session['uid']),rating_content=user_review,rating_value=rating_value,product=tbl_product.objects.get(id=pid))
    stardata=tbl_rating.objects.filter(product=pid).order_by('-rating_datetime')
    return render(request,"User/AjaxRating.html",{'data':stardata,'ar':parray})

def starrating(request):
    r_len = 0
    five = four = three = two = one = 0
    # cdata = tbl_booking.objects.get(id=request.GET.get("pdt"))
    rate = tbl_rating.objects.filter(product=request.GET.get("pdt"))
    ratecount = tbl_rating.objects.filter(product=request.GET.get("pdt")).count()
    for i in rate:
        if int(i.rating_value) == 5:
            five = five + 1
        elif int(i.rating_value) == 4:
            four = four + 1
        elif int(i.rating_value) == 3:
            three = three + 1
        elif int(i.rating_value) == 2:
            two = two + 1
        elif int(i.rating_value) == 1:
            one = one + 1
        else:
            five = four = three = two = one = 0
        # print(i.rating_value)
        # r_len = r_len + int(i.rating_value)
    # rlen = r_len // 5
    # print(rlen)
    result = {"five":five,"four":four,"three":three,"two":two,"one":one,"total_review":ratecount}
    return JsonResponse(result)

def ViewSubscription(request,):
    all_plans = tbl_plan.objects.all()
    return render(request, "User/ViewSubscription.html", {
        'all_plans': all_plans,   # for dropdown
    })

def Subscription(request, planid):
    if 'uid' not in request.session:
        return redirect('login')

    plan = get_object_or_404(tbl_plan, id=planid)
    user = get_object_or_404(tbl_user, id=request.session['uid'])

    # Deactivate old subscriptions
    tbl_subscription.objects.filter(user=user, is_active=True).update(is_active=False)

    expiry = timezone.now() + timedelta(days=int(plan.plan_duration))

    tbl_subscription.objects.create(
        user=user,
        plan=plan,
        expiry_date=expiry,
        is_active=True
    )

    return render(request, 'User/ViewSubscription.html', {'msg': "Subscribed Successfully"})

def check_subscription(user):
    try:
        subscription = tbl_subscription.objects.get(user=user, is_active=True)

        if subscription.expiry_date < timezone.now():
            subscription.is_active = False
            subscription.save()
            return False

        return True

    except tbl_subscription.DoesNotExist:
        return False

def Viewdietinfo(request):
    if 'uid' not in request.session:
        return redirect('login')
    user = tbl_user.objects.get(id=request.session['uid'])
    if not check_subscription(user):
        return redirect("User:ViewSubscription")
    viewdata=tbl_recipe.objects.all()  
    return render(request,"User/Viewdietinfo.html",{'viewdata':viewdata})

def Viewrating(request,mid):
    parray=[1,2,3,4,5]
    mid=mid
    # wdata=tbl_booking.objects.get(id=mid)
    
    counts=0
    counts=stardata=tbl_rating.objects.filter(product=mid).count()
    if counts>0:
        res=0
        stardata=tbl_rating.objects.filter(product=mid).order_by('-rating_datetime')
        for i in stardata:
            res=res+i.rating_value
        avg=res//counts
        # print(avg)
        return render(request,"User/Viewrating.html",{'mid':mid,'data':stardata,'ar':parray,'avg':avg,'count':counts})
    else:
         return render(request,"User/Viewrating.html",{'mid':mid})

# if 'uid' not in request.session:
#         return redirect('login')
#     user = tbl_user.objects.get(id=request.session['uid'])
#     if not check_subscription(user):
#         return redirect("User:ViewSubscription")



