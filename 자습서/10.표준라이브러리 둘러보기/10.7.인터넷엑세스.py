# 가장 간단한 두 개는 URL에서 데이터를 읽어오는 urllib.request 와
# 메일을 보내는 smtplib 입니다:

from urllib.request import urlopen

with urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl') as response:
    for line in response:
        line = line.decode('utf-8')
        if 'EST' in line or 'EDT' in line:
            print(line)

import smtplib

server = smtplib.SMTP('localhost')
server.sendmail('sm.choi@telechips.com', 'whi0331@hanmail.net',
                """
                TO: sm.choi@telechips.com
                FROM: whi0331@hanmail.net
                
                보드는 없어.
                """)
server.quit()
