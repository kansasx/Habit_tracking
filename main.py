import requests
import os
from datetime import datetime as dt

date = dt.today()
date = date.strftime("%Y%m%d")
# print(date)


url = "https://pixe.la/v1/users"
token = os.environ.get("token")
username = os.environ["username"]


headers = {
        "X-USER-TOKEN": token
    }


def create_user():
    """
    creates a new pixela user
    :return:
    """
    parameters = {
        "token": token,
        "username": username,
        "agreeTermsOfService": "yes",
        "notMinor": "yes",
    }

    response = requests.post(url=url, json=parameters)
    response.raise_for_status()


def create_new_graph():
    """
    creates a new pixela graph
    :return:
    """
    graph_creation_url = f"{url}/{username}/graphs"
    graph_body = {
        "id": "graph1",
        "name": "coding_practice",
        "unit": "hours",
        "type": "int",
        "color": "shibafu"
    }

    graph1 = requests.post(url=graph_creation_url, json=graph_body,
                           headers=headers)
    print(graph1.text)


def create_data(id_="graph1", qty=15):
    """
    inputs data to created graphs
    :param id_:
    :param qty:
    :return:
    """
    put_url = f"{url}/{username}/graphs/{id_}"

    content = {
        "date": date,
        "quantity": f"{qty}",
        "optionalData": '{"message": "today was awesome! had lots of fun coding"}'
    }

    update_graph = requests.post(url=put_url, json=content, headers=headers)
    print(update_graph.text)


def update_data(id_: str = "graph1"):
    """
    updates the data created
    :param id_:
    :return:
    """
    update_url = f"{url}/{username}/graphs/{id_}/{date}"
    update = requests.put(url=update_url, headers=headers)
    update.raise_for_status()
    pass


def delete_data(id_: str = "graph1"):
    """
    deletes an earlier created entry
    :param id_:
    :return:
    """
    delete_url = f"{url}/{username}/graphs/{id_}/{date}"
    requests.delete(delete_url, headers=headers)
