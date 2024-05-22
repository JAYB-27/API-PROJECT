from django.shortcuts import render
from .serializers import StudentSerializer, StudentCreateSerializer, StudentRetrieverSerializer
from .models import Student
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import response, status, exceptions, generics

# Create your views here.
# class StudentEndpoint(APIView):
#     def get(self,request, *args, **kwargs): #GET retrieving list of student
#        students=Student.objects.all()
#        serializer= StudentRetrieverSerializer(students, many=True)
#        return response.Response(serializer.data, status=status.HTTP_200_OK)



#     def post(self,request, *args, **kwargs):#POST creating new student
#         serializer=StudentCreateSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#            serializer.save()
#            return response.Response({'message': 'student created successfully',
#                                      'data' : serializer.data
#                                      }, status=status.HTTP_201_CREATED)
#         return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentEndpoint(generics.ListCreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentCreateSerializer
    permission_classes=[IsAuthenticated]
    


# class StudentDetailEndpoint(APIView):
#     def get_object(self, student_id):
#         try:
#             student=Student.objects.get(id=student_id)
#             return student
#         except Student.DoesNotExist:
#             raise exceptions.NotFound("student not found")


    # def get(self, request, pk):
    #     student=self.get_object(id=pk)
    #     serializer=StudentCreateSerializer(student)
    #     return response.Response(serializer.data, status=status.HTTP_200_OK)
    
    # def put(self, request, pk):
    #     student=self.get_object(pk)
    #     serializer= StudentCreateSerializer(instance=student, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return response.Response(data=serializer.data, status=status.HTTP_200_OK)
    #     return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    # def delete(self, request, pk):
    #     student=self.get_object(pk)
    #     student.delete()
    #     return response.Response({"message": "student deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    


class StudentDetailEndpoint(generics.RetrieveUpdateDestroyAPIView):
    queryset=Student.objects.all
    serializer_class=StudentCreateSerializer
    lookup_field='pk'

            






