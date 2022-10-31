from student_management.models import *
from rest_framework import serializers


class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('user_type', 'profile_pic')


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ('name', 'created_at', 'updated_at')


class Session_YearSerializer(serializers.ModelSerializer):

    class Meta:
        model = Session_Year
        fields = ('session_start', 'session_end')


class StudentSerializer(serializers.ModelSerializer):
    # course_id = CourseSerializer()
    # session_year_id = Session_YearSerializer()

    class Meta:
        model = Student
        fields = ('admin', 'address', 'gender', 'course_id',
                  'session_year_id', 'created_at', 'updated_at')


class StaffSerializer(serializers.ModelSerializer):
    #     course_id = CourseSerializer()
    #     session_year_id = Session_YearSerializer()

    class Meta:
        model = Staff
        fields = ('admin', 'address', 'gender',
                  'created_at', 'updated_at')


class SubjectSerializer(serializers.ModelSerializer):
    #     # course_id = CourseSerializer()
    #     # session_year_id = Session_YearSerializer()

    class Meta:
        model = Subject
        fields = ('name', 'course', 'staff', 'updated_at', 'created_at')


class Staff_NotificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Staff_Notification
        fields = ('staff_id', 'message',
                  'created_at', 'status')


class Staff_leaveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Staff_leave
        fields = ('staff_id', 'data', 'message',
                  'created_at', 'updated_at', 'status')


class Staff_FeedbackSerializer(serializers.ModelSerializer):

    class Meta:
        model = Staff_Feedback
        fields = ('staff_id', 'feedback', 'feedback_reply',
                  'created_at', 'updated_at')


class Student_NotificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student_Notification
        fields = ('student_id',  'message',
                  'created_at', 'status')


class Student_FeedbackSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student_Feedback
        fields = ('student_id', 'feedback', 'feedback_reply', 'status',
                  'created_at', 'updated_at')


class StudentResultSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentResult
        fields = ('student_id', 'subject_id',
                  'assignment_mark', 'exam_mark', 'created_at', 'updated_at')


class Attendance_ReportSerializer(serializers.ModelSerializer):

    class Meta:
        model = Attendance_Report
        fields = ('student_id', 'attendance_id', 'created_at', 'updated_at')


class AttendanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Attendance
        fields = ('subject_id', 'attendance_data',
                  'session_year_id', 'created_at', 'updated_at')


class Student_leaveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student_leave
        fields = ('student_id', 'data', 'message',
                  'created_at', 'updated_at', 'status')
