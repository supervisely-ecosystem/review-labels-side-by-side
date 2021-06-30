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


def get_users(context, ann: sly.Annotation):
    user_id = context["userId"]
    user_login = cache.get_user_login(user_id)

    users = defaultdict(int)
    for label in ann.labels:
        if label.geometry.labeler_login == user_login:
            continue
        users[label.geometry.labeler_login] += 1

    res = []
    for user, count in users.items():
        res.append({
            "login": user,
            "count": count
        })
    return res


def get_classes(context, ann: sly.Annotation):
    user_id = context["userId"]
    user_login = cache.get_user_login(user_id)

    classes = defaultdict(int)
    for label in ann.labels:
        if label.geometry.labeler_login == user_login:
            continue
        classes[label.obj_class.name] += 1

    res = []
    for name, count in classes.items():
        res.append({
            "name": name,
            "count": count
        })
    return res


def refresh(context, users, classes):
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
        # {"field": "data.objects", "payload": None},
        # {"field": "state.objCheck", "payload": None},
    ]
    refresh_objects_table(context, userCheck, classCheck, fields)
    g.api.task.set_fields(g.task_id, fields)


def refresh_objects_table(context, userCheck, classCheck, fields):
    project_id = context["projectId"]
    image_id = context["imageId"]

    project_meta = cache.get_meta(project_id)
    image_info = cache.get_image_info(image_id)
    ann = cache.get_annotation(project_id, image_id)

    res_labels = []
    for label in ann.labels:
        cls_name = label.obj_class.name
        login = label.geometry.labeler_login
        if userCheck.get(login, False) is True and classCheck[cls_name] is True:
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

    fields.extend([
        {"field": "data.objects", "payload": objects_table},
        {"field": "state.objCheck", "payload": objects_check},
    ])


@g.my_app.callback("filter")
@sly.timeit
def filter(api: sly.Api, task_id, context, state, app_logger):
    userCheck = state["userCheck"]
    classCheck = state["classCheck"]

    fields = []
    refresh_objects_table(context, userCheck, classCheck, fields)
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


@g.my_app.callback("copy_objects")
@sly.timeit
def copy_objects(api: sly.Api, task_id, context, state, app_logger):
    selected_objects = state["objCheck"]
    project_id = context["projectId"]
    image_id = context["imageId"]

    user_id = context["userId"]
    user_login = cache.get_user_login(user_id)

    project_meta = cache.get_meta(project_id)
    image_info = cache.get_image_info(image_id)
    ann = cache.get_annotation(project_id, image_id)

    res_labels = []
    for label in ann.labels:
        sly_id = str(label.geometry.sly_id)
        if sly_id in selected_objects and selected_objects[sly_id] is True:
            new_geom = label.geometry.clone()
            new_geom.sly_id = None
            new_geom.labeler_login = user_login
            new_geom.updated_at = None
            new_geom.created_at = None
            res_labels.append(label.clone(geometry=new_geom))

    new_ann = ann.add_labels(res_labels)
    cache.update_ann(project_id, image_id, new_ann)

    #@TODO: wip
    # header x-job-id
    #figures.bulk.add

