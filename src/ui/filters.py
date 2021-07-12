from collections import defaultdict

import gallery
import supervisely_lib as sly
import globals as g
import cache


def init(data, state):
    data["users"] = None  # {}
    state["userCheck"] = None  #{}
    # for key in ["objects", "tags"]:
    #     data["users"][key] = None
    #     state["userCheck"][key] = None

    data["classes"] = None
    state["classCheck"] = None

    data["objects"] = None
    state["objCheck"] = None

    data["tagsCount"] = None
    data["tagsTable"] = None
    state["tagCheck"] = None

    state['firstState'] = None


def get_users(context, ann: sly.Annotation):
    user_id = context["userId"]
    user_login = cache.get_user_login(user_id)

    users = dict(objects=defaultdict(int), tags=defaultdict(int))
    for label in ann.labels:
        if label.geometry.labeler_login == user_login:
            continue
        users['objects'][label.geometry.labeler_login] += 1

    for tag in ann.img_tags:
        if tag.labeler_login == user_login:
            continue
        users['tags'][tag.labeler_login] += 1

    res = dict(objects=list(), tags=list())
    for item_type, item_data in users.items():
        for user, count in item_data.items():
            res[item_type].append(
                {
                    "login": user,
                    "count": count
                }
            )
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


def get_tags(context, ann: sly.Annotation):
    user_id = context["userId"]
    user_login = cache.get_user_login(user_id)

    tags = defaultdict(int)
    tagName2slyId = dict()
    for tag in ann.img_tags:
        if tag.labeler_login == user_login:
            continue
        tags[tag.name] += 1
        tagName2slyId[tag.name] = tag.meta.sly_id
    res = []
    for name, count in tags.items():
        res.append({
            "name": name,
            "count": count,
            "tagId": tagName2slyId[name]
        })
    return res


def _get_or_create_tag_meta(project_id, tag_meta):
    project_meta = cache.get_meta(project_id)
    project_tag_meta: sly.TagMeta = project_meta.get_tag_meta(tag_meta.name)
    if project_tag_meta is None:
        project_meta = project_meta.add_tag_meta(tag_meta)
        cache.update_project_meta(project_id, project_meta)
        project_meta = cache.get_meta(project_id)
        project_tag_meta = project_meta.get_tag_meta(tag_meta.name)
    return project_tag_meta


def _assign_tag_to_image(project_id, image_id, tag_meta):
    project_tag_meta: sly.TagMeta = _get_or_create_tag_meta(project_id, tag_meta)
    g.api.image.add_tag(image_id, project_tag_meta.sly_id)


def refresh(context, users, classes, tags, first_state=None):
    userCheck = {}
    for item_type, item_info in users.items():
        userCheck[item_type] = {}
        for user_info in item_info:
            userCheck[item_type][user_info["login"]] = True

    classCheck = {}
    for class_info in classes:
        classCheck[class_info["name"]] = True

    tagCheck = {}
    for tag_info in tags:
        tagCheck[tag_info["name"]] = True  # ??? name ???

    fields = [
        {"field": "data.users", "payload": users},
        {"field": "state.userCheck", "payload": userCheck},
        {"field": "data.classes", "payload": classes},
        {"field": "state.classCheck", "payload": classCheck},
        {"field": "data.tagsCount", "payload": tags},
        {"field": "state.tagCheck", "payload": tagCheck},
        {"field": "state.firstState", "payload": first_state},
        # {"field": "data.objects", "payload": None},
        # {"field": "state.objCheck", "payload": None},
    ]
    refresh_objects_table(context, userCheck['objects'], classCheck, fields)
    refresh_tags_table(context, userCheck['tags'], tagCheck, fields)
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
        try:
            if userCheck['objects'].get(login, False) is True and classCheck[cls_name] is True:
                res_labels.append(label)
        except:
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


def refresh_tags_table(context, userCheck, tagCheck, fields):
    project_id = context["projectId"]
    image_id = context["imageId"]

    # project_meta = cache.get_meta(project_id)
    # image_info = cache.get_image_info(image_id)
    ann = cache.get_annotation(project_id, image_id)

    res_tags = []
    for tag in ann.img_tags:
        tag_name = tag.name
        login = tag.labeler_login
        # if userCheck.get(login, False) is True and tagCheck[tag_name] is True:
        #     res_tags.append(tag)
        try:
            if userCheck['tags'].get(login, False) is True and tagCheck[tag_name] is True:  # tag_name str(tag.meta.sly_id)
                res_tags.append(tag)
        except:
            if userCheck.get(login, False) is True and tagCheck[tag_name] is True:
                res_tags.append(tag)

    tags_table = []
    tags_check = {i: False for i in tagCheck}  # {}
    for tag in res_tags:
        tags_table.append({
            "tagName": tag.name,
            "createdBy": tag.labeler_login,
            "tagId": str(tag.meta.sly_id)
        })
        tags_check[tag.name] = True  # str(tag.meta.sly_id)

    fields.extend([
        {"field": "data.tagsTable", "payload": tags_table},
        {"field": "state.tagCheck", "payload": tags_check},
    ])


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
    job_id = context.get("jobId", None)
    if job_id is not None:
        api.add_header('x-job-id', str(job_id))

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

    if job_id is not None:
        api.pop_header('x-job-id')


@g.my_app.callback("copy_tags")
@sly.timeit
def copy_tags(api: sly.Api, task_id, context, state, app_logger):
    job_id = context.get("jobId", None)
    if job_id is not None:
        api.add_header('x-job-id', str(job_id))

    selected_tags = state["tagCheck"]
    project_id = context["projectId"]
    image_id = context["imageId"]

    user_id = context["userId"]
    user_login = cache.get_user_login(user_id)

    project_meta = cache.get_meta(project_id)
    image_info = cache.get_image_info(image_id)
    ann = cache.get_annotation(project_id, image_id)

    res_tags = []
    for tag in ann.img_tags:
        # sly_id = str(tag.meta.sly_id)
        sly_id = tag.name
        if sly_id in selected_tags and selected_tags[sly_id] is True:
            new_tag = tag.clone()
            new_tag.labeler_login = user_login
            new_tag.updated_at = None
            new_tag.created_at = None
            res_tags.append(new_tag)

    tag_names = list(set([i.name for i in res_tags]))
    tag_metas = [project_meta.get_tag_meta(tag_name) for tag_name in tag_names]
    for tag_meta in tag_metas:
        _assign_tag_to_image(project_id, image_id, tag_meta)
    cache.get_annotation(project_id, image_id, optimize=False)

    if job_id is not None:
        api.pop_header('x-job-id')


@g.my_app.callback("filter")
@sly.timeit
def filter(api: sly.Api, task_id, context, state, app_logger):
    userCheck = state["userCheck"]
    classCheck = state["classCheck"]
    tagCheck = state["tagCheck"]
    fields = []
    refresh_objects_table(context, userCheck, classCheck, fields)
    refresh_tags_table(context, userCheck, tagCheck, fields)
    g.api.task.set_fields(g.task_id, fields)
