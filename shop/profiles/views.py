# from django.shortcuts import render

import logging
from django.http import HttpResponse

logger = logging.getLogger(__name__)


def profiles(request):
    if request.GET.get("param"):
        logger.info(f"My param = {request.GET.get('param')}")
    return HttpResponse("Profiles view")

# Create your views here.
