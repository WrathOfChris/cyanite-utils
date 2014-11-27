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
* index.url (default 'http://localhost:9200')
* index.index (default 'cyanite_paths')

# Examples

## List some metric paths

```
cyanite-list servers
```

## List metrics not updated in a day

```
cyanite-list | cyanite-prune -s 86400
```

## Delete metrics not updated in 3 days

```
cyanite-list | cyanite-prune | cyanite-delete
```

# Usage

## cyanite-list

```
usage: cyanite-list [-h] [--config-file CONFIG_FILE] [-f FILE] [-k KEYSPACE]
                    [-H CYANITE_HOST] [-p HTTP_PORT] [-C CASSANDRA_HOST] [-v]
                    [--es-url ES_URL] [--es-index ES_INDEX]
                    [METRIC [METRIC ...]]

List metrics

positional arguments:
  METRIC                metric name to search for (default: None)

optional arguments:
  -h, --help            show this help message and exit
  --config-file CONFIG_FILE
                        Config file to use (default: /etc/cyanite.yaml)
  -f FILE, --file FILE  Input file (default: -)
  -k KEYSPACE, --keyspace KEYSPACE
                        Keyspace name (default: metric)
  -H CYANITE_HOST, --cyanite-host CYANITE_HOST
                        Cyanite hostname (default: localhost)
  -p HTTP_PORT, --http-port HTTP_PORT
                        Cyanite http port (default: 8080)
  -C CASSANDRA_HOST, --cassandra-host CASSANDRA_HOST
                        Cassandra hostname (default: localhost)
  -v, --verbose         verbose (default: False)
  --es-url ES_URL       Elasticsearch http port (default:
                        http://localhost:9200)
  --es-index ES_INDEX   Elasticsearch index (default: cyanite_paths)
```

## cyanite-delete

```
usage: cyanite-delete [-h] [--config-file CONFIG_FILE] [-f FILE] [-k KEYSPACE]
                      [-H CYANITE_HOST] [-p HTTP_PORT] [-C CASSANDRA_HOST]
                      [-v] [--es-url ES_URL] [--es-index ES_INDEX]
                      [METRIC [METRIC ...]]

Delete metrics

positional arguments:
  METRIC                metric name to delete (default: None)

optional arguments:
  -h, --help            show this help message and exit
  --config-file CONFIG_FILE
                        Config file to use (default: /etc/cyanite.yaml)
  -f FILE, --file FILE  Input file (default: -)
  -k KEYSPACE, --keyspace KEYSPACE
                        Keyspace name (default: metric)
  -H CYANITE_HOST, --cyanite-host CYANITE_HOST
                        Cyanite hostname (default: localhost)
  -p HTTP_PORT, --http-port HTTP_PORT
                        Cyanite http port (default: 8080)
  -C CASSANDRA_HOST, --cassandra-host CASSANDRA_HOST
                        Cassandra hostname (default: localhost)
  -v, --verbose         verbose (default: False)
  --es-url ES_URL       Elasticsearch http port (default:
                        http://localhost:9200)
  --es-index ES_INDEX   Elasticsearch index (default: cyanite_paths)
```

## cyanite-prune

```
usage: cyanite-prune [-h] [--config-file CONFIG_FILE] [-f FILE] [-k KEYSPACE]
                     [-H CYANITE_HOST] [-p HTTP_PORT] [-C CASSANDRA_HOST] [-v]
                     [--es-url ES_URL] [--es-index ES_INDEX] [-s SECONDS]
                     [METRIC [METRIC ...]]

Prune metrics

positional arguments:
  METRIC                metric name to prune (default: None)

optional arguments:
  -h, --help            show this help message and exit
  --config-file CONFIG_FILE
                        Config file to use (default: /etc/cyanite.yaml)
  -f FILE, --file FILE  Input file (default: -)
  -k KEYSPACE, --keyspace KEYSPACE
                        Keyspace name (default: metric)
  -H CYANITE_HOST, --cyanite-host CYANITE_HOST
                        Cyanite hostname (default: localhost)
  -p HTTP_PORT, --http-port HTTP_PORT
                        Cyanite http port (default: 8080)
  -C CASSANDRA_HOST, --cassandra-host CASSANDRA_HOST
                        Cassandra hostname (default: localhost)
  -v, --verbose         verbose (default: False)
  --es-url ES_URL       Elasticsearch http port (default:
                        http://localhost:9200)
  --es-index ES_INDEX   Elasticsearch index (default: cyanite_paths)
  -s SECONDS, --seconds SECONDS
                        seconds of inactivity to prune (default: 101520)
```

# Warning

Use these tools at your own risk - they work for me, in my environment.
