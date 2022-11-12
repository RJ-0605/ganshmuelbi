
import pytest

from .conftests import *
from flask import json
from db import  get_provider, create_provider, connect, clear_provider_table
connection=connect()



def test_mock_route(client):
    rv = client.get("/mock_route")
    

    print("##### Begin Testing the apis status code######")

    assert rv.status_code is 200 , f" 200 status_code  if successful expected, got something else"
    

    print("##### Ended Testing the apis status code######")
    print("#################################################")
    print("#################################################")



def test_mock_route_return_value(client):
    rv = client.get("/mock_route")


    print("##### Started Testing the return  ######")

    assert b"Hello World" == rv.data, f" 'Hello World' return statement  if successful expected, got something else"

    print("##### Ended Testing the apis status code######")



def test_post_provider_value(client):

    clear_provider_table(connection)
    rv = client.post('/provider', json={
        'name': 'kwameJude'}, content_type='application/json')

    assert rv.status_code is 200 , f" 200 status_code  if successful expected, got something else"

    json_data = rv.data
    # my_res_data =  json.dumps({'id': 10001})

    assert b'10002' in json_data

    clear_provider_table(connection)



    








