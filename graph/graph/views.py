from django.http import JsonResponse
from django.shortcuts import render
from django.db.models import Max

import json

from tuobu.models import Graph


def index(request):
    # 获取最新的一条数据
    graph_obj = Graph.objects.latest('create_time')
    test = graph_obj.graph_json
    return render(request, 'test.html', locals())


def test(request):
    data = request.GET.get('test')
    print(data)
    graph = Graph(graph_json=json.loads(data))
    graph.save()
    return JsonResponse({
        'code': 201
    })
