from django.shortcuts import render,redirect
from Admin.models import*
from Guest.models import*
from User.models import*


def District(request):
        districtdata=tbl_district.objects.all() 
       
        
        if request.method=="POST":
                district=request.POST.get("txt_district")
                disrictcount = tbl_district.objects.filter(district_name=district).count()
                if disrictcount > 0:
                         return render( request, "Admin/District.html",{'msg': "Already Exists"} )
                else:
                        tbl_district.objects.create(district_name=district)
                        return render(request,"Admin/District.html",{'msg':"Data inserted"})
        
        else:
               return render(request,"Admin/District.html",{'districtdata':districtdata})

def Category(request):
        categorydata=tbl_category.objects.all()
        if request.method=="POST":
                category=request.POST.get("txt_category")
                tbl_category.objects.create(category_name=category)
                return render(request,"Admin/Category.html",{'msg':"Data inserted"})
        
        else:
               return render(request,"Admin/Category.html",{'categorydata':categorydata})

def AdminRegistration(request):
        registrationdata=tbl_adminreg.objects.all()
        if request.method=="POST":
                name=request.POST.get("txt_name")
                email=request.POST.get("txt_email")
                password=request.POST.get("txt_password")
                admincount=tbl_adminreg.objects.filter(admin_email=email).count()
                if admincount > 0:
                         return render( request, "Admin/AdminRegistration.html",{'msg': "Email Already Exists"} )
                else:
                        tbl_adminreg.objects.create(admin_name=name,admin_email=email,admin_password=password)
                        return render(request,"Admin/AdminRegistration.html",{'msg':"Data inserted"})
        else:
               return render(request,"Admin/AdminRegistration.html",{'registrationdata':registrationdata})
               
def deldistrict(request,did):
        tbl_district.objects.get(id=did).delete()
        return redirect("Admin:District")
def delcategory(request,cid):
        tbl_category.objects.get(id=cid).delete()
        return redirect("Admin:Category")
def deladminregistration(request,rid):
        tbl_adminreg.objects.get(id=rid).delete()
        return redirect("Admin:AdminRegistration")


def editdistrict(request,did):
        editdata=tbl_district.objects.get(id=did)
        if request.method=="POST":
                district=request.POST.get("txt_district")
                editdata.district_name=district
                editdata.save()
                return redirect("Admin:District")
        else:
                return render(request,"Admin/District.html",{'editdata':editdata})
        

def editcategory(request,cid):
        editdata=tbl_category.objects.get(id=cid)
        if request.method=="POST":
                category=request.POST.get("txt_category")
                editdata.category_name=category
                editdata.save()
                return redirect("Admin:Category")
        else:
                return render(request,"Admin/Category.html",{'editdata':editdata})

def editadmin(request,rid):
        editdata=tbl_adminreg.objects.get(id=rid)
        if request.method=="POST":
                name=request.POST.get("txt_name")
                email=request.POST.get("txt_email")
                password=request.POST.get("txt_password")
                editdata.admin_name=name
                editdata.admin_email=email
                editdata.admin_password=password
                editdata.save()
                return redirect("Admin:AdminRegistration")
        else:
                return render(request,"Admin/AdminRegistration.html",{'editdata':editdata})
        
def Place(request):
        districtdata=tbl_district.objects.all()
        placedata=tbl_place.objects.all()  
        if request.method=="POST":
                district=tbl_district.objects.get(id=request.POST.get("sel_district"))
                place=request.POST.get("txt_place")
                tbl_place.objects.create(place_name=place,district=district)
                return render(request,"Admin/Place.html",{'msg':"Data inserted"})
        
        else:
                return render(request,"Admin/Place.html",{'districtdata':districtdata,'placedata':placedata})
        



def delplace(request,pid):
        tbl_place.objects.get(id=pid).delete()
        return redirect("Admin:Place")


def editplace(request,pid):
        districtdata=tbl_district.objects.all()
        editdata=tbl_place.objects.get(id=pid)
        if request.method=="POST":
                district=tbl_district.objects.get(id=request.POST.get("sel_district"))
                place=request.POST.get("txt_place")
                editdata.place_name=place
                editdata.district=district
                editdata.save()
                return redirect("Admin:Place")
        else:
                return render(request,"Admin/Place.html",{'editdata':editdata,'districtdata':districtdata})


