from django.shortcuts import render
from .models import Company , userModel , quizz , leaderboard , userWallet
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import CompanySerializer , userSerializer
from django.db.models import F

def home(request):

    companies = Company.objects.all()

    return render(request, 'home.html', {
        'companies': companies
    })

@api_view(['GET'])
def test(request):
    users = userModel.objects.all()

    serializer = userSerializer(users , many = True)

    return Response(serializer.data)


# NEW APIs
@api_view(['POST'])
def login(request):

    email = request.data.get('email')
    password = request.data.get('password')

    user = userModel.objects.filter(
        email = email,
        password = password
    ).first()

    if user :
        return Response({
            'status' : True,
            'message' : "Login Success",
            'name' : user.name,
            'email' : email,
        })
    else:
        return Response({
        'success': False,
        'message': 'Invalid Email or Password',
        'name' : "",
        'email' : email,
    })

@api_view(["POST"])
def register(request):

    name = request.data.get('name')
    email = request.data.get('email')
    mobile = request.data.get('mobile')
    password = request.data.get('password')   

    checkUser = userModel.objects.filter(
        email = email
    ).first()

    if checkUser :
        return Response({
            'status' : False,
            'message' : 'Email already exists'
        }) 
    else:
        leaderboard.objects.create(
            email = email,
        )
        user = userModel.objects.create(
            name = name,
            email = email,
            mobile = mobile,
            password = password
        )
        return Response({
            'status' : True,
            'message' : 'Register Success',
            'email' : email
        })
    
@api_view(['POST'])
def addQuiz(request):
    question = request.data.get('question')
    level = request.data.get('level')
    op1 = request.data.get('op1')
    op2 = request.data.get('op2')
    op3 = request.data.get('op3')
    op4 = request.data.get('op4')
    ans = request.data.get('ans')

    newQuiz = quizz.objects.create(
        question = question,
        level = level,
        op1 = op1,
        op2 = op2,
        op3 = op3,
        op4 = op4,
        ans = ans
    )

    return Response({
        'status' : True,
        'message':'Quizz Added Successfully',
        'quiz': {
        'id': newQuiz.id,
        'question': newQuiz.question,
        'level': newQuiz.level,
        'op1': newQuiz.op1,
        'op2': newQuiz.op2,
        'op3': newQuiz.op3,
        'op4': newQuiz.op4,
        'ans': newQuiz.ans,
        }
    })

@api_view(['POST'])
def getQuizz(request):
    level = request.data.get('level')
    idd = request.data.get('id')

    quiz = quizz.objects.filter(
        level = level,
        id__gt = idd
    )
    
    if quiz.exists():
        data = []

        for q in quiz :
            data.append({
                "id": q.id,
                "question": q.question,
                "op1": q.op1,
                "op2": q.op2,
                "op3": q.op3,
                "op4": q.op4,
                "ans": q.ans
            })
        return Response({
            'status' : True,
            'quiz' : data
        })    
    else:
        return Response({
            'status' : False,
            "quiz": "All Quiz are Completed"
        })

@api_view(['POST'])
def quizSubmit(request):
    id = request.data.get('id')
    email = request.data.get('email')
    selectOp = request.data.get('selectOp')

    quiz = quizz.objects.filter(
        id = id,
    ).first()

    if quiz.ans == selectOp :
        leaderboard.objects.filter(
            email = email
        ).update(
            score = F('score') +1
        )
        return Response({
            'status' : True,
            'answer' : 'correct'
        })
    return Response({
            'status' : True,
            'answer' : 'Incorrect'
        })

@api_view(['POST'])
def profile(request):
    email = request.data.get('email')

    user = userModel.objects.filter(
        email = email
    ).first()

    if not user :
        return Response({
            'status' : False,
            'message' : 'User Not Found'
        })

    return Response({
        'status' : True,
        'message' : "User Found",
        'user' : {
            'name' : user.name,
            'email' : user.email,
            'mobile' : user.mobile,
        }
    })

@api_view(["POST"])
def updateProfile(request):
    email = request.data.get('email')
    name = request.data.get('name')
    mobile = request.data.get('mobile')

    userModel.objects.filter(
        email = email
    ).update(
        name = name,
        mobile = mobile
    )
    user = userModel.objects.filter(email = email).first()
    if not user :
        return Response({
            'status' : False,
            'user' : "User not Found"
        })
        
    
    return Response({
        'status' : True,
        'user' : {
            'email' : user.email,
            'name' : user.name,
            'mobile' : user.mobile
        }
        })

@api_view(["POST"])
def leaderboardAll(request):
    email = request.data.get('email')

    check = leaderboard.objects.filter(
        email = email
    )
    if not check:
        leaderboard.objects.create(
            email = email,
            score = 0
        )

    all = leaderboard.objects.all()

    scores = []
    for s in all:
        scores.append({
            "id" : s.id,
            "email" : s.email,
            "score" : s.score
        })
    return Response({
        'leaderboad' :  scores
    })

@api_view(["POST"])
def getUserWallet(request):
    email = request.data.get('email')

    obj , created = userWallet.objects.get_or_create(
        email = email,
        defaults={'wallet' : 0}
    )
    obj.arefresh_from_db
    return Response({
        'status' : True,
        'wallet' : obj.wallet
    })
    
@api_view(["POST"])
def addMoneyWallet(request):
    email = request.data.get('email')
    money = int(request.data.get('money'))

    obj , created = userWallet.objects.get_or_create(
        email = email,
        defaults = {'wallet' : 0}
    )
    userWallet.objects.filter(email = email).update(wallet = F('wallet') + money)

    obj.refresh_from_db()
    return Response({
        'status' : True,
        'message' : 'Money Added Success',
        'email' : email,
        'wallet' : money
    })    



