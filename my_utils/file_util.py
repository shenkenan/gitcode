"""
接收传入文件的路径，打印文件的全部内容，如果文件不存在则捕获异常，
输出提示信息，通过finally关闭文件对象
"""
def print_file_info(file_name):
    try:
        fr = open(file_name)
        print(fr)
    except Exception as e:
        print("发现异常")
    finally:
        fr.close()

print_file_info()



    #接收文件路径以及传入数据，将数据追加写入到文件中
def append_to_file(file_name, data):
