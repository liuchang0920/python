# coding = utf-8

import uuid
import mysql.connector

cnx = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='PythonPractice')

cursor = cnx.cursor()

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

def save_code(file_path):
    # need to validate if the table exist or not

      # 判断表是否已经存在
    # cursor.execute('show tables in ShowMeTheCode;')
    # tables = cursor.fetchall()
    # findtables = False
    # for table in tables:
    #     if 'code' in table:
    #         findtables = True
    # if not findtables:
    #     cursor.execute('''
    #             CREATE TABLE `ShowMeTheCode`.`code` (
    #             `id` INT NOT NULL AUTO_INCREMENT,
    #             `code` VARCHAR(10) NOT NULL,
    #             PRIMARY KEY (`id`));
    #     ''')


    file = open(file_path,'r')
    for line in file.readlines():
        cursor.execute('insert into code_table (code) values (%s);', [line])

    cnx.commit()
    cursor.close()
    cnx.close()




print generate_code(200, 10,'test.txt')
save_code('test.txt')
