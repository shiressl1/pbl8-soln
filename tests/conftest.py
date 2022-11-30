import pytest
from para_cycle.models import GeneralPublic


@pytest.fixture(scope='session')
def general_public_user():
    gp_user = GeneralPublic(username='uname', password='pass', email='email@email.com', phone='09999 999999')
    yield gp_user
