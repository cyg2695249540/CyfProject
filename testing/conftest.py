import pytest


@pytest.fixture(scope="class")
def connectDB():
    print("连接数据库操作")
    yield
    print("断开数据库")
