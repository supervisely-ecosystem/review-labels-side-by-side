import supervisely as sly
import globals as g
import cache

try:
    from supervisely.app.v1.widgets.single_image_gallery import SingleImageGallery

    single_image_gallery = SingleImageGallery(
        task_id=g.task_id,
        api=g.api,
        v_model='data.gallery',
        project_meta=sly.ProjectMeta()  # заглушка
    )
except:
    pass


def init(data, state):
    data["gallery"] = None
    state['active'] = None
    pass


def refresh(project_meta: sly.ProjectMeta, image_url, ann: sly.Annotation, update_options=False, output=False):
    content = {
        "projectMeta": project_meta.to_json(),
        "annotations": {
            "ann1": {
                "url": image_url,
                "figures": [label.to_json() for label in ann.labels],
            }
        },
        "layout": [["ann1"]]
    }
    options = {
        "showOpacityInHeader": False,
        "opacity": 0.8,
        "fillRectangle": False,
    }
    data_infos = {"content": content}
    if update_options:
        data_infos["options"] = options
    fields = [
        {"field": "data.gallery", "payload": data_infos},
    ]
    g.api.task.set_fields(g.task_id, fields)
    if output:
        return data_infos

# def refresh_labels(labels):
#     fields = [
#         {
#             "field": "data.gallery.content.annotations.ann1.figures",
#             "payload": [label.to_json() for label in labels]
#         },
#     ]
#     g.api.task.set_fields(g.task_id, fields)
