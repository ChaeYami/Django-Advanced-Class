from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.decorators import api_view
from articles.models import Article
from articles.serializers import ArticleSerializer
from rest_framework import status # 상태 보내줄 때 사용
from rest_framework.generics import get_object_or_404 # 없는 글 조회 에러처리에 사용


# Create your views here.

# =============== 조회, 생성 (GET, POST) =============== 

# 특정 데이터 선택
# @api_view(['GET'])
# def index(request):
#     articles = Article.objects.all()
#     articles = articles[0]
#     serializer = ArticleSerializer(articles)
#     return Response(serializer.data)


#전체 데이터
@api_view(['GET','POST'])
def articleAPI(request):
     # READ
    if request.method == 'GET':
        articles = Article.objects.all() # 데이터 가져오기
        serializer = ArticleSerializer(articles, many = True) # 데이터 보여주기
        return Response(serializer.data)
     # CREATE
    elif request.method == 'POST':
        serializer = ArticleSerializer(data = request.data) # 데이터 받아오기
        if serializer.is_valid(): # 유효성 검사 통과
            serializer.save() # 받아온 데이터 db에 저장
            return Response(serializer.data, status=status.HTTP_201_CREATED) # 정상 생성 (등록) 상태
        else: # 유효성 검사 만족 X -> 입력값에 문제
            print(serializer.errors) 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # 에러를 반환, 잘못된 요청 상태

@api_view(['GET','PUT','DELETE'])
def articleDetailAPI(request,article_id):
    if request.method == 'GET': # 상세페이지
        article = get_object_or_404(Article, id = article_id) # 데이터 가져오기
        serializer = ArticleSerializer(article) # 데이터 보여주기
        return Response(serializer.data)
    elif request.method == 'PUT': # 수정
        article = get_object_or_404(Article, id = article_id) # 데이터 가져오기
        serializer = ArticleSerializer(article, data = request.data) # 데이터 받아오기 (post 와 get 이 섞인 느낌!)
        if serializer.is_valid(): # 유효성 검사 통과
            serializer.save() # 받아온 데이터 db에 저장
            return Response(serializer.data) # 정상 생성 (등록) 상태
        else: # 유효성 검사 만족 X -> 입력값에 문제
            print(serializer.errors) 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # 에러를 반환, 잘못된 요청 상태
    elif request.method == 'DELETE':
        article = get_object_or_404(Article, id = article_id)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)