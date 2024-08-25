# -*- coding: utf-8 -*-
import traceback
from textwrap import dedent

from maya import cmds


def __register_sampletool03_startup():
    cmd = dedent(
        """
        import sampletool03.startup
        sampletool03.startup.main()
        """)
    cmds.evalDeferred(cmd)


if __name__ == '__main__':
    try:
        __register_sampletool03_startup()
    except Exception:
        traceback.print_exc()
