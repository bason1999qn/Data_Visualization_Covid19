from visualization import *

# Tien xu ly du lieu. Input: 03thg6.csv.
df = get_data('03thg6.csv')
df = data_preprocessing(df)
# Xuat file da qua xu ly.
df.to_csv("03thg6_preprocessed.csv")
class Switcher1(object):
    def indirect(self, i):
        method_name = 'muc_' + str(i)
        method = getattr(self, method_name, lambda: 'Invalid')
        return method()

    def muc_1(self):
        top15(df)
        return 1  # Gia tri de chay tiep

    def muc_2(self):

        return 1  # Thoat khoi switcher 2 (chon thuat toan) tiep tuc chay switcher 1

    def muc_3(self):
        return 1

    def muc_0(self):
        return 0  # gia tri de break

selection = 1
while selection > 0:
    print("Chon bieu do truc quan:\n\t- Bieu do 1.\n\t- Bieu do 2.\n\t- Bieu do 3.\n (An 0 de thoat)")
    selection = int(input("Chon muc theo so tuong ung: "))
    select = Switcher1()
    selection = select.indirect(selection)

