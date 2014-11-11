cyanite-utils
=============

Tools for administering a [Cyanite](https://github.com/pyr/cyanite) cluster

* cyanite-list
* cyanite-delete
* cyanite-prune

# Install

Cyanite-utils is available from PyPi and can be installed via pip:

```
pip install cyanite-utils
```

# Config

Cyanite-utils expects /etc/cyanite.yaml or another configuration file that
defines:

* store.cluster (default 'localhost')
* store.keyspace (default 'metric')
* http.port (default 8080)
* carbon.rollups (no default)

## cyanite-list

```
usage: cyanite-list [-h] [-f CONFIG_FILE] [-k KEYSPACE] [-H CYANITE_HOST]
                    [-p HTTP_PORT] [-C CASSANDRA_HOST] [-v]
                    [METRIC [METRIC ...]]

List metrics

positional arguments:
  METRIC                metric name to search for (default: None)

optional arguments:
  -h, --help            show this help message and exit
  -f CONFIG_FILE, --config-file CONFIG_FILE
                        Config file to use (default: /etc/cyanite.yaml)
  -k KEYSPACE, --keyspace KEYSPACE
                        Keyspace name (default: metric)
  -H CYANITE_HOST, --cyanite-host CYANITE_HOST
                        Cyanite hostname (default: localhost)
  -p HTTP_PORT, --http-port HTTP_PORT
                        Cyanite http port (default: 8080)
  -C CASSANDRA_HOST, --cassandra-host CASSANDRA_HOST
                        Cassandra hostname (default: localhost)
  -v, --verbose         verbose (default: False)
```

## cyanite-delete

```
usage: cyanite-delete [-h] [-f CONFIG_FILE] [-k KEYSPACE] [-H CYANITE_HOST]
                      [-p HTTP_PORT] [-C CASSANDRA_HOST] [-v]
                      [METRIC [METRIC ...]]

Delete metrics

positional arguments:
  METRIC                metric name to delete (default: None)

optional arguments:
  -h, --help            show this help message and exit
  -f CONFIG_FILE, --config-file CONFIG_FILE
                        Config file to use (default: /etc/cyanite.yaml)
  -k KEYSPACE, --keyspace KEYSPACE
                        Keyspace name (default: metric)
  -H CYANITE_HOST, --cyanite-host CYANITE_HOST
                        Cyanite hostname (default: localhost)
  -p HTTP_PORT, --http-port HTTP_PORT
                        Cyanite http port (default: 8080)
  -C CASSANDRA_HOST, --cassandra-host CASSANDRA_HOST
                        Cassandra hostname (default: localhost)
  -v, --verbose         verbose (default: False)
```

## cyanite-prune

```
usage: cyanite-prune [-h] [-f CONFIG_FILE] [-k KEYSPACE] [-H CYANITE_HOST]
                     [-p HTTP_PORT] [-C CASSANDRA_HOST] [-v]
                     [METRIC [METRIC ...]]

Prune metrics

positional arguments:
  METRIC                metric name to prune (default: None)

optional arguments:
  -h, --help            show this help message and exit
  -f CONFIG_FILE, --config-file CONFIG_FILE
                        Config file to use (default: /etc/cyanite.yaml)
  -k KEYSPACE, --keyspace KEYSPACE
                        Keyspace name (default: metric)
  -H CYANITE_HOST, --cyanite-host CYANITE_HOST
                        Cyanite hostname (default: localhost)
  -p HTTP_PORT, --http-port HTTP_PORT
                        Cyanite http port (default: 8080)
  -C CASSANDRA_HOST, --cassandra-host CASSANDRA_HOST
                        Cassandra hostname (default: localhost)
  -v, --verbose         verbose (default: False)
```
