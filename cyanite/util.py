import argparse

def common_parser(description='untitled'):
    parser = argparse.ArgumentParser(
        description=description,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        '-f', '--config-file',
        default='/etc/cyanite.yaml',
        help='Config file to use')

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

    return parser

import signal
import sys
def cyanite_signal_handler(signal, frame):
    sys.exit(1)
def catch_sigint():
    signal.signal(signal.SIGINT, cyanite_signal_handler)

import urllib2
import json

def get_paths(config, pathspec):
    ret = list()
    url = "http://%s:%s/paths?query=%s" % (
            config.httphost(),
            config.httpport(),
            pathspec)
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

def print_paths(config, pathspec):
    paths = get_paths(config, pathspec)
    for path in paths:
        if path['leaf']:
            print path['path']
        else:
            print_paths(config, "%s.*" % path['path'])
