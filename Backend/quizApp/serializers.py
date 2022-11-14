from rest_framework import serializers
from .models import *


class UserRegisterationSerializer(serializers.ModelSerializer):
    class Meta:
        model=End_User
        fields='__all__'



class OptionSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    question=serializers.IntegerField()
    option=serializers.CharField(max_length=100)
    image=serializers.ImageField()


class QuestionSerializer(serializers.ModelSerializer):
    options=OptionSerializer(many=True)
    class Meta:
        model=Quiz
        fields=['id' ,'For', 'question', "options"  ]


class UserAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model=User_quiz
        fields=['user' , 'user_question' , 'user_answer']


class UserSpecificSerializer(serializers.ModelSerializer):
    user=serializers.IntegerField()
    user_question=serializers.CharField(max_length=200)
    user_answer=serializers.IntegerField()
    u_answer=OptionSerializer(many=True)
    class Meta:
        model=User_quiz
        fields=['user' , 'user_question' , 'user_answer', "u_answer"]


class UserFriendSerializer(serializers.ModelSerializer):
    class Meta:
        model=User_friend
        fields='__all__'


class DeleteQuizSerializer(serializers.ModelSerializer):
    class Meta:
        model=End_User
        fields="__all__"



