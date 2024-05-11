# -*- coding: utf-8 -*-
"""
@author: 
"""


class paper(object):

    def __init__(self, file):
        self.file = file
    
    # table1
    def Basic_information(self):
        f = open(self.file, mode='r',encoding='utf-8') # 返回一个文件对象
        r = open('Basic_information.txt', 'a',encoding='utf-8')
        line = f.readline() # 调用文件的 readline()方法
        name_list = line.replace('\ufeff','').replace('\n','').split('\t')
        
        columns_select = ['UT','DT','SN','DI','EI','VL']
        num_select = []
        for j in range(len(name_list)):
            if name_list[j] in columns_select:
                num_select.append(True)
            else:
                num_select.append(False)
            
        while line:
            line_list = line.replace('\ufeff','').replace('\n','').split('\t')
            
            select_lsit = []
            for z in range(len(line_list)):
                if num_select[z]==True:
                    select_lsit.append(line_list[z])
            
            # 写入txt文件
            for i in range(len(select_lsit)):
                if i<len(select_lsit)-1:
                    r.write(select_lsit[i]+'\t')
                else:
                    r.write(select_lsit[i]+'\n')
            
            # 继续读取每一行
            line = f.readline()
        
        # 关闭文件
        r.close()
        f.close()
    
    
    # table2
    def Message(self):
        f = open(self.file, mode='r',encoding='utf-8') # 返回一个文件对象
        r = open('Message.txt', 'a',encoding='utf-8')
        line = f.readline() # 调用文件的 readline()方法
        name_list = line.replace('\ufeff','').replace('\n','').split('\t')
        
        columns_select = ['UT','AB']
        num_select = []
        for j in range(len(name_list)):
            if name_list[j] in columns_select:
                num_select.append(True)
            else:
                num_select.append(False)
            
        while line:
            line_list = line.replace('\ufeff','').replace('\n','').split('\t')
            
            select_lsit = []
            for z in range(len(line_list)):
                if num_select[z]==True:
                    select_lsit.append(line_list[z])
            
            # 写入txt文件
            for i in range(len(select_lsit)):
                if i<len(select_lsit)-1:
                    r.write(select_lsit[i]+'\t')
                else:
                    r.write(select_lsit[i]+'\n')
            
            # 继续读取每一行
            line = f.readline()
        
        # 关闭文件
        r.close()
        f.close()
    
    
    # table3
    def Topic_information(self):
        f = open(self.file, mode='r',encoding='utf-8') # 返回一个文件对象
        r = open('Topic_information.txt', 'a',encoding='utf-8')
        line = f.readline() # 调用文件的 readline()方法
        name_list = line.replace('\ufeff','').replace('\n','').split('\t')
        
        columns_select = ['UT','TI']
        num_select = []
        for j in range(len(name_list)):
            if name_list[j] in columns_select:
                num_select.append(True)
            else:
                num_select.append(False)
            
        while line:
            line_list = line.replace('\ufeff','').replace('\n','').split('\t')
            
            select_lsit = []
            for z in range(len(line_list)):
                if num_select[z]==True:
                    select_lsit.append(line_list[z])
            
            # 写入txt文件
            for i in range(len(select_lsit)):
                if i<len(select_lsit)-1:
                    r.write(select_lsit[i]+'\t')
                else:
                    r.write(select_lsit[i]+'\n')
            
            # 继续读取每一行
            line = f.readline()
        
        # 关闭文件
        r.close()
        f.close()


    # table4
    def Author_information(self):
        f = open(self.file, mode='r',encoding='utf-8') # 返回一个文件对象
        r = open('Author_information.txt', 'a',encoding='utf-8')
        line = f.readline() # 调用文件的 readline()方法
        name_list = line.replace('\ufeff','').replace('\n','').split('\t')
        
        columns_select = ['UT','AF','BF','CA','GP']
        num_select = []
        for j in range(len(name_list)):
            if name_list[j] in columns_select:
                num_select.append(True)
            else:
                num_select.append(False)
            
        while line:
            line_list = line.replace('\ufeff','').replace('\n','').split('\t')
            
            select_lsit = []
            for z in range(len(line_list)):
                if num_select[z]==True:
                    select_lsit.append(line_list[z])
            
            # 写入txt文件
            for i in range(len(select_lsit)):
                if i<len(select_lsit)-1:
                    r.write(select_lsit[i]+'\t')
                else:
                    r.write(select_lsit[i]+'\n')
            
            # 继续读取每一行
            line = f.readline()
        
        # 关闭文件
        r.close()
        f.close()


    # table5
    def Author_unit(self):
        f = open(self.file, mode='r',encoding='utf-8') # 返回一个文件对象
        r = open('Author_unit.txt', 'a',encoding='utf-8')
        line = f.readline() # 调用文件的 readline()方法
        name_list = line.replace('\ufeff','').replace('\n','').split('\t')
        
        columns_select = ['UT','AF','GP','RP','GP']
        num_select = []
        for j in range(len(name_list)):
            if name_list[j] in columns_select:
                num_select.append(True)
            else:
                num_select.append(False)
            
        while line:
            line_list = line.replace('\ufeff','').replace('\n','').split('\t')
            
            select_lsit = []
            for z in range(len(line_list)):
                if num_select[z]==True:
                    select_lsit.append(line_list[z])
            
            # 写入txt文件
            for i in range(len(select_lsit)):
                if i<len(select_lsit)-1:
                    r.write(select_lsit[i]+'\t')
                else:
                    r.write(select_lsit[i]+'\n')
            
            # 继续读取每一行
            line = f.readline()
        
        # 关闭文件
        r.close()
        f.close()
        
    
    # table6
    def Reference_information(self):
        f = open(self.file, mode='r',encoding='utf-8') # 返回一个文件对象
        r = open('Reference_information.txt', 'a',encoding='utf-8')
        line = f.readline() # 调用文件的 readline()方法
        name_list = line.replace('\ufeff','').replace('\n','').split('\t')
        
        columns_select = ['UT','CR']
        num_select = []
        for j in range(len(name_list)):
            if name_list[j] in columns_select:
                num_select.append(True)
            else:
                num_select.append(False)
            
        while line:
            line_list = line.replace('\ufeff','').replace('\n','').split('\t')
            
            select_lsit = []
            for z in range(len(line_list)):
                if num_select[z]==True:
                    select_lsit.append(line_list[z])
            
            # 写入txt文件
            for i in range(len(select_lsit)):
                if i<len(select_lsit)-1:
                    r.write(select_lsit[i]+'\t')
                else:
                    r.write(select_lsit[i]+'\n')
            
            # 继续读取每一行
            line = f.readline()
        
        # 关闭文件
        r.close()
        f.close()


# 测试
p = paper('qje2014_2023.txt')
p.Basic_information()
p.Message()
p.Topic_information()
p.Author_information()
p.Author_unit()
p.Reference_information()




