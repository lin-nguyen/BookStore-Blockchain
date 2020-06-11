from django.urls import path
from . import views
from .views import HomePageView, AboutPageView, HistoryPageView, ProfileView, PurchasePageView, \
    UserPaymentMethod, PaymentMethodCreate, PaymentMethodUpdate, PaymentMethodDelete

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('history/', HistoryPageView.as_view(), name='history'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('purchase/', PurchasePageView.as_view(), name='purchase'),
    path('audit/book/<int:isbn>', views.audit_page_view, name='audit'),
    # path('audit/<slug:name>', views.audit_page_view, name='audit'), using slug for creating meaningful urls
    path('payment_methods', UserPaymentMethod.as_view(), name='payment-method'),
    path('method/new/', PaymentMethodCreate.as_view(), name='method-create'),
    path('method/<int:pk>/update/', PaymentMethodUpdate.as_view(), name='method-update'),
    path('method/<int:pk>/delete/', PaymentMethodDelete.as_view(), name='method-delete'),
]
