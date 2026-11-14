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
    void reorderList(ListNode* head) {
        ListNode* front = head;
        ListNode* back = head;
        ListNode* fast = head; // helps us put back at the midpoint
        while (fast && fast->next) {
            // Stops at final node;
            fast = fast->next->next;
            back = back->next;
        }
        ListNode* stopper = back;

        // Step 2: reverse the back half;
        ListNode* prev = NULL;
        ListNode* curr = back->next;
        back->next = NULL; //split
        while (curr) {
            ListNode* temp = curr->next;
            curr->next = prev;
            prev = curr;
            curr = temp;
        }
        // If odd size, there will be one extra element in the back half
        while (prev) {
            ListNode* temp1 = front->next;
            ListNode* temp2 = prev->next;
            front->next = prev;
            prev->next = temp1;
            front = temp1;
            prev = temp2;
        }
       

    }
};
// go from head and tail alternating until they point at eachother
