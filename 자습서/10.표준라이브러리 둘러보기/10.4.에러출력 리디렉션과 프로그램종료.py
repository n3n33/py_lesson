# sys 모듈은 stdin, stdout, stderr 어트리뷰트도 갖고 있습니다. 가장 마지막 것은 stdout 이 리디렉트 되었을 때도 볼 수 있는 경고와 에러 메시지들을 출력하는데 쓸모가 있습니다:
#
# >>>
# >>> sys.stderr.write('Warning, log file not found starting a new one\n')
# Warning, log file not found starting a new one
# 가장 직정적인 방법은 sys.exit()
