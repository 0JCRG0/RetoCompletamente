from django.test import TestCase
from django.db import connection
from .utils.main_utils import *
from .utils.UserCV_utils import *
from pgvector.psycopg2 import register_vector
import pandas as pd
import asyncio
import logging
import pretty_errors
from mysite.settings import DEBUG, ALLOWED_HOSTS
from django.contrib.postgres.search import SearchVector, SearchQuery
from .models import SuitableJobs

