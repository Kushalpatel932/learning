from django.contrib import admin

# Register your models here.
from student.models import UserProfile
from django.contrib.auth.models import User
from django.contrib.admin.sites import NotRegistered
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model
User = get_user_model()

class UserProfileInline(admin.StackedInline):
    model= UserProfile
    can_delete =False
    verbose_name_plural = "User Profile"

class UserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline,)
    
    def get_readonly_fields(self,request,obj=None):
        django_readonly = super().get_readonly_fields(request,obj)
        if obj:
            return django_readonly + ('username',)
        return django_readonly


try:
    admin.site.unregister(User)
except NotRegistered:
    pass
admin.site.register(User,UserAdmin)