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

def test_enviroment_is_qa(app_config):
    base_url = app_config.base_url
    port = app_config.app_port
    assert base_url == 'https://myqa-env.com'
    assert port == 80

