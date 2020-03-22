"""
You are given two linked-lists representing two non-negative integers. 
The digits are stored in reverse order and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.
Example:
  Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
  Output: 7 -> 0 -> 8
  Explanation: 342 + 465 = 807.

Credit: Daily Interview Pro: https://www.techseries.dev/daily
"""
# Definition for singly-linked list.
class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
  def addTwoNumbers(self, l1, l2, c = 0):
    # compute value for this decimal case
    dst = ListNode(l1.val + l2.val + c);
    # check for overflow
    if dst.val >= 10:
      dst.val -= 10
      c = 1
    else:
      c = 0
    # if there is another digit
    if l1.next and l2.next:
      dst.next = self.addTwoNumbers(l1.next, l2.next, c)
    return dst
    
def main():
  l1 = ListNode(2)
  l1.next = ListNode(4)
  l1.next.next = ListNode(3)

  l2 = ListNode(5)
  l2.next = ListNode(6)
  l2.next.next = ListNode(4)

  result = Solution().addTwoNumbers(l1, l2)
  while result:
    print(result.val)
    result = result.next
  # expected: 7 0 8

if __name__== "__main__":
  main()