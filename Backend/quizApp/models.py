from django.db import models
import uuid

gender=(
    ('M' , 'Male'),
    ('F' , 'Female')
)
class End_User(models.Model):
    class Meta:  
        verbose_name_plural = 'End_User'
    name=models.CharField(max_length=100)
    gender=models.CharField(choices=gender , max_length=50)
    u_id=models.UUIDField(unique=True , default=uuid.uuid4 , editable=False , auto_created=True)

    def __str__(self):
        return self.name

For=(
    ('M' , 'Male'),
    ('F' , 'Female'),
    ('B' , 'Both')
)

class Quiz(models.Model):
    class Meta:  
        verbose_name_plural = 'Quiz'
    For=models.CharField(choices=For , max_length=50 , default='B')
    question=models.CharField(max_length=200 )

    def __str__(self):
        return self.question


class Option(models.Model):
    class Meta:  
        verbose_name_plural = 'Option'
    id=models.IntegerField(primary_key=True , unique=True , auto_created=True)
    question=models.ForeignKey(Quiz , on_delete=models.CASCADE  , related_name='options')
    option=models.CharField(max_length=100)
    image=models.ImageField( upload_to='images/' , default="images/cricket-bat-ball-26560801_RG0J7GO.jpeg")

    def __str__(self):
        return self.option


class User_quiz(models.Model):
    class Meta:  
        verbose_name_plural = 'User_quiz'
    user=models.ForeignKey(End_User , on_delete=models.CASCADE , related_name='belong_to')
    user_question=models.ForeignKey(Quiz , on_delete=models.CASCADE , related_name='u_question')
    user_answer=models.ForeignKey(Option , on_delete=models.CASCADE , related_name='u_answer')

    def __str__(self):
        return self.user.name


class User_friend(models.Model):
    class Meta:
        verbose_name_plural='User_friend'
    user=models.ForeignKey(End_User , on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    score=models.IntegerField()

    def __str__(self):
        return self.name