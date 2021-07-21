from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),

    path('questionslist/', views.questions_list, name="questions"),
    path('renderquestions/<str:que_type>/', views.render_questions_of_a_type, name="renderquestions"),
    path('completed/<str:que_type>/<str:que_status>/', views.completed_question, name="completed"),
    path('changeStatus/<str:que_id>/<str:que_type>/<str:que_status>/<str:return_id>/<str:addOrRemove>', views.changeQuestionStatus, name='changeStatus'),
]