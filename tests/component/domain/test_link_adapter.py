import typing
import pytest
import bookmarks.domain as bookmarks_domain
import bookmarks.infra as bookmarks_infra


def json_factory(tmp_path):
    return bookmarks_infra.LinkAdapterJSON(str(tmp_path / "links.json"))


def in_memory_factory(_):
    return bookmarks_infra.LinkAdapterInMemory()


FACTORIES = [
    json_factory,
    in_memory_factory
]


@pytest.mark.parametrize("factory", FACTORIES)
def test_is_link_adapter(tmp_path, factory: typing.Callable):
    # Given
    adapter = factory(tmp_path)

    # When
    actual = isinstance(adapter, bookmarks_domain.LinkAdapter)

    # Then
    assert actual


@pytest.mark.parametrize("factory", FACTORIES)
def test_save_get_objects_identical(tmp_path, valid_link, factory: typing.Callable):
    # Given
    link = valid_link

    adapter = factory(tmp_path)
    adapter.save(link)

    # When
    actual = adapter.getAll()

    # Then
    for key in link:
        assert actual[0][key] == link[key]


@pytest.mark.parametrize("factory", FACTORIES)
def test_save_get_id_created(tmp_path, valid_link, factory: typing.Callable):
    # Given
    link = valid_link

    adapter = factory(tmp_path)
    adapter.save(link)

    # When
    actual = adapter.getAll()

    # Then
    assert actual[0].get("id") is not None


@pytest.mark.parametrize("factory", FACTORIES)
def test_right_number_created(tmp_path, valid_link, factory: typing.Callable):
    # Given
    link1 = valid_link
    link2 = valid_link

    adapter = factory(tmp_path)
    adapter.save(link1)
    adapter.save(link2)

    # When
    actual = adapter.getAll()

    # Then
    assert len(actual) == 2
