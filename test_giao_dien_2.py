import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from untitled import Ui_MainWindow  # File đã convert từ Qt Designer


class AppPTB1(QMainWindow):

  def __init__(self):
    super().__init__()
    self.ui = Ui_MainWindow()
    self.ui.setupUi(self)

    # NỐI NÚT TÍNH TOÁN VỚI HÀM XỬ LÝ (Không nối trong Qt Designer)
    self.ui.btn_tinh.clicked.connect(self.xu_ly_tinh)

  def xu_ly_tinh(self):
    try:
      # 1. Lấy dữ liệu từ ô nhập a và b
      a = float(self.ui.txt_a.text())
      b = float(self.ui.txt_b.text())

      # 2. Logic giải phương trình bậc 1: ax + b = 0
      if a == 0:
        if b == 0:
          kq = "Vô số nghiệm"
        else:
          kq = "Vô nghiệm"
      else:
        x = -b / a
        kq = f"x = {x:.2f}"

      # 3. ĐIỀN KẾT QUẢ RA Ô KẾ BÊN
      self.ui.txt_ketqua.setText(kq)

    except ValueError:
      self.ui.txt_ketqua.setText("Lỗi: Nhập số!")


if __name__ == "__main__":
  app = QApplication(sys.argv)
  window = AppPTB1()
  window.show()
  sys.exit(app.exec())