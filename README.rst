======================
django-json-response
======================

django-json-response
======================

class JsonResponse(data, encoder=DjangoJSONEncoder, safe=True, **kwargs) is New in Django 1.7
Ref: https://docs.djangoproject.com/en/1.8/ref/request-response/#jsonresponse-objects

Installation
============

::

    pip install django-json-response


Usage
=====

::

    from json_response import JsonResponse

    def excelview(request):
        objs = SomeModel.objects.all()
        return JsonHttpResponse({
            'status': 200,
            'message': u'成功'
            'data': {
                'data1': 'xxx',
                'data2': 'ooo',
                'objs': [obj.data for obj in objs]
            }
        })
