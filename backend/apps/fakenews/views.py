from rest_framework import mixins, status
from rest_framework import viewsets
from rest_framework.response import Response

from apps.fakenews.serializers import InputSerializer
import rpyc


class FakenewsViewset(viewsets.GenericViewSet):
    """
    """
    serializer_class = InputSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        title = serializer.validated_data['title']
        text  = serializer.validated_data['text']

        conn = rpyc.connect('cse256.fduo.me',8080)
        res  = conn.root.exposed_task2(title,text) 

#         res['res'] = True

#         res['resProb'] = 87.89

#         res['explain'] = "The input is: " + title + text + ". Waiting for Fuo Duo and Cheng Qian."

#         res['wordRatio'] = [{'label': 'Good', 'data': [90, 10]},
#                             {'label': 'Great', 'data': [78, 22]},
#                             {'label': 'OK', 'data': [70, 30]},
#                             {'label': 'Thank', 'data': [60, 40]}]

        return Response({'res': res}, status=status.HTTP_200_OK)
