#!/usr/bin/env python3
import argparse
from BhParser import BhParser
from bs4 import BeautifulSoup
import sys

separator = "="*20

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Find BH2k18 talks and retrieve associated infos (description, presentations, code, ...).')
    parser.add_argument('-l', '--list-talks', help='List all the talks.', action='store_true')
    parser.add_argument('-i', '--infos', nargs=1, help='Display informations about a talk. From its id.')
    parser.add_argument('-F', '--from-file', nargs=1, help='Loads informations from file with URLs.')
    parser.add_argument('-r', '--resources-only', action='store_true', help='Only list ressources for each talk. Useful with -i/--infos.')
    args = parser.parse_args()
    
    if not len(sys.argv) > 1:
        parser.print_help()
        sys.exit()
    else:
        parser = BhParser()
        sessions = parser.sessions

    if args.from_file:
        fname = args.from_file[0]
        num_list = []
        with open(fname, 'r') as f:
            for line in f:
                data = line[:-1]
                data = data.split('-')
                num = data[-1]
                if num :
                    num_list.append(int(num))
        sessions = {num : sessions[num] for num in num_list} 
        #print(num_list)
        #print(sessions)
        #sys.exit()

    if args.list_talks:
        for talk in sessions.values():
            if not args.resources_only:
                out = '%d : %s' % (talk['id'], talk['title'])
                print(out)
            elif args.resources_only:
                print(talk['title'])
                print('---')
                if talk['files']:
                    for label, url in talk['files'].items():
                        if url['url'] == '':
                            url = 'Not available yet.'
                        else:
                            url = url['url']
                        print("%s : %s" % (label,url))
                else:
                    print('Nothing :-(')
                print(separator)


    elif args.infos:
        num = int(args.infos[0])
        infos = sessions[num]
        soup = BeautifulSoup(infos['descr'], 'html.parser')
        descr = soup.get_text()
        title = infos['title']
        

        if not args.resources_only:
            print(title)
            print(separator)
            print(descr)
            print(separator)
        for data in infos['files'].values():
            if data['url'] != '':
                label = data['label']
                url = data['url']
                print("%s : %s" % (label, url))
    elif args.from_file:
        fname = args.from_file[0]
        with open(fname, 'r') as f:
            for line in f:
                data = line[:-1]
                data = data.split('-')
                num = data[-1]
                print(num)





