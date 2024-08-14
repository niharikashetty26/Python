from django.urls import path
from .views import StudentListCreateView, StudentRetrieveUpdateDestroyView, StudentListRetrieveView
from .views import RegisterView, CustomAuthToken, LogoutView

urlpatterns = [
    path('students/', StudentListCreateView.as_view(), name='student-list-create'),
    path('students/<int:pk>/', StudentRetrieveUpdateDestroyView.as_view(), name='student-detail'),
    path('students-list-retrieve/', StudentListRetrieveView.as_view(), name='student-list-retrieve'),
    path('students-list-retrieve/<int:pk>/', StudentListRetrieveView.as_view(), name='student-list-retrieve-specific'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomAuthToken.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='login'),

]
