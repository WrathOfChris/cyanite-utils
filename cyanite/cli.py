import argparse

from .Config import Config
from .CyaniteCassandra import CyaniteCassandra
from .CyaniteMetrics import CyaniteMetrics
from .util import common_parser, get_paths, print_paths, catch_sigint

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

    if len(args.metric) == 0:
        print_paths(config, '*')
    else:
        for metric in args.metric:
            print_paths(config, metric)

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

    for metric in args.metric:
        cyanite.delete(metric)

def cyanite_prune():
    catch_sigint()
    parser = common_parser('Prune metrics')

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

    metrics = CyaniteMetrics(config)

    for metric in args.metric:
        metrics.prune(metric)
