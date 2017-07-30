# -*- coding:utf-8 -*-

"""
DIY Django's JsonResponse and JsonpResponse

class JsonResponse(data, encoder=DjangoJSONEncoder, safe=True, **kwargs) is New in Django 1.7
Ref: https://docs.djangoproject.com/en/1.8/ref/request-response/#jsonresponse-objects
"""

from __future__ import unicode_literals

import datetime
import decimal
import json
import uuid

from django.http import HttpResponse
from django.utils.timezone import is_aware


class DjangoJSONEncoder(json.JSONEncoder):
    """ JSONEncoder subclass that knows how to encode datetime/date/time, Decimal and UUID. """
    def default(self, o):
        # See "Date Time String Format" in the ECMA-262 specification.
        if isinstance(o, datetime.datetime):
            r = o.isoformat()
            if o.microsecond:
                r = r[:23] + r[26:]
            if r.endswith('+00:00'):
                r = r[:-6] + 'Z'
            return r
        elif isinstance(o, datetime.date):
            return o.isoformat()
        elif isinstance(o, datetime.time):
            if is_aware(o):
                raise ValueError("JSON can't represent timezone-aware times.")
            r = o.isoformat()
            if o.microsecond:
                r = r[:12]
            return r
        elif isinstance(o, decimal.Decimal):
            return str(o)
        elif isinstance(o, uuid.UUID):
            return str(o)
        else:
            return super(DjangoJSONEncoder, self).default(o)


class JsonResponse(HttpResponse):
    """ Docstring for JsonHttpResponse """

    def __init__(self, data, encoding='utf8', *args, **kwargs):
        try:
            content = json.dumps(data, ensure_ascii=False, cls=DjangoJSONEncoder, *args)
        except Exception as err:
            content = '{0} can\'t be jsonlized, due to {1}'.format(data, err)

        super(JsonResponse, self).__init__(
            content=content,
            content_type='application/json;charset=UTF-8',
        )


class JsonpResponse(HttpResponse):
    """ Docstring for JsonpHttpResponse """

    def __init__(self, callback, data, encoding='utf8', *args, **kwargs):
        try:
            content = '{0}({1});'.format(callback, json.dumps(data, ensure_ascii=False, cls=DjangoJSONEncoder, *args))
        except Exception as err:
            content = '{0} can\'t be jsonlized, due to {1}'.format(data, err)

        super(JsonpResponse, self).__init__(
            content=content,
            content_type='application/application;charset=UTF-8',
        )


def json_response(func):
    """
    A decorator thats takes a view response and turns it into json.
    """
    def decorator(request, *args, **kwargs):
        objects = func(request, *args, **kwargs)
        if isinstance(objects, (HttpResponse, JsonResponse, JsonpResponse)):
            return objects
        return JsonResponse(objects)
    return decorator


def jsonp_response(func):
    """
    A decorator thats takes a view response and turns it into jsonp.
    """
    def decorator(request, *args, **kwargs):
        objects = func(request, *args, **kwargs)
        if isinstance(objects, (HttpResponse, JsonResponse, JsonpResponse)):
            return objects
        return JsonpResponse(request.GET.get('callback', ''), objects)
    return decorator


def auto_response(func):
    """
    A decorator thats takes a view response and turns it into json.
    If a callback is added through GET or POST the response is JSONP.
    """
    def decorator(request, *args, **kwargs):
        objects = func(request, *args, **kwargs)
        if isinstance(objects, (HttpResponse, JsonResponse, JsonpResponse)):
            return objects
        return JsonpResponse(request.GET.get('callback', ''), objects) if 'callback' in request.GET else JsonResponse(objects)
    return decorator


# For backwards compatibility
LazableJSONEncoder = DjangoJSONEncoder
