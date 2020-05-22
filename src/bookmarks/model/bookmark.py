import typing


class Bookmark:
    def __init__(self, bookmark_id: str, meta: typing.Dict):
        self.bookmark_id = bookmark_id
        self.meta = meta
