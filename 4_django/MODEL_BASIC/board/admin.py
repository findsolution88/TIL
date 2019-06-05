from django.contrib import admin
from .models import Article

# Register your models here.
admin.site.register(Article)

"""
1. python manage.py migrate -> 모든 숨겨진 결재를 실행
2. python manage.py createsuperuser -> 절대 관리자를 생성
3. Domain/admin에 접속 -> 관리자 사이트 갈 수 있음
4. LOG IN
"""