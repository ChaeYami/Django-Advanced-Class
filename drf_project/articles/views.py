from rest_framework.views import APIView
from rest_framework import status, permissions  # permission_classes 사용
from rest_framework.response import Response
from users.serializers import UserSerializer


# Create your views here.


class ArticleView(APIView):
    # 글 목록
    def get(self, request):  # => request.method == 'GET':
        pass
    # 글 작성
    def post(self, request):  # => request.method == 'POST':
        pass


class ArticleDetailView(APIView): 
    # 상세페이지
    def get(self, request, article_id):  # => request.method == 'GET':
        pass
    # 글 작성 (수정?)
    def post(self, request, article_id):  # => request.method == 'POST':
        pass
    # 글 삭제
    def delete(self, request, article_id):  # => request.method == 'POST':
        pass

class CommentView(APIView): 
    # 댓글 불러오기 (댓글 리스트)
    def get(self, request):  # => request.method == 'GET':
        pass
    # 댓글 달기
    def post(self, request):  # => request.method == 'POST':
        pass
    
class CommentDetailView(APIView):    
    '''
    # 댓글 수정
    def put(self, request, comment_id):  # => request.method == 'POST':
        pass
    '''
    # 댓글 삭제
    def delete(self, request, comment_id):  # => request.method == 'POST':
        pass

class LikeView(APIView):
    def post(self,request):
        pass