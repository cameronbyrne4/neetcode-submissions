/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    bool hasCycle(ListNode* head) {
        // fast and slow pointers that might collide? how long do we run it tho
        // we can stop if both pointers reach null!
        ListNode* fast =head;
        ListNode* slow = head;

        // avoid seg fault
        while (fast && fast->next) {
            // Since we start at head, must move forward first things
            fast = fast->next->next;
            slow = slow->next;

            // Check for cycles
            if (slow == fast) return true;
        
        }
        return false;
    }
};
