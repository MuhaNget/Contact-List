from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.index, name='index'),
    path('add_contact/', views.addContact, name='add_contact'),
    path('edit_contact/<str:pk>', views.editContact, name='edit_contact'),
    path('contact_profile/<str:pk>', views.profileContact, name='contact_profile'),
    path('delete_contact/<str:pk>', views.deleteContact, name='delete')
]