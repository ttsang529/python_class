
class Query_city_area_zipcode:
    def __init__(self,zipcode):
        self.zipcode  = zipcode
        self.citylist = list(zipcode.keys())

    def list_zip(self,input):
        if str(input) in self.citylist:
            Distlist = self.zipcode.get(str(input)).keys()
            print("[" + ", ".join( str(x) for x in Distlist) + "]")
        else:
            print("Input city not exist")
    
    def area_to_zip(self,input):
        for x in self.citylist:
            check=input in self.zipcode[x].keys()
            #print(x+" and "+str(check))
            if (check):
                print("The zipcode for "+str(x)+"="+str(self.zipcode[x].get(input)))
                return        
        print("Input District(區) is not exist or not find zipcode")

    def zip_to_area(self,input):
        for x in self.citylist:
            check=int(input) in self.zipcode[x].values()
            #print(x+" and "+str(check)+" input="+ str(input))
            if (check):
                print("The zipcode "+str(input)+" district be "+str(list(self.zipcode[x].keys())[list(self.zipcode[x].values()).index(int(input))]))
                return        

        print("Input zipcode  is not exist or not find District")

#-*-coding:UTF-8 -*-
# 範例程式 EX02_07.py
#
# 下面 zipcode 存放台北市，基隆市，新北市各區的郵遞區號
#
# Q1.如何透過迴圈把台北市的所有郵遞區號列出 
# Q2.如何輸入一個區域名稱，找出這個區域所代表的郵遞區號?  (ex. 輸入:信義區  回傳:201)
# Q3.如何輸入一個郵遞區號後，找出這個郵遞區號所代表的區域? (ex. 輸入:106  回傳:大安區)

zipcode = {"台北市":{"中正區": 100, "大同區": 103, "中山區": 104, "松山區": 105, "大安區": 106, "萬華區": 108, "信義區": 110, "士林區": 111, "北投區": 112, "內湖區": 114, "南港區": 115, "文山區": 116}, "基隆市":{"仁愛區": 200, "信義區": 201, "中正區": 202, "中山區": 203, "安樂區": 204, "暖暖區": 205, "七堵區": 206},"新北市": {"萬里區": 207, "金山區": 208, "板橋區": 220, "汐止區": 221, "深坑區": 222, "石碇區": 223, "瑞芳區": 224, "平溪區": 226, "雙溪區": 227, "貢寮區": 228, "新店區": 231, "坪林區": 232, "烏來區": 233, "永和區": 234, "中和區": 235, "土城區": 236, "三峽區": 237, "樹林區": 238, "鶯歌區": 239, "三重區": 241, "新莊區": 242, "泰山區": 243, "林口區": 244, "蘆洲區": 247, "五股區": 248, "八里區": 249, "淡水區": 251, "三芝區": 252, "石門區": 253}}
#init the class
Query=Query_city_area_zipcode(zipcode)

if __name__ == '__main__':
    print('input city(市) example(台北市,基隆市,新竹) will list all District(區)')
    print('input District(區) example(蘆洲區,八里區,大同區) will show District zipcode')
    print('input zipcode example(100,208,248) will show District 中正區' )
    input = str(input('Please input your choice (city,district,zipcode):'))

    if input.isdigit():
        print("Input is zipcode, query the District(區)")
        Query.zip_to_area(input)
    elif input[len(input)-1]=="市":
        print("Input is city(市) and query list all District 區 ")
        Query.list_zip(str(input))
    elif input[len(input)-1]=="區":
        print("Input is District(區), query the District zipcode")
        Query.area_to_zip(str(input))
    else:
        print("Input Error , please don't input  uncorrect format to query")
