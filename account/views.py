from django.shortcuts import render
import requests
import json
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserInfoSerializer
from .models import User

# Create your views here.
@permission_classes ([permissions.AllowAny])
@api_view(['POST'])
def requestCode(request):
    request_data = request.data

    certifyURL = "https://univcert.com/api/v1/certify"
    email = request_data.get('email')
    univ_name = request_data.get('univName')

    body = {
        "key": "3b69aa74-fc31-4dd9-976f-d809da83e4d4",
        "email": email,
        "univName": univ_name,
        "univ_check": False
        }
    
    response = requests.post(certifyURL, json=body)
    response_data = json.loads(response.content)

    if response_data["success"] == True:
        print("코드 전송 성공")
    elif response_data["success"] == False and response_data["message"] == "이미 완료된 요청입니다.":
        print("이미 인증, 로그인 처리")
    else:
        print("실패, 오류 출력")

@permission_classes ([permissions.AllowAny])
@api_view(['POST'])
def checkCode(request):
    certifycodeURL = "https://univcert.com/api/v1/certifycode"
    email = "jiwoong264@mail.hongik.ac.kr"
    univ_name = "홍익대학교"
    code = 2106

    body = {
        "key": "3b69aa74-fc31-4dd9-976f-d809da83e4d4",
        "email": email,
        "univ_Name": univ_name,
        "code": code
        }

    response = requests.post(certifyURL, json=body)

    response_data = json.loads(response.content)

    if response_data["success"] == True:
        print("코드 확인 성공, 로그인 처리")
    elif response_data["success"] == False and response_data["message"] == "이미 완료된 요청입니다.":
        print("이미 인증, 로그인 처리")
    else:
        print("실패, 오류 출력")