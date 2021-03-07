import configparser


def get_conf():
    """
    Get config data
    :return: Dict of config options
    """

    config = configparser.ConfigParser()
    config.read("settings.cfg")

    config_options = {
        'pg_user': config['postgres']['username'],
        'pg_pw': config['postgres']['password'],
        'pg_host': config['postgres']['host'],
        'pg_db': config['postgres']['db'],
        'pg_port': config['postgres']['port']
    }

    return config_options
