from django.urls import path , include
from django.contrib import admin
from bloodbank.views import home, display
# from accounts.views import landing

urlpatterns = [
    path('', home, name='home'),
    path('display/', display, name='display'),
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls'))
    
]



# from django.urls import path , include
# from django.contrib import admin
# from bloodbank.views import home, display
# from accounts.views import landing

# urlpatterns = [
#     path('', landing, name='landing'),
#     path('display/', display, name='display'),
#     path('admin/', admin.site.urls),
#     path('accounts/',include('accounts.urls'))
    
# ]