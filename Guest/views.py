from django.shortcuts import render,redirect
from Guest.models import*
from Admin.models import*
from User.models import*
from Seller.models import*

def Newuser(request):
        placedata=tbl_place.objects.all()
        districtdata=tbl_district.objects.all()
        # userdata=tbl_user.objects.all()  
        if request.method=="POST":
                place=tbl_place.objects.get(id=request.POST.get("sel_place"))
                # district=tbl_district.objects.get(id=request.POST.get("sel_district"))
                name=request.POST.get("txt_name")
                gender=request.POST.get("gender")
                contact=request.POST.get("txt_contact")
                email=request.POST.get("txt_email")
                password=request.POST.get("txt_password")
                address=request.POST.get("txt_address")
                photo=request.FILES.get("txt_photo")
                usercount=tbl_user.objects.filter(user_email=email).count()
                if usercount > 0:
                         return render( request, "Guest/Newuser.html",{'msg': "Email Already Exists"} )
                else:
                        tbl_user.objects.create(user_name=name,user_gender=gender,user_contact=contact,user_email=email,user_password=password,user_address=address,user_place=place,user_photo=photo)
                        return render(request,"Guest/Newuser.html",{'msg':"Data inserted"})
        else:
                return render(request,"Guest/Newuser.html",{'placedata':placedata,'districtdata':districtdata})

def Ajaxplace(request):
        districtid=request.GET.get('did')
        placedata=tbl_place.objects.filter(district=districtid)
        return render(request,"Guest/Ajaxplace.html",{'placedata':placedata})

def Login(request):
        if request.method=="POST":
                email=request.POST.get("txt_email")
                password=request.POST.get("txt_password")
                usercount=tbl_user.objects.filter(user_email=email,user_password=password).count()
                admincount=tbl_adminreg.objects.filter(admin_email=email,admin_password=password).count()
                sellercount=tbl_seller.objects.filter(seller_email=email,seller_password=password).count()
                deliverycount=tbl_deliveryboy.objects.filter(delivery_email=email,delivery_password=password).count()


                if usercount>0:
                       userdata=tbl_user.objects.get(user_email=email,user_password=password)
                       request.session['uid']=userdata.id
                       return redirect("User:Homepage")
                elif admincount>0:
                        admindata=tbl_adminreg.objects.get(admin_email=email,admin_password=password)
                        request.session['mid']=admindata.id
                        return redirect("Admin:Homepage")
                elif sellercount>0:
                        sellerdata=tbl_seller.objects.get(seller_email=email,seller_password=password)
                        request.session['sid']=sellerdata.id
                        return redirect("Seller:Homepage")
                elif deliverycount>0:
                        deliverydata=tbl_deliveryboy.objects.get(delivery_email=email,delivery_password=password)
                        request.session['delid']=deliverydata.id
                        return redirect("Delivery:Homepage")
                else:
                        return render(request,"Guest/Login.html",{'msg':'Inavlidlogin'})
        else:
              return render(request,"Guest/Login.html")   
        
    
   

def Newseller(request):
        placedata=tbl_place.objects.all()
        districtdata=tbl_district.objects.all()
        # sellerdata=tbl_seller.objects.all()  
        if request.method=="POST":
                place=tbl_place.objects.get(id=request.POST.get("sel_place"))
                # district=tbl_district.objects.get(id=request.POST.get("sel_district"))
                name=request.POST.get("txt_name")
                contact=request.POST.get("txt_contact")
                email=request.POST.get("txt_email")
                password=request.POST.get("txt_password")
                establishdate=request.POST.get("txt_establishdate")
                licenseno=request.POST.get("txt_licenseno")
                ownername=request.POST.get("txt_owner")
                licenseproof=request.FILES.get("txt_licenseproof")
                ownerproof=request.FILES.get("txt_ownerproof")
                sellercount=tbl_seller.objects.filter(seller_email=email).count()
                if sellercount > 0:
                         return render( request, "Guest/Newseller.html",{'msg': "Email Already Exists"} )
                tbl_seller.objects.create(seller_name=name,seller_contact=contact,seller_email=email,seller_password=password,seller_establishdate=establishdate,seller_place=place,seller_licenseno=licenseno,seller_ownername=ownername,seller_licenseproof=licenseproof,seller_ownerproof=ownerproof)
                return render(request,"Guest/Newseller.html",{'msg':"Data inserted"})
        
        else:
                return render(request,"Guest/Newseller.html",{'placedata':placedata,'districtdata':districtdata})
        

def Deliveryboy(request):
        placedata=tbl_place.objects.all()
        districtdata=tbl_district.objects.all()
        # deliverydata=tbl_deliveryboy.objects.all()  
        if request.method=="POST":
                place=tbl_place.objects.get(id=request.POST.get("sel_place"))
                # district=tbl_district.objects.get(id=request.POST.get("sel_district"))
                name=request.POST.get("txt_name")
                gender=request.POST.get("gender")
                email=request.POST.get("txt_email")
                contact=request.POST.get("txt_contact")
                doj=request.POST.get("txt_doj")
                address=request.POST.get("txt_address")
                photo=request.FILES.get("txt_photo")
                proof=request.FILES.get("txt_proof")
                password=request.POST.get("txt_password")
                deliverycount=tbl_deliveryboy.objects.filter(delivery_email=email).count()
                if deliverycount > 0:
                         return render( request, "Guest/Deliveryboy.html",{'msg': "Email Already Exists"} )
                else:
                        tbl_deliveryboy.objects.create(delivery_name=name,delivery_gender=gender,delivery_email=email,delivery_contact=contact,delivery_doj=doj,delivery_address=address,delivery_photo=photo,delivery_proof=proof,delivery_place=place,delivery_password=password)
                        return render(request,"Guest/Deliveryboy.html",{'msg':"Data inserted"})
        
        else:
                return render(request,"Guest/Deliveryboy.html",{'placedata':placedata,'districtdata':districtdata})
def Index(request):
       return render(request,"Guest/Index.html")


def Viewproduct(request,):
    productviewdata=tbl_product.objects.all()
    branddata=tbl_brand.objects.all()
    categorydata=tbl_category.objects.all()
    subcategorydata=tbl_subcategory.objects.all()

#     if request.method == "POST":
#          productname = request.POST.get('txt_productname')
#          category = request.POST.get('sel_category')
#          subcategory = request.POST.get('sel_subcategory')
#          brand = request.POST.get('sel_brand')

#          productviewdata = tbl_product.objects.all()
#          if productname:
#             productviewdata = productviewdata.filter(product_name__icontains=productname)
#          if category:
#               productviewdata = productviewdata.filter(subcategory__category_id=category)
#          if subcategory:
#             productviewdata = productviewdata.filter(subcategory_id=subcategory)
#          if brand:
#             productviewdata = productviewdata.filter(brand_id=brand)
       
    return render(request,"Guest/Index.html",{'productviewdata':productviewdata,'branddata':branddata,'categorydata':categorydata,'subcategorydata':subcategorydata})



        