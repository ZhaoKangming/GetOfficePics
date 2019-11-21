import os
import shutil
import zipfile
import win32com.client as win32

# TODO:界面选择，文件还是文件夹
# TODO:对wps文件类型的支出与处理

def file_checker(file_path: str) -> list:
    '''
    【功能】检查文档是否为指定类型文档
    :param file_path: 文件的路径
    '''
    temp_path: str = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'temp')
    if not os.path.exists(temp_path):
        os.makedirs(temp_path)
    # 检测文件是否为指定文档类型
    allowed_suffix_list: list = ['xls', 'xlsx', 'xlsm', 'ppt', 'pptx', 'ppsx', 'ppsm', 'pptm', 'doc', 'docx']
    file_suffix = os.path.splitext(file_path)[1]
    if file_suffix == '':
        result = ['NO', '[WARNING] 无后缀名文件！']
    elif not file_suffix in allowed_suffix_list:
        result = ['NO', '[WARNING] 非支持类型的文件！']
    elif file_suffix in ['xls', 'ppt', 'doc']:
        shutil.copy(file_path, temp_path)
        new_file_path: str = file_convertor(file_path)
        result = ['YES', new_file_path]
    else:
        shutil.copy(file_path, temp_path)
        new_file_path: str = os.path.join(temp_path, os.path.basename(file_path) + 'x')
        result = ['YES', new_file_path]



def file_convertor(file_path: str) -> str:
    '''
    【功能】将旧格式的office文件转为新版本office文件
    :param file_path: 文件的路径
    :param file_suffix: office文件后缀名
    '''
    file_suffix = os.path.splitext(file_path)[1]
    param_dict: dict = {'ppt': ['PowerPoint.Application', 1], 'xls': ['Excel.Application', 51], 'doc': ['Word.Application', 16]}
    app = win32.gencache.EnsureDispatch(param_dict[file_suffix][0])
    new_file_path: str = file_path + 'x'

    if file_suffix == 'xls':
        office_obj = app.Workbooks.Open(file_path)
    elif file_suffix == 'doc':
        office_obj = app.Documents.Open(file_path)
    elif file_suffix == 'ppt':
        office_obj = app.Presentations.Open(file_path, WithWindow=False)

    if file_suffix == 'ppt':
        office_obj.SaveAs(new_file_path)
        office_obj.Close()
        app.Quit()
    else:
        office_obj.SaveAs(new_file_path, FileFormat=param_dict[file_suffix][1])
        office_obj.Close()
        app.Application.Quit()

    # 源文件处理与新文件输出
    os.remove(file_path)
    return new_file_path



# 判断是否是文件和判断文件是否存在
def isfile_exist(file_path):
    if not os.path.isfile(file_path):
        print("It's not a file or no such file exist ! %s" % file_path)
        return False
    else:
        return True


# 修改指定目录下的文件类型名，将excel后缀名修改为.zip
def change_file_name(file_path, new_type='.zip'):
    if not isfile_exist(file_path):
        return ''

    extend = os.path.splitext(file_path)[1]  # 获取文件拓展名
    if extend != '.xlsx' and extend != '.xls':
        print("It's not a excel file! %s" % file_path)
        return False

    file_name = os.path.basename(file_path)  # 获取文件名
    new_name = str(file_name.split('.')[0]) + new_type  # 新的文件名，命名为：xxx.zip

    dir_path = os.path.dirname(file_path)  # 获取文件所在目录
    new_path = os.path.join(dir_path, new_name)  # 新的文件路径
    if os.path.exists(new_path):
        os.remove(new_path)

    os.rename(file_path, new_path)  # 保存新文件，旧文件会替换掉

    return new_path  # 返回新的文件路径，压缩包


# 解压文件
def unzip_file(zipfile_path):
    if not isfile_exist(zipfile_path):
        return False

    if os.path.splitext(zipfile_path)[1] != '.zip':
        print("It's not a zip file! %s" % zipfile_path)
        return False

    file_zip = zipfile.ZipFile(zipfile_path, 'r')
    file_name = os.path.basename(zipfile_path)  # 获取文件名
    zipdir = os.path.join(os.path.dirname(zipfile_path), str(file_name.split('.')[0]))  # 获取文件所在目录
    for files in file_zip.namelist():
        file_zip.extract(files, os.path.join(zipfile_path, zipdir))  # 解压到指定文件目录

    file_zip.close()
    return True

#xl\media  ppt\media

# 读取解压后的文件夹，打印图片路径
def read_img(zipfile_path, img_path):
    if not isfile_exist(zipfile_path):
        return False

    dir_path = os.path.dirname(zipfile_path)  # 获取文件所在目录
    file_name = os.path.basename(zipfile_path)  # 获取文件名
    unzip_dir = os.path.join(dir_path, str(file_name.split('.')[0]))
    pic_dir = 'xl' + os.sep + 'media'  # excel变成压缩包后，再解压，图片在media目录
    pic_path = os.path.join(dir_path, str(file_name.split('.')[0]), pic_dir)

    file_list = os.listdir(pic_path)
    for file in file_list:
        filepath = os.path.join(pic_path, file)
        print(filepath, img_path)
        shutil.move(filepath, img_path)
    os.unlink(zipfile_path)
    shutil.rmtree(unzip_dir)


# 组合各个函数
def compenent(excel_file_path, img_path):
    zip_file_path = change_file_name(excel_file_path)
    if not os.path.exists(img_path):
        os.mkdir(img_path)
    if zip_file_path != '':
        unzip_msg = unzip_file(zip_file_path)
        if unzip_msg:
            read_img(zip_file_path, img_path)
