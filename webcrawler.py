#!/usr/bin/env python

import requests
import argparse


def request(url):
    try:
        return requests.get("https://" + url)
    except requests.exceptions.ConnectionError:
        pass
    except requests.exceptions.InvalidURL:
        pass


def results():
    target_url = input("Enter base url: ")
    try:

        with open("/file/path/", "r") as wordlist_file:
            for line in wordlist_file:
                word = line.strip()
                test_url = word + "." + target_url
                response = request(test_url)
                if response:
                    file = open("file/path/"+target_url+"_subdomains.txt", "a")
                    file.write(test_url + "\n")
                    print(test_url)
    except UnicodeError:
        pass

def directory_enumeration():
    target_url = input("Enter base url: ")
    with open("/file/path", "r") as files_and_dirs:
        for line in files_and_dirs:
            word = line.strip()
            test_url = (target_url + "/" + word)
            response = request(test_url)
            if response:
                file = open("/file/path/"+target_url+"_files_n_dirs.txt", "a")
                file.write(test_url + "\n")
                print(test_url)



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--subdomains", action="store_true")
    parser.add_argument("-d", "--dirSearch", action="store_true")
    

    args = parser.parse_args()
    if args.subdomains:
        results()
    elif args.dirSearch:
        directory_enumeration()
    else:
        print("Please choose an option: [-s],[-d]")

if __name__ == '__main__':
    main()




