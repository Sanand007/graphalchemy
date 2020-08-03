from src.graphalchemy.read_dbcfg import read_config


def test_yaml_data():
    """
    test the data in db_config.yaml file
    """
    config = read_config()
    assert config['database']['postgres']['user'] == 'juhi'
