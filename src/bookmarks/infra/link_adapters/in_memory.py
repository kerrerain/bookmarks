import typing
import bookmarks.domain as bookmarks_domain


class LinkAdapterInMemory(bookmarks_domain.LinkAdapter):
    def __init__(self):
        self.link_collection = []

    def save(self, link: typing.Dict):
        self.link_collection.append({
            "id": 0,
            **link
        })

    def getAll(self) -> typing.List[typing.Dict]:
        return self.link_collection
