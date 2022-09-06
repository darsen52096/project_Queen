#!/usr/bin/env python
# launch project /python3 main.py

import config_os
import get_func
import crawlers
import os
import formalizations

# absolute source path (files.xlsx)
path_of_incoming_folder = "/home/arsen52096/projects_Arsen/project_Queen/crawler_files"
# absolute destination path (files.xlsx)
path_of_outcoming_folder = "/home/arsen52096/projects_Arsen/project_Queen/"


if __name__ == '__main__':
    # start
    print(os.getcwd())
    print('Queen.Crawler starting work...')
    config_os.remove_files_and_dir(path_of_incoming_folder)
    print('Files with the extensions .csv and directory deleted')
    checking_files = config_os.creating_csv_files(path_of_incoming_folder)
    print('Paths of files with the extensions .csv  generated')
    horizontal_lists, vertical_lists = crawlers.crawl_files(checking_files, 'horizontally'), crawlers.crawl_files(checking_files, 'vertically')
    print('Files are crawled by horizontally and vertically')
    print(type(vertical_lists))
    formalizations.remove_values_from_list(vertical_lists, "")
    print(vertical_lists)


    # formalizations.remove_values_from_list(horizontal_lists, "")


    config_os.remove_files_and_dir(path_of_incoming_folder)
    print('Files with the extensions .csv and directory deleted')
    # end
    print('Good work! Project Queen\nBeautiful is better than ugly')