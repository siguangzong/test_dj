from django.urls import path
from . import views
from django.conf.urls import url, include
from rest_framework import routers
from learn import views
from django.conf.urls import url, include

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'books', views.BookViewSet)

# 原始定义url
#
# urlpatterns = [
#     path('my_first/', views.index, name='index'),
#     path('detail/<int:question_id>', views.detail, name='detail'),
# ]


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('my_first/', views.index, name='index'),
]