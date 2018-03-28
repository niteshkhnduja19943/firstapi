from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.permissions import AllowAny
from rest_framework.mixins import status


def send_email(email):
    from django.core.mail import send_mail
    send_mail(
        'user login details',
        'my msg',
        'kartik.bhatnagar@civilmachines.com',
        [email],
        fail_silently=False,
    )
    return Response("email has been sent",status.HTTP_201_CREATED)


class TestTableApi(APIView):
    permission_classes =(AllowAny,)
    renderer_classes = (JSONRenderer,)




    def get(self, request):


        send_email("niteshkhanduja19943@gmail.com")

        return Response("success",status.HTTP_202_ACCEPTED)








    def post(self,request):

        from .serializers import TestTableSerializers
        sdata = TestTableSerializers(data=request.data)

        if sdata.is_valid():
            sdata.save()
            return Response(sdata.data, status=status.HTTP_201_CREATED)
        else:


            return Response(sdata.errors, status=status.HTTP_400_BAD_REQUEST)


    def  delete(self,request):
        from .serializers import Delete
        sdata =Delete(data=request.data)
        if sdata.is_valid():
            from .models import TestTable
            obj = TestTable.objects.get(pk=sdata.validated_data.get('id', 0))
            obj.delete()
            return Response("Deleted Succesfully", status=status.HTTP_202_ACCEPTED)
        else:
            return Response(sdata.errors, status=status.HTTP_400_BAD_REQUEST)

    def forgot_id(self, request):
        from .serializers import forgot_id
        sdata = forgot_id(data=request.data)
        if sdata.is_valid():
            from .serializers import TestTableSerializers
            return Response(sdata.data, status=status.HTTP_202_ACCEPTED)
        else:
            send_email("niteshkhanduja19943@gmail.com")
















































