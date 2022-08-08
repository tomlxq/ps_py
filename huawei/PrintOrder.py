import copy


class PrintOrder:
    def func(self, line: str) -> str:
        vals = list(map(int, line.split(",")))
        # 拷贝一份数据
        sort_idx = copy.deepcopy(vals)
        # 按大小排序，最大的排前面
        sort_idx.sort(reverse=True)
        # 组成字典，键为索引，值为索引对应的值
        vals_idx = {i: sort_idx[i] for i in range(len(vals))}
        # 按值排序，最大的排最后面
        vals_idx = sorted(vals_idx.items(), reverse=True)
        # 以值为健，索引为值，由于值可重复，因为值为数组
        new_dict = {}
        for t in vals_idx:
            new_dict.setdefault(t[1], []).append(t[0])
        qs = []
        for i in vals:
            min_dct = min(new_dict[i])
            qs.append(str(min_dct))
            new_dict[i].remove(min_dct)
        return ','.join(qs)
