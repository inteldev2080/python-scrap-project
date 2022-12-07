from rest_framework.views import APIView
from rest_framework.response import Response
from try_final import scrapWebsite
from .serializers import CryptoSerializer
from .models import CryptoModel
import time


class CryptoAPIView(APIView):

    def get(self, request):

        all_objs = CryptoModel.objects.all()
        serializer = CryptoSerializer(all_objs, many=True)      
        
        return Response(serializer.data, status=200)        


    def post(self, request):

        # clear old data from db
        CryptoModel.objects.all().delete()

        if CryptoModel.objects.all().count() == 0:

            # Scrap and save data in db
            required_obj = scrapWebsite('https://coinmarketcap.com/')
            
            # print("total objects", len(required_obj))

            for each_obj in required_obj:
                serializer = CryptoSerializer(data=each_obj)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                else:
                    return Response({"error": serializer.error}, status=400)
            
        return Response({"msg": "data fetched successfully."}, status=200)
