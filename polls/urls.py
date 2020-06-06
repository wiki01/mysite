from django.urls import path
from . import views

urlpatterns = [
    path('', views.Test_Index),
]

print('여기는 Polls 에서 views.py 로 연결하기 위한 패턴???')
print(path('', views.index, name = 'index'))