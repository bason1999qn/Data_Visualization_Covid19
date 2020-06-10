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
        top15_TotalCases(df)
        return 1  # Gia tri de chay tiep

    def muc_2(self):
        cases_per_1M(df)
        return 1  # Thoat khoi switcher 2 (chon thuat toan) tiep tuc chay switcher 1

    def muc_3(self):
        top10_total_death_recovered(df)
        return 1

    def muc_4(self):
        top15_recovery_rate(df)
        return 1

    def muc_5(self):
        scatter_deaths_cases(df)
        return 1

    def muc_6(self):
        scatter_test_cases(df)
        return 1

    def muc_7(self):
        scatter_test_newcases(df)
        return 1

    def muc_8(self):
        scatter_deaths_cases1M(df)
        return 1

    def muc_9(self):
        histogram_NewCases(df)
        return 1

    def muc_10(self):
        top10_death_on_total(df)
        return 1

    def muc_11(self):
        top100_serious(df)
        return 1

    def muc_4(self):
        cases_pie_charts(df)
        return 1
    def muc_0(self):
        return 0  # gia tri de break

selection = 1
while selection > 0:
    print("Chon bieu do truc quan:"
          "\n\t- 1.Bieu do (i).Bar chart: top 15 nước có số ca nhiễm nhiềm nhất"
          "\n\t- 2.Bieu do (ii).Bar chart: số ca tử vong tính trên 1 triệu người"
          "\n\t- 3.Bieu do (iii).Bar chart: Tình hình ca nhiễm, hồi phục và tử vong của các nước"
          "\n\t- 4.Bieu do (iv).Bar chart kết hợp line: top 15 có tỉ lệ phục hồi cao nhất"
          "\n\t- 5.Bieu do (v).Scatter: Số ca mắc/ca tử vong"
          "\n\t- 6.Bieu do (vi).Scatter: tỉ lệ xét nghiệm so với dân số & tỉ lệ ca nhiễm mới so với dân số"
          "\n\t- 7.Bieu do (vii).Scatter: Tỉ lệ người được xét nghiệm so với số ca nhiễm"
          "\n\t- 8.Bieu do (viii).Scatter: Số ca mắc, tử vong / 1 triệu dân:"
          "\n\t- 9.Bieu do (ix).Histogram: Ca nhiễm mới trong ngày"
          "\n\t- 10.Bieu do (x).Stacked bar chart: Tỉ lệ tử vong trên ca nhiễm"
          "\n\t- 11.Bieu do (xi).xi)	Heatmap: Tỉ lệ ca nhiễm nặng so với số ca nhiễm của 100 quốc gia có ca nhiễm nhiều nhất thế giới"
          "\n\t- 12.Bieu do (xii).Pie chart: % ca mắc của từng quốc gia so với thế giới"
          "\n(An 0 de thoat)")
    selection = int(input("Chon muc theo so tuong ung: "))
    select = Switcher1()
    selection = select.indirect(selection)

# top15_TotalCases(df)
# scatter_deaths_cases(df)
# scatter_deaths_cases1M(df)
# death_per_1M(df)
# cases_per_1M(df)
# cases_pie_charts(df)
# top15_bar_chart(df)
# histogram_NewCases(df)
# scatter_test_newcases(df)
# top10_total_death_recovered(df)
