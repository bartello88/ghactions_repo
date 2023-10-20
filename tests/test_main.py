import pytest
import requests

from main import sum

def test_sum_function():
    assert sum(4,4) == 8

def test_sum2_function():
    assert sum(4,5) == 9


def test_sum3_function():
    assert sum(4,10) == 14

def test_flask_app():
    r = requests.get("http://127.0.0.1:5000")
    assert r.status_code==200