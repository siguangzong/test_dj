from django.urls import path
from snippets import views

urlpatterns = [
    # path('snippets/', views.snippet_list),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
    path('snippets/', views.SnippetList.as_view(), name='snippet-list'),
    path('list_api', views.api_root),

]
