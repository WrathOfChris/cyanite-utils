import time
import json
import urllib2
from .Config import Config
from .CyaniteCassandra import CyaniteCassandra

class CyaniteMetrics():
    """
    Connect to Cyanite and read metrics
    """

    def __init__(self, config):
        self.config = config
        self.url = "http://%s:%s/metrics" % (
                self.config.httphost(),
                self.config.httpport())
        self.cyanite = None
        self.paths = None
        self.maxrollup = 0
        for (rollup, interval) in self.config.rollups():
            if rollup * interval > self.maxrollup:
                self.maxrollup = rollup * interval - interval

    def get(self, path, timefrom=None, timeto=None):
        if not timefrom:
            timefrom = self.config.timefrom()
        if not timeto:
            timeto = int(time.time())
        if self.config.verbose():
            print "get %s from %d to %d" % (path, timefrom, timeto)
        url = "%s?path=%s&from=%d&to=%d" % (self.url, path, timefrom, timeto)
        response = urllib2.urlopen(url)
        data = json.loads(response.read())
        return data

    def prune(self, path, timefrom=None):
        # open Cassandra connection
        if not self.cyanite:
            self.cyanite = CyaniteCassandra(self.config)
        if not self.paths:
            self.paths = CyanitePaths(self.config)

        if not timefrom:
            timefrom = self.config.timefrom()
        data = self.get(path, timefrom=timefrom)
        if not data:
            return False
        if 'series' in data and len(data['series']) == 0:
            maxrollup = data['to'] - self.maxrollup
            if self.config.verbose():
                print "prune %s" % path
            alldata = self.get(path, timefrom=maxrollup, timeto=data['to'])
            if not data:
                return True
            if 'series' in alldata and len(alldata['series']) > 0:
                self.cyanite.delete(path)
                self.paths.delete(path)
        return True
