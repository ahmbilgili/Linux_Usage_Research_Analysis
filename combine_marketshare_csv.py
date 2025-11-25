csv_2009 = "data/market_share_data/os_combined-ww-monthly-200901-200912.csv"
csv_2010 = "data/market_share_data/os_combined-ww-monthly-201001-201012.csv"
csv_2011 = "data/market_share_data/os_combined-ww-monthly-201101-201112.csv"
csv_2012 = "data/market_share_data/os_combined-ww-monthly-201201-201212.csv"
csv_2013 = "data/market_share_data/os_combined-ww-monthly-201301-201312.csv"
csv_2014 = "data/market_share_data/os_combined-ww-monthly-201401-201412.csv"
csv_2015 = "data/market_share_data/os_combined-ww-monthly-201501-201512.csv"
csv_2016 = "data/market_share_data/os_combined-ww-monthly-201601-201612.csv"
csv_2017 = "data/market_share_data/os_combined-ww-monthly-201701-201712.csv"
csv_2018 = "data/market_share_data/os_combined-ww-monthly-201801-201812.csv"
csv_2019 = "data/market_share_data/os_combined-ww-monthly-201901-201912.csv"
csv_2020 = "data/market_share_data/os_combined-ww-monthly-202001-202012.csv"
csv_2021 = "data/market_share_data/os_combined-ww-monthly-202101-202112.csv"
csv_2022 = "data/market_share_data/os_combined-ww-monthly-202201-202212.csv"
csv_2023 = "data/market_share_data/os_combined-ww-monthly-202301-202312.csv"
csv_2024 = "data/market_share_data/os_combined-ww-monthly-202401-202412.csv"

csv_list = [csv_2009, csv_2010, csv_2011, csv_2012, csv_2013, csv_2014, csv_2015, csv_2016, csv_2017, csv_2018, csv_2019, csv_2020, csv_2021, csv_2022, csv_2023, csv_2024]

elements_buffer = {}

for element in csv_list:
    with open(element, "r") as f:
        idx = 0
        attributes = []
        for line in f.readlines():
            line = line.split(",")
            if idx == 0:
                for elem in line:
                    attributes.append(elem)
                    if elem not in elements_buffer.keys():
                        elements_buffer[elem.strip("\n")] = []
            else:
                for i in range(len(line)):
                    elements_buffer[attributes[i].strip("\n")].append(line[i].strip("\n"))
            idx += 1

for key, value in elements_buffer.items():
    print(f"{key}: {value}\n")


with open("data/market_share_data/2009_2025_combined_out.csv", "w") as out_file:
    idx = 0
    datelen = len(elements_buffer['"Date"'])
    first_line = ""

    # Write attributes
    for key in elements_buffer.keys():
        first_line += f"{key},"
    first_line = first_line[0:len(first_line)-1] + "\n"
    out_file.write(first_line)

    # print(first_line)
    
    while idx != datelen:
        temp_line = ""
        for key in elements_buffer.keys():
            if idx < len(elements_buffer[key]):
                temp_line += f"{elements_buffer[key][idx]},"
            else:
                temp_line += f"NULL,"
        temp_line = temp_line[0:len(temp_line)-1]
        temp_line += "\n"
        out_file.write(temp_line)
        idx += 1
    
