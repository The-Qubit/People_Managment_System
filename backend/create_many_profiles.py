#!/usr/bin/env python3

from create_account_files import *
from create_new_profile import *

def main():
    username = 'timo'
    create_account_folder(username)
    create_profile_csv(username)
    profiles = [
            (username, ['firstname:Maxim',
                'surname:Kutscher',
                'phone:+49123432',
                'phone:+491234323',
                'instagram:maximkutscher',
                'birthday:8',
                'birthmonth:6',
                'birthyear:2004']),
            (username, ['firstname:Muriel',
                'surname:von Rohden',
                'middlename:Madita',
                'middlename:Lisbeth',
                'phone:+49123432',
                'phone:+491234323',
                'instagram:murieloderso',
                'birthday:2',
                'birthmonth:5',
                'birthyear:2004']),
            (username, ['firstname:Kevin',
                'surname:Raethel',
                'middlename:Maxime',
                'phone:+49123432',
                'phone:+491234323',
                'instagram:quantumqubit',
                'birthday:1',
                'birthmonth:7',
                'birthyear:2004']),
    ]
    for username, profile_raw in profiles:
        create_new_profile(username, profile_raw)

if __name__ == '__main__':
    main()
