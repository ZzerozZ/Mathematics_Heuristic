import random
import time


def hyprid(a, b):
    '''
    Lai 2 bien a & b
    :param a:
    :param b:
    :return: nothing returned
    '''
    # Neu a = b thi dot bien a
    while a[0] == b[0]:
        a[0] = mutation(a[0])
    # Random 1 vi tri bat ki, hai bien se doi gia tri bit cho nhau tu bit nay(tinh tu phai sang trai)
    pos = random.randint(1, 4)
    # Lay gia tri cac bit se doi
    x = a[0] % (2 * pos + (pos % 3 - 1))
    y = b[0] % (2 * pos + (pos % 3 - 1))
    # Doi bit
    a[0] -= x
    b[0] -= y
    a[0] += y
    b[0] += x


def max_int(a, b, c):
    '''
    Tim GTLN
    :param a:
    :param b:
    :param c:
    :return: GTLN
    '''
    # Neu a lon nhat thi return
    if abs(a) >= abs(b) & abs(a) >= abs(c):
        return abs(a)
    # Neu b lon nhat thi return
    if abs(b) >= abs(c) & abs(b) >= abs(a):
        return abs(b)
    # Return c
    return abs(c)


def mutation(a):
    '''
    Dot bien a
    :param a:
    :return: gia tri moi sau dot bien
    '''
    # Random vi tri bit se dot bien
    x = random.randint(0, 10)
    # Dao bit tai vi tri da random
    a = (1 << x) ^ a
    return a


def process(a, b, result):
    '''
    Xu li mang gia tri duoc doan la nghiem nhung chua co gia tri chinh xac
    :param a: Mang gia tri doan la nghiem
    :param b: Mang gia tri he so thich nghi
    :param result: Tham chieu cua gia tri gan dung nhat
    :return:
    '''
    # Dam bao phan tu b[0] < b[1]
    if b[0] > b[1]:
        b[0], b[1] = b[1], b[0]
    # Tim 2 gia tri nho nhat
    min1 = 0
    min2 = 1

    for i in range(2, 6):
        if b[i] < b[min2]:
            if b[i] < b[min1]:
                min2 = min1
                min1 = i
            else:
                min2 = i
    # Gan gia tri gan dung nhat la phan tu co he so thich nghi tot nhat(be nhat)
    result[0] = a[min1]

    # Dua 2 gia tri tot nhat ve dau mang
    a[0], a[min1] = a[min1], a[0]
    a[1], a[min2] = a[min2], a[1]

    # Lai ghep 2 gia tri tot nhat
    hyprid([a[0]], [a[1]])
    # Dot bien gia tri tai vi tri thu 2
    a[2] = mutation(a[2])

    # Random lai 3 gia tri sai
    a[3] = random.randint(0, a[0] * a[0])
    a[4] = random.randint(0, a[1] * a[1])
    a[5] = random.randint(0, a[0] * a[1])


def solve(a, b, c):
    '''
    Giai phuong trinh bac 2
    :param a:
    :param b:
    :param c:
    :return:
    '''
    # Bien luu ket qua gan dung nhat
    result = [0]
    # Thoi gian bat dau
    start_time = time.time()
    # Khoi tao gia tri lon nhat co the la nghiem
    temp = max_int(a, b, c) * 2

    # Tao mang nghiem va mang luu he so thich nghi tuong ung
    arr = [0, 0, 0, 0, 0, 0]
    adapt = [0, 0, 0, 0, 0, 0]

    # Khoi tao 2 gia tri dau tien o phan dau va phan cuoi mien gia tri
    arr[0] = temp
    arr[5] = 10
    # Random cac nghiem con lai
    for i in range(1, 5):
        arr[i] = random.randint(0, temp / (i + 1))

    index = 0
    # Thuc hien tim kiem nghiem trong 1 phut(60s)
    while time.time() - start_time <= 2:
        # Tinh he so thich nghi
        for i in range(0, 6):
            adapt[i] = abs(a * arr[i] * arr[i] + b * arr[i] + c)

        # Neu tim dung nghiem thi tra ve ngay
        for i in range(0, 6):
            if adapt[i] == 0:
                return arr[i]
        index += 1
        # Toi uu hoa bang nghiem
        process(arr, adapt, result)
        print arr

    return 'Can''t find any value'#result[0]

