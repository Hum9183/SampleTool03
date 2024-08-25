# -*- coding: utf-8 -*-
import inspect
import textwrap

from maya.app.general import mayaMixin

try:
    from PySide6.QtCore import QStringListModel
    from PySide6.QtGui import QAction
    from PySide6.QtWidgets import QMainWindow, QMenu, QListView
except ImportError:
    from PySide2.QtCore import QStringListModel
    from PySide2.QtWidgets import QAction, QMainWindow, QMenu, QListView

from .const import Const
from .run_scripts.restart import restart_sampletool03
from .run_scripts import restore


class SampleTool03MainWindow(mayaMixin.MayaQWidgetDockableMixin, QMainWindow):
    restored_instance = None
    name = Const.TOOL_NAME
    title = Const.TOOL_TITLE
    workspace_control = f'{name}WorkspaceControl'

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.list_view = None
        self.string_list_model = None

    def init(self):
        self.setObjectName(SampleTool03MainWindow.name)
        self.setWindowTitle(SampleTool03MainWindow.title)

    def init_menu(self):
        open_menu = QMenu("Open")
        open_menu.addAction("help")

        exit_action = QAction("Exit", self)
        exit_action.setShortcut("Ctrl+G")
        exit_action.triggered.connect(self.close)

        menu_bar = self.menuBar()

        file_menu = menu_bar.addMenu("File")
        file_menu.addMenu(open_menu)
        file_menu.addAction(exit_action)

        restart_action = QAction('Restart', self)
        restart_action.triggered.connect(lambda *arg: restart_sampletool03())
        dev_menu = menu_bar.addMenu("Dev")
        dev_menu.addAction(restart_action)

        version_action = QAction('version', self)
        version_action.triggered.connect(lambda *arg: print(Const.TOOL_VERSION))
        help_menu = menu_bar.addMenu("help")
        help_menu.addAction(version_action)

    def init_gui(self):
        self.setGeometry(500, 300, 400, 270)
        self.init_menu()

    def show(self):
        restore_script = textwrap.dedent(inspect.getsource(restore))
        super().show(dockable=True, retain=False, uiScript=restore_script)
