from django.urls import path
from products.views import BulkProductInsert

urlpatterns = [
    path('bulk-insert/', BulkProductInsert.as_view(), name='bulk-insert'),
]
