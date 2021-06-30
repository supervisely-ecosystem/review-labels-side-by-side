import supervisely_lib as sly
import globals as g
import cache


def init(data, state):
    data["gallery"] = None
    pass


def refresh(project_meta: sly.ProjectMeta, image_url, ann: sly.Annotation):
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


# def refresh_labels(labels):
#     fields = [
#         {
#             "field": "data.gallery.content.annotations.ann1.figures",
#             "payload": [label.to_json() for label in labels]
#         },
#     ]
#     g.api.task.set_fields(g.task_id, fields)