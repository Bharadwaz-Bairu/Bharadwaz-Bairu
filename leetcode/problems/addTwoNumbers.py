# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        valu = 0
        val = l1.val+l2.val
        node = ListNode()
        if val >= 10:
            node = ListNode(val%10)
            valu = 1
        if val < 10 :
            node = ListNode(val)
            valu = 0
        temp = node
        while l1.next and l2.next :
            l1=l1.next
            l2=l2.next
            #if val == 1 :
            val = l1.val+l2.val + valu
            if val >= 10:
                temp.next = ListNode(val%10)
                valu = 1
            elif val < 10 :
                temp.next = ListNode(val)
                valu = 0 
            temp = temp.next
        while l1.next :
            l1 = l1.next 
            val = l1.val + valu
            if val >= 10 :
                temp.next = ListNode((val%10))
                valu = 1
            if val < 10 :
                temp.next = ListNode(val)
                valu = 0
            temp = temp.next
            
        while l2.next :
            l2 = l2.next 
            val = l2.val + valu
            if val >= 10 :
                temp.next = ListNode(val%10)
                valu = 1 
            if val < 10 :
                temp.next = ListNode(val)
                valu = 0
            
            temp = temp.next
        if valu == 1 :
            
            temp.next = ListNode(valu)
        return node
      
                    
                
        
            
                
