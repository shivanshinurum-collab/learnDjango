from django.shortcuts import render
from .models import Company , userModel
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import CompanySerializer

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
        'message': 'Invalid Email or Password'
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
    




    