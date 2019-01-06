# -*- coding:utf-8 -*- 
import django_filters
from rest_framework import viewsets, filters
from rest_framework.response import Response

import json
import requests
from bs4 import BeautifulSoup
from requests_oauthlib import OAuth1Session

from .models import Account, RefineTweet
from .serializer import AccountSerializer, SearchAccountSerializer, RefineTweetSerializer


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    filter_class = SearchAccountSerializer


class RefineTweetViewSet(viewsets.ModelViewSet):
    queryset = RefineTweet.objects.all()
    serializer_class = RefineTweetSerializer
