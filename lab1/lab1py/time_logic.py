print("Enter total number of seconds")
totalseconds = int(input())
hours = totalseconds // 3600
remainingseconds = totalseconds % 3600
minutes = remainingseconds // 60
seconds = remainingseconds % 60
print(f"{hours} hours, {minutes} minutes, {seconds} seconds")