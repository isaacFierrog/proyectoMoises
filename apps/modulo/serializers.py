from rest_framework import serializers
from .models import ModuloModel


class ModuloSerializer(serializers.ModelSerializer):
    class Meta:
<<<<<<< HEAD
        model = ModuloModel
        fields = '__all__'
=======
        model = ModuloModel
>>>>>>> 83aa6e4be512664272abd6a805f129a5130b92c3
