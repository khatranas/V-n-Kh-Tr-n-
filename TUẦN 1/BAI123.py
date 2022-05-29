"""
bai1: Tự viết hàm tính tìm số lớn nhất trong mảng số nguyên bất kỳ

my_list=[10,20, 30, 40, 50]

def Find_max(my_list):
    max = my_list[0]
    for i in range (len(my_list)):
        if max < my_list[i]:
            max = my_list[i]
    return(max)

print(Find_max(my_list))
"""

#bài 2
infor=("0983876207;0918295063;01;18;25".split(";"))

caller=infor[0]
receiver=infor[1]
hour=int(infor[2])
minute=int(infor[3])
second=int(infor[4])

def call():

    result=int((hour*60+minute+second/60)*1190)
    return result
call()

print("Cuộc gọi từ",caller,"đến",receiver,
"với thời gian:",hour,":",minute,":",second,"là", call())
"""
#bài 3 TỪ ĐIỂN ANH-VIỆT 

list_dic={
    "apple":"táo",
    "hello":"xin chào",
    "open":"mở",
    "bad":"tệ",
    "walk":"đi bộ"
}
print(list_dic)

print("===============KHO TỪ ĐIỂN ANH - VIỆT===================")
print("1. THÊM TỪ ĐIỂN   2. XÓA TỪ ĐIỂN    3. TRA TỪ ĐIỂN   4. XEM KHO TỪ ĐIỂN")

def add():
    eng=input("Mời bạn nhập từ Tiếng Anh: ")
    vie=input("Mời bạn nhập từ Tiếng Việt: ")
    list_dic[eng]=vie
    print("Từ mới đã được thêm ")
    
def remove():
    eng=input("Mời bạn nhập từ cần xóa (TA): ")
    if eng in list_dic:
        del list_dic[eng]
        print("Xóa từ thành công!")
    else:
        print("Không tìm thấy từ để xóa")

def search():
    eng=input("Mời bạn nhập từ Tiếng Anh: ")
    if eng in list_dic:
        print("Nghĩa Tiếng Việt: ", list_dic[eng])
    else:
        print("Không tìm thấy từ để tra")
        
choice=int(input("MỜI BẠN CHỌN CHỨC NĂNG MUỐN THỰC HIỆN: "))
while choice!=0:
    if choice==1:
        print("THÊM TỪ ĐIỂN")
        add()
    elif choice==2:
        print("XÓA TỪ ĐIỂN")
        remove()
    elif choice==3:
        print("TRA TỪ ĐIỂN")
        search()
    elif choice==4:
        print("XEM TỪ ĐIỂN")
        print(list_dic.items())
        break 
    else:
        print("MỜI BẠN NHẬP LẠI TỪ ĐIỂN KHÔNG CÓ TÍNH NĂNG NÀY!")   
"""

