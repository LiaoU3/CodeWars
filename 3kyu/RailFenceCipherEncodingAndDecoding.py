# https://www.codewars.com/kata/58c5577d61aefcf3ff000081/train/python

def encode_rail_fence_cipher(string, n):
    code = [[]for i in range(n)]
    pos = 0
    while pos < len(string) :
        for cnt in range(n*2 -2):
            if cnt < n:
                code[cnt].append(string[pos])
            else:
                code[n*2 - cnt -2].append(string[pos])
            pos += 1
            if pos == len(string):
                break
    for i in range(1, n):
        code[0].extend(code[i])

    return ''.join(code[0])

#wrong answer
# def decode_rail_fence_cipher(string, n):
#     code = [[]for i in range(n)]
#     turn = len(string) // (n*2 -2)
#     last = len(string) % (n*2 -2)

#     add = [0 for i in range(n)]
#     if string == '':
#         return ''
#     if last <= n:    
#         for row in range(n):
#             add[row] += 1
#             last -= 1
#             if last == 0:
#                 break
#     else :
#         for row in range(n):
#             add[row] += 1
#             last -= 1
#         for row in range(n-1, 0, -1):
#             add[row] += 1
#             last -= 1
#             if last <= 0:
#                 break   

#     for row in range(n):
#         if row == 0 or row == n-1:
#             add[row] += turn
#         else:
#             add[row] += turn*2

#     pos = 0    
#     for row in range(n):
#         code[row].extend(list(string[pos:pos+add[row]]))
#         pos += add[row]
#         if pos == len(string):
#             break

#     ans = ''    
#     pos = 0
    
#     while True :
#         for cnt in range(n*2 - 2):
#             if pos == len(string):
#                 break            
#             if cnt < n :
#                 ans += ''.join(code[cnt][0])
#                 del code[cnt][0]
#             else:
#                 ans +=''.join(code[n*2 - cnt -2][0])
#                 del code[n*2 - cnt -2][0]
#             pos += 1

#         if pos == len(string):
#             break            
#     return ans

def decode_rail_fence_cipher(string, n):

	result = ""

	matrix = [["" for x in range(len(string))] for y in range(n)]

	idx = 0
	increment = 1

	for selectedRow in range(0, len(matrix)):
		row = 0

		for col in range(0, len(matrix[ row ])):
			if row + increment < 0 or row + increment >= len(matrix):
				increment = increment * -1

			if row == selectedRow:
				matrix[row][col] += string[idx]
				idx += 1
			
			row += increment
	
	matrix = transpose( matrix )
	for list in matrix:
		result += "".join(list)

	return result    
def transpose( m ):
	
	result = [ [ 0 for y in range( len(m) ) ] for x in range( len(m[0]) ) ]
	
	for i in range( len(m) ):
		for j in range( len(m[0]) ):
			result[ j ][ i ] = m[ i ][ j ]
	
	return result

# print('encode : ')
# print(encode_rail_fence_cipher("WEAREDISCOVEREDFLEEATONCE", 3))
# print(encode_rail_fence_cipher("Hello, World!", 3))
# print(encode_rail_fence_cipher("Hello, World!", 4))
# print(encode_rail_fence_cipher("", 3))

print('\ndecode : ')
print(decode_rail_fence_cipher("Amet non facere minima iure unde, provident,     veritatis officiis asperiores ipsa eveniet sit! Deserunt     autem excepturi quibusdam iure unde! Porro alias distinctio     ipsam iure exercitationem molestiae. Voluptate fugiat quasi maiores!jk", 9))
print(decode_rail_fence_cipher("H !e,Wdloollr", 4))
print(decode_rail_fence_cipher ("", 3))