def Department(request):
        departmentdata=tbl_department.objects.all() 
        if request.method=="POST":
                department=request.POST.get("txt_dept")
                tbl_department.objects.create(department_name=department)
                return render(request,"Admin/Department.html",{'msg':"Data inserted"})
        
        else:
               return render(request,"Admin/Department.html",{'departmentdata':departmentdata})

def deldepartment(request,deid):
        tbl_department.objects.get(id=deid).delete()
        return redirect("Admin:Department") 

def editdepartment(request,deid):
        editdata=tbl_department.objects.get(id=deid)
        if request.method=="POST":
                department=request.POST.get("txt_dept")
                editdata.department_name=department
                editdata.save()
                return redirect("Admin:Department")
        else:
                return render(request,"Admin/Department.html",{'editdata':editdata})   

def Designation(request):
        designationdata=tbl_designation.objects.all() 
        if request.method=="POST":
                designation=request.POST.get("txt_desi")
                tbl_designation.objects.create(designation_name=designation)
                return render(request,"Admin/Designation.html",{'msg':"Data inserted"})
        
        else:
               return render(request,"Admin/Designation.html",{'designationdata':designationdata})

def deldesignation(request,dsid):
        tbl_designation.objects.get(id=dsid).delete()
        return redirect("Admin:Designation") 

def editdesignation(request,dsid):
        editdata=tbl_designation.objects.get(id=dsid)
        if request.method=="POST":
                designation=request.POST.get("txt_desi")
                editdata.designation_name=designation
                editdata.save()
                return redirect("Admin:Designation")
        else:
                return render(request,"Admin/Designation.html",{'editdata':editdata})


def Employee(request):
        departmentdata=tbl_department.objects.all()
        designationdata=tbl_designation.objects.all() 
        employeedata=tbl_employee.objects.all()  
        if request.method=="POST":
                department=tbl_department.objects.get(id=request.POST.get("sel_department"))
                designation=tbl_designation.objects.get(id=request.POST.get("sel_designation"))
                name=request.POST.get("txt_empname")
                gender=request.POST.get("gender")
                contact=request.POST.get("txt_contact")
                doj=request.POST.get("txt_doj")
                salary=request.POST.get("txt_salary")
                tbl_employee.objects.create(emp_name=name,emp_gender=gender,emp_contact=contact,emp_doj=doj,emp_department=department,emp_designation=designation,emp_salary=salary)
                return render(request,"Admin/Employee.html",{'msg':"Data inserted"})
        
        else:
                return render(request,"Admin/Employee.html",{'departmentdata':departmentdata,'designationdata':designationdata,'employeedata':employeedata})
        

def delemployee(request,eid):
        tbl_employee.objects.get(id=eid).delete()
        return redirect("Admin:Employee")

def editemployee(request,eid):
        departmentdata=tbl_department.objects.all()
        designationdata=tbl_designation.objects.all() 
        editdata=tbl_employee.objects.get(id=eid)
        if request.method=="POST":
                department=tbl_department.objects.get(id=request.POST.get("sel_department"))
                designation=tbl_designation.objects.get(id=request.POST.get("sel_designation"))
                name=request.POST.get("txt_empname")
                gender=request.POST.get("gender")
                contact=request.POST.get("txt_contact")
                doj=request.POST.get("txt_doj")
                salary=request.POST.get("txt_salary")

                editdata.emp_name=name
                editdata.emp_gender=gender
                editdata.emp_contact=contact
                editdata.emp_doj=doj
                editdata.emp_department=department
                editdata.emp_designation=designation
                editdata.emp_salary=salary
                editdata.save()
                return redirect("Admin:Employee")
        else:
                return render(request,"Admin/Employee.html",{'editdata':editdata,'departmentdata':departmentdata,'designationdata':designationdata})

def UserList(request):
    userdata=tbl_user.objects.all()
    accuserdata=tbl_user.objects.filter(user_status=1)
    rejuserdata=tbl_user.objects.filter(user_status=2)
    return render(request,"Admin/UserList.html",{'userdata':userdata,'accuserdata':accuserdata,'rejuserdata':rejuserdata})

