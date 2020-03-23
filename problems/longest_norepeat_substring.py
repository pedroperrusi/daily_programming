"""
Given a string, find the length of the longest substring without repeating characters.
Example:
  Input: 'abrkaabcdefghijjxxx'
  Output: 10

Credit: Daily Interview Pro: https://www.techseries.dev/daily
"""
# Definition for singly-linked list.
class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
  """
    Naive solution: put each char in a dictionary and count its occurences
  """
  def lengthOfLongestSubstring(self, s):
    letters = set()
    n_no_repeat = 0
    for char in s:
      if char not in letters:
        letters.add(char)
        n_no_repeat += 1
    return n_no_repeat
    
class SolutionLinearTime:
  """
    Linear time solution as described by https://www.geeksforgeeks.org/length-of-the-longest-substring-without-repeating-characters/
  """
  def lengthOfLongestSubstring(self, s):
    BITS_CHAR = 256
    n = len(s)
    max_len = 1 # maximum substring length (output)
    current_len = 1 # current substring length
    # visited is an array which will store letter indexes when they occur
    visited = [-1] * BITS_CHAR # -1 means unvisited
    # process the first char and add its index
    visited[ord(s[0])] = 0

    for idx in range(1, n):
      visited_idx = visited[ord(s[idx])]
      # if char has not yet been visited
      if visited_idx == -1:
        current_len += 1
      # if that's not the case, reset the counting from its index
      else:
        if current_len > max_len:
          max_len = current_len
        current_len = idx - visited_idx
      # update index of current character
      visited[ord(s[idx])] = idx
    # compare for the last letters
    if current_len > max_len:
      max_len = current_len
    return max_len

def main():
  print ('Naive solution')
  print (Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx'))
  print (SolutionLinearTime().lengthOfLongestSubstring('abrkaabcdefghijjxxx'))
  # Expected: 13
  print ('Linear time solution')
  print (Solution().lengthOfLongestSubstring('ABDEFGABEF'))
  print (SolutionLinearTime().lengthOfLongestSubstring('ABDEFGABEF'))
  # Expected: 6


if __name__== "__main__":
  main()