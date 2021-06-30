@g.my_app.callback('manual_selected_figure_changed')
@sly.timeit
def manual_selected_figure_changed(api: sly.Api, task_id, context, state, app_logger):
    pass
    #print('manual_selected_figure_changed')
    #manual_template(api, state, context)

@g.my_app.callback("show_info")
@sly.timeit
def show_info(api: sly.Api, task_id, context, state, app_logger):
    # print('manual_selected_image_changed')
    # print('context = ', context)
    # print('state = ', state)
    # selected_lablers = state['userNames']
    # show_gallery(api, context, selected_lablers)
    # ui.objects.update_table(api, ann_1, state)
    pass


@g.my_app.callback("refresh_annotations")
@sly.timeit
def refresh_annotations(api: sly.Api, task_id, context, state, app_logger):
    # print('manual_selected_image_changed')
    # print('context = ', context)
    # print('state = ', state)
    # selected_lablers = state['userNames']
    # show_gallery(api, context, selected_lablers)
    # ui.objects.update_table(api, ann_1, state)
    # # @TODO: replace annotation ?
    # # @TODO: add new annotation
    pass


def show_gallery(api, context, selected_lablers):
    # global ann_1
    # print('Show_images: ', context)
    # if context['imageId'] is None:
    #     pass
    # image_id = context['imageId']
    # ann_1 = api.annotation.download(image_id)
    # if selected_lablers:
    #     selected_labler_objs = []
    #     for i in ann_1.annotation['objects']:
    #         if i['labelerLogin'] in selected_lablers:
    #             selected_labler_objs.append(i)
    #     ann_1.annotation['objects'] = selected_labler_objs
    # content = {
    #     "projectMeta": {
    #         "classes": g.meta_['classes'],
    #         "tags": []
    #     },
    #     "annotations": {
    #         "ann_1": {
    #             "url": api.image.get_info_by_id(image_id).full_storage_url,
    #             "figures": ann_1.annotation['objects'],
    #             "info": {"title": "original"}
    #         }
    #     },
    #     "layout": [["ann_1"]]
    # }
    # # <pre>{{data.previewContent}}</pre> # to show code
    # options = {
    #     "showOpacityInHeader": True,
    #     "opacity": 0.8,
    #     "fillRectangle": False,
    # }
    # fields = [
    #     {"field": "data.previewContent", "payload": content},
    #     {"field": "data.previewOptions", "payload": options},
    # ]
    # api.app.set_fields(g.task_id, fields)
    pass


def manual_template(api, state, context):
    # print('context = ', context)
    # print('state = ', state)
    # selected_lablers = state['userNames']
    # show_gallery(api, context, selected_lablers)
    # ui.objects.update_table(api, ann_1, state)
    pass