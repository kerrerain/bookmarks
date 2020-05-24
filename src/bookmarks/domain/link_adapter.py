import abc
import typing


class LinkAdapter(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def save(self, link: typing.Dict):
        pass

    @abc.abstractmethod
    def getAll(self) -> typing.List[typing.Dict]:
        pass
