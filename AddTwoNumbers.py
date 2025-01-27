class Solution(object):
    def addTwoNumbers(self, l1, l2):
        # Initialize variables
        head = None  # Points to first node of result list
        temp = None  # Used to traverse and build result list
        sum = 0  # Stores sum of current digits
        carry = 0  # Stores carry forward value
        t1 = l1  # Pointer for first list
        t2 = l2  # Pointer for second list
        it = 0  # Control variable for while loop

        # Using it==0 as an alternative to true for continuous loop
        # Loop will break when both lists are exhausted and no carry remains
        while it == 0:
            # Create new node for current sum digit
            new_list = ListNode()

            # Get values from both lists (0 if node doesn't exist)
            n1 = t1.val if t1 is not None else 0
            n2 = t2.val if t2 is not None else 0

            # Calculate sum and handle cases where sum >= 10
            sum = (n1 + n2 + carry) if (n1 + n2 + carry) < 10 else (n1 + n2 + carry) % 10

            # Calculate carry for next iteration
            carry = (n1 + n2 + carry) // 10

            # Set the value in new node
            new_list.val = sum

            # Link the new node to result list
            if head is not None:
                # If not first node, add to end and move temp pointer
                temp.next = new_list
                temp = temp.next
            else:
                # If first node, initialize both head and temp
                head = new_list
                temp = head

            # Move to next nodes in both lists if they exist
            t1 = t1.next if t1 is not None else t1
            t2 = t2.next if t2 is not None else t2

            # Break condition: both lists exhausted and no carry remaining
            if t1 is None and t2 is None and carry == 0:
                it = 1

        return head