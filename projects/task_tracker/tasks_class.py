import json
from datetime import datetime


class Task:
    def __init__(self, id,  description, created_at, status="todo"):
        # For the id need to check what the last id is in the list
        # self.id = id
        self.description = description
        self.status = status
        self.created_at = created_at
