s = "Hello,World"
print(s[1]) # 'e', 取出某个位置的字符
print(s[1:6]) # 'ello,' ，字符串切片
print(len(s)) # 11, 返回字符串的长度print("e" in s) # True, 返回字符是否在字符串中
print(s.lower()) # 'hello,world', 将字符串所有元素变为小写
print(s.upper()) # 'HELLO,WORLD', 将字符串所有元素变为大写
s += '...' # Hello,World... ，字符串拼接，在字符串后拼接另一个字符串
print(s.find('lo')) # 3, 返回第一次找到指定字符串的起始位置（从左往右找）
print(s.swapcase()) # hELLO,wORLD..., 将大小写互换
print(s.split(',')) # ['Hello', 'World...'], 将字符串根据目标字符分割