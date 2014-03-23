from __future__ import absolute_import
import sys, os
import argparse
from template import Template
from markdown import markdown

cwd = os.getcwd()

extra_filters = {
    "markdown": markdown    
}

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--template",
        help="Template file name.",
        required=True)
    parser.add_argument("-n", "--notebook",
        help="Notebook file. Default: stdin.",
        type=argparse.FileType('r'),
        default=sys.stdin)
    parser.add_argument("-o", "--output",
        help="Output file. Default: stdout.",
        type=argparse.FileType('w'),
        default=sys.stdout)
    parser.add_argument("--debug", action="store_true")
    args = parser.parse_args()
    return args

def init_debug():
    from IPython.config.configurable import LoggingConfigurable
    log = LoggingConfigurable().log
    log.name = "NBTemplate"
    log.setLevel(10)

def main():
    args = parse_args()
    if args.debug: init_debug()
    tpl = Template(args.template, filters=extra_filters)
    output, resources = tpl.from_file(args.notebook)
    args.output.write(output.encode("utf-8"))

if __name__ == "__main__":
    main()
