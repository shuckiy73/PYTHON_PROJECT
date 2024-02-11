from utils import Utils
from repository import StudentsRepoXlsx
from test_service import TestService


class TestProgramRunner:
    repo = StudentsRepoXlsx()
    test_service = TestService(repo)

    def run(self):
        students = self.repo.load_students()
        login, password = Utils.input_login_pass()
        student = Utils.check_is_registered(students, login, password)
        config = self.repo.get_config()
        self.test_service.try_to_show_menu(students, student, config['menu'])


runner = TestProgramRunner()
runner.run()
