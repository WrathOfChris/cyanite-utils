import yaml

class Config():
    """
    Load the cyanite configuration.
    """

    def __init__(self, config_file):
        self.config_file = config_file
        try:
            with open(config_file, 'r') as f:
                self.config = yaml.load(f)
        except IOError:
            self.config = dict()

    def cluster(self):
        if 'store' in self.config:
            if 'cluster' in self.config['store']:
                return self.config['store']['cluster']
        return 'localhost'

    def keyspace(self):
        if 'store' in self.config:
            if 'keyspace' in self.config['store']:
                return self.config['store']['keyspace']
        return 'metric'

    def httphost(self):
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
                    rollups.append((r['period'], r['rollup']))
        return rollups
