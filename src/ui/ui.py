import globals as g
import gallery
import filters


def init(data, state):
    data["ownerId"] = g.owner_id
    data["ownerLogin"] = g.owner_login
    gallery.init(data, state)
    filters.init(data, state)
    pass
