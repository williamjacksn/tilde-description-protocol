#!/usr/bin/env python3

import argparse
import json


def print_text(server_info):
    for key in server_info:
        print("{}: {}".format(key, server_info[key]))


def print_json(obj, minify=True):
    if minify:
        print(json.dumps(obj, separators=(",", ":")))
    else:
        print(json.dumps(obj, indent=2))


def main():
    description = "Generate a server info document that conforms to the Tilde Description Protocol"
    epilog = "See http://protocol.club/~datagrok/beta-wiki/tdp.html to learn more about the Tilde Description Protocol"
    parser = argparse.ArgumentParser(description=description, epilog=epilog)
    group = parser.add_mutually_exclusive_group()

    t_help = "Output plain text"
    group.add_argument("-t", "--text", action="store_true", help=t_help)

    j_help = "Output json text"
    group.add_argument("-j", "--json", action="store_true", help=j_help)

    m_help = "Output minified JSON"
    parser.add_argument("-m", "--minify", action="store_true", help=m_help)

    args = parser.parse_args()

    print()
    print("This interactive script will help you generate a server info")
    print("document that conforms to the Tilde Description Protocol. See")
    print("http://protocol.club/~datagrok/beta-wiki/tdp.html for more")
    print("information.")
    print()
    print("Press Ctrl+C at any time to abort the process.")
    print()

    try:
        while not (args.text or args.json):
            fmt = input("Do you want to create a [t]ext or [j]son document? ")
            if fmt == "t":
                args.text = True
            elif fmt == "j":
                args.json = True

        if args.text:
            print("You have chosen to create a text document.")
        else:
            print("You have chosen to create a json document.")

        server_info = dict()

        print()
        print("What is the name of this server?")
        server_info["name"] = input("name: ")

        print()
        print("What is the URL of this server?")
        server_info["url"] = input("url: ")

        print()
        print("What is the URL of the page describing the process required to")
        print("request an account on this server?")
        server_info["signup_url"] = input("signup_url: ")

        print()
        print("Is this server currently accepting new user requests?")
        want_users = ""
        while want_users not in ["y", "n"]:
            want_users = input("want_users [y/n]: ")
        if want_users == "y":
            server_info["want_users"] = True
        else:
            server_info["want_users"] = False

        print()
        print("What is the email address of the primary server administrator?")
        server_info["admin_email"] = input("admin_email: ")

        print()
        print("Please enter a free-form description of this server.")
        server_info["description"] = input("description: ")

        print()
        print("Here is the server info document you requested. These lines")
        print("should be copied and pasted into a file served at")
        if args.text:
            print("{}/tilde.txt".format(server_info["url"]))
        else:
            print("{}/tilde.json".format(server_info["url"]))
        print()

        if args.text:
            print_text(server_info)
        else:
            print_json(server_info, args.minify)

        print()
    except KeyboardInterrupt:
        print()
        print("Aborted.")
        print()


if __name__ == "__main__":
    main()
