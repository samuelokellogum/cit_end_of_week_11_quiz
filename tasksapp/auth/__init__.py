from tasksapp.tasks.resource import AuthResource


def auth_routes(api):
    api.add_resource(UsersResource, '/api/auth', '/api/auth/')
    