import globals as g
import objects


def init(data, state):
    name_to_id = dict()
    for user_info in g.api.user.get_team_members(g.team_id):
        name_to_id[user_info.login] = user_info.id
    print(name_to_id)

    data['options'] = [{"value": name, "label": name} for name in name_to_id]
    data['previewContent'] = {}
    data['previewOptions'] = {}

    state['userNames'] = []

    objects.init(data, state)
