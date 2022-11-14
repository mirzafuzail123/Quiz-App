from django.contrib import admin
from .models import *

class optionInline(admin.TabularInline):
    model=Option

class quizAdmin(admin.ModelAdmin):
    inlines=[
        optionInline,
    ]

class user_quizInline(admin.TabularInline):
    model=User_quiz

class End_UserAdmin(admin.ModelAdmin):
    list_display=['u_id' , 'name' , 'gender']
    inlines=[user_quizInline]


admin.site.register(End_User , End_UserAdmin)
admin.site.register(Quiz,quizAdmin)
admin.site.register(User_quiz)
admin.site.register(Option)
admin.site.register(User_friend)