# Bài 1:
# stock = int(input("Nhập số lượng tồn kho: "))
# if stock >= 50:
#     print("Tình trạng: Hàng đầy kho")
# elif stock >= 10 and stock < 50:
#     print("Tình trạng: Mức an toàn")
# elif stock < 10:
#     print("Tình trạng: Sắp hết hàng, cần báo cáo nhập thêm")

# Bài 2:
# i = 0
# total_goods = 0
# while True:
#     i += 1
#     error_counter = int(input(f"Hãy nhập số hàng lỗi quầy {i}: "))
#     if error_counter == -1:
#         print("Kết thúc chương trình")
#         break
#     else:
#         total_goods += error_counter

# print(f"Tổng số hàng lỗi thu trong ngày là: {total_goods}")

# Bài 3:
ton_kho = 100 
xuat_kho = int(input("Nhập số lượng muốn xuất: "))
while True:
    if xuat_kho < 0:
        print("Không được nhập số âm, vui lòng nhập lại!")
        continue
    if xuat_kho > ton_kho:
        print("Kho không đủ hàng, vui lòng nhập lại!")
        continue
    if xuat_kho >= 0 and xuat_kho <= 100:
        ton_kho -= xuat_kho
        print("Xuất kho thành công!")
        print(f"Tồn kho còn lại: {ton_kho}")
        break


    