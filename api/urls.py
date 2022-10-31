from django.urls import include, path
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'customusers', views.CustomUserViewSet, basename='customuser')
router.register(r'courses', views.CourseViewSet, basename='course')
router.register(r'session_years', views.Session_YearViewSet,
                basename='session_year')
router.register(r'students', views.StudentViewSet, basename='student')
router.register(r'staffs', views.StaffViewSet, basename='staff')
router.register(r'subjects', views.SubjectViewSet, basename='subject')
router.register(r'staff_notifications',
                views.Staff_NotificationViewSet, basename='staff_notification')
router.register(r'staff_leaves', views.Staff_leaveViewSet,
                basename='staff_leave')
router.register(r'staff_feedbacks', views.Staff_FeedbackViewSet,
                basename='staff_feedback')
router.register(r'student_notifications',
                views.Student_NotificationViewSet, basename='student_notification')
router.register(r'student_feedbacks',
                views.Student_FeedbackViewSet, basename='student_feedback')
router.register(r'student_leaves', views.Student_leaveViewSet,
                basename='student_leave')
router.register(r'attendances', views.AttendanceViewSet, basename='attendance')
router.register(r'attendance_reports',
                views.Attendance_ReportViewSet, basename='attendance_reports')
router.register(r'student_results', views.StudentResultViewSet,
                basename='student_result')
urlpatterns = router.urls
