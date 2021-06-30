import globals as g
import gallery
import filters


def init(data, state):
    gallery.init(data, state)
    filters.init(data, state)
    pass
