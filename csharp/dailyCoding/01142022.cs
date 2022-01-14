/* Solution by: https://github.com/zach-v
 * January 14, 2022
 * https://leetcode.com/problems/add-two-numbers/
 * You are given two non-empty linked lists representing two non-negative integers.
 * The digits are stored in reverse order, and each of their nodes contains a single digit.
 * Add the two numbers and return the sum as a linked list.
 * You may assume the two numbers do not contain any leading zero, except the number 0 itself.
 */
public class _01142022
{
	public static void main()
	{
		Console.WriteLine("Testing Add Two Numbers");
		Console.WriteLine("Return: " + Build(AddTwoNumbers(ListNode.Make(342), ListNode.Make(465))));
		Console.WriteLine("Return: " + Build(AddTwoNumbers(ListNode.Make(9999999), ListNode.Make(9999))));
	}
	// Solution method
	static ListNode AddTwoNumbers(ListNode l1, ListNode l2)
	{
		// Get the converted numbers
		int l1num = int.Parse(Build(l1));
		int l2num = int.Parse(Build(l2));
		int sum = l1num + l2num;
		return ListNode.Make(sum);
	}
	// Recursive string builder
	static string Build(ListNode head)
	{
		if (head == null)
			return "";
		return Build(head.next) + head.val;
	}
}
public class ListNode
{
	public int val;
	public ListNode next;
	public ListNode(int val = 0, ListNode next = null)
	{
		this.val = val;
		this.next = next;
	}
	/// <summary>
	/// Returns the head of a ListNode structure from a list of ints.
	/// </summary>
	/// <param name="items"></param>
	/// <returns></returns>
	public static ListNode Make(params int[] items)
	{
		if (items == null)
			return null;
		// we keep track of a previous to make sure we set the next listnode
		ListNode head = new ListNode(items[items.Length - 1]);
		ListNode previous = head;
		// iterate through the items given
		for(int i = items.Length - 2; i >= 0; i--)
		{
			// make a new node and set previous to it
			ListNode temp = new ListNode(items[i]);
			previous.next = temp;
			previous = temp;
		}
		return head;
	}
	/// <summary>
	/// Returns the head of a ListNode structure from an int.
	/// </summary>
	/// <param name="items"></param>
	/// <returns></returns>
	public static ListNode Make(int number)
	{
		return Make(SplitDigits(number));
	}
	/// <summary>
	/// Splits a number into an array by each digit.
	/// </summary>
	/// <param name="number"></param>
	/// <returns></returns>
	public static int[] SplitDigits(int number)
	{
		List<int> listOfInts = new List<int>();
		while (number > 0)
		{
			listOfInts.Add(number % 10);
			number = number / 10;
		}
		listOfInts.Reverse();
		return listOfInts.ToArray();
	}
}