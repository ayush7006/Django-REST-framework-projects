

# Create your views here.

from .serializers import StudentSerializer
from .models import Student
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
# Create yourfrom views here.


class LCStudentAPi(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class RUDStudentAPI(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
