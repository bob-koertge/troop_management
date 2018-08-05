from django.contrib import admin
from django.urls import include, path

from troop.views import troop, scouts, parents, leaders

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('troop.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', troop.SignUpView.as_view(), name='signup'),
    path('accounts/signup/scout/',
         scouts.ScoutSignUpView.as_view(), name='scout_signup'),
    path('accounts/signup/parent/',
         parents.ParentSignUpView.as_view(), name='parent_signup'),
    path('accounts/signup/leader/',
         leaders.LeaderSignUpView.as_view(), name='leader_signup'),

]
