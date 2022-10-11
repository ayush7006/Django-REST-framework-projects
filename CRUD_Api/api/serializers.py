from .models import Student
from rest_framework import serializers





#normal serializer 
"""
class StudentSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=100)
    roll=serializers.IntegerField()
    city=serializers.CharField(max_length=100)


    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.roll = validated_data.get('roll', instance.roll)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance

#field lavel validation
    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError('seat full')
        return value  
"""          

#model serializer
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name','roll','city']
        #read_only_field=['name','city']
        #extra_kwargs = {'name':{'read_only':True}}

        
#field lavel validation        
    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError('seat full')
        return value


        