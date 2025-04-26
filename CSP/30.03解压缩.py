def parse_leadin(bytes_data, pos):  # 定义解析导引域的函数，输入字节数组和起始位置
    """解析导引域，返回原始长度 n 和新的位置"""
    n = 0  # 初始化原始数据长度
    k = 0  # 初始化指数计数器
    while pos < len(bytes_data):  # 循环直到字节数组结束
        byte = bytes_data[pos]  # 获取当前字节
        c_k = byte & 0x7F  # 提取低 7 位作为系数 c_k
        n += c_k * (128 ** k)  # 计算 n = ∑ c_k * 128^k
        pos += 1  # 位置前进一位
        if not (byte & 0x80):  # 如果高位为 0，则导引域结束
            break  # 退出循环
        k += 1  # 增加指数
    return n, pos  # 返回原始长度和新位置

def decompress(bytes_data):  # 定义解压缩主函数，输入字节数组
    """解压缩主函数"""
    pos = 0  # 初始化字节数组读取位置
    # 解析导引域
    original_len, pos = parse_leadin(bytes_data, pos)  # 获取原始长度和新位置
    buffer = []  # 初始化解压缓冲区，存储解压后的字节

    # 处理数据域
    while pos < len(bytes_data) and len(buffer) < original_len:  # 循环直到字节结束或缓冲区满
        first_byte = bytes_data[pos]  # 获取当前元素的首字节
        type_bits = first_byte & 0x03  # 提取最低两位，判断元素类型
        pos += 1  # 位置前进一位

        if type_bits == 0:  # 如果最低两位是 00，表示字面量
            length_minus_1 = first_byte >> 2  # 高 6 位表示长度减 1
            if length_minus_1 < 60:  # 如果高 6 位 < 60
                l = length_minus_1 + 1  # 长度 l = 高6位 + 1
            else:  # 如果高 6 位 >= 60
                # 根据 60-63 确定长度字节数
                num_bytes = length_minus_1 - 59  # 计算额外长度字节数 (60->1, 61->2, 62->3, 63->4)
                length_bytes = bytes_data[pos:pos + num_bytes]  # 读取长度字节
                pos += num_bytes  # 位置前进 num_bytes 位
                l = int.from_bytes(length_bytes, 'little') + 1  # 小端序转换为长度并加 1
            # 添加字面量字节
            buffer.extend(bytes_data[pos:pos + l])  # 将后续 l 个字节加入缓冲区
            pos += l  # 位置前进 l 位

        elif type_bits == 1:  # 如果最低两位是 01，回溯引用 (4<=l<=11)
            l_minus_4 = (first_byte >> 2) & 0x07  # 提取位 2-4，表示 l-4
            l = l_minus_4 + 4  # 计算长度 l
            o_high = first_byte >> 5  # 提取高 3 位作为偏移量高位
            o_low = bytes_data[pos]  # 读取下一字节作为偏移量低 8 位
            pos += 1  # 位置前进一位
            o = (o_high << 8) | o_low  # 组合偏移量 o (11 位)
            # 处理回溯
            p = len(buffer)  # 获取当前缓冲区长度
            if o >= l:  # 如果偏移量 >= 长度
                start = p - o  # 计算回溯起始位置
                buffer.extend(buffer[start:start + l])  # 复制 l 个字节到缓冲区
            else:  # 如果偏移量 < 长度
                start = p - o  # 计算回溯起始位置
                chunk = buffer[start:start + o]  # 获取 o 个字节的片段
                while len(chunk) < l:  # 循环直到片段长度够 l
                    chunk.extend(chunk)  # 重复自身
                buffer.extend(chunk[:l])  # 取前 l 个字节加入缓冲区

        elif type_bits == 2:  # 如果最低两位是 10，回溯引用 (1<=l<=64)
            l_minus_1 = first_byte >> 2  # 高 6 位表示 l-1
            l = l_minus_1 + 1  # 计算长度 l
            o_bytes = bytes_data[pos:pos + 2]  # 读取后续两字节作为偏移量
            pos += 2  # 位置前进两位
            o = int.from_bytes(o_bytes, 'little')  # 小端序转换为偏移量 o (16 位)
            # 处理回溯
            p = len(buffer)  # 获取当前缓冲区长度
            if o >= l:  # 如果偏移量 >= 长度
                start = p - o  # 计算回溯起始位置
                buffer.extend(buffer[start:start + l])  # 复制 l 个字节到缓冲区
            else:  # 如果偏移量 < 长度
                start = p - o  # 计算回溯起始位置
                chunk = buffer[start:start + o]  # 获取 o 个字节的片段
                while len(chunk) < l:  # 循环直到片段长度够 l
                    chunk.extend(chunk)  # 重复自身
                buffer.extend(chunk[:l])  # 取前 l 个字节加入缓冲区

    return buffer[:original_len]  # 返回缓冲区内容，确保长度匹配原始长度

def format_output(data):  # 定义输出格式化函数，输入解压后的字节列表
    """格式化输出，每行 8 字节"""
    for i in range(0, len(data), 8):  # 每 8 个字节一组循环
        chunk = data[i:i + 8]  # 取当前 8 个字节（最后可能不足 8 个）
        print(''.join(f'{byte:02x}' for byte in chunk))  # 格式化为两位十六进制并打印

# 主程序
s = int(input())  # 读取压缩数据字节数 s
bytes_data = []  # 初始化字节数组
for _ in range((s + 7) // 8):  # 循环读取 ⌈s/8⌉ 行
    line = input().strip()  # 读取一行输入，去除首尾空白
    for i in range(0, len(line), 2):  # 每两个字符组成一个字节
        byte = int(line[i:i + 2], 16)  # 将两位十六进制转换为整数
        bytes_data.append(byte)  # 添加到字节数组

result = decompress(bytes_data)  # 调用解压缩函数处理字节数组
format_output(result)  # 格式化并输出解压结果