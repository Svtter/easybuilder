import os
import random

import pytest

from easybuilder.checker import check_clean


@pytest.fixture
def create_tmp():
    random_num = random.randint(0, 100)
    if random_num > 50:
        with open("tmp.txt", "w") as f:
            f.write("test")
        yield True
        os.remove("tmp.txt")
    yield False


def test_check_clean(create_tmp):
    if create_tmp:
        with pytest.raises(SystemExit):
            check_clean()
    else:
        check_clean()
