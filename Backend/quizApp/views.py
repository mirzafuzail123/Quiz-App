from django.shortcuts import render
from .serializers import *
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView , ListAPIView , RetrieveAPIView , DestroyAPIView
from .models import *
from rest_framework.response import Response
from django.forms.models import model_to_dict
import json
# Create your views here.

#Creating User
class UserRegistrationView(CreateAPIView):
    serializer_class=UserRegisterationSerializer
    queryset=End_User.objects.all()


#Fetching Questions
class QuizView(APIView):
    def get(self , request , format=None ):
        gender=request.data.get('gender')
        data=[]
        if gender=='M':
            quiz=Quiz.objects.all().exclude(For='F')
        else:
            quiz=Quiz.objects.all().exclude(For='M')
            
        for i in quiz:
            a=model_to_dict(i)
            option=Option.objects.filter(question=i)
            data2=[]
            for ii in option:
                aa=model_to_dict(ii)
                data2.append(aa)
            a['options']=data2
            data.append(a)
        print(data)
        serializer=QuestionSerializer( data=data , many=True)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)


#Saving Answers of User
class UserAnswerView(CreateAPIView):
    serializer_class=UserAnswerSerializer
    queryset=User_quiz.objects.all()


#Fetching User Selected Questions
class UserSpecificView(APIView):
    def get(self , request , format=None , u_id=None):
        user=End_User.objects.filter(u_id=u_id).first()
        questions=User_quiz.objects.filter(user=user)
        data_list=[]
        dict={}
        for i in questions:
            opt=Option.objects.filter(question=i.user_question.id)
            dict['id']=i.id
            dict['user']=i.user.id
            dict['user_question']=i.user_question.question
            dict['user_answer']=i.user_answer.id
            a=model_to_dict(i)
            data_ii=[]
            for ii in opt:
                data_ii.append(model_to_dict(ii))
            dict['u_answer']=data_ii
            data_list.append(dict)
            print(data_list)
        serializer=UserSpecificSerializer(data=data_list , many=True)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)


#Saving Friend's score
class UserFriendView(CreateAPIView):
    serializer_class=UserFriendSerializer
    queryset=User_friend.objects.all()



#Deleting Quiz
class DeleteQuizView(DestroyAPIView):
    serializer_class=DeleteQuizSerializer
    queryset=End_User.objects.all()

