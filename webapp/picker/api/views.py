from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from picker.utils.algorithm import get_best_heroes
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from .serializers import PickerSerializer

class PickerAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = PickerSerializer

    def get(self, request, *args, **kwargs):
        data = request.GET
        home_team = []
        for i in range(1,6):
            if data.get('Home'+str(i)) is not '':
                home_team.append(data.get('Home'+str(i)))
        enemy_team = []
        for i in range(1,6):
            if data.get('Enemy'+str(i)) is not '':
                enemy_team.append(data.get('Enemy'+str(i)))
        results = get_best_heroes(enemy_team, home_team)
        if not results:
            return Response({"Response":'Invalid'}, status=HTTP_400_BAD_REQUEST)
        return Response({"Response":results}, status=HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = request.data
        home_team = []
        for i in range(1,6):
            if data.get('Home'+str(i)) is not '':
                home_team.append(data.get('Home'+str(i)))
        enemy_team = []
        print(home_team)
        for i in range(1,6):
            if data.get('Enemy'+str(i)) is not '':
                enemy_team.append(data.get('Enemy'+str(i)))
        results = get_best_heroes(enemy_team, home_team)
        if not results:
            return Response({"Response":'Invalid'}, status=HTTP_400_BAD_REQUEST)
        return Response({"Response":results}, status=HTTP_200_OK)


'''
sample curl
curl -H "Content-Type: application/json"
    -X POST
    -d '{"Enemy1":"Zeus","Enemy2":"Brewmaster","Enemy3":"","Enemy4":"","Enemy5":"","Home1":"","Home2":"","Home3":"","Home4":"","Home5":""}'
    http://url/api/
'''
