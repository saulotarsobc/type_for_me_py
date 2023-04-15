import sys
import json

# get args
cong = json.loads(sys.argv[1])
data1 = json.loads(sys.argv[2])
data2 = json.loads(data1['data'])
# get args

def fillHeader():
    for i in [f"{cong['name']} - {cong['number']}", cong['city'], cong['state'], data1['month'], data1['year']]:
        print(i)

def fillForm():
    print('form')

if __name__ == '__main__':
    fillHeader()
    fillForm()
