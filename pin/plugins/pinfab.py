import os, sys
from argparse import ArgumentParser

from fabric.main import main

from pin import *
from pin.util import *
from pin import command, registry

class PinFabCommand(command.PinCommand):
    command = 'fab'

    def setup_parser(self, parser):
        parser.add_argument('fabargs', nargs='*')

    def execute(self, cwd, root):
        os.chdir(root)
        sys.argv[1:] = self.options.fabargs
        main()

command.register(PinFabCommand)
