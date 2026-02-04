from django.db import models

class tbl_district(models.Model):
    district_name=models.CharField(max_length=50)

class tbl_category(models.Model):
    category_name=models.CharField(max_length=50)

class tbl_adminreg(models.Model):
    admin_name=models.CharField(max_length=50)
    admin_email=models.CharField(max_length=50)
    admin_password=models.CharField(max_length=50)

class tbl_place(models.Model):
    place_name=models.CharField(max_length=50)
    district=models.ForeignKey(tbl_district,on_delete=models.CASCADE)

class tbl_department(models.Model):
    department_name=models.CharField(max_length=50)

class tbl_designation(models.Model):
   designation_name=models.CharField(max_length=50)

class tbl_employee(models.Model):
    emp_name=models.CharField(max_length=50)
    emp_gender=models.CharField(max_length=50)
    emp_contact=models.CharField(max_length=15)
    emp_doj=models.DateField(max_length=50)
    emp_department=models.ForeignKey(tbl_department,on_delete=models.CASCADE)
    emp_designation=models.ForeignKey(tbl_designation,on_delete=models.CASCADE)
    emp_salary=models.IntegerField(max_length=50)

class tbl_brand(models.Model):
    brand_name=models.CharField(max_length=50)

class tbl_subcategory(models.Model):
    subcategory_name=models.CharField(max_length=50)
    category=models.ForeignKey(tbl_category,on_delete=models.CASCADE)

class tbl_mealtype(models.Model):
    mealtype_name=models.CharField(max_length=50)
    meal_fromtime=models.TimeField()
    meal_totime=models.TimeField()


class tbl_foodcategory(models.Model):
   foodcategory_name=models.CharField(max_length=50)


class tbl_recipe(models.Model):
    recipe_name=models.CharField(max_length=50)
    recipe_details=models.CharField(max_length=70)
    recipe_file=models.FileField(upload_to ='Assets/RecipeDocs')
    mealtype=models.ForeignKey(tbl_mealtype,on_delete=models.CASCADE)
    foodcategory=models.ForeignKey(tbl_foodcategory,on_delete=models.CASCADE)

class tbl_ingredients(models.Model):
    ingredients_name=models.CharField(max_length=50)
    ingredients_quantity=models.CharField(max_length=50)
    ingredients_remark=models.CharField(max_length=50)
    recipe=models.ForeignKey(tbl_recipe,on_delete=models.CASCADE)


class tbl_plan(models.Model):
    plan_name=models.CharField(max_length=50)
    plan_duration=models.CharField(max_length=50)
    plan_details=models.CharField(max_length=70)
    plan_amount=models.IntegerField(max_length=40)