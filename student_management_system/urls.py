from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views, Hod_Views, Student_Views, Staff_Views
from django.urls import include, path
from rest_framework import routers
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# router = routers.SimpleRouter()
# router.register(r'customuser', CustomUserViewSet)
# router.register(r'courses', CourseViewSet)
# router.register(r'session_year', Session_YearViewSet)
# router.register(r'student', StudentViewSet)


schema_view = get_schema_view(
    openapi.Info(
        title="Student_management API",
        default_version='v1',
        description="Student_management APIsi",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="qoziyevsharofiddin199805@gmail.com"),
        license=openapi.License(name="Student_management litsenziyasi"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny, ],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/v1/', include('api.urls')),
    path('api/v1/dj-rest-auth/', include('dj_rest_auth.urls')),
    path('api/v1/dj-rest-auth/registration/',
         include('dj_rest_auth.registration.urls')),
    path('api/v1/allauth/', include('allauth.urls')),
    path('base/', views.BASE, name='base'),
    path('', views.LOGIN, name='login'),
    path('dologin', views.doLogin, name='doLogin'),



    # This Is Hod Urls
    path('hod/home', Hod_Views.HOME, name='hod_home'),
    path('hod/student/add', Hod_Views.ADD_STUDENT, name='add_student'),
    path('hod/student/view', Hod_Views.VIEW_STUDENT, name='view_student'),
    path('hod/student/edit/<str:id>', Hod_Views.EDIT_STUDENT, name='edit_student'),
    path('hod/student/update/', Hod_Views.UPDATE_STUDENT, name='update_student'),
    path('hod/student/delete/<str:admin>',
         Hod_Views.DELETE_STUDENT, name='delete_student'),

    path('hod/course/add', Hod_Views.ADD_COURSE, name='add_course'),
    path('hod/course/view', Hod_Views.VIEW_COURSE, name='view_course'),
    path('hod/course/edit/<str:id>', Hod_Views.EDIT_COURSE, name='edit_course'),
    path('hod/course/update', Hod_Views.UPDATE_COURSE, name='update_course'),
    path('hod/course/delete/<str:id>',
         Hod_Views.DELETE_COURSE, name='delete_course'),

    path('hod/staff/add/', Hod_Views.ADD_STAFF, name='add_staff'),
    path('hod/staff/view/', Hod_Views.VIEW_STAFF, name='view_staff'),
    path('hod/staff/edit/<str:id>', Hod_Views.EDIT_STAFF, name='edit_staff'),
    path('hod/staff/update/', Hod_Views.UPDATE_STAFF, name='update_staff'),
    path('hod/staff/delete/<str:admin>',
         Hod_Views.DELETE_STAFF, name='delete_staff'),

    path('hod/subject/add', Hod_Views.ADD_SUBJECT, name='add_subject'),
    path('hod/subject/view', Hod_Views.VIEW_SUBJECT, name='view_subject'),
    path('hod/subject/edit/<str:id>', Hod_Views.EDIT_SUBJECT, name='edit_subject'),
    path('hod/subject/update/', Hod_Views.UPDATE_SUBJECT, name='update_subject'),
    path('hod/subject/delete/<str:id>',
         Hod_Views.DELETE_SUBJECT, name='delete_subject'),

    path('hod/session/add', Hod_Views.ADD_SESSION, name='add_session'),
    path('hod/session/view', Hod_Views.VIEW_SESSION, name='view_session'),
    path('hod/session/edit/<str:id>', Hod_Views.EDIT_SESSION, name='edit_session'),
    path('hod/session/update/', Hod_Views.UPDATE_SESSION, name='update_session'),
    path('hod/session/delete/<str:id>',
         Hod_Views.DELETE_SESSION, name='delete_session'),

    path('hod/staff/send_notification', Hod_Views.STAFF_SEND_NOTIFICATION,
         name='staff_send_notification'),
    path('hod/staff/save_notification', Hod_Views.SAVE_STAFF_NOTIFICATION,
         name='save_staff_notification'),
    path('hod/staff/leave_view', Hod_Views.STAFF_LEAVE_VIEW,
         name='staff_leave_view'),
    path('hod/staff/leave/approve_leave/<str:id>',
         Hod_Views.STAFF_APPROVE_LEAVE, name='staff_approve_leave'),
    path('hod/staff/leave/disapprove_leave/<str:id>',
         Hod_Views.STAFF_DISAPPROVE_LEAVE, name='staff_disapprove_leave'),

    path('hod/staff/feedback', Hod_Views.STAFF_FEEDBACK,
         name='staff_feedback_reply'),
    path('hod/staff/feedback/save', Hod_Views.STAFF_FEEDBACK_SAVE,
         name='staff_feedback_reply_save'),

    path('hod/student/sent_notification',
         Hod_Views.STUDENT_SENT_NOTIFICATION, name='student_sent_notification'),
    path('hod/student/save_notification',
         Hod_Views.SAVE_STUDENT_NOTIFICATION, name='student_save_notification'),
    path('hod/student/feedback', Hod_Views.STUDENT_FEEDBACK,
         name='get_student_feedback'),
    path('hod/student/feedback/reply_save',
         Hod_Views.REPLY_STUDENT_FEEDBACK, name='reply_student_feedback'),
    path('hod/student/leave_view', Hod_Views.STUDENT_LEAVE_VIEW,
         name='student_leave_view'),
    path('hod/student/leave/approve_leave/<str:id>',
         Hod_Views.STUDENT_APPROVE_LEAVE, name='student_approve_leave'),
    path('hod/student/leave/disapprove_leave/<str:id>',
         Hod_Views.STUDENT_DISAPPROVE_LEAVE, name='student_disapprove_leave'),


    # This Is Staff Urls


    path('staff/home', Staff_Views.HOME, name='staff_home'),
    path('staff/notifications', Staff_Views.NOTIFICATIONS, name='notifications'),
    path('staff/mark_as_done/<str:status>', Staff_Views.STAFF_NOTIFICATION_MARK_AS_DONE,
         name='staff_notification_mark_as_done'),
    path('staff/apply_leave', Staff_Views.STAFF_APPLY_LEAVE,
         name='staff_apply_leave'),
    path('staff/apply_leave/save', Staff_Views.STAFF_APPLY_LEAVE_SAVE,
         name='staff_apply_leave_save'),
    path('staff/feedback', Staff_Views.STAFF_FEEDBACK, name='staff_feedback'),
    path('staff/feedback/save', Staff_Views.STAFF_FEEDBACK_SAVE,
         name='staff_feedback_save'),
    path('staff/take_attendance', Staff_Views.TAKE_ATTENDANCE,
         name='staff_take_attendance'),
    path('staff/save_attendance', Staff_Views.STAFF_SAVE_ATTENDANCE,
         name='staff_save_attendance'),
    path('staff/view_attendance', Staff_Views.STAFF_VIEW_ATTENDANCE,
         name='staff_view_attendance'),
    path('staff/add/result', Staff_Views.STAFF_ADD_RESULT, name='staff_add_result'),

    #  This Is Student Urls

    path('student/home', Student_Views.HOME, name='student_home'),
    path('student/notifications',
         Student_Views.STUDENT_NOTIFICATION, name='notifications'),
    path('student/mark_as_done/<str:status>', Student_Views.STUDENT_NOTIFICATION_MARK_AS_DONE,
         name='student_notification_mark_as_done'),
    path('student/feedback', Student_Views.STUDENT_FEEDBACK,
         name='student_feedback'),
    path('student/feedback/save', Student_Views.STUDENT_FEEDBACK_SAVE,
         name='student_feedback_save'),

    path('student/apply_for_leave',
         Student_Views.STUDENT_LEAVE, name='student_leave'),
    path('student/leave_save', Student_Views.STUDENT_LEAVE_SAVE,
         name='student_leave_save'),


    path('doLogout', views.doLogout, name='dologout'),
    path('profile', views.PROFILE, name='profile'),
    path('profile/update', views.PROFILE_UPDATE, name='profile_update'),
    path('swagger/', schema_view.with_ui('swagger',
                                         cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
                                       cache_timeout=0), name='schema-redoc'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
