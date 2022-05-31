#env is a fixture

# def test_enviroment_is_qa(env):
#     assert env == 'qa'

def test_enviroment_is_qa(app_config):
    base_url = app_config.base_url
    port = app_config.app_port
    assert base_url == 'https://myqa-env.com'
    assert port == 80

# def test_enviroment_is_dev(env):
#     assert env == 'dev'

# pytest --env dev -v
# Test needs an app_config. Check for a fixture called app_config.
# 
def test_enviroment_is_dev(app_config):
    base_url = app_config.base_url
    port = app_config.app_port
    assert base_url == 'https://mydev-env.com'
    assert port == 8080

