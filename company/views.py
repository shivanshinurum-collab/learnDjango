from django.shortcuts import render
from .models import Company , UserModel
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import CompanySerializer
from django.contrib.auth.hashers import check_password, make_password

def home(request):

    companies = Company.objects.all()

    return render(request, 'home.html', {
        'companies': companies
    })


@api_view(['GET'])
def test(request):
    companies = Company.objects.all()

    serializer = CompanySerializer(companies , many = True)

    return Response(serializer.data)




@api_view(['POST'])
def login(request):

    email = request.data.get('email')
    password = request.data.get('password')

    if not email or not password:
        return Response({
            "status": False,
            "message": "Email and password required"
        })

    user = UserModel.objects.filter(email=email).first()

    if user and check_password(password, user.password):
        return Response({
            "status": True,
            "message": "Login successful",
            "user": {
                "id": user.id,
                "name": user.name,
                "email": user.email,
            }
        })

    return Response({
        "status": False,
        "message": "Invalid email or password"
    })


@api_view(["POST"])
def register(request):

    name = request.data.get('name')
    email = request.data.get('email')
    mobile = request.data.get('mobile')
    password = request.data.get('password')

    if not name or not email or not password:
        return Response({
            "status": False,
            "message": "Missing required fields"
        })

    checkUser = UserModel.objects.filter(email=email).first()

    if checkUser:
        return Response({
            'status': False,
            'message': 'Email already exists'
        })

    user = UserModel.objects.create(
        name=name,
        email=email,
        mobile=mobile,
        password=make_password(password)
    )

    return Response({
        'status': True,
        'message': 'Register Success',
        'email': email
    })







