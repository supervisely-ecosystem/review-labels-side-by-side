import os
import supervisely_lib as sly
import sys
from pathlib import Path
my_app = sly.AppService()

task_id = my_app.task_id
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