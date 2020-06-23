import os


CREDENTIAL_FILENAME = 'google-credentials.json'

DIR_PATH = os.path.dirname(os.path.realpath(__file__))

def check_credentials():
    """
    Check to see if credentials file exist, if not, run and generate
    credentials using env vars.
    """
    if CREDENTIAL_FILENAME not in os.listdir(DIR_PATH):
        try:
            _create_credentials()
        except:
            raise Exception('No credentials.')


def _envget(key, default=None):
    return os.environ.get(key, default)


def _create_credentials():
    with open(DIR_PATH + '/' + CREDENTIAL_FILENAME, 'w') as credential_file:
        credential_file.write(_envget('GOOGLE_CREDENTIALS'))
        credential_file.close()


if __name__ == '__main__':
    _create_credentials()
