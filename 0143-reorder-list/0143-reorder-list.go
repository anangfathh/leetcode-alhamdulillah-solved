/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func reorderList(head *ListNode)  {
    slow := head;
    fast := head.Next;

    for fast != nil && fast.Next != nil{
        slow = slow.Next
        fast = fast.Next.Next
    }

    second := slow.Next
    var prev *ListNode = nil
    slow.Next = nil
    for second != nil{
        tmp := second.Next
        second.Next = prev
        prev = second
        second = tmp
    }

    first := head
    second = prev
    for second != nil{
        tmp1 := first.Next
        tmp2 := second.Next
        first.Next = second
        second.Next = tmp1
        first = tmp1
        second = tmp2
    }
}