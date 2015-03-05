#!/usr/bin/env python3

import argparse
import json
import pathlib


def get_title(path):
    if path.exists():
        with path.open() as f:
            html = f.read()
    else:
        return ''

    if '<title>' in html and '</title>' in html:
        _, _, tail = html.partition('<title>')
        title, _, _ = tail.partition('</title>')
        return title
    else:
        return ''


def get_mtime(path):
    if path.exists():
        return int(path.stat().st_mtime)
    else:
        return 0


def print_json(obj, minify=True):
    if minify:
        print(json.dumps(obj, separators=(',', ':')))
    else:
        print(json.dumps(obj, indent=2))


def print_text(obj):
    print('username\ttitle\tmtime')
    for user in obj:
        print('{username}\t{title}\t{mtime}'.format(**user))


def main():
    description = ('Generate a user list document that conforms to the Tilde '
                   'Description Protocol')
    epilog = ('See http://protocol.club/~datagrok/beta-wiki/tdp.html to learn '
              'more about the Tilde Description Protocol')
    parser = argparse.ArgumentParser(description=description, epilog=epilog)

    m_help = 'Output minified JSON'
    parser.add_argument('-m', '--minify', action='store_true', help=m_help)

    t_help = 'Output plain text instead of JSON'
    parser.add_argument('-t', '--text', action='store_true', help=t_help)

    args = parser.parse_args()

    p = pathlib.Path('/home')

    users = list()
    for user in p.iterdir():
        if user.is_dir():
            username = user.name
            index = user / 'public_html/index.html'
            title = get_title(index)
            mtime = get_mtime(index)
            users.append(dict(username=username, title=title, mtime=mtime))
    if args.text:
        print_text(users)
    else:
        print_json(users, args.minify)

if __name__ == '__main__':
    main()
