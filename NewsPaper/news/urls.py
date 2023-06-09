from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from .views import NewsList, NewsDetail, SearchList, PostCreateView, PostDeleteView, PostUpdateView, RegisterView, \
    get_author

urlpatterns = [
    path('', NewsList.as_view(), name='news'),
    path('<int:pk>', NewsDetail.as_view(), name='news_detail'),
    path('search', SearchList.as_view(), name='search'),
    path('add', PostCreateView.as_view(), name='add_post'),
    path('update/<int:pk>', PostUpdateView.as_view(), name='post_update'),
    path('delete/<int:pk>', PostDeleteView.as_view(), name='post_delete'),
    path('login/', LoginView.as_view(template_name='login_page.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout_page.html'), name='logout'),
    path('login/signup/', RegisterView.as_view(), name='signup'),
    path('accounts/', include('allauth.urls')),
    path('getauthor/', get_author, name='getauthor')
]
