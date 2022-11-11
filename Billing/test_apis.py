
import pytest

from conftests import *

def test_square(client):
    rv = client.get("/test_route")
    assert b"Hello World" == rv.data








