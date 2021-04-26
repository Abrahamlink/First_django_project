from django.urls import path
from . import views
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', views.index, name='index'),
    path('article/', views.fib, name='fib'),
    path('article/<int:number>', views.article, name='article'),
    path('users/', views.greet, name='greet'),
    path('users/<username>/<lastname>', views.greeting, name='greeting'),
    path('test/', views.test, name='test'),
    path('blog/', views.header, name='header'),
    path('blog/logout', views.user_logout, name='logout'),
    path('blog/analytics', views.analytics, name='analytics'),
    path('blog/analytics/users', views.users_analytics, name='users_analytics'),
    path('blog/questions', views.questions, name='questions'),
    path('blog/answers', views.answers, name='answers'),
    path('blog/new_question', views.create_question, name='create_question'),
    path('blog/questions/<int:question_id>', views.create_answer, name='create_answer'),
    path('blog/auth', views.auth, name='auth'),
    path('blog/reg', views.reg, name='reg'),
    path('blog/user', views.account, name='account'),
    path('blog/user_profile/<int:user_id>', views.user_profile, name='user_profile'),
    path('blog/user/change', views.change_data, name='change_data'),
    path('blog/user/edit_question/<int:id>', views.change_question, name='edit_question'),
    path('blog/user/edit_answer/<int:id>', views.change_answer, name='edit_answer'),
    path('blog/messages', views.message, name='message'),
    path('blog/write_message', views.write_message, name='write_message'),
    path('blog/delete_message/<str:id>', views.delete_message, name='delete_message')
]

# if settings.DEBUG:
#     urlpatterns += staticfiles_urlpatterns() + static(
#     settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
