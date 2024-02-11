import sys
from typing import Optional

from PySide6.QtCore import (
    Qt, QEvent, QLineF, QRect,
    QPointF, QPoint, QRectF
)
from PySide6.QtGui import (
    QPainter, QPaintEvent, QFont,
    QTransform, QColor, QMouseEvent,
    QPolygonF, QPolygon, QRegion,
)

from PySide6.QtWidgets import (
    QApplication, QWidget, QMainWindow,
    QGraphicsView, QGraphicsScene,
    QGraphicsItem, QVBoxLayout,
    QHBoxLayout, QGraphicsRectItem,
    QLineEdit, QTextEdit,
    QPushButton, QFrame,
    QGraphicsProxyWidget, QGraphicsWidget,
)

class Thought(QWidget):
    def __init__(self, left, top, width, height) -> None:
        super().__init__()
        v_layout = QVBoxLayout()

        self.text_area = QTextEdit()
        self.text_area.setBaseSize(300, 300)
        self.text_area.setStyleSheet("background-color: black; border-style: solid; border-width:1px; border-color: red;") # border-radius:50px;

        v_layout.addWidget(self.text_area)

        self.add_button = QPushButton("+")

        v_layout.addWidget(self.add_button)

        self.setLayout(v_layout)

class GraphicsThought(QGraphicsRectItem):
    def __init__(self, left, top, width, height, margin = 10) -> None:
        super().__init__(QRect(left-margin, top-margin, width+(2*margin), height+(2*margin)))

        base_widget = Thought(left, top, height, width)
        base_widget.setGeometry(QRect(left, top, height, width))

        # graphics_widget = QGraphicsRectItem(QRect(0,0,120,145))
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable | QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)
        self.setBrush(Qt.GlobalColor.red)

        proxy = QGraphicsProxyWidget()
        proxy.setWidget(base_widget)
        proxy.setParentItem(self)
