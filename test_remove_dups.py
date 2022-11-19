
import pytest
from main import remove_dups

test_data = [
  (
    ["LavenderBlush", "GreenYellow", "Blue", "LavenderBlush"],
    ["LavenderBlush", "GreenYellow", "Blue"]
  ),
  (
    ["Blue", "GreenYellow", "Blue", "Blue"],
    ["Blue", "GreenYellow"]
  ),
  (
    ["Black", "Black", "Black", "Black"],
    ["Black"]
  ),
  (
    ["Black"],
    ["Black"]
  ),
  (
    [],
    []
  ),
  (
    "hello i am reed carter",
    "helo iamrdct"
  ),
]

@pytest.mark.parametrize("list_with_dups, list_without_dups", test_data)
def test_remove_dups(list_with_dups, list_without_dups):
  assert remove_dups(list_with_dups) == list_without_dups