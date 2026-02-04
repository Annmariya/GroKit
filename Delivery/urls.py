from django.urls import path
from  Delivery import views
app_name="Delivery"
urlpatterns = [
       path('Homepage/',views.Homepage,name="Homepage"),
       path('Myprofile/',views.Myprofile,name="Myprofile"),
       path('Editprofile/',views.Editprofile,name="Editprofile"),
       path('Changepassword/',views.Changepassword,name="Changepassword"),
       path('Mydelivery/',views.Mydelivery,name="Mydelivery"),
       path('UpdateCartStatus/<int:cid>/<int:status>/',views.UpdateCartStatus,name='UpdateCartStatus'),



]