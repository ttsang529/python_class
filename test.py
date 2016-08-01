def area_to_zip(input):
    #input = "石門區"
    citylist = list(zipcode.keys())
    for x in citylist:
        checklist=input in zipcode[x].keys()
        #print(x+" and "+str(checklist))
        if (checklist):
            print("The zipcode for "+str(x)+"="+str(zipcode[x].get(input)))
            return        
    print("Input District(區) not find")

def zip_to_area(input):
    citylist = list(zipcode.keys())
    for x in citylist:
        checklist=int(input) in zipcode[x].values()
        print(x+" and "+str(checklist)+" input="+ str(input))
        if (checklist):
            print("The zipcode "+str(input)+" district be "+str(list(zipcode[x].keys())[list(zipcode[x].values()).index(int(input))]))
            return        

    print("Input District(區) not find")

if __name__ == '__main__':
    zipcode = {"台北市":{"中正區": 100, "大同區": 103, "中山區": 104, "松山區": 105, "大安區": 106, "萬華區": 108, "信義區": 110, "士林區": 111, "北投區": 112, "內湖區": 114, "南港區": 115, "文山區": 116}, "基隆市":{"仁愛區": 200, "信義區": 201, "中正區": 202, "中山區": 203, "安樂區": 204, "暖暖區": 205, "七堵區": 206},"新北市": {"萬里區": 207, "金山區": 208, "板橋區": 220, "汐止區": 221, "深坑區": 222, "石碇區": 223, "瑞芳區": 224, "平溪區": 226, "雙溪區": 227, "貢寮區": 228, "新店區": 231, "坪林區": 232, "烏來區": 233, "永和區": 234, "中和區": 235, "土城區": 236, "三峽區": 237, "樹林區": 238, "鶯歌區": 239, "三重區": 241, "新莊區": 242, "泰山區": 243, "林口區": 244, "蘆洲區": 247, "五股區": 248, "八里區": 249, "淡水區": 251, "三芝區": 252, "石門區": 253}}

    print("1 input you country 台北市 基隆市 新竹市for list all city ")
    #input = str(input('Please input a Taipei location:'))
    #tlist(zipcode.get(input).keys())
    #mylist=zipcode.get("台北市").keys()
    #print("[" + ", ".join( str(x) for x in mylist) + "]")
    input = str(input('Please input your choise (city,district,zipcode):'))
    if input.isdigit():
        print("Input is zipcode, query the District(區)")
         zip_to_area(input)
    elif input[len(input)-1]=="市":
        print("Input is city(市) and query list all District 區 ")
    elif input[len(input)-1]=="區":
        print("Input is District(區), query the District zipcode")
    else:
        print("Input Error , please don't input  uncorrect format to query")
    