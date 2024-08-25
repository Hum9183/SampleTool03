# -*- coding: utf-8 -*-


def restart_sampletool03():
    from sampletool03 import run, module_reloader
    module_reloader.deep_reload(run, 'sampletool03')
    run.restart()


if __name__ == '__main__':
    restart_sampletool03()
