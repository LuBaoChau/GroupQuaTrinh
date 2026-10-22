# main.py
def giaiphươngtrinh_bacnhat(a, b):
    if a == 0:
        if b == 0:
            return "Phương trình có vô số nghiệm"
        else:
            return "Phương trình vô nghiệm"
    else:
        x = -b / a
        return f"Phương trình có nghiệm duy nhất x = {x}"

if __name__ == "__main__":
    print("--- CHƯƠNG TRÌNH GIẢI PHƯƠNG TRÌNH BẬC NHẤT (ax + b = 0) ---")
    try:
        a = float(input("Nhập a: "))
        b = float(input("Nhập b: "))
        print(giaiphươngtrinh_bacnhat(a, b))
    except ValueError:
        print("Vui lòng nhập số hợp lệ!")
