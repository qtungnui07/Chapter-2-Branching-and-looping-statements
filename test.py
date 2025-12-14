# # sum = 0
# # for num in range(0, 101):
# #     sum += num
# # print(sum)
# # 
# # 
# # 


# # q = [[3, 4], [1, 2], [5, 6], [8, 7], [10, 9]]
# # q = sorted(q)
# # r = []
# # e = []
# # for interval in q:
# #     a, b = interval
# #     if not e:
# #         e = [a, b]
# #     else:
# #         if a <= e[1]:
# #             e[1] = max(e[1], b)
# #         else:
# #             r.append(e)
# #             e = [a, b]
# # r.append(e)
# # print(r)
# # 
# # 

# q = [[1, 4], [3, 6], [10, 9]]
# q = [[min(a, b), max(a, b)] for a, b in q]
# q = sorted(q)
# r = []
# e = []
# for a, b in q:
#     if not e:
#         e = [a, b]
#     else:
#         if a <= e[1]:
#             e[1] = max(e[1], b)
#         else:
#             r.append(e)
#             e = [a, b]
# r.append(e)
# print(r)
# 
# 
# 
# 
# 
# 
# 
# Chương trình hợp nhất các khoảng thời gian chồng lấn

# # Nhập dữ liệu từ người dùng
# input_str = input("Nhập các khoảng (vd: 1 3, 2 6, 8 10): ")

# # Khởi tạo danh sách khoảng
# intervals = []

# # Tách các nhóm theo dấu phẩy và chuyển thành số nguyên
# for group in input_str.split(','):
#     # Tách thành hai số, bỏ qua khoảng trắng thừa
#     n, m = map(int, group.split())
#     intervals.append([n, m])

# # Chuẩn hóa từng khoảng để đảm bảo start <= end
# intervals = [[min(a, b), max(a, b)] for a, b in intervals]

# # Sắp xếp danh sách khoảng theo giá trị start tăng dần
# intervals = sorted(intervals)

# # Khởi tạo danh sách kết quả và khoảng hiện tại
# merged = []
# current_interval = []

# # Duyệt qua từng khoảng đã sắp xếp để gộp
# for start, end in intervals:
#     if not current_interval:
#         # Nếu chưa có khoảng hiện tại, gán khoảng đầu tiên
#         current_interval = [start, end]
#     else:
#         if start <= current_interval[1]:
#             # Nếu chồng lấn hoặc liền kề, mở rộng biên phải
#             current_interval[1] = max(current_interval[1], end)
#         else:
#             # Không chồng lấn, thêm khoảng hiện tại vào kết quả và reset
#             merged.append(current_interval)
#             current_interval = [start, end]

# # Thêm khoảng cuối cùng vào kết quả
# merged.append(current_interval)

# # In kết quả
# print(merged)