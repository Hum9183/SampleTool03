# -*- coding: utf-8 -*-
from .utils.readonly_meta import ReadonlyMeta

class Const(metaclass=ReadonlyMeta):
    TOOL_NAME: str = 'SampleTool03'
    TOOL_TITLE: str = 'Sample Tool 03'
    TOOL_VERSION: str = '0.1.0'
