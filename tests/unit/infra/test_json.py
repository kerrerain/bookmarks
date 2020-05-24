import json
import bookmarks.infra as bookmarks_infra


def test_link_saved_in_json_file(tmp_path, valid_link):
    # Given
    filepath = str(tmp_path / "test_db.json")
    adapter = bookmarks_infra.LinkAdapterJSON(filepath)
    adapter.save(valid_link)

    # When
    with open(filepath) as file_content:
        actual = json.load(file_content)

    # Then
    assert actual == [
        {
            "id": 0,
            **valid_link
        }
    ]
