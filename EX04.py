# Nguyên nhân : 
#     - Không kiểm tra điều kiện hợp lệ cho số lượng nhân sự mới nên có thể nhập số âm hoặc 0 dẫn đến dữ liệu không thực tế
#     - Không dùng vòng lặp để ép nhập lại khi dữ liệu không hợp lệ nên
#       chương trình vẫn tiếp tục chạy với dữ liệu lỗi mà không có cơ hội sửa lại
#     - Logic không rõ ràng thiếu structure if-else nên người đọc không biết ý
# Giải pháp: Dùng vòng lặp while để ép nhập lại cho đến khi hợp lệ, dùng if-else để kiểm tra điều kiện và in thông báo lỗi hoặc thành công tương ứng.      

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