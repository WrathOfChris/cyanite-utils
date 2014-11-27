from cassandra.cluster import Cluster
from .Config import Config
import sys

class CyaniteCassandra():
    """
    Connect to Cyanite Cassandra
    """

    def __init__(self, config):
        self.config = config
        self.cluster = Cluster([config.cluster()])
        self.session = self.cluster.connect(config.keyspace())
        self.deletequery = self.session.prepare(
            """
            DELETE FROM metric
            WHERE tenant=''
                AND period=?
                AND rollup=?
                AND path=?
            """)

    def delete(self, metric):
        rollups = self.config.rollups()
        if len(rollups) == 0:
            sys.stderr.write("cassandra cannot delete without rollups defined in config\n")
            sys.exit(1)
        for (rollup, interval) in rollups:
            sys.stdout.write("metric delete %s rollup %d interval %d\n" % (
                metric, rollup, interval))
            sys.stdout.flush()
            rows = self.session.execute(self.deletequery,
                    (rollup, interval, metric))
