from django.urls import path
from  Guest import views
app_name="Guest"
urlpatterns = [
       path('Newuser/',views.Newuser,name="Newuser"),
       path('Ajaxplace/',views.Ajaxplace,name="Ajaxplace"),
       path('Login/',views.Login,name="Login"),
       path('Newseller/',views.Newseller,name="Newseller"),
       path('Deliveryboy/',views.Deliveryboy,name="Deliveryboy"),
       path('Index/',views.Index,name="Index"),
       path('Viewproduct/',views.Viewproduct,name="Viewproduct"),
       


]