# from django.urls import path

from rest_framework import routers
from .views import AccountViewSet, RefineTweetViewSet

router = routers.DefaultRouter()
router.register(r'accounts', AccountViewSet)
router.register(r'refine_tweets', RefineTweetViewSet)
# refine_tweet_router = routers.NestedSimpleRouter(router, r'accounts', lookup='account')
# refine_tweet_router.register(r'refine_tweets', RefineTweetViewSet, base_name='account-tweets')