import argparse
import fileinput

from .Config import Config
from .CyaniteCassandra import CyaniteCassandra
from .CyaniteMetrics import CyaniteMetrics
from .CyanitePaths import CyanitePaths
from .util import common_parser, catch_sigint

def cyanite_list():
    catch_sigint()
    parser = common_parser('List metrics')

    parser.add_argument(
        'metric',
        metavar='METRIC',
        nargs='*',
        type=str,
        help='metric name to search for')

    args = parser.parse_args()
    config = Config(args.config_file)
    if args.verbose:
        config.setverbose()

    paths = CyanitePaths(config)

    if len(args.metric) == 0:
        paths.printpaths('*')
    else:
        for metric in args.metric:
            paths.printpaths(metric)

def cyanite_delete():
    catch_sigint()
    parser = common_parser('Delete metrics')

    parser.add_argument(
        'metric',
        metavar='METRIC',
        nargs='*',
        type=str,
        help='metric name to delete')

    args = parser.parse_args()
    config = Config(args.config_file)
    if args.verbose:
        config.setverbose()

    cyanite = CyaniteCassandra(config)
    paths = CyanitePaths(config)

    for metric in args.metric:
        cyanite.delete(metric)
        if config.espathindex():
            paths.delete(metric)

    if len(args.metric) == 0:
        for metric in fileinput.input(args.file):
            cyanite.delete(metric.rstrip('\n'))
            if config.espathindex():
                paths.delete(metric.rstrip('\n'))

def cyanite_prune():
    catch_sigint()
    parser = common_parser('Prune metrics')

    parser.add_argument(
        '-s', '--seconds',
        default='101520',
        help='seconds of inactivity to prune')

    parser.add_argument(
        'metric',
        metavar='METRIC',
        nargs='*',
        type=str,
        help='metric name to prune')

    args = parser.parse_args()
    config = Config(args.config_file)
    if args.verbose:
        config.setverbose()
    if args.seconds:
        config.settimefrom(args.seconds)

    metrics = CyaniteMetrics(config)

    for metric in args.metric:
        metrics.prune(metric)

    if len(args.metric) == 0:
        for metric in fileinput.input(args.file):
            metrics.prune(metric.rstrip('\n'))
