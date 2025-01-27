def lengthOfLongestSubstring(self, s):
    # Initialize a set to keep track of characters in current window
    # Using set because lookup/insert/delete operations are O(1)
    seen = set()

    # Left pointer of window - marks the start of current window
    left = 0

    # Variable to store the length of longest substring found so far
    maxLen = 0

    # Right pointer of window - marks the end of current window
    # Loop through each character in string using right pointer
    for right in range(len(s)):
        # If current character is already in our window
        # We need to shrink window from left until we remove the duplicate
        while s[right] in seen:
            # Remove the leftmost character from window
            seen.remove(s[left])
            # Move left pointer one step right to shrink window
            left += 1

        # At this point, we're sure current character is not in window
        # Add current character to our set
        seen.add(s[right])

        # Calculate current window size (right - left + 1)
        # Update maxLen if current window is longer
        maxLen = max(maxLen, right - left + 1)

    return maxLen

# Let's see how it works with example "abcabcbb":
# Initial state: seen = {}, left = 0, maxLen = 0
#
# 1st iteration (right = 0, char = 'a'):
#   - seen = {'a'}
#   - window = "a", length = 1
#   - maxLen = 1
#
# 2nd iteration (right = 1, char = 'b'):
#   - seen = {'a', 'b'}
#   - window = "ab", length = 2
#   - maxLen = 2
#
# 3rd iteration (right = 2, char = 'c'):
#   - seen = {'a', 'b', 'c'}
#   - window = "abc", length = 3
#   - maxLen = 3
#
# 4th iteration (right = 3, char = 'a'):
#   - 'a' is in seen, so remove chars from left until old 'a' is gone
#   - Remove 'a', left moves to 1
#   - seen = {'b', 'c', 'a'}
#   - window = "bca", length = 3
#   - maxLen stays 3
#
# Process continues similarly...
#
# Time Complexity: O(n) - each character is processed at most twice 
#                        (once by right pointer, once by left pointer)
# Space Complexity: O(min(m,n)) - where m is size of character set