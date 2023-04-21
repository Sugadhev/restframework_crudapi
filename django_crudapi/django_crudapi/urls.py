from django.urls import path
from  api import views



urlpatterns = [

    path("",views.StudentListAPIView.as_view(),name="student_list"),
    path("create/", views.StudentCreateAPIView.as_view(),name="student_create"),
    path("update/<int:pk>/",views.StudentUpdateAPIView.as_view(),name="student_update"),
    path("delete/<int:pk>/",views.StudentDeleteAPIView.as_view(),name="student_delete")

]
