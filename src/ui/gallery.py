import supervisely_lib as sly
import globals as g
import cache

try:
    from supervisely_lib.app.widgets import SingleImageGallery

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


def refresh(project_meta: sly.ProjectMeta, image_url, ann: sly.Annotation, output=False):
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
    fields = [
        {"field": "data.gallery", "payload": {"content": content, "options": options}},
    ]
    g.api.task.set_fields(g.task_id, fields)
    if output:
        return {"content": content, "options": options}

# def refresh_labels(labels):
#     fields = [
#         {
#             "field": "data.gallery.content.annotations.ann1.figures",
#             "payload": [label.to_json() for label in labels]
#         },
#     ]
#     g.api.task.set_fields(g.task_id, fields)
