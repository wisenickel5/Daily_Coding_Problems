/* Solution by: https://github.com/zach-v
 * January 12, 2022
 * Given an array of integers, return a new array such that each element at index i of the
 * new array is the product of all the numbers in the original array except the one at i.
 * 
 * For example, if our input was [1, 2, 3, 4, 5],
 * the expected output would be [120, 60, 40, 30, 24].
 * If our input was [3, 2, 1],
 * the expected output would be [2, 3, 6].
 */

public class _01122022
{
	public static void main()
	{
		Console.WriteLine("Testing Product array.");
		Console.WriteLine("Return: " + String.Join(",", Product(3)));
		Console.WriteLine("Return: " + String.Join(",", Product(3, 2, 1)));
		Console.WriteLine("Return: " + String.Join(",", Product(1, 2, 3, 4, 5)));
	}
	static int[] Product(params int[] input)
	{
		// base case
		if (input.Length == 1)
		{
			// return just the element
			return new int[] { input[0] };
		}
		// all other cases
		int[] sender = new int[input.Length];
		for (int i = 0; i < input.Length; i++)
		{
			int product = 1;
			// iterate through
			for (int j = 0; j < input.Length; j++)
			{
				if (input[j] != input[i])
					product = product * input[j];
			}
			sender[i] = product;
		}
		return sender;
	}
}