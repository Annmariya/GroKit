from django.urls import path
from  Seller import views
app_name="Seller"
urlpatterns = [
       path('Myprofile/',views.Myprofile,name="Myprofile"),
       path('Editprofile/',views.Editprofile,name="Editprofile"),
       path('Homepage/',views.Homepage,name="Homepage"),
       path('Changepassword/',views.Changepassword,name="Changepassword"),
       path('Product/',views.Product,name="Product"),
       path('Ajaxproduct/',views.Ajaxproduct,name="Ajaxproduct"),
       path('Delproduct/<int:pid>',views.delproduct,name="delproduct"),
       path('Stock/<int:pid>',views.Stock,name="Stock"),
       path('Delestock/<int:soid>/<int:pid>',views.delestock,name="delestock"),
       path('Gallery/<int:pid>',views.Gallery,name="Gallery"),
       path('Delegallery/<int:gid>/<int:pid>',views.delegallery,name="delegallery"),
       path('ViewBookings/',views.ViewBookings,name="ViewBookings"),
       path('UpdateCartStatus/<int:cid>/<int:status>/',views.UpdateCartStatus,name='UpdateCartStatus'),
       path('Logout/',views.Logout,name="Logout"),






]