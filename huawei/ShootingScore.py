class ShootingScore:
    def func(self, times: int, ids: str, scores: str) -> str:
        list_ids = ids.split(",")
        list_scores = list(map(int, scores.split(",")))
        data = {}
        for i in range(times):
            if list_ids[i] in data:
                data[list_ids[i]].append(list_scores[i])
            else:
                data[list_ids[i]] = [list_scores[i]]
        for k, v in data.items():
            if len(v) < 3:
                data.pop(k)
            else:
                v.sort(reverse=True)
                data[k] = sum(v[:3])
        res = sorted(data.items(), key=lambda x: (x[1], x[0]), reverse=True)
        return ','.join(k for k, v in res)
