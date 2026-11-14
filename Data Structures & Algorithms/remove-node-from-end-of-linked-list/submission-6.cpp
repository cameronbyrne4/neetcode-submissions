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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        // Find length of list
        // Use that to know how far to increment a slow ponter
        ListNode* move = head;
        int length = 1;
        while (move->next) {
            move = move->next;
            length++;
        }
        cout << length << endl;

        // Move to the node BEFORE the node we have to kill
            // Need checkf for when length is 1 and d=0

        
        
        int dist = length - n; // number of times we need to move
        if (dist==0) return head->next;
        cout << "Distance = length - n = " << length << " - " << n << " = " << dist << endl;
        ListNode* curr = head;
        for (int i = 0; i < dist-1; i++) {
            curr = curr->next;
        }

        curr->next = curr->next->next;
        return head;

    }
};

//from the end??

// we know how to reverse and run two pointers
