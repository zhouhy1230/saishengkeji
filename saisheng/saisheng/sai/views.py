# Create your views here.
from rest_framework import status, mixins
from rest_framework.response import Response
from rest_framework.views import APIView
from .utils.serializers import ClientSerializer
from .models import ClientName


class PutView(APIView):
    '''
    输入客户端分数
    '''

    def post(self, request):
        if 'HTTP_X_FORWARDED_FOR' in request.META:
            ip = request.META['HTTP_X_FORWARDED_FOR']
        else:
            ip = request.META['REMOTE_ADDR']
        score = request.data.get('score')
        data_dic = {'ip': ip, 'score': score}
        if ClientName.objects.filter(ip=ip).first():
            serializer = ClientSerializer(instance=ClientName.objects.get(ip=ip), data=data_dic)
        else:
            serializer = ClientSerializer(data=data_dic)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SearchView(APIView):
    '''
    获取排行榜返回数据
    '''

    def get(self, request):
        start = int(self.request.query_params.get('start')) - 1
        end = int(self.request.query_params.get('end'))
        if 'HTTP_X_FORWARDED_FOR' in request.META:
            ip = request.META['HTTP_X_FORWARDED_FOR']
        else:
            ip = request.META['REMOTE_ADDR']

        score = ClientName.objects.get(ip=ip).score
        rank = ClientName.objects.filter(score=score).count()
        clientscore = {"ip": ip, "score": score, "rank": rank + 1}
        values_list = list(ClientName.objects.order_by('-score').values())
        print(values_list)
        values = []
        for val in values_list:
            val["rank"] = values_list.index(val) + 1
            values.append(val)
        # values_list = ClientName.objects.order_by('-score')
        # print(values_list)
        # import pandas as pd
        # df = pd.DataFrame(values_list, columns=["ip", "score"])
        # df.reset_index(inplace=True)
        # print(df)
        # dic = df.to_dict(orient='')
        result = values[start:end]
        result.append(clientscore)
        return Response(result)


# 附加题在versions.py文件中
