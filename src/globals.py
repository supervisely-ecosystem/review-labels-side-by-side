import os
import supervisely_lib as sly

my_app = sly.AppService()

task_id = my_app.task_id
team_id = int(os.environ['context.teamId'])
workspace_id = int(os.environ['context.workspaceId'])

api = my_app.public_api
users_info = api.user.get_team_members(team_id)
