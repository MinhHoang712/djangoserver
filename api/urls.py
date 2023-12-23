from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import ChapterDetailView, RegisterView, LoginView, BookListView, CategoryList, BookInfo, ChangePasswordView, SearchBookView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('books/', BookListView.as_view(), name='books'),
    path('books/<int:pk>/', BookInfo.as_view(), name='book-info'),
    path('categories/', CategoryList.as_view(), name='categories'),
    path('change_password/', ChangePasswordView.as_view(), name='change-password'),
    path('chapters/<int:pk>/', ChapterDetailView.as_view(), name='chapter-detail'),
    path('books_search/', SearchBookView.as_view(), name='search_books'),

]
