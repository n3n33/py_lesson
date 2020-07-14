# os 모듈은 운영체제와 상호작용하기 위한 수십가지 함수를 제공함
import os
import shutil

os.getcwd()  # 최근 작업한 디렉토리 반환

os.chdir('/server/accesslogs')  # 최근 작업한 디렉토리 변경

os.system('mkdir today')  # 쉘에 mkdir today 입력됨

dir(os)

shutil.copyfile('data.db', 'archive.db')
shutil.move('/build/executables', 'installdir')