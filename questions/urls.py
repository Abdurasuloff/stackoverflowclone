from django.urls import path, include
from . import views
from answers.views import like

urlpatterns = [
      #path('', views.ArticleListView.as_view(), name="home"),
      path('', views.home, name="home"),
      path('askquestion/', views.askquestion, name="askquestion"),
      path('detail/<int:id>/<str:slug>', views.detail, name="detail"),
      path('category/<slug:slug>', views.category, name="category-slug"),
      path('<int:answer_id>/like', like, name='postlike'),
      
]