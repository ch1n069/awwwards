from rest_framework import serializers



from award.models import *



class ProfileSerializer(serializers.HyperlinkedModelSerializer):


    class Meta:
        model = Profile
        fields = ('id', 'user_id', 'bio')

