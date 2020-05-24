import os
import json
import typing
import bookmarks.domain as bookmarks_domain


class LinkAdapterJSON(bookmarks_domain.LinkAdapter):
    def __init__(self, filepath: str):
        self.filepath = filepath
        self._init_storage()

    def _init_storage(self):
        if not os.path.exists(self.filepath):
            with open(self.filepath, "w") as json_file:
                json.dump([], json_file)

    def save(self, link: typing.Dict):
        with open(self.filepath) as json_file:
            link_collection = json.load(json_file)

        link_collection.append({
            "id": 0,
            **link
        })

        with open(self.filepath, "w") as json_file:
            json.dump(link_collection, json_file)

    def getAll(self) -> typing.List[typing.Dict]:
        with open(self.filepath) as json_file:
            return json.load(json_file)
