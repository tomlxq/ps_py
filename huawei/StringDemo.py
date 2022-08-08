class StringDemo:
    def findString(self, search: str, letters: str) -> int:
        idx = letters.rfind(search)
        if idx == -1:
            return idx
        else:
            return idx + len(search)

    def findString2(self, search: str, letters: str) -> int:
        fast, slow = len(letters) - 1, len(search) - 1
        while fast >= 0 and slow >= 0:
            if search[slow] == letters[fast]:
                if slow == 0:
                    return fast
                slow -= 1
            fast -= 1
        return -1
