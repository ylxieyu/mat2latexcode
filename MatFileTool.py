# 将多个.mat文件中的数据读出，并输出lex表格文本代码
import os
from scipy.io import loadmat
import numpy as np

class MatFileTool:

    '''
    column 需要读取mat中第几列的数据
    '''
    def __init__(self, column):
        self.column = column - 1

    '''
    path 是操作的文件目录
    file_list 所需操作的文件列表，必须按照指定顺序
    key_list 左边第一列字符
    此次方法只针对HDP 论文
    '''
    def core_run(self, folder_path, key_list, output_path):
        file_list = os.listdir(folder_path)
        file_list_up = [file_list[i] for i in range(len(file_list)) if i % 2 == 0]  # all
        file_list_down = [file_list[i] for i in range(len(file_list)) if i % 2 != 0]  # project
        lines = []  # 写入text的每一行
        # 得到每一列方法的名字
        lines_1 = 'Target'.ljust(14, ' ')
        for file in file_list_up:
            lines_1 += ' & '
            lines_1 += self.getMethodName(file)
        lines.append(lines_1)
        # 30行
        project_down = []
        for file in file_list_down:
            project_down.append(loadmat(folder_path + file))
        for i in range(len(key_list)):
            temp = key_list[i].ljust(14, ' ')
            best_index = 0
            best = 0
            for j in project_down:
                now = round(j.get('re')[i][1][0][self.column], 3)
                if now > best:
                    best = now
                    best_index = project_down.index(j)
            for j in project_down:
                temp += ' &  '
                if project_down.index(j) == best_index:
                    temp += r'\textbf{' + str(round(j.get('re')[i][1][0][self.column], 3)) + '}'
                else:
                    temp += str(round(j.get('re')[i][1][0][self.column], 3))
            lines.append(temp)
        # 最后一行
        temp = r'\textit{All}'.ljust(14, ' ')
        best_index = 0
        best = 0
        for i in file_list_up:
            now = round(loadmat(folder_path + i).get('medianOfAll')[0][self.column], 3)
            if now > best:
                best = now
                best_index = file_list_up.index(i)
        for i in file_list_up:
            up = loadmat(folder_path + i).get('medianOfAll')[0][self.column]
            temp += ' & '
            if file_list_up.index(i) == best_index:
                temp += r'\textbf{' + str(round(up, 3)) + '}'
            else:
                temp += str(round(up, 3))
        lines.append(temp)
        with open(output_path + 'result_' + str(self.column + 1) + '.txt', 'w') as txt_file:
            for i in range(len(lines)):
                hline_list = [0, 5, 10, 13, 18, 30, 31]
                if i in hline_list:
                    txt_file.writelines(lines[i] + r' \\ ' + r' \hline' + '\n')
                else:
                    txt_file.writelines(lines[i] + r' \\ ' + '\n')


    '''
    得到文件名中的方法名
    '''
    @staticmethod
    def getMethodName(file_name):
        # 后缀名之前的文件名
        return os.path.splitext(file_name)[0].split('_')[0]
