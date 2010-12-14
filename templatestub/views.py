# coding: utf-8
import os
from django import template
from django.template import Context, Template, Library, Node
from django.utils import simplejson
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render_to_response

def tag_with_value(value=''):
    class TagNode(Node):
        def render(self,context):
            return value
    def tag(a,b):
        return TagNode()
    return tag

def filter_with_value(value=''):
    def filter(a=None,b=None):
        return value
    return filter

def replace_tags(request,register):
    for tag in request.GET.getlist('tt'):
        tokens = tag.split(':')
        tag_name = tokens[0]
        tag_value = tokens[1] if len(tokens) > 1 else '' 
        register.tag(tag_name, tag_with_value(tag_value) )
        
def replace_filters(request,register):
    for filtro in request.GET.getlist('f'):
        tokens = filtro.split(':')
        filter_name = tokens[0]
        filter_value = tokens[1] if len(tokens) > 1 else '' 
        register.filter(filter_name, filter_with_value(filter_value) )

def replace_filters_and_tags(request):
    register = Library()
    register.tag('load', tag_with_value() )
    replace_tags(request,register)
    replace_filters(request,register)
    template.builtins.append(register)
    
def create_context(request):
    if 'c' not in request.GET:
        return Context({})
    return Context(simplejson.loads(request.GET.get('c')))

def templatestub(request):
    replace_filters_and_tags(request)
    return render_to_response(request.GET.get('t'),create_context(request))
