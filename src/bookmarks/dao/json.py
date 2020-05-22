import bookmarks.model as model

SAVED_BOOKMARK = None


def save(bookmark: model.Bookmark):
    global SAVED_BOOKMARK
    SAVED_BOOKMARK = bookmark


def get(bookmark_id: int):
    return SAVED_BOOKMARK
