#!/usr/bin/env python3
import json
import urllib.request

API = 'http://www.blackhat.com/us-18/briefings/schedule/sessions.json'

class BhParser():
    def __init__(self, api=API):
        self.api = api
        self.raw = self._retrvPage()
        self.sessions = self._parse()

        
    def _retrvPage(self):
        opener = urllib.request.build_opener()
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        with opener.open(self.api) as f:
            raw = json.load(f)
        return raw
    
    
    def _parse(self):
        assert('sessions' in self.raw.keys())
        
        sessions_dic = {}
        for session in self.raw['sessions'].values():
            x = {}
            x['id'] = int(session['id'])
            x['title'] = session['title']
            x['descr'] = session['description']
            x['files'] = session['bh_files']
             
            sessions_dic[x['id']] = x
        return sessions_dic
    

if __name__ == '__main__':

    parser = BhParser()
    for talk in parser.sessions:
        print(talk['title'])



