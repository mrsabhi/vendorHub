from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from vendor_accounts.models import VendorAccounts
from vendor_accounts.serializer import VendorAccountSerializer


# Create your views here.
class VendorAccountsView(APIView):
    def get(self, request):
        user = VendorAccounts.objects.all()
        serializer = VendorAccountSerializer(user, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = VendorAccountSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"message": "create your vendor account successfully"},
                            status=status.HTTP_200_OK)
        else:
            return Response({"message": "create your vendor account successfully"},
                            status=status.HTTP_400_BAD_REQUEST)
