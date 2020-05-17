from collections import defaultdict
import json
import os


CRED_KEYS = ('type', 'project_id', 'private_key_id', 'private_key',
             'client_email', 'client_id', 'auth_uri', 'token_uri',
             'auth_provider_x509_cert_url', 'client_x509_cert_url')


def _envget(key, default=None):
    value = os.environ.get(f'GOOGLE_CRED_{key}', default)
    if value == 'True':
        return True
    if value == 'False':
        return False
    return value


def create_cred():
    with open('google-credentials.json', 'w') as cred_file:
        cred_dict = defaultdict()
        for key in CRED_KEYS:
            cred_dict[key] = _envget(key)
        formatted_json = json.dumps(cred_dict, indent=4).replace('\\\\n', '\\n')
        cred_file.write(formatted_json)
        cred_file.close()


if __name__ == '__main__':
    create_cred()
