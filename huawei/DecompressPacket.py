class DecompressPacket:
    def func(self, line: str) -> str:
        def process(line: str):
            if line == '' or line.find('[') == -1:
                if line == ']':
                    return ''
                return line
            open_idx = line.find('[')
            close_idx = line.find(']')
            tmp = line[open_idx + 1:close_idx]
            num = int(line[0:open_idx])
            if tmp.find('[') == -1:
                return tmp * num + process(line[close_idx + 1:len(line)])
            else:
                n = tmp.count('[') + 1
                last_idx = close_idx
                while (last_idx := line.find(']')) != -1 and n > 0:
                    n -= 1
                close_idx = last_idx
                tmp = line[open_idx + 1:close_idx + 1]
                i, j = 0, 0
                for i in range(len(tmp)):
                    if tmp[i].isalpha():
                        continue
                    break
                pre_str = tmp[j:i]
                return (pre_str + process(tmp[i:len(tmp)])) * num
        return process(line)
