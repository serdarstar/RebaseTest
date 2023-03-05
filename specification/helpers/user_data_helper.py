# pylint: disable=too-many-branches

"""Helpers for generating data"""
import json

USER_FILE_PATH = "specification/features/data/users/%s.json"


def get_user_data(user_type):
    """Gets user data as dict"""
    with open(USER_FILE_PATH % user_type, encoding="utf-8") as file:
        return json.load(file)
