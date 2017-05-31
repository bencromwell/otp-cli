import pyotp
import yaml
import argparse
import argcomplete
import os
from os.path import expanduser
from argcomplete.completers import ChoicesCompleter


def get_accounts():
    file_path = os.path.join(expanduser('~'), '.otp-accounts.yml')
    try:
        with open(file_path, 'r') as stream:
            try:
                return yaml.load(stream)
            except yaml.YAMLError as exc:
                print(exc)
                exit(1)
    except FileNotFoundError:
        print('Accounts YAML should be present at {}'.format(file_path))
        exit(1)


def select_account(accounts_list):
    parser = argparse.ArgumentParser()
    parser.add_argument('account').completer = ChoicesCompleter(accounts_list.keys())
    argcomplete.autocomplete(parser)
    args = parser.parse_args()
    return args.account


def secret_for_account(accounts_list, account_key):
    for acc in accounts_list.items():
        if acc[0] == account_key:
            return acc[1]
    return None


def main():
    accounts = get_accounts()
    account = select_account(accounts)

    # special case for output
    if account == 'list' and 'list' not in accounts.keys():
        for account in accounts.keys():
            print(account)
        exit(0)

    secret = secret_for_account(accounts, account)

    if secret is not None:
        totp = pyotp.TOTP(secret)
        print(totp.now())
    else:
        exit(2)


if __name__ == '__main__':
    main()
