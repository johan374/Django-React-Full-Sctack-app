# Importing the User model from Django's built-in auth system and the serializers module from DRF
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Note

# Define a custom serializer class for the User model
# Inheriting from `serializers.ModelSerializer` to automatically generate a serializer for the User model
class UserSerializer(serializers.ModelSerializer):
    
    # Define metadata for the serializer
    # The `Meta` class defines some important settings for the serializer
    class Meta:
        model = User  # This tells the serializer which model to serialize (in this case, the `User` model).
        fields = ["id", "username", "password"]  # The fields to be serialized: id, username, and password
        # The `extra_kwargs` is used to define special handling for certain fields
        # For example, we want the password field to be "write-only" (it will not be returned in API responses)
        extra_kwargs = {"password": {"write_only": True}}

    # Custom create method to handle user creation securely
    def create(self, validated_data):
        try:
            user = User.objects.create_user(**validated_data)
            print(f"User created: {user.username}")
            return user
        except Exception as e:
            print(f"User creation error: {e}")
            raise serializers.ValidationError(str(e))
            
    
# Define the NoteSerializer class that will serialize the Note model
class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        # This tells the serializer which model it will work with. In this case, it's the `Note` model.
        model = Note
        
        # Specifies the list of fields that should be included when the model is serialized.
        # These fields will be converted to JSON when the serializer is used.
        fields = ["id", "title", "content", "create_at", "author"]
        
        # `extra_kwargs` allows additional configurations for certain fields.
        # In this case, we're making the 'author' field read-only.
        # This means the 'author' field will be automatically set when creating or updating a note 
        # and won't be editable by the user through the API.
        extra_kwargs = {"author": {"read_only": True}}
