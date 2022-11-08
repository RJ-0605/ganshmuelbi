
import pytest



# def test_request_example(client):
#     response=None
#     response = client.get("/")

#     print ("##################################")
#     print ("##################################")
#     print ('#####Test has started#############')
#     print ("##################################")

#     print ("this is the response", response)

#     assert b"Welcome to Billing" in response.data

#     print ("##################################")
#     print ("##################################")


# def test_request_example(client):
#     response = client.get("/posts")
#     assert b"<h2>Hello, World!</h2>" in response.data



def another_fixture_test(example_people_data):
    value_odtest = example_people_data()
    print ("values ", value_odtest)

    assert value_odtest[1] is  "chiken"
