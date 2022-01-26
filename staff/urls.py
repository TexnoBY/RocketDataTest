from django.urls import path
from .views import CommonView, LevelView, MeView

urlpatterns = [
    path('', CommonView.as_view(), name='all-users'),
    path('levelusers/<int:level>', LevelView.as_view(), name='level-users'),
    path('me', MeView.as_view(), name='me'),
]