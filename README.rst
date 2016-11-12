====================
django-json-response
====================

django-json-response
====================

* JsonResponse is New in Django 1.7

* Ref: https://docs.djangoproject.com/en/1.8/ref/request-response/#jsonresponse-objects

Installation
============

::

    pip install django-json-response


Warning
=======

::

    Since Version 1.1.3, the JsonpResponse return Object replace of String.

    "{}('{}')" ==> '{}({});'


Usage
=====

::

    from json_response import JsonResponse

    def json_view(request):
        objs = SomeModel.objects.all()

        return JsonResponse({
            'status': 200,
            'message': u'成功',
            'data': {
                'data1': 'xxx',
                'data2': 'ooo',
                'objs': [obj.data for obj in objs]
            }
        })


    or


    from json_response import JsonpResponse

    def jsonp_view(request):
        callback = request.GET.get('callback', '')

        objs = SomeModel.objects.all()

        return JsonpResponse(callback, {
            'status': 200,
            'message': u'成功',
            'data': {
                'data1': 'xxx',
                'data2': 'ooo',
                'objs': [obj.data for obj in objs]
            }
        })

    or

    from json_response import json_response, jsonp_response, auto_response

    @json_response
    def json_view(request):
        objs = SomeModel.objects.all()

        return {
            'status': 200,
            'message': u'成功',
            'data': {
                'data1': 'xxx',
                'data2': 'ooo',
                'objs': [obj.data for obj in objs]
            }
        }

    @jsonp_response
    def jsonp_view(request):
        objs = SomeModel.objects.all()

        return {
            'status': 200,
            'message': u'成功',
            'data': {
                'data1': 'xxx',
                'data2': 'ooo',
                'objs': [obj.data for obj in objs]
            }
        }

    @auto_response
    def jsonp_view(request):
        objs = SomeModel.objects.all()

        return {
            'status': 200,
            'message': u'成功',
            'data': {
                'data1': 'xxx',
                'data2': 'ooo',
                'objs': [obj.data for obj in objs]
            }
        }


