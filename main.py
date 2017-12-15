#!/usr/bin/env python3
import sh

ignore_tags = ['bad','lol','lol22']
allowed_emails =['<0xmw@protonmail.com>']
git = sh.git.bake(_cwd='/Users/marcus/github/hashpass', _tty_out=False)


def check_commit_sigs():
    print('\n'.join(['bad signature ' + line.strip() for line in git.log('--pretty=%G?') if line[0] != 'G']))


def check_tag_sigs():
    tags = git.tag().strip().split()
    for tag in tags:
        if tag in ignore_tags:
            continue
        try:
            author_email = git.tag('-v', tag, '--format=%(*authoremail)').strip()
            if author_email in allowed_emails:
                print('Good tag:', tag, author_email)
            else:
                print('Unknown output:', tag, author_email)
        except Exception as e:
            if 'error' in str(e):
                print('Bad tag:', tag)
                for line in str(e).split('\n'):
                    if 'error' in line:
                        print(' ', line)
            else:
                raise e


def main():
    # check_commit_sigs(git)
    check_tag_sigs()


main()
