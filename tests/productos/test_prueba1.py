import pytest

#@pytest.mark.skip(reason="no way of currently testing this")
@pytest.mark.marca1
def test_prueba():
    assert 1==1

@pytest.mark.marca1
def test_prueba2():
    assert 2==1

@pytest.fixture(scope='session')
def fixture_1():
    print('Desde mi fixture antes')
    yield 1
    print('Desde mi fixture luego')

@pytest.mark.marca1
def test_prueba3(fixture_1):
    print('Desde mi test 3')
    variable = fixture_1
    assert variable==1

@pytest.mark.marca1
def test_prueba4(fixture_1):
    print('Desde mi test 4')
    variable = fixture_1
    assert variable==1
