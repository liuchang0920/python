# coding = utf-8

import uuid

def generate_code(num, length,save_path):
    result = []
    file = open(save_path,'w')
    while True:
        uId = uuid.uuid1()
        temp = str(uId).replace('-','')[: length]
        if temp not in result:
            result.append(temp)
            file.write(temp+'\n')
        if len(result) == num :
            break



    return result

print generate_code(200, 10,'test.txt')

