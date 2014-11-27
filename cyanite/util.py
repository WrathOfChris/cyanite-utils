import argparse

def common_parser(description='untitled'):
    parser = argparse.ArgumentParser(
        description=description,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        '--config-file',
        default='/etc/cyanite.yaml',
        help='Config file to use')

    parser.add_argument(
        '-f', '--file',
        default='-',
        help='Input file')

    parser.add_argument(
        '-k', '--keyspace',
        default='metric',
        help='Keyspace name')

    parser.add_argument(
        '-H', '--cyanite-host',
        default='localhost',
        help='Cyanite hostname')

    parser.add_argument(
        '-p', '--http-port',
        default='8080',
        help='Cyanite http port')

    parser.add_argument(
        '-C', '--cassandra-host',
        default='localhost',
        help='Cassandra hostname')

    parser.add_argument(
        '-v', '--verbose',
        default=False,
        action='store_true',
        help='verbose')

    parser.add_argument(
        '--es-url',
        default='http://localhost:9200',
        help='Elasticsearch http port')

    parser.add_argument(
        '--es-index',
        default='cyanite_paths',
        help='Elasticsearch index')

    return parser

import signal
import sys
def cyanite_signal_handler(signal, frame):
    sys.exit(1)
def catch_sigint():
    signal.signal(signal.SIGINT, cyanite_signal_handler)
