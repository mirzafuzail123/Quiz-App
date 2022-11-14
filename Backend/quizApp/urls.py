from django.urls import path
from .views import *
urlpatterns = [
    path('user_register/' , UserRegistrationView.as_view() , name='user-register'),
    path('quiz/' , QuizView.as_view() , name='quiz'),
    path('user_answer/' , UserAnswerView.as_view() , name='user-answer'),
    path('user_specific/<u_id>/' , UserSpecificView.as_view() , name='user-specific'),
    path('user_friend/' , UserFriendView.as_view() , name='user-friend'),
    path('delete_quiz/<pk>/' ,DeleteQuizView.as_view() , name='delete-quiz'),
]
