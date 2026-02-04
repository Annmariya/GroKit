from django.urls import path
from  User import views
app_name="User"
urlpatterns = [
       path('Myprofile/',views.Myprofile,name="Myprofile"),
       path('Editprofile/',views.Editprofile,name="Editprofile"),
       path('Changepassword/',views.Changepassword,name="Changepassword"),
       path('Homepage/',views.Homepage,name="Homepage"),
       path('Complaint/',views.Complaint,name="Complaint"),
       path('delecomplaint/<int:cid>',views.delecomplaint,name="delecomplaint"),
       path('Viewproduct/',views.Viewproduct,name="Viewproduct"),
       path('Addtocart/<int:pid>/', views.Addtocart, name='Addtocart'),
       path('Mycart/', views.MyCart, name='MyCart'),
       path('DelCart/<int:did>/', views.DelCart, name='DelCart'),
       path('CartQty/', views.CartQty, name='CartQty'),
       path('MyBooking/',views.MyBooking,name="MyBooking"),
       path('Payment/',views.Payment,name="Payment"),
       path('Index/',views.Index,name="Index"),
       path('Logout/',views.Logout,name="Logout"),
       path('Viewrecipe/',views.Viewrecipe,name="Viewrecipe"),
       path('Viewingrediants/<int:rid>/', views.Viewingrediants, name='Viewingrediants'),
       path('Addwishlist/<int:pid>/', views.Addwishlist, name='Addwishlist'),
       path('Mywishlist/',views.Mywishlist, name='Mywishlist'),
       path('Delwishlist/<int:wid>/', views.Delwishlist, name='Delwishlist'),
       path('timerecipe/', views.time_based_recipe, name='timerecipe'),
       path('Addtocart1/<int:pid>/', views.Addtocart1, name='Addtocart1'),

      


      
]