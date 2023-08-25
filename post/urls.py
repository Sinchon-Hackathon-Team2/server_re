# from django.conf import settings
# from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    # path('comment/', include('comment.urls')),
    # path('follow/', include('follow.urls')),
    # path('like/', include('like.urls')),
    # path('post/', include('post.urls')),
]