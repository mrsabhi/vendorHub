from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from authentications.models import User
from vendor_accounts.models import VendorAccounts
from vendor_accounts.serializer import VendorAccountSerializer


# Create your views here.
class VendorAccountsView(APIView):
    def get(self, request):
        user = VendorAccounts.objects.all()
        serializer = VendorAccountSerializer(user, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        print(request.user,"jay mata di")
        serializer = VendorAccountSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = request.data.get("vendor_email")
            user = User.objects.get(email=email)
            if user is not None:
                if not user.is_vendor:
                    user.is_vendor = True
                    user.save()
                    serializer.save()
                    return Response({"message": "create your vendor account successfully",
                                     "msg": "is vendor becomes true"},
                                    status=status.HTTP_200_OK)
                else:
                    return Response({"msg": "try again","status":"You are already vendor "},
                                    status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({"msg": "user does not exist"},
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
