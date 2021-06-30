from collections import defaultdict

import gallery
import supervisely_lib as sly
import globals as g
import cache


def init(data, state):
    data["users"] = None
    state["userCheck"] = None

    data["classes"] = None
    state["classCheck"] = None

    data["objects"] = None
    state["objCheck"] = None


def get_users(ann: sly.Annotation):
    users = defaultdict(int)
    for label in ann.labels:
        users[label.geometry.labeler_login] += 1

    res = []
    for user, count in users.items():
        res.append({
            "login": user,
            "count": count
        })
    return res


def get_classes(ann: sly.Annotation):
    classes = defaultdict(int)
    for label in ann.labels:
        classes[label.obj_class.name] += 1

    res = []
    for name, count in classes.items():
        res.append({
            "name": name,
            "count": count
        })
    return res


def refresh(users, classes):
    userCheck = {}
    for user_info in users:
        userCheck[user_info["login"]] = True

    classCheck = {}
    for class_info in classes:
        classCheck[class_info["name"]] = True

    fields = [
        {"field": "data.users", "payload": users},
        {"field": "state.userCheck", "payload": userCheck},
        {"field": "data.classes", "payload": classes},
        {"field": "state.classCheck", "payload": classCheck},
        {"field": "data.objects", "payload": None},
        {"field": "state.objCheck", "payload": None},
    ]
    g.api.task.set_fields(g.task_id, fields)


@g.my_app.callback("filter")
@sly.timeit
def filter(api: sly.Api, task_id, context, state, app_logger):
    userCheck = state["userCheck"]
    classCheck = state["classCheck"]

    project_id = context["projectId"]
    image_id = context["imageId"]

    project_meta = cache.get_meta(project_id)
    image_info = cache.get_image_info(image_id)
    ann = cache.get_annotation(project_id, image_id)

    res_labels = []
    for label in ann.labels:
        cls_name = label.obj_class.name
        login = label.geometry.labeler_login
        if userCheck[login] is True and classCheck[cls_name] is True:
            res_labels.append(label)

    new_ann = ann.clone(labels=res_labels)
    gallery.refresh(project_meta, image_info.full_storage_url, new_ann)

    objects_table = []
    objects_check = {}
    for label in res_labels:
        objects_table.append({
            "objClass": label.obj_class.name,
            "shape": label.geometry.geometry_name(),
            "createdBy": label.geometry.labeler_login,
            "objId": str(label.geometry.sly_id)
        })
        objects_check[str(label.geometry.sly_id)] = True

    fields = [
        {"field": "data.objects", "payload": objects_table},
        {"field": "state.objCheck", "payload": objects_check},
    ]
    g.api.task.set_fields(g.task_id, fields)


@g.my_app.callback("show_selected_objects")
@sly.timeit
def show_selected_objects(api: sly.Api, task_id, context, state, app_logger):
    selected_objects = state["objCheck"]
    project_id = context["projectId"]
    image_id = context["imageId"]

    project_meta = cache.get_meta(project_id)
    image_info = cache.get_image_info(image_id)
    ann = cache.get_annotation(project_id, image_id)

    res_labels = []
    for label in ann.labels:
        sly_id = str(label.geometry.sly_id)
        if sly_id in selected_objects and selected_objects[sly_id] is True:
            res_labels.append(label)

    new_ann = ann.clone(labels=res_labels)
    gallery.refresh(project_meta, image_info.full_storage_url, new_ann)
