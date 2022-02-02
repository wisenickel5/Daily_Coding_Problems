# Completed by Dylan Alexander on 02/01/2022
# This problem was asked by Snapchat.
# Given an array of time intervals (start, end) for 
# classroom lectures (possibly overlapping), find 
# the minimum number of rooms required.
# Assume the left tuple value will always be less than the right
# For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.

def minimum_rooms(lectures: list[(int, int)]) -> int:
	if len(lectures) == 0:
		return 0
	
	starting_times, ending_times = [], []

	for i in range(0, len(lectures) - 1):
		[start_time, end_time] = lectures[i]
		starting_times.append(start_time)
		ending_times.append(end_time)
	
	starting_times.sort()
	ending_times.sort()

	start_idx, end_idx, = 0, 0
	max_rooms, curr_rooms = 0, 0

	while (start_idx < len(starting_times) or end_idx < len(ending_times)):
		# Don't traverse through the ending times if all the starting times rooms are used
		if (start_idx > len(starting_times)): break

		if (starting_times[start_idx] < ending_times[end_idx]):
			curr_rooms += 1
			start_idx += 1
		else:
			curr_rooms -= 1
			end_idx += 1

		max_rooms = max(max_rooms, curr_rooms)
	
	return max_rooms

if __name__ == "__main__":
	class_times = [(30, 75), (0, 50), (60, 150)]
	num_rooms = minimum_rooms(class_times)
	print(num_rooms)