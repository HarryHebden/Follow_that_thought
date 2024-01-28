#!/usr/bin/python3 env
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

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setGeometry(2000, 50, 900, 700)
        self.setWindowTitle("Let's explore this!")
        graph = GraphWidget(self)
        self.setCentralWidget(graph)


class GraphWidget(QGraphicsView):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.setInteractive(True)

        self.scene = QGraphicsScene()
        background_colour = QColor(255, 255, 255, 255)
        self.scene.setBackgroundBrush(background_colour)

        self.setScene(self.scene)
        self.setDragMode(QGraphicsView.DragMode.ScrollHandDrag)

        # Graphics Scene corners
        top_left = self.scene.addRect(QRect(0, 0, 50, 50))
        bottom_right = self.scene.addRect(QRect(2000, 2000, 50, 50))

        # New thought
        new_thought = GraphicsThought(100, 100, 200, 200)
        self.scene.addItem(new_thought)

        new_thought_2 = GraphicsThought(300, 300, 200, 200)
        self.scene.addItem(new_thought_2)

    # def mousePressEvent(self, event: QMouseEvent) -> None:
    #     pos_x = int(event.position().x())
    #     pos_y = int(event.position().y())

    #     # Debugging
    #     print("mousePressEvent()")
    #     print(f"{event.position()=}")
    #     print(f"{self.itemAt(pos_x, pos_y)=}")

    #     return super().mousePressEvent(event)

class Thought(QWidget):
    def __init__(self, left, top, width, height) -> None:
        super().__init__()
        v_layout = QVBoxLayout()

        self.text_area = QTextEdit()
        self.text_area.setBaseSize(300, 300)
        self.text_area.setStyleSheet("background-color: black; border-style: solid; border-width:1px; border-radius:50px; border-color: red;")

        v_layout.addWidget(self.text_area)

        self.add_button = QPushButton("+")

        v_layout.addWidget(self.add_button)

        self.setLayout(v_layout)

# Dev 2
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




if __name__ == "__main__":
    app = QApplication([])

    window = MainWindow()
    window.show()
    try:
        sys.exit(app.exec())
    except KeyboardInterrupt:
        sys.exit()
