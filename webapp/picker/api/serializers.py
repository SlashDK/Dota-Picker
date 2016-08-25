from rest_framework.serializers import Serializer, CharField

class PickerSerializer(Serializer):
    Home1 = CharField(max_length=50, default='')
    Home2 = CharField(max_length=50, default='')
    Home3 = CharField(max_length=50, default='')
    Home4 = CharField(max_length=50, default='')
    Home5 = CharField(max_length=50, default='')
    Enemy1 = CharField(max_length=50, default='')
    Enemy2 = CharField(max_length=50, default='')
    Enemy3 = CharField(max_length=50, default='')
    Enemy4 = CharField(max_length=50, default='')
    Enemy5 = CharField(max_length=50, default='')
