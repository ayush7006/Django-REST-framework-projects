from .models import Student
from rest_framework import serializers

#model serializer
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','name','roll','city']
        #read_only_field=['name','city']
        #extra_kwargs = {'name':{'read_only':True}}

        
#field lavel validation    
'''    
    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError('seat full')
        return value 
        
        '''


        