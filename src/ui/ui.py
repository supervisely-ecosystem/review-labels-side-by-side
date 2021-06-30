import globals as g
import gallery
import objects
import filters


def init(data, state):
    gallery.init(data, state)
    filters.init(data, state)
    pass
    # name_to_id = dict()
    # for user_info in g.api.user.get_team_members(g.team_id):
    #     name_to_id[user_info.login] = user_info.id
    # print(name_to_id)
    #
    # data['options'] = [{"value": name, "label": name} for name in name_to_id]
    # data['previewContent'] = {}
    # data['previewOptions'] = {}
    # objects.init(data, state)
