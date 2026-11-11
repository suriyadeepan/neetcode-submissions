class Solution:

    def minWindow(self, s: str, t: str) -> str:
        # Corner case 1: if t is empty string
        if t == "": return ""

        # initialize hash maps
        window, T = {}, {}
        for ch in t:
            T[ch] = 1 + T.get(ch, 0)

        # have and need variables
        have, need = 0, len(T) # number of unique characters in T
        # placeholders to store results
        res, resLen = [-1, -1], float("infinity")

        # init left pointer
        l = 0
        for r in range(len(s)):  # move the right pointer right
            ch = s[r]
            window[ch] = 1 + window.get(ch, 0)  # adding any character to window

            # check ch and update have
            if ch in T and T[ch] == window[ch]:  # (1) do we care about ch (2) do we have the right count?
                have += 1

            # are the needs met?
            while have == need:  # why a loop though?
                # calculate size of current window
                windowSize = r - l + 1
                if windowSize < resLen:   # is it less than our results (in length)
                    # update results
                    res = [l, r]
                    resLen = windowSize
                # answer to 'why loop?' => while the condition is met, keep shrinking the substring
                # meaning => move left pointer right
                # (1) Pop from the left of the window
                window[s[l]] -= 1
                # (2) Has that affected our "have"?
                if s[l] in T and window[s[l]] < T[s[l]]:
                    # (i)  is that a character we care about?
                    # (ii) do we not have enough?
                    have -= 1

                l += 1
        
        # out of the loop
        # expand the results
        l, r = res
        return s[l:r+1] if resLen <= len(s) else ""





