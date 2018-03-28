from rest_framework import serializers





class TestTableSerializers(serializers.ModelSerializer):

    class Meta:
        from .models import TestTable

        model = TestTable
        fields = '__all__'




class Delete(serializers.Serializer):
    id = serializers.IntegerField(required=True)


class forgot_id(serializers.Serializer):
        id = serializers.IntegerField(required=True)










