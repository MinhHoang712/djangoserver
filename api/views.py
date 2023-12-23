from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import check_password
from .models import User, Book, Category, Chapter   
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import ChapterSerializer, UserSerializer, BookSerializer, CategorySerializer, BookDetailSerializer, ChangePasswordSerializer
from django.db.models import F
from django.db.models.functions import Greatest

# Create your views here.
class RegisterView(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        if User.objects.filter(username=username).exists():
            return Response({'error': 'Tên người dùng này đã tồn tại.'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = User.objects.filter(username=username).first()
        print(user.role)
        if user and check_password(password, user.password):
            refresh = RefreshToken.for_user(user)
            return Response({
                'username': str(username),
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user_role': str(user.role),
            }, status=status.HTTP_200_OK)

        return Response({'error': 'Sai username hoặc password'}, status=status.HTTP_401_UNAUTHORIZED)
    
class BookListView(APIView):
    def get(self, request, format=None):
        books = Book.objects.all().order_by('-last_updated')
        print(books)
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
class SearchBookView(APIView):
    def get(self, request, format=None):
        query = request.query_params.get('q', '') 
        books = Book.objects.filter(title__icontains=query) | Book.objects.filter(author__icontains=query)

        serializer = BookSerializer(books, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    
class CategoryList(APIView):
    def get(self, request, format=None):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
    
class BookInfo(APIView):
    def get(self, request, pk, format=None):
        try:
            book = Book.objects.get(pk=pk)
            serializer = BookDetailSerializer(book)
            return Response(serializer.data)
        except Book.DoesNotExist:
            return Response({'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)
        
class ChangePasswordView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ChangePasswordSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data.get('username')
            old_password = serializer.validated_data.get('old_password')
            new_password = serializer.validated_data.get('new_password')
            
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                return Response({'error': 'Người dùng không tồn tại.'}, status=status.HTTP_404_NOT_FOUND)
            
            # Kiểm tra mật khẩu hiện tại có chính xác không
            if not check_password(old_password, user.password):
                return Response({'error': 'Mật khẩu hiện tại không chính xác.'}, status=status.HTTP_400_BAD_REQUEST)
            
            # Cập nhật mật khẩu mới
            user.password = new_password
            user.save()
            return Response({'message': 'Mật khẩu đã được thay đổi thành công.'}, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ChapterDetailView(APIView):
    def get(self, request, pk, format=None):
        try:
            chapter = Chapter.objects.get(pk=pk)
            serializer = ChapterSerializer(chapter)
            return Response(serializer.data)
        except Chapter.DoesNotExist:
            return Response({'error': 'Chương không tồn tại'}, status=status.HTTP_404_NOT_FOUND)