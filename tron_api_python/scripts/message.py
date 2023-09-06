

message = "56616c6964617465207369676e6174757265206572726f723a20736967206572726f72"

hex_str =message

# 将十六进制字符串转换为字节串
byte_str = bytes.fromhex(hex_str)

# 解码字节串为普通的Unicode字符串
decoded_str = byte_str.decode('utf-8')

# 打印解码后的字符串
print(decoded_str)