from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('logReg/', views.logReg),
    path('login/', views.login),
    path('reg/', views.register),
    path('theAdmin/', views.theAdmin),
    path('logout/', views.logout),
    path('movie/', views.allMovies),
    path('movie/<int:dvd_id>/view/', views.viewMovie),
    path('theAdmin/movie/create/', views.createDvd),
    path('theAdmin/movie/<int:dvd_id>/update/', views.updateDvd),
    path('theAdmin/movie/<int:dvd_id>/delete/', views.deleteDvd),
    path('music/', views.allMusic),
    path('music/<int:cds_id>/view/', views.viewMusic),
    path('theAdmin/music/create/', views.createCds),
    path('theAdmin/music/<int:cds_id>/update/', views.updateCds),
    path('theAdmin/music/<int:cds_id>/delete/', views.deleteCds)
]