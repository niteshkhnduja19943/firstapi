from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.permissions import AllowAny
from rest_framework.mixins import status

# function send_mail is made which will be later called in another function(def get),
# it contains two variables stre and email  which can be user defined.

def send_mail(stre, email):

    from django.core.mail import send_mail

    send_mail(
        'user login details',
        stre,
        'kartik.bhatnagar@civilmachines.com',
        [email],

        fail_silently=False, )


class TestTableApi(APIView):
    permission_classes = (AllowAny,)
    renderer_classes = (JSONRenderer,)

    def get(self):

        import random

        stre = str(random.randrange(1, 101))
        send_mail(stre, 'niteshkhanduja19943@gmail.com')
        return Response("success", status.HTTP_201_CREATED)
    # By running this function get the email will be sent to  provided email
    #  Random function will generate random no. from 1 to 100 and will be sent in message of the email

# this post method is used to put user details we put are inserted in table.

    def post(self, request):
        from .serializers import TestTableSerializers
        sdata = TestTableSerializers(data=request.data)

        if sdata.is_valid():
            sdata.save()
            return Response(sdata.data, status=status.HTTP_201_CREATED)
        else:
            return Response(sdata.errors, status=status.HTTP_400_BAD_REQUEST)

    # delete function is used to delete the user from the table

    def delete(self, request):
        from .serializers import Delete
        sdata = Delete(data=request.data)
        if sdata.is_valid():
            from .models import TestTable
            obj = TestTable.objects.get(pk=sdata.validated_data.get('id', 0))
            obj.delete()
            return Response("Deleted Successfully", status=status.HTTP_202_ACCEPTED)
        else:
            return Response(sdata.errors, status=status.HTTP_400_BAD_REQUEST)

