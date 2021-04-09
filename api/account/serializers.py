from rest_framework import serializers
from account import models
from rest_framework.serializers import ValidationError




class UserSerializer(serializers.ModelSerializer):



    confirm_password = serializers.CharField(
        label='Confirm Password',
        write_only=True,
        required=True,
        style={'input_type': 'password'})



    class Meta:

        model = models.User
        fields = ('id', 'username', 'name', 'password','confirm_password')
        extra_kwargs = {
            'password':{
                'write_only': True,
                'style':{'input_type': 'password'}
            }
        }


    def create(self, validated_data):



        if validated_data['password']!=validated_data['confirm_password']:

                raise ValidationError('Passwords do not match')


        user = models.User.objects.create_user(
            username=validated_data['username'],
            name=validated_data['name'],


        )
        user.set_password(validated_data['password'])
        user.save()

        return user
