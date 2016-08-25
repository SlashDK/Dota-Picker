from django.conf.urls import url,include
from . import views

urlpatterns = [
	url(r'^$', views.PickerAPIView.as_view(), name='get_results'),
]
