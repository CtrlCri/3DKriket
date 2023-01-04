from django.urls import path

from users import views


urlpatterns = [
    path('create_user/', views.CreateUserView.as_view()),
    path('auth_token/', views.CreateTokenView.as_view()),
    path('user/', views.RetreiveUpdateUserView.as_view()),
]

