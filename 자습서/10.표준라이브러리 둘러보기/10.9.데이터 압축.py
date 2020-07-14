# 일반적인 데이터 보관 및 압축 형식들을 다음과 같은 모듈들이 직접 지원합니다:
# zlib, gzip, bz2, lzma, zipfile, tarfile.

import zlib
s = b'witch which has which witches wrist watch'
len(s)
# 41
t = zlib.compress(s)
len(t)
# 37
zlib.decompress(t)
# b'witch which has which witches wrist watch'
zlib.crc32(s)
# 226805979