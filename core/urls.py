from django.urls import path #path function
from . import views # . is shorthand for the current directory

# one urlpattern per line
urlpatterns = [
    path('', views.index, name='index'),
    # path('about/', views.about, name='about'),
    # path('login/', views.login, name='login'),
    # path('registration/', views.registration, name='registration'),
    # path('home/', views.products, name='home'),
    # path('cart/', views.view_cart, name='view_cart'),
    # path('home/<Products_id>/add_to_cart', views.add_to_cart, name='add_to_cart'),
    # # path('checkout/', views.checkout, name='checkout'),
]