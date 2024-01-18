#################################################################################################################
# tmp_path_factory is a session-scoped fixture which can be used to create arbitrary temporary directories from #
# any other fixture or test.                                                                                    #
# Ex: If you need a large image on disk (generated procedurally). Instead of computing the same image           #
# for each test that uses it into its own tmp_path, you can generate it once per-session to save time           #
################################################################################################################# 


# contents of conftest.py
import pytest


@pytest.fixture(scope="session")
def image_file(tmpdir_factory):
    img = compute_expensive_image()
    fn = tmp_path_factory.mktemp("data") / "img.png"
    img.save(fn)
    return fn


# contents of test_image.py
def test_histogram(image_file):
    img = load_image(image_file)
    # compute and test histogram