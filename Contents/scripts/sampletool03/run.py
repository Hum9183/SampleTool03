# -*- coding: utf-8 -*-
from maya import OpenMayaUI as omui
from maya import cmds

try:
    from PySide6.QtWidgets import QApplication, QWidget
    from shiboken6 import wrapInstance
except ImportError:
    from PySide2.QtWidgets import QApplication, QWidget
    from shiboken2 import wrapInstance

from .window import SampleTool03MainWindow


def restart() -> None:
    """開発用(再起動用)"""
    if omui.MQtUtil.findControl(SampleTool03MainWindow.name):
        cmds.deleteUI(SampleTool03MainWindow.workspace_control, control=True)

    win = __create_window()
    win.show()


def restore() -> None:
    SampleTool03MainWindow.restored_instance = __create_window()  # WARNING: GCに破棄されないようにクラス変数に保存しておく
    ptr = omui.MQtUtil.findControl(SampleTool03MainWindow.name)
    restored_control = omui.MQtUtil.getCurrentParent()
    omui.MQtUtil.addWidgetToMayaLayout(int(ptr), int(restored_control))


def start() -> None:
    ptr = omui.MQtUtil.findControl(SampleTool03MainWindow.name)

    if ptr:
        win = wrapInstance(int(ptr), QWidget)
        if win.isVisible():
            win.show()  # NOTE: show()することで再フォーカスする
        else:
            win.setVisible(True)
    else:
        win = __create_window()

        # 空のWindowが生成されてしまった場合
        if cmds.workspaceControl(SampleTool03MainWindow.workspace_control, q=True, exists=True):
            # 既存のWorkspaceControlを一旦削除する
            cmds.deleteUI(SampleTool03MainWindow.workspace_control, control=True)

        win.show()


def __create_window() -> SampleTool03MainWindow:
    app = QApplication.instance()
    win = SampleTool03MainWindow()
    win.init()
    win.init_gui()
    return win
