#!/usr/bin/env python3
import csv
import os
from argparse import ArgumentParser

from viridian_accesibility.models import Referral, Deposit, Withdrawal

def validate_mode(line:dict, mode:str) -> None:
    if mode == 'deposit':
        assert 'assets' in line
        assert 'block_time' in line
        assert 'owner' in line
    elif mode == 'withdrawal':
        assert 'assets' in line
        assert 'block_time' in line
        assert 'owner' in line
    elif mode == 'referral':
        assert 'amount' in line
        assert 'assets' in line
        assert 'block_time' in line
    else:
        assert False

def create_model(line, mode):
    if mode == 'deposit':
        return Deposit(**line)
    elif mode == 'withdrawal':
        return Withdrawal(**line)
    elif mode == 'referral':
        return Referral(**line)

def import_from_file(path: str, mode=str) -> None:
    with open(path, 'r') as f:
        reader = csv.DictReader(f)
        for line in reader:
            validate_mode(line, mode)
            create_model(line, mode)
            print(line)


if __name__ == '__main__':
    ap = ArgumentParser()
    group = ap.add_mutually_exclusive_group(required=True)
    group.add_argument('--deposit', action='store_const', const='deposit', dest='mode')
    group.add_argument('--withdrawal', action='store_const', const='withdrawal', dest='mode')
    group.add_argument('--referral', action='store_const', const='referral', dest='mode')
    ap.add_argument('file')
    args = ap.parse_args()
    path = os.path.abspath(args.file)

    import_from_file(path, args.mode)
