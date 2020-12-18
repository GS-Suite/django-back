from rest_framework_jwt.views import refresh_jwt_token, obtain_jwt_token, verify_jwt_token
from django.urls import path, include
from django.conf.urls import url


urlpatterns = [
    ### JWT urls for auth
    path('auth/jwt/', obtain_jwt_token, name="new_token"),              # returns token
    path('auth/jwt_verify/', verify_jwt_token, name="verify_token"),    # returns token
    #path('auth/jwt_refresh/', refresh_jwt_token, name="refresh_token"), 
]

