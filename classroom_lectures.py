""" From the "Daily Coding Problem" https://www.dailycodingproblem.com/

"Given an array of time intervals (start, end) for classroom lectures
(possibly overlapping), find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2."
"""

def scheduler(lectures):
    # Get lecture end times from the tuples.
    lecture_end_times = [lecture[1] for lecture in lectures]
    
    # Create "schedule" for every 5 minutes based on the latest lecture end time.
    schedule = [time for time in range(0, max(lecture_end_times) + 1, 5)]

    # Make it a dictionary to mark if reservation is needed at each specific time.
    schedule = { time: 0 for time in schedule }

    # Populate the dict based on each lecture.
    for lecture in lectures:
        lecture_needed_times = [time for time in range(lecture[0], lecture[1], 5)]
        for needed_time in lecture_needed_times:
            schedule[needed_time] += 1

    # Find the time with most needed rooms.
    max_rooms = max(schedule.values())

    return max_rooms


rooms_required = scheduler([(30, 75), (0, 50), (60, 150)])
print(rooms_required)

rooms_required = scheduler([(30, 75), (0, 50), (60, 150), (60, 150)])
print(rooms_required)

rooms_required = scheduler([(30, 75), (0, 50), (60, 150), (150, 200), (30, 60), (30, 90), (145, 155)])
print(rooms_required)