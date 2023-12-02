class Solution:
    def interpret(self, command: str) -> str:
        ans = ""
        n = len(command) - 1
        for i, c in enumerate(command):
            if c == "(" and i + 1 <= n and command[i + 1] == ")":
                ans += "o"
            elif c == "(" and i + 1 <= n and command[i + 1] == "a":
                ans += "al"
            elif c == "G":
                ans += "G"
            else:
                continue
        return ans