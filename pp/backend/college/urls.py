from django.urls import include, path
from college import views


COURSES_LIST = views.CourseViewSet.as_view({
    'post' : 'create_course',
    'get'  : 'list_all_courses'
})
COLLEGE_LIST = views.CollegeViewSet.as_view({
    'post' : 'add_college',
    'get'  : 'list_all_colleges'
})
EXAM_LIST = views.ExamViewSet.as_view({
    'post' : 'add_exam',
    'get'  : 'list_all_exams'
})
EXAM_LATEST = views.ExamViewSet.as_view({
    'get'  : 'latest_exam'
})
urlpatterns = [
    path(r'course/add/', views.CourseViewSet.as_view(
        {'post': 'create_course'},name='course_create'
    )),
    path(r'course/list/', views.CourseViewSet.as_view(
        {'get': 'list_all_courses'},name='course_list'
    )),
    path(r'list/', views.CollegeViewSet.as_view(
        {'get': 'list_all_colleges'},name='college_list'
    )),
    path(r'add/', views.CollegeViewSet.as_view(
        {'post': 'add_college'},name='college_added'
    )),    
    path(r'exam/list/', views.ExamViewSet.as_view(
        {'get': 'list_all_exams'},name='exam_list'
    )),
    path(r'exam/add/', views.ExamViewSet.as_view(
        {'post': 'add_exam'},name='exam_added'
    )),    
    path(r'exam/latest/', views.ExamViewSet.as_view(
        {'get': 'latest_exam'},name='exam_latest'
    )), 
    ]   