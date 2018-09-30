from Tools.MatFileTool import MatFileTool

path = 'D:\\data_hdp\\'
output_path = 'D:\\hdp_result\\'
key_list = ['CM1', 'MW1', 'PC1', 'PC3', 'PC4', 'ar1', 'ar3', 'ar4', 'ar5', 'ar6', 'Apache', 'Safe', 'Zxing', 'EQ', 'JDT', 'LC', 'ML', 'PDE', 'ant-1.7', 'camel-1.6', 'ivy-2.0', 'jedit-4.0', 'log4j-1.0', 'lucene-2.4', 'poi-3.0', 'synapse-1.2', 'tomcat', 'velocity-1.6', 'xalan-2.4', 'xerces-1.3']
num = [5, 7, 8, 11]
for i in num:
    MatFileTool(i).core_run(path, key_list, output_path)
