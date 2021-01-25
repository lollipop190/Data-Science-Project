
def can_attend_meetings(intervals):
    
    intervals = sorted(intervals, key=lambda x: x.start)
    for i in range(1, len(intervals)):
        if intervals[i].start < intervals[i - 1].end:
            return False
    return True
