from tasksapp.tasks.resource import TasksResource


def auth_routes(api):
    api.add_resource(UsersResource, '/api/auth', '/api/auth/')
    