from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('login/',views.login,name="login"),
    path('logout/',views.logout,name="logout"),
    # path('create/',views.create,name="create"),
    # path('<int:pk>/',views.detail,name="detail"),
    # path('',views.index,name="index"),
]