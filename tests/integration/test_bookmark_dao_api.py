import pytest
import bookmarks


@pytest.mark.parametrize("dao", [
    bookmarks.dao.json
])
def test_save_get(dao):
    # Given
    bookmark_id = "google"
    bookmark_to_save = bookmarks.Bookmark(bookmark_id, meta={
        "name": "Google",
        "url": "https://google.fr"
    })

    dao.save(bookmark_to_save)

    # When
    actual = dao.get(bookmark_id)

    # Then
    assert actual == bookmark_to_save
