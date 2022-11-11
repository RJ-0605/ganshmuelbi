
import pytest

from .conftests import *

def test_mock_route(client):
    rv = client.get("/mock_route")
    assert b"Hello World" == rv.data

    print("##### Started Testing the apis status code######")
    assert rv.status_code is 200 
    print("##### Ended Testing the apis status code######")








