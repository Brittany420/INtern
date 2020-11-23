

from django.urls import path, include

from . import views

from APP import views as APP_views


urlpatterns = [
    # path('log-out/', views.logout, name='log-out'),

    path('signup/', views.signup, name='signup'),
    path('student/',views.student, name='student'),
    #path('student_moreinfo/',views.student_moreinfo, name='student_moreinfo'),

    path('sboard/', views.sboard, name='sboard'),
    path('eboard/', views.eboard, name='eboard'),

    path('e_profile/',views.e_profile, name='e_profile'),


    path('employer/',views.employer, name='employer'),
    path('employer_moreinfo/',views.employer_moreinfo, name='employer_moreinfo'),




    path('s_profile/',views.s_profile, name='s_profile'),
    path('create_s_profile/',views.create_s_profile, name='create_s_profile'),

    # path('/',views.e_profile, name='e_profile'),



    path('log-in/home.html', APP_views.home, name='home'),
    path('log-in/contact-us.html', APP_views.contact, name='contact'),
    path('log-in/about.html', APP_views.why, name='why'),
    path('home.html',APP_views.home, name='home'),

    path('signup/home.html', APP_views.home, name='home'),
    path('log-in/log-in.html',views.login, name='log-in'),
    path('log-in/', views.login, name='log-in'),



]
