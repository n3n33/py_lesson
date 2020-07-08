# 함수가 임의의 개수 인자로 호출될 수 있도록 지정하는 것입니다.
# 이 인자들은 튜플로 묶입니다.
# 가변 길이 인자 앞에, 없거나 여러 개의 일반 인자들이 올 수 있습니다.


# def write_multiple_items(file, separator, *args):
#     file.write(separator.join(args))

def concat(*args, sep="+"):
    return sep.join(args)


concat("earth", "mars", "venus")
