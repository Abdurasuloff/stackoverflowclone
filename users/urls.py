from django.urls import path
from .views import SignUpView, ProfileEditView , profile


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('edit/<str:username>/', ProfileEditView.as_view(), name=''),
    path('profile/<str:username>/', profile, name='user_detail'),
]