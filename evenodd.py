s = input()
even = odd = 0
for i in range(len(s)):
	if i%2 ==0 :
		odd += int(s[i])
	else:
		even += int(s[i])


print("YES" if even-odd %11 == 0 else "NO")

s, t = input(), input()
if (t == s[::-1]) :
	print("YES")
else:
	print("NO")
