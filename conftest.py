@pytest.fixture(scope="function")
def collector():
    return BooksCollector()