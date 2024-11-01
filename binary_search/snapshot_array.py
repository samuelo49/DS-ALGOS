'''
Implement a SnapshotArray that supports the following interface:

SnapshotArray(int length) initializes an array-like data structure with the given length. Initially, each element equals 0.
void set(index, val) sets the element at the given index to be equal to val.
int snap() takes a snapshot of the array and returns the snap_id: the total number of times we called snap() minus 1.
int get(index, snap_id) returns the value at the given index, at the time we took the snapshot with the given snap_id
Example 1:

Input: ["SnapshotArray","set","snap","set","get"]

[[3],[0,5],[],[0,6],[0,0]]

Output: [null,null,0,null,5]

Explanation:

SnapshotArray snapshotArr = new SnapshotArray(3); // set the length to be 3

snapshotArr.set(0,5);  // Set array[0] = 5

snapshotArr.snap();  // Take a snapshot, return snap_id = 0

snapshotArr.set(0,6);

snapshotArr.get(0,0);  // Get the value of array[0] with snap_id = 0, return 5
Constraints:

1 <= length <= 5 * 104
0 <= index < length
0 <= val <= 109
0 <= snap_id < (the total number of times we call snap())
At most 5 * 104 calls will be made to set, snap, and get.

plan
- Instead of copying the whole array each time we take a snapshot, we wish to only store the changes
    to each index. 
- so we keep a histories array that keeps track of any changes of the array[i]'s values.
- we use the pair (snap_id, value) to indicate we have updated array[i]=value at the time we took 
    the snapshot with the given snap_id

- so when implementing the get(snap_id) for index i, we do binary search on histories[i] to find
    the index pos in histories[i] that contains the most recent value up to the time we took the 
    snapshot with the given snap_id.
'''
class SnapshotArray(object):

    def __init__(self, n):
        # set up histories so that each index has its own history
        self.histories = [[[-1, 0]] for _ in range(n)]
        self.snap_id = 0

    def set(self, index, val):
        self.histories[index].append([self.snap_id, val])

    def snap(self):
        self.snap_id += 1
        return self.snap_id - 1

def get(self, index, snap_id):
    left, right, pos = 0, len(self.histories[index])-1, -1
    while left <= right:
        mid = (left+right) // 2
        if self.histories[index][mid][0] <= snap_id:
            left = mid + 1
            pos = mid
        else:
            right = mid - 1
    return self.histories[index][pos][1]