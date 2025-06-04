class User:
    def __init__(self, id, email, password, name):
        self.id = id
        self.email = email
        self.password = password
        self.name = name

class Task:
    def __init__(self, id, title, description,assignee, storyPoints, status ):
        self.id = id
        self.title = title
        self.description = description
        self.assignee = assignee
        self.storyPoints = storyPoints
        self.status = status