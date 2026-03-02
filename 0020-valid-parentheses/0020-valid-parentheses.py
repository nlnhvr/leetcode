class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        store = []
        d = {"()", "[]", "{}"}
        for c in s:
            if c in "([{":
                store.append(c)
            elif not store or store.pop() + c not in d:
                return False
            
        return not store