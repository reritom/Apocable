from django.urls import path
from backend.views.accounts import login_user, logout_user, signup_user

urlpatterns = [
    path('login/', login_user),
    path('logout/', logout_user),
    path('signup/', signup_user)
]