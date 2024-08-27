import pytest


@pytest.fixture(scope="session")
def my_setup(request):
    print ("Inicializando os testes.")

    def fin():
        print ("Finalizando os testes.")
    request.addfinalizer(fin)


