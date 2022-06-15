import cache
import supervisely as sly
import globals as g
import ui
import gallery
import filters


@g.my_app.callback("manual_selected_image_changed")
@sly.timeit
def manual_selected_image_changed(api: sly.Api, task_id, context, state, app_logger):

    first_state, ann = filters.get_markups(context)
    users = filters.get_users(context, ann)
    classes = filters.get_classes(context, ann)
    tags = filters.get_tags(context, ann)
    filters.refresh(context, users, classes, tags, first_state, ann)


def main():
    sly.logger.info("Script arguments", extra={
        "context.teamId": g.team_id,
        "context.workspaceId": g.workspace_id
    })

    data = {}
    state = {}
    ui.init(data, state)

    g.my_app.compile_template(g.root_source_dir)
    g.my_app.run(data=data, state=state)


if __name__ == "__main__":
    sly.main_wrapper("main", main)
