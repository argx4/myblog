from django.urls import path # type: ignore
from app_blog import views

urlpatterns = [
 path('', views.HomePageView.as_view()),
]
