from rest_framework import serializers

from student.models import UserProfile
from django.contrib.auth.models import User

class UserDataSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source = "user.username")
    email = serializers.EmailField(source='user.email') 
    password = serializers.CharField(source = "user.password")

    class Meta:
        model = UserProfile
        fields=["username","email","name","password","phone_number","location","address"]

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        username = user_data.get('username')
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError({'username': 'This username is already taken.'})
        user = User.objects.create(**user_data)
        user_profile = UserProfile.objects.create(user=user, **validated_data)
        return user_profile



class GetUsersSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source="profile.name")
    location = serializers.CharField(source="profile.location")
    phone_number = serializers.IntegerField(source="profile.phone_number")
    age = serializers.IntegerField(source = "profile.age",read_only=True)
    class Meta:
        model = User
        fields = ("username","email","name","location","phone_number","age")


