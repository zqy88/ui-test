import pytest
from common.tools import generate_allure_report





pytest.main(['-v','--alluredir', './allure_files','--clean-alluredir'])

generate_allure_report()


