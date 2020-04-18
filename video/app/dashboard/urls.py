# coding:utf-8

from django.urls import path
from .views.base import Index
from .views.auth import Login, AdminManger, Logout, UpdateAdminStatus
from .views.video import (
    ExternalVideo, VideoSubView,
    VideoUpdate, VideoStarView, StarDelete, SubDelete, VideoUpdateStatus)

urlpatterns = [
    path('', Index.as_view(), name='dashboard_index'),
    path('login', Login.as_view(), name='login'),
    path('logout', Logout.as_view(), name='logout'),
    path('admin/manger', AdminManger.as_view(), name='admin_manger'),
    path('admin/manger/update/status',
         UpdateAdminStatus.as_view(),
         name='admin_update_status'
         ),
    path('video/external', ExternalVideo.as_view(), name='external_video'),
    path('video/videosub/<int:video_id>', VideoSubView.as_view(), name='video_sub'),
    path('video/star', VideoStarView.as_view(), name='video_star'),
    path('video/star/delete/<int:star_id>/<int:video_id>', StarDelete.as_view(), name='star_delete'),
    path('video/sub/delete/<int:videosub_id>/<int:video_id>', SubDelete.as_view(), name='sub_delete'),
    path('video/update/<int:video_id>', VideoUpdate.as_view(), name='video_update'),
    path('video/update/status/<int:video_id>', VideoUpdateStatus.as_view(), name='video_update_status')


]