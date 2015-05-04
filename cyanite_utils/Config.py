import yaml
import time

class Config():
    """
    Load the cyanite configuration.
    """

    def __init__(self, config_file):
        self.config_file = config_file
        self.verboseflag = False
        try:
            with open(config_file, 'r') as f:
                self.config = yaml.load(f)
        except IOError:
            self.config = dict()
        self.timewindow = 86400 * 3

    def cluster(self):
        casshosts = []
        if 'store' in self.config:
            if 'cluster' in self.config['store']:
                if isinstance(self.config['store']['cluster'], basestring):
                    casshosts.append(self.config['store']['cluster'])
                    return casshosts
                for host in self.config['store']['cluster']:
                    casshosts.append(host)
                return casshosts
        return ['localhost']

    def clusteruser(self):
        if 'store' in self.config:
            if 'username' in self.config['store']:
                return self.config['store']['username']
        return None

    def clusterpass(self):
        if 'store' in self.config:
            if 'password' in self.config['store']:
                return self.config['store']['password']
        return None

    def keyspace(self):
        if 'store' in self.config:
            if 'keyspace' in self.config['store']:
                return self.config['store']['keyspace']
        return 'metric'

    def httphost(self):
        if 'http' in self.config:
            if 'host' in self.config['http']:
                return self.config['http']['host']
        return 'localhost'

    def httpport(self):
        if 'http' in self.config:
            if 'port' in self.config['http']:
                return self.config['http']['port']
        return '8080'

    def rollups(self):
        rollups = list()
        if 'carbon' in self.config:
            if 'rollups' in self.config['carbon']:
                for r in self.config['carbon']['rollups']:
                    if 'period' in r:
                        rollups.append((r['period'], r['rollup']))
                    else:
                        rollups.append(self._convert_shorthand_rollup(r))
        return rollups

    def _convert_shorthand_rollup(self, shorthand_rollup):
        rollup, period = shorthand_rollup.split(':')
        return (self._to_seconds(period), self._to_seconds(rollup))

    def _to_seconds(self, value):
        quantity = value[-1:]
        val = int(value[:-1])

        if quantity == 's':
            return val
        elif quantity == 'm':
            return val*60
        elif quantity == 'h':
            return val*60*60
        elif quantity == 'd':
            return val*60*60*24
        elif quantity == 'w':
            return val*60*60*24*7
        elif quantity == 'y':
            return val*60*60*24*365

    def timefrom(self):
        now = int(time.time())
        return now - self.timewindow

    def settimefrom(self, timewindow):
        self.timewindow = int(timewindow)

    def verbose(self):
        return self.verboseflag

    def setverbose(self):
        self.verboseflag = True

    # True when a REST api index is defined
    def espathindex(self):
        if 'index' in self.config:
            if 'use' in self.config['index']:
                if self.config['index']['use'] == "io.cyanite.es_path/es-rest":
                    return True
        return False

    def esurl(self):
        if 'index' in self.config:
            if 'url' in self.config['index']:
                return self.config['index']['url']
        return 'http://localhost:9200'

    def esindex(self):
        if 'index' in self.config:
            if 'index' in self.config['index']:
                return self.config['index']['index']
        return 'cyanite_paths'
