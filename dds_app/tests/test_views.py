import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Category, Status, RecordType, Record
from ..serializers import CategorySerializer, StatusSerializer, RecordTypeSerializer, RecordSerializer


# initialize the APIClient app
client = Client()