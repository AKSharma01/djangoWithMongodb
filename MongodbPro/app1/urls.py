from django.conf.urls import url,include
from app1 import views,models


# view=views.ViewData

urlpatterns = [
	url(r'^$',views.indexHtml),
	url(r'^insertData/',views.insertData),
	url(r'^viewData/',views.viewData),
	url(r'^insertInto/',views.insertInto),
]