import cache
import supervisely_lib as sly
import globals as g
import ui
import gallery
import filters


@g.my_app.callback("manual_selected_image_changed")
@sly.timeit
def manual_selected_image_changed(api: sly.Api, task_id, context, state, app_logger):
    # print('manual_selected_image_changed')
    # manual_template(api, state, context)

    project_id =  context["projectId"]
    image_id = context["imageId"]

    project_meta = cache.get_meta(project_id)
    image_info = cache.get_image_info(image_id)
    ann = cache.get_annotation(project_id, image_id)

    gallery.refresh(project_meta, image_info.full_storage_url, ann)
    users = filters.get_users(context, ann)
    classes = filters.get_classes(context, ann)
    filters.refresh(context, users, classes)


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

#@TODO: add laodings
#TODO: refresh ann cache after copy + refresh UI (hide user's annotations)
#@TODO: reimplement copy figures to handle job stats
#@TODO: get job classes and tags and use only them in filters
if __name__ == "__main__":
    sly.main_wrapper("main", main)
