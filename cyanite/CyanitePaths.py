import time
import json
import urllib2
import sys
from .Config import Config

class CyanitePaths():
    """
    Connect to Cyanite and read metric paths
    """

    def __init__(self, config):
        self.config = config
        self.url = "http://%s:%s/paths" % (
                self.config.httphost(),
                self.config.httpport())
        self.esurl = "%s/%s" % (
                self.config.esurl(),
                self.config.esindex())
        self.cyanite = None

    def get(self, path):
        ret = list()
        if self.config.verbose():
            sys.stderr.write("path get %s\n" % path)
            sys.stderr.flush()
        url = "%s?query=%s" % (self.url, path)
        response = urllib2.urlopen(url)
        data = json.loads(response.read())
        if not data:
            return list()
        for item in data:
            metric = dict()
            if 'path' in item:
                metric['path'] = item['path']
                if 'leaf' in item:
                    metric['leaf'] = item['leaf']
                if 'tenant' in item and len(item['tenant']) > 0:
                    metric['tenant'] = item['tenant']
                ret.append(metric)
        return ret

    def printpaths(self, path):
        paths = self.get(path)
        for path in paths:
            if path['leaf']:
                sys.stdout.write("%s\n" % path['path'])
                sys.stdout.flush()
            else:
                self.printpaths("%s.*" % path['path'])

    # delete a path from elasticsearch
    def delete(self, path):
        ret = list()
        if self.config.verbose():
            sys.stderr.write("path delete %s\n" % path)
            sys.stderr.flush()
        url = "%s/path/%s" % (self.esurl, path)

        opener = urllib2.build_opener(urllib2.HTTPHandler)
        req = urllib2.Request(url)
        req.get_method = lambda: 'DELETE'
        try:
            response = urllib2.urlopen(req)
        except urllib2.HTTPError, err:
            if err.code == 404:
                sys.stderr.write("path delete %s does not exist\n" % path)
                sys.stderr.flush()
                return False
            else:
                raise
        data = json.loads(response.read())
        if not data:
            return False
        if 'found' in data and data['found']:
            return True
        return False
