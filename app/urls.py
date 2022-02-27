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
    path('theAdmin/genre/add/', views.createGenre),
    path('theAdmin/genre/<int:topic_id>/update/', views.updateTopic),
    path('theAdmin/genre/<int:topic_id>/delete/', views.deleteTopic),
    path('theAdmin/movie/create/', views.createDvd),
    path('theAdmin/movie/genre/add/', views.addMovieGenre),
    path('theAdmin/movie/<int:dvd_id>/update/', views.updateDvd),
    path('theAdmin/movie/<int:dvd_id>/delete/', views.deleteDvd),
    path('music/', views.allMusic),
    path('music/<int:cds_id>/view/', views.viewMusic),
    path('theAdmin/music/create/', views.createCds),
    path('theAdmin/music/<int:cds_id>/update/', views.updateCds),
    path('theAdmin/music/<int:cds_id>/delete/', views.deleteCds)
]