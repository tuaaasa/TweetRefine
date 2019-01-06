from rest_framework import serializers
from django_filters import rest_framework as filters 

from .models import Account, RefineTweet
from .src.refine_tweet import RefineTweets

    
class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'

        
class SearchAccountSerializer(filters.FilterSet):
    screen_name = filters.CharFilter(lookup_expr='exact')

    class Meta:
        model = Account
        fields = '__all__'


class RefineTweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = RefineTweet
        fields = ('created_at', 'text', 'url', 'image_url', 'title', 'account')


class RefineTweetListSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        tweets = [RefineTweet(**tweet) for tweet in validated_data]
        return RefineTweet.objects.bulk_create(tweets)