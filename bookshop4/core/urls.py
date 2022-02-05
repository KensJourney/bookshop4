from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls', namespace='store')),
    path('basket/', include('basket.urls', namespace='basket')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





# <div class="col">
#           <div class="card shadow-sm">
#
#             <div class="form-control">
#               <p class="card-text">
#                 <a class="text-dark text-decoration-none" href="{{ note.get_absolute_url }}">{{ note.title }}</a>
#
#               </p>
#             </div>
#           </div>
#         </div>