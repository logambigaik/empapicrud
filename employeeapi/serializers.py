# api  -mobile /web app /etc -it communicates with any of app.
# data -delas with .json/xml

from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        #field = ('id','fullname')   to specify particular column name
        fields = '__all__'    # to select all the fields from Employee table