def SellerList(request):
    sellerdata=tbl_seller.objects.all()
    accsellerdata=tbl_seller.objects.filter(seller_status=1)
    rejsellerdata=tbl_seller.objects.filter(seller_status=2)
    return render(request,"Admin/SellerList.html",{'sellerdata':sellerdata,'accsellerdata':accsellerdata,'rejsellerdata':rejsellerdata})


def acceptseller(request,aid):
        data=tbl_seller.objects.get(id=aid)
        data.seller_status=1
        data.save()
        return render(request,'Admin/SellerList.html',{'msg':'Verified'})
def rejectseller(request,rid):
        data=tbl_seller.objects.get(id=rid)
        data.seller_status=2
        data.save()
        return render(request,'Admin/SellerList.html',{'msg':'Rejected'})

def acceptuser(request,uid):
        data=tbl_user.objects.get(id=uid)
        data.user_status=1
        data.save()
        return render(request,'Admin/UserList.html',{'msg':'Verified'})

def rejectuser(request,uid):
        data=tbl_user.objects.get(id=uid)
        data.user_status=2
        data.save()
        return render(request,'Admin/UserList.html',{'msg':'Rejected'})
def Homepage(request):
          if 'mid' not in request.session:
             return redirect("Guest:Login")
          admindata=tbl_adminreg.objects.get(id=request.session['mid'])
          return render(request,"Admin/Homepage.html",{'admindata':admindata})
        # print(request.session['mid'])
         
def Viewcomplaint(request):
    Viewdata=tbl_Complaint.objects.filter(complaint_status=0)
    replied=tbl_Complaint.objects.filter(complaint_status=1)
    return render(request,"Admin/Viewcomplaint.html",{'Viewdata':Viewdata,'replied':replied})

def Reply(request,cid):
        complaintdata=tbl_Complaint.objects.get(id=cid)
        if request.method=="POST":
                reply=request.POST.get("txt_reply")
                complaintdata.complaint_replay=reply
                complaintdata.complaint_status=1
                complaintdata.save()
                return render(request,"Admin/Reply.html",{'msg':"Replied....."})
        else:
                return render(request,"Admin/Reply.html")

def Brand(request):
        branddata=tbl_brand.objects.all() 
        if request.method=="POST":
                brand=request.POST.get("txt_brand")
                tbl_brand.objects.create(brand_name=brand)
                return render(request,"Admin/Brand.html",{'msg':"Data inserted"})
        
        else:
               return render(request,"Admin/Brand.html",{'branddata':branddata})

def delebrand(request,bid):
        tbl_brand.objects.get(id=bid).delete()
        return redirect("Admin:Brand")

def Deliveryboyview(request):
    deliverydata=tbl_deliveryboy.objects.all()
    accdeliverydata=tbl_deliveryboy.objects.filter(delivery_status=1)
    rejdeliverydata=tbl_deliveryboy.objects.filter(delivery_status=2)
    return render(request,"Admin/Deliveryboyview.html",{'deliverydata':deliverydata,'accdeliverydata':accdeliverydata,'rejdeliverydata':rejdeliverydata})

def acceptdelivery(request,daid):
        data=tbl_deliveryboy.objects.get(id=daid)
        data.delivery_status=1
        data.save()
        return render(request,'Admin/Deliveryboyview.html',{'msg':'Verified'})
def rejectdelivery(request,drid):
        data=tbl_deliveryboy.objects.get(id=drid)
        data.delivery_status=2
        data.save()
        return render(request,'Admin/Deliveryboyview.html',{'msg':'Rejected'})
def Subcategory(request):
        categorydata=tbl_category.objects.all()
        subcategorydata=tbl_subcategory.objects.all()  
        if request.method=="POST":
                category=tbl_category.objects.get(id=request.POST.get("sel_category"))
                subcategory=request.POST.get("txt_subcategory")
                tbl_subcategory.objects.create(subcategory_name=subcategory,category=category)
                return render(request,"Admin/Subcategory.html",{'msg':"Data inserted"})
        
        else:
                return render(request,"Admin/Subcategory.html",{'categorydata':categorydata,'subcategorydata':subcategorydata})
        
