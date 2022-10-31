from pyexpat import model
from student_management.models import *
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import *
from .permissions import IsOwnerOrReadOnly


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all().order_by('-date_joined')
    serializer_class = CustomUserSerializer
    permission_classes = [IsOwnerOrReadOnly, ]


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsOwnerOrReadOnly, ]


class Session_YearViewSet(viewsets.ModelViewSet):
    queryset = Session_Year.objects.all()
    serializer_class = Session_YearSerializer
    permission_classes = [IsOwnerOrReadOnly, ]


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsOwnerOrReadOnly, ]


class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    permission_classes = [IsOwnerOrReadOnly, ]


class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [IsOwnerOrReadOnly, ]


class Staff_NotificationViewSet(viewsets.ModelViewSet):
    queryset = Staff_Notification.objects.all()
    serializer_class = Staff_NotificationSerializer
    permission_classes = [IsOwnerOrReadOnly, ]


class Staff_leaveViewSet(viewsets.ModelViewSet):
    queryset = Staff_leave.objects.all()
    serializer_class = Staff_leaveSerializer
    permission_classes = [IsOwnerOrReadOnly, ]


class Staff_FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Staff_Feedback.objects.all()
    serializer_class = Staff_FeedbackSerializer
    permission_classes = [IsOwnerOrReadOnly, ]


class Student_NotificationViewSet(viewsets.ModelViewSet):
    queryset = Student_Notification.objects.all()
    serializer_class = Student_NotificationSerializer
    permission_classes = [IsOwnerOrReadOnly, ]


class Student_FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Student_Feedback.objects.all()
    serializer_class = Student_FeedbackSerializer
    permission_classes = [IsOwnerOrReadOnly, ]


class Student_leaveViewSet(viewsets.ModelViewSet):
    queryset = Student_leave.objects.all()
    serializer_class = Student_leaveSerializer
    permission_classes = [IsOwnerOrReadOnly, ]


class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [IsOwnerOrReadOnly, ]


class Attendance_ReportViewSet(viewsets.ModelViewSet):
    queryset = Attendance_Report.objects.all()
    serializer_class = Attendance_ReportSerializer
    permission_classes = [IsOwnerOrReadOnly, ]


class StudentResultViewSet(viewsets.ModelViewSet):
    queryset = StudentResult.objects.all()
    serializer_class = StudentResultSerializer
    permission_classes = [IsOwnerOrReadOnly, ]
