# Contain with most water
Two pointer moving problem in LeetCode

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.

![Screenshot 2025-03-16 183931](https://github.com/user-attachments/assets/8fc63f26-1145-4e50-abe2-4a18dfd6a161)


Initialize two pointers:

left starts at index 0
right starts at the last index len(height) - 1
max_water keeps track of the maximum area found.
Calculate the area between height[left] and height[right].

Update max_water if the current area is larger.

Move the pointer pointing to the shorter line:

If height[left] < height[right], increment left (since moving the shorter one may allow a taller one to be found).
Otherwise, decrement right.
Repeat until the two pointers meet.