def delsubcategory(request,subid):
        tbl_subcategory.objects.get(id=subid).delete()
        return redirect("Admin:Subcategory")


def Mealtype(request):
        mealdata=tbl_mealtype.objects.all()
        if request.method=="POST":
                mealtype=request.POST.get("txt_mealtype")
                fromtime=request.POST.get("txt_fromtime")
                totime=request.POST.get("txt_totime")
                tbl_mealtype.objects.create(mealtype_name=mealtype,meal_fromtime=fromtime,meal_totime=totime)
                return render(request,"Admin/Mealtype.html",{'msg':"Data inserted"})
        
        else:
               return render(request,"Admin/Mealtype.html",{'mealdata':mealdata})
        
def delmealtype(request,meid):
        tbl_mealtype.objects.get(id=meid).delete()
        return redirect("Admin:Mealtype")


def Recipe(request):
        foodcategorydata=tbl_foodcategory.objects.all()
        mealdata=tbl_mealtype.objects.all()
        recipedata=tbl_recipe.objects.all()  
        if request.method=="POST":
                mealtype=tbl_mealtype.objects.get(id=request.POST.get("sel_mealtype"))
                foodcategory=tbl_foodcategory.objects.get(id=request.POST.get("sel_foodcategory"))

                name=request.POST.get("txt_name")
                details=request.POST.get("txt_details")
                file=request.FILES.get("txt_file")

                tbl_recipe.objects.create(recipe_name=name,recipe_details=details,recipe_file=file,mealtype=mealtype,foodcategory=foodcategory)
                return render(request,"Admin/Recipe.html",{'msg':"Data inserted"})
        
        else:
                return render(request,"Admin/Recipe.html",{'mealdata':mealdata,'recipedata':recipedata,'foodcategorydata':foodcategorydata})

def delrecipe(request,reid):
        tbl_recipe.objects.get(id=reid).delete()
        return redirect("Admin:Recipe")

def Foodcategory(request):
        foodcategorydata=tbl_foodcategory.objects.all() 
        if request.method=="POST":
                foodcategory=request.POST.get("txt_foodcategory")
                tbl_foodcategory.objects.create(foodcategory_name=foodcategory)
                return render(request,"Admin/Foodcategory.html",{'msg':"Data inserted"})
        
        else:
               return render(request,"Admin/Foodcategory.html",{'foodcategorydata':foodcategorydata})
    
def delefoodcategory(request,fid):
        tbl_foodcategory.objects.get(id=fid).delete()
        return redirect("Admin:Foodcategory")

def Ingredients(request,rid):
        ingredientdata=tbl_ingredients.objects.all()
        Recipe=tbl_recipe.objects.get(id=rid)
        if request.method=="POST":
                Name=request.POST.get("txt_ingredientname")
                quantity=request.POST.get("txt_quantity")
                remark=request.POST.get("txt_remark")
                tbl_ingredients.objects.create(ingredients_name=Name,ingredients_quantity=quantity,ingredients_remark=remark,recipe=Recipe)
                return render(request,"Admin/Addingredients.html",{'msg':"Data inserted",'rid':rid})
        
        else:
               return render(request,"Admin/Addingredients.html",{'ingredientdata':ingredientdata,'rid':rid})
def delingredients(request,inid,rid):
        tbl_ingredients.objects.get(id=inid).delete()
        return redirect("Admin:Ingredients",rid)


def Plan(request):
        plandata=tbl_plan.objects.all() 
        if request.method=="POST":
                name=request.POST.get("txt_name")
                duration=request.POST.get("txt_duration")
                details=request.POST.get("txt_details")
                amount=request.POST.get("txt_amount")
                tbl_plan.objects.create(plan_name=name,plan_duration=duration,plan_details=details,plan_amount=amount)
                return render(request,"Admin/Plan.html",{'msg':"Data inserted"})
        
        else:
               return render(request,"Admin/Plan.html",{'plandata':plandata})
def delplan(request,plid):
        tbl_plan.objects.get(id=plid).delete()
        return redirect("Admin:Plan")


def Form(request):
       return render(request,"Admin/Form.html")



def Logout(request):
       del request.session['mid']
       return redirect("Guest:Login")