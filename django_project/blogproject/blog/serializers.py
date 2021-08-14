from rest_framework.serializers import ModelSerializer
from .models import Addblog

class ShowBlog(ModelSerializer):

    class Meta:
        model = Addblog 
        fields = ['title', 'post'] # __all__