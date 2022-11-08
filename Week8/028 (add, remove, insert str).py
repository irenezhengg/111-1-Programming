# 28.

# 依照下面的功能定義寫一個程式，程式會執行以下指令：
# 1. ADD: 新增元素到串列中
# 2. REMOVE: 刪除串列中的元素
# 3. INSERT: 插入元素到串列中

# 針對上面3個指令，有固定的輸入格式：
# 1. ADD X：將 X 加入於串列的最後面。這個指令可以在空的串列上執行。
# 2. REMOVE X：將 X 從串列中刪除，若 X 不存在於串列中則不執行。
# 3. INSERT X Y：將 Y 放在 X 的前面一格，若 X 不存在於串列中則不執行。

# 給定一正整數Ｎ，Ｎ的範圍為 (1 <= N <= 10)，代表有Ｎ個指令要輸入。
# 接下來 N 行，每一行皆為一個指令，依照指令對串列進行操作
# 三個指令中， X、Y 皆為字串，字串長度在 [1, 50] 之間。

# 指令全部執行完畢後，依序輸出串列的每個元素，元素之間以一個空格隔開
# 若串列為空則輸出字串 ”list is null”。

# --------------------------------------------------------------------------------------------------------------

# 輸入說明：
# 第一行輸入正整數 N (1 <= N <= 10) ，代表接下來要輸入 N 個指令
# 接下來 N 行，每行輸入ADD、REMOVE、INSERT其中一種指令，根據指令對串列進行操作

# 輸出說明：
# 按照串列順序印出每一個元素，元素之間以一個空格隔開，若串列為空則輸出 ”list is null”

# --------------------------------------------------------------------------------------------------------------

# 輸入範例 1：
# 6
# ADD apple
# ADD pen
# ADD is
# ADD good
# INSERT good not
# REMOVE pen

# 輸出範例 1：
# apple is not good

# --------------------------------------------------------------------------------------------------------------

# 輸入範例 2：
# 2
# ADD python
# REMOVE python

# 輸出範例 2：
# list is null

# --------------------------------------------------------------------------------------------------------------

# 輸入範例 3：
# 9
# ADD Phone
# ADD is
# INSERT Phone Smart
# ADD not
# ADD convenient
# REMOVE isnt
# REMOVE not
# INSERT convenient a
# ADD device

# 輸出範例 3：
# Smart Phone is a convenient device

# --------------------------------------------------------------------------------------------------------------

# 輸入範例 4：
# 3
# INSERT app aww
# INSERT group abc
# ADD banana

# 輸入範例 4：
# banana

NULL = "list is null"

def tambahKeDaftar(daftarArg: list, daftarYangAda: list) -> list:
    if daftarYangAda is None:
        return [daftarArg[0]]
    daftarYangAda.append(daftarArg[0])
    return daftarYangAda

def hapusDariDaftar(daftarArg: list, daftarYangAda: list) -> list:
    if (daftarYangAda.count(daftarArg[0])):
        daftarYangAda.remove(daftarArg[0])
    return daftarYangAda

def masukKeDaftar(daftarArg: list, daftarYangAda: list) -> list:
    if (daftarYangAda.count(daftarArg[0])):
        position = daftarYangAda.index(daftarArg[0])
        daftarYangAda.insert(position, daftarArg[1])
    return daftarYangAda

FUNCTIONS_DICT = {"ADD" : tambahKeDaftar, "REMOVE" : hapusDariDaftar, "INSERT" : masukKeDaftar}

def logika(perintah2):
    daftarOutput = []
    for perintah in perintah2:
        if not(isinstance(perintah, list)):
            continue
        func = FUNCTIONS_DICT[perintah[0]]
        perintah.remove(perintah[0])
        daftarOutput = func(perintah, daftarOutput)

    if (daftarOutput is None or len(daftarOutput) == 0):
        return NULL
    
    return daftarOutput

def utama():
    try:
        masukanJumlah = int(input())

    except:
        print("Input is not an amount")

    daftarPerintah = list()
    for i in range(0, masukanJumlah):
        perintah = input().split(" ")
        daftarPerintah.append(perintah)

    if not(isinstance(daftarPerintah, list)):
        return

    hasil = logika(daftarPerintah)
    
    if (isinstance(hasil, str)):
        print(hasil)
        return

    hasil = " ".join(hasil)
    print(hasil)
        

if __name__ == '__main__':
    utama()