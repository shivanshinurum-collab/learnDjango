from django.urls import path
from .views import home , test , login , register

urlpatterns = [
    path('',home),
    path('test',test),
    
    path('api/auth/login',login),
    path('api/auth/register',register),
    # path('/api/user/dashboard',test),
    # path('/api/quiz/live',test),
    # path('/api/quiz/submit-answer',test),
    # path('/api/leaderboard',test),
    # path('/api/wallet',test),
    # path('/api/wallet/add-money',test),
    # path('/api/profile',test),
    # path('/api/profile/update',test),
    # path('/api/admin/dashboard',test),
    # path('/api/admin/quizzes',test),
    # path('/api/admin/quizzes',test),
    # path('/api/admin/quizzes/:id',test),
    # path('/api/admin/quizzes/:id',test),
    # path('/api/admin/questions',test),
    # path('/api/admin/questions',test)

]
