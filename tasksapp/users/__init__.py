from tasksapp.tasks.resource import UsersResource


def user_routes(api):
    api.add_resource(UsersResource, '/api/users', '/api/users/<int:user_id>')
    