import os
import supervisely as sly
import sys
from supervisely.app.v1.app_service import AppService
from pathlib import Path
my_app: AppService = AppService()

task_id = my_app.task_id
owner_id = int(os.environ['context.userId'])
owner_login = os.environ['context.userLogin']

team_id = int(os.environ['context.teamId'])
workspace_id = int(os.environ['context.workspaceId'])

#project_id = int(os.environ['context.projectId'])
api = my_app.public_api
users_info = api.user.get_team_members(team_id)

#meta_ = api.project.get_meta(project_id)
#meta = sly.ProjectMeta.from_json(meta_)

root_source_dir = str(Path(sys.argv[0]).parents[1])
sly.logger.info(f"Root source directory: {root_source_dir}")
sys.path.append(root_source_dir)

source_path = str(Path(sys.argv[0]).parents[0])
sly.logger.info(f"Source directory: {source_path}")
sys.path.append(source_path)

ui_sources_dir = os.path.join(source_path, "ui")
sys.path.append(ui_sources_dir)
sly.logger.info(f"Added to sys.path: {ui_sources_dir}")