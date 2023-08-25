from django.shortcuts import render
import requests
import json
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import *
from .models import User
from rest_framework import status

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
    print(response_data)
   

    if response_data["success"] == True:
        print("코드 전송 성공")
        response_body = { "success": True }
        return Response(response_body)
    
    elif response_data["success"] == False and response_data["message"] == "이미 완료된 요청입니다.":
        print("이미 인증, 로그인 처리")
        
        univObj = Univ.objects.get(univName = univ_name)

        extra_fields = {
        # 'email': email,
        'univ_id': univObj,
        'nickName': "닉네임",
        }
        user = User.objects.create_user(email=email, password='', **extra_fields)

        # 2. 해당 정보로 access token, refresh token 발급
        refresh = RefreshToken.for_user(user)
        serializer = UserSerializer(instance=user)
        response_body = serializer.data
        response_body['accessToken'] = str(refresh.access_token) # Replace with the actual access token
        print(response_body)
        return Response(response_body, status=status.HTTP_200_OK)
    
        user = User.objects.get(email = email)
        serializer = UserSerializer(instance=user)
        response_body = serializer.data
        response_body['message'] = "이미 인증된 사용자입니다." # Replace with the actual access token
        print(response_body)
        return Response(response_body, status=status.HTTP_200_OK)

    else:
        print("실패, 오류 출력")


@permission_classes ([permissions.AllowAny])
@api_view(['POST'])
def checkCode(request):
    request_data = request.data

    certifycodeURL = "https://univcert.com/api/v1/certifycode"
    email = request_data.get('email')
    univ_name = request_data.get('univName')
    code = request_data.get('code')
    nickName = request_data.get('nickName')

    body = {
        "key": "3b69aa74-fc31-4dd9-976f-d809da83e4d4",
        "email": email,
        "univ_Name": univ_name,
        "code": code
        }
    # data={
    #     "email":email,
    #     "univName":univ_name,
    #     "nickName":nickName
    # }
    # print("로그인 성공")
    # return Response(data=data)
    response = requests.post(certifycodeURL, json=body)
    print(response)
    response_data = json.loads(response.content)
    print(response_data)
    
    if response_data["success"] == True:
        print("코드 확인 성공, 로그인 처리")
        
        univObj = Univ.objects.get(univName = univ_name)

        extra_fields = {
        'email': email,
        'univ_id': univObj.id,
        'nickName': nickName,
        }
        user = User.objects.create_user(email=email, password='', **extra_fields)

        # 2. 해당 정보로 access token, refresh token 발급
        serializer = UserSerializer(instance=user)
        response_body = serializer.data
        response_body['Message'] = "로그인 성공! 재방문을 환영합니다." # Replace with the actual access token
        print(response_body)
        return Response(response_body, status=status.HTTP_200_OK)
    
    elif response_data["success"] == False and response_data["message"] == "일치하지 않는 인증코드입니다.":
        print("이미 인증, 로그인 처리")
        data={
            "email":email,
            "univName":univ_name,
            "nickName":nickName
        }
        response_body = data
        response_body['Message'] = '로그인 성공! 재방문을 환영합니다.' # Replace with the actual access token
        print(response_body)
        return Response(response_body)

    else:
        return Response("오류")

@permission_classes ([permissions.AllowAny])
@api_view(['POST'])
def makeUniv(request):
    # return Response(status=status.HTTP_100_CONTINUE)
    data = {"univName" : "서강대학교"}
    serializer = UnivSerializer(data=data)
    print(serializer)
    # print(serializer.data)
    if serializer.is_valid():
        serializer.save()  # 데이터베이스에 저장
        print("학교 등록 성공")
        print(serializer.data)
    data = {"univName" : "연세대학교"}
    serializer = UnivSerializer(data=data)
    print(serializer)
    # print(serializer.data)
    if serializer.is_valid():
        serializer.save()  # 데이터베이스에 저장
        print("학교 등록 성공")
        print(serializer.data)
    data = {"univName" : "이화여자대학교"}
    serializer = UnivSerializer(data=data)
    print(serializer)
    # print(serializer.data)
    if serializer.is_valid():
        serializer.save()  # 데이터베이스에 저장
        print("학교 등록 성공")
        print(serializer.data)
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)