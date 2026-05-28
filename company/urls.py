from django.urls import path
from .views import home , test , login , register , addQuiz , getQuizz , profile , quizSubmit , updateProfile , leaderboardAll , getUserWallet , addMoneyWallet

urlpatterns = [
    path('',home),
    path('test',test),
    
    path('api/auth/login/',login),
    path('api/auth/register/',register),
    path('api/addQuiz/',addQuiz),
    path('api/getQuiz/',getQuizz),
    path('api/profile/',profile),
    path('api/updateProfile/',updateProfile),
    path('api/quiz/live/submit/',quizSubmit),
    path('api/leaderboard/',leaderboardAll),
    path('api/wallet/',getUserWallet),
    path('api/wallet/add-money/',addMoneyWallet)
    
]
