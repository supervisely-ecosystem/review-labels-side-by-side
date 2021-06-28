import supervisely_lib as sly
import globals as g


@g.my_app.callback("show_info")
@sly.timeit
def show_info(api: sly.Api, task_id, context, state, app_logger):
    print('context = ', context)
    print('state = ', state)
    image = api.image.get_info_by_id(context['imageId'])


def show_gallery(api, context):
    image_id = context['imageId']
    image = api.image.get_info_by_id(context['imageId'])
    fields = [
        {"field": "data.perClassExtendedTable", "payload": table_data},
        # {"field": "data.perClassTable", "payload": {"columns": metrics.table_classes_columns,
        #                                             "data": table_classes}},
        {"field": "data.perClassLineChartOptions", "payload": line_chart_options},
        {"field": "data.perClassLineChartSeries", "payload": line_chart_series}
    ]
    api.app.set_fields(g.task_id, fields)
    pass


@g.my_app.callback("manual_selected_image_changed")
@sly.timeit
def manual_selected_image_changed(api: sly.Api, task_id, context, state, app_logger):
    print('manual_selected_image_changed')
    print('context = ', context)
    print('state = ', state)
    show_gallery(api, context)


@g.my_app.callback('manual_selected_figure_changed')
@sly.timeit
def manual_selected_figure_changed(api: sly.Api, task_id, context, state, app_logger):
    print('manual_selected_figure_changed')
    print('context = ', context)
    print('state = ', state)
    show_gallery(api, context)


def main():
    sly.logger.info("Script arguments", extra={
        "context.teamId": g.team_id,
        "context.workspaceId": g.workspace_id
    })

    data = {}
    state = {}

    name_to_id = dict()
    for user_info in g.api.user.get_team_members(g.team_id):
        name_to_id[user_info.login] = user_info.id
    print(name_to_id)
    data['userNames'] = []
    data['options'] = [{"value": i, "label": i} for i in name_to_id]
    g.my_app.run(data=data, state=state)


if __name__ == "__main__":
    sly.main_wrapper("main", main)
