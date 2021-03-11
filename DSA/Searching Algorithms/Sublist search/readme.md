# Sublist search
Sublist search is used to detect a presence of one list in another list. Suppose we have a single-node list (let's say the first list), and we want to ensure that the list is present in another list (let's say the second list), then we can perform the sublist search to find it. For instance, the first list contains these elements: 23 -> 30 -> 41, and the second list contains these elements: 10 -> 15 -> 23 -> 30 -> 41 -> 49. At a glance, we see that the first list presents in the second list.

## Algorithm

    1- Take first node of second list. 
    2- Start matching the first list from this first node. 
    3- If whole lists match return true. 
    4- Else break and take first list to the first node again. 
    5- And take second list to its second node. 
    6- Repeat these steps until any of linked lists becomes empty. 
    7- If first list becomes empty then list found else not.

## Performance
Time Complexity : O(m*n) where m is the number of nodes in second list and n in first.