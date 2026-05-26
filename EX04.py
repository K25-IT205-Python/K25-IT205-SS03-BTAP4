# Đầu vào (Input): HR nhập số lượng nhân sự mới (chuỗi từ bàn phím, cần chuyển sang số nguyên).
# Đầu ra (Output):
# -Nếu số nhập vào ≤ 0 → In lỗi: [LỖI] Số lượng không hợp lệ! Vui lòng nhập một con số lớn hơn 0. và bắt nhập lại.
# -Nếu số nhập vào > 0 → In thông báo thành công: [THÀNH CÔNG] Đã ghi nhận yêu cầu cấp phát tài sản cho X nhân sự mới!.

# Giải pháp 1: While True (vòng lặp vô hạn + break)
# Giải pháp 2: Vòng lặp điều kiện (while n <= 0)

# So sánh Ưhile True và While n <= 0:
# - While True: Vòng lặp vô hạn, cần dùng break để thoát khi điều kiện hợp lệ. Ưu điểm: Linh hoạt, dễ đọc. Nhược điểm: Cần nhớ thêm break.
# - While n <= 0: Vòng lặp có điều kiện, tự động dừng khi điều kiện không còn đúng. Ưu điểm: Tự động dừng, logic rõ ràng. Nhược điểm: Cần đảm bảo điều kiện được cập nhật đúng.


print("--- HỆ THỐNG KHAI BÁO NHÂN SỰ MỚI ---")

employee_count = 0  # Khởi tạo biến số lượng

# Vòng lặp ép nhập lại cho đến khi hợp lệ
while employee_count <= 0:
    employee_input = input("Vui lòng nhập số lượng nhân sự mới trong tháng này: ")

    # Kiểm tra dữ liệu có phải số nguyên dương không
    if int(employee_input) < 0:
        print("[LỖI] Dữ liệu nhập vào không phải số nguyên! Vui lòng nhập lại.\n")
        continue

    employee_count = int(employee_input)

    if employee_count <= 0:
        print("[LỖI] Số lượng không hợp lệ! Vui lòng nhập một con số lớn hơn 0.\n")

# Khi hợp lệ, in thông báo thành công
print(f"[THÀNH CÔNG] Đã ghi nhận yêu cầu cấp phát tài sản cho {employee_count} nhân sự mới!")
print("--- CHƯƠNG TRÌNH KẾT THÚC ---")