import supervisely_lib as sly
import globals as g


def init(data, state):
    columns = [
        {"title": "Class"},
        {"title": "Shape"},
        {"title": "Created_by"},
    ]
    rows = [
        # {
        #     "Class": "lemon",
        #     "Shape": "Bitmap",
        #     "Created_by": "DmitriyM",
        # },
        # {
        #     "Class": "kiwi",
        #     "Shape": "Bitmap",
        #     "Created_by": "DmitriyM",
        # },
    ]
    data["myColumns"] = columns
    data["myRows"] = rows
    state["classChecked"] = {
        "lemon": False,
        "kiwi": True
    }


def update_table(api, annotation, state):
    print(1)
    rows = []
    for object_ in annotation.annotation['objects']:
        print(object_)
        row = {
            "Class": object_['classTitle'],
            "Shape": object_['geometryType'],
            "Created_by": object_['labelerLogin']
        }
        rows.append(row)

    fields = [
        {"field": "data.myRows", "payload": rows}
    ]
    api.app.set_fields(g.task_id, fields)
