from django.urls import path, include
from . import views


urlpatterns = [
      path('notifications/votes', views.nots_like, name="likes"),
      path('notifications/answers', views.nots_answer, name="answers"),
      path('notifications/comments', views.nots_reply, name="comments"),
     
]