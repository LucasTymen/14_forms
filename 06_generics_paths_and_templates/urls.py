from django.urls import path

from . import views

# Add your path inside urlpatterns:
urlpatterns = [
   path("", views.home, name="home"),
   path("owner/list", views.OwnerList.as_view(), name="ownerlist"),

]
