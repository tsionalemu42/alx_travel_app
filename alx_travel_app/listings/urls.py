# Create URLs for listings app
cat > listings/urls.py << 'EOL'

from django.urls import path
from .views import hello

urlpatterns = [
    path("", hello, name="listings-hello"),
    path('listings/', views.listings_list, name='listings-list'),
    path('listings/<int:pk>/', views.listing_detail, name='listing-detail'), 
]
EOL
