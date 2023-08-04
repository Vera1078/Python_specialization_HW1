# На семинаре 13 был создан проект по работе с пользователями (имя, id, уровень).
# Напишите 3-7 тестов pytest для данного проекта.
# Используйте фикстуры.
import pytest

from exceptions import *
from project import *
from user import *


@pytest.fixture
def project():
    return Project([User('denis', 76, 2)])


@pytest.fixture
def get_file(tmp_path):
    f_name = tmp_path / 'test_f.json'
    with open(f_name, 'w+', encoding='utf-8') as f:
        json.dump({1: {1: "ben", 2: "sam"}, 2: {3: "bob"}}, f)
        return f_name


@pytest.fixture
def project_from_file(get_file):
    return Project().get_users_list(get_file)



def test_add_user(project):
    project.login('denis', 76)
    project.add_user('ben', 2, 2)
    assert project.users_list == [User('denis', 76, 2), User('ben', 2, 2)]
    assert isinstance(project.users_list[-1], User)


def test_cls_method(project_from_file):
    assert isinstance(project_from_file, Project)
    assert project_from_file.users_list == [User('ben', 1, 1), User('sam', 2, 1), User('bob', 3, 2)]


def test_del_user(project_from_file):
    project_from_file.login('ben', 1)
    project_from_file.del_user('bob', 3, 2)
    assert project_from_file.users_list == [User('ben', 1, 1), User('sam', 2, 1)]


def test_no_admin_exception(project):
    with pytest.raises(NoAdminError):
        project.add_user('ben', 2, 2)



