from rest_framework import serializers
from watchlist.models import WatchList, StreamPlatform, Review



class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        exclude = ('watchlist', )
        # fields = "__all__"



class WatchListSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    class Meta:
        model = WatchList
        fields = "__all__"


class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist = WatchListSerializer(many=True, read_only=True)

    class Meta:
        model = StreamPlatform
        fields = "__all__"



        # fields = ['id', 'name', 'description']
        # exclude = ['active']

    # def validate(self, data):
    #     if data['name'] == data['description']:
    #         raise serializers.ValidationError("Title and Description cannot be the same!")
    #     return data

    # def validate_name(self, value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError("Name is to short")
    #     else:
    #         return value



# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
#     description = serializers.CharField()
#     active = serializers.BooleanField()

#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()

#         return instance

#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError("Title and Description cannot be the same!")
#         return data

#     def validate_name(self, value):
#         if len(value) < 2:
#             raise serializers.ValidationError("Name is to short")
#         else:
#             return value