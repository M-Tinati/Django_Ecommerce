from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('signup/', views.AccountsView.as_view(), name="signup"),
    path('logout/', views.UserLogOutView.as_view(), name="logout"),
    path('login/', views.UserLoginView.as_view(), name="login"),

]
