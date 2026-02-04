from django.urls import path
from  Admin import views
app_name="Admin"
urlpatterns = [
   path('District/',views.District,name="District"),
   path('Category/',views.Category,name="Category"),
   path('AdminRegistration/',views.AdminRegistration,name="AdminRegistration"),
   path('Deldistrict/<int:did>',views.deldistrict,name="deldistrict"),
   path('Delcategory/<int:cid>',views.delcategory,name="delcategory"),
   path('Deladminregistration/<int:rid>',views.deladminregistration,name="deladminregistration"),
   path('Editdistrict/<int:did>',views.editdistrict,name="editdistrict"),
   path('Editcategory/<int:cid>',views.editcategory,name="editcategory"),
   path('EditAdmin/<int:rid>',views.editadmin,name="editadmin"),
   path('Place/',views.Place,name="Place"),
   path('Editplace/<int:pid>',views.editplace,name="editplace"),
   path('Delplace/<int:pid>',views.delplace,name="delplace"),
   path('Department/',views.Department,name="Department"),
   path('Deldepartment/<int:deid>',views.deldepartment,name="deldepartment"),
   path('Editdepartment/<int:deid>',views.editdepartment,name="editdepartment"),
   path('Designation/',views.Designation,name="Designation"),
   path('Deldesignation/<int:dsid>',views.deldesignation,name="deldesignation"),
   path('Editdesignation/<int:dsid>',views.editdesignation,name="editdesignation"),
   path('Employee/',views.Employee,name="Employee"),
   path('Delemployee/<int:eid>',views.delemployee,name="delemployee"),
   path('Editemployee/<int:eid>',views.editemployee,name="editemployee"),
   path('UserList/',views.UserList,name="UserList"),
   path('SellerList/',views.SellerList,name="SellerList"),   
   path('acceptseller/<int:aid>',views.acceptseller,name="acceptseller"),
   path('rejectseller/<int:rid>',views.rejectseller,name="rejectseller"),
   path('rejectuser/<int:uid>',views.rejectuser,name="rejectuser"),
   path('acceptuser/<int:uid>',views.acceptuser,name="acceptuser"),
   path('Homepage/',views.Homepage,name="Homepage"),
   path('Viewcomplaint/',views.Viewcomplaint,name="Viewcomplaint"),
   path('Reply/<int:cid>',views.Reply,name="Reply"),
   path('Brand/',views.Brand,name="Brand"),
   path('Delebrand/<int:bid>',views.delebrand,name="delebrand"),
   path('Deliveryboyview/',views.Deliveryboyview,name="Deliveryboyview"),
   path('acceptdelivery/<int:daid>',views.acceptdelivery,name="acceptdelivery"),
   path('rejectdelivery/<int:drid>',views.rejectdelivery,name="rejectdelivery"),
   path('Subcategory/',views.Subcategory,name="Subcategory"),
   path('Delsubcategory/<int:subid>',views.delsubcategory,name="delsubcategory"),
   path('Mealtype/',views.Mealtype,name="Mealtype"),
   path('Delmealtype/<int:meid>',views.delmealtype,name="delmealtype"),
   path('Recipe/',views.Recipe,name="Recipe"),
   path('Delrecipe/<int:reid>',views.delrecipe,name="delrecipe"),
   path('Foodcategory/',views.Foodcategory,name="Foodcategory"),
   path('Delefoodcategory/<int:fid>',views.delefoodcategory,name="delefoodcategory"),
   path('Ingredients/<int:rid>',views.Ingredients,name="Ingredients"),
   path('Delingredients/<int:inid>/<int:rid>',views.delingredients,name="delingredients"),
   path('Plan/',views.Plan,name="Plan"),
   path('Delplan/<int:plid>',views.delplan,name="delplan"),
   path('Form/',views.Form,name="Form"),
   path('Logout/',views.Logout,name="Logout"),






  
  





  






]
