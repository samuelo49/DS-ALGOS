'''
❓ PROMPT
Given a two dimensional array, output a new one dimensional array with the elements of the input in zig zag order. 
This means that the first row will be in the output from first to last, but the second row will be the reverse, last to first, 
then the third is back to normal order again, each row the opposite order of the ones before and after.

Example(s)
const matrix = [
  [1, 2, 3],
  [4, 5, 6]
]
linearizeZigZag(matrix) == [1,2,3,6,5,4]
 

🔎 EXPLORE
List your assumptions & discoveries:
 

Insightful & revealing test cases:
 

🧠 BRAINSTORM
What approaches could work?
Algorithm 1:
Time: O()
Space: O()
 

📆 PLAN
Outline of algorithm #: 
1. initialize an output array
2. traverse items at the odd index left -> right
    append the items to the output
3. traverse items at the even index in reverse.
    append the items to the output array
5. return out array



🛠️ IMPLEMENT
function linearizeZigZag(matrix) {
def linearizeZigZag(matrix: list[list[int]]) -> list[int]:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''
def linearizeZigZag(matrix):
    result = []
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if row % 2 != 0:
                result.append(matrix[row][len(matrix[row]) - 1 - col])
            else:
                result.append(matrix[row][col])
    return result


matrix = [
  [1, 2, 3],
  [4, 5, 6]
]

print(linearizeZigZag(matrix=matrix))

matrix_1 = [[]]
print(linearizeZigZag(matrix_1))

matrix_2 = [[1, 2, 3]]
print(linearizeZigZag(matrix_2))

matrix_3 = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]]

print(linearizeZigZag(matrix_3))