driving = input('請問你有沒有開過車？')
if driving != '有' and driving != '沒有':
	print('只能輸入 有/沒有')
	raise SystemExit
age = input('請問你的年齡？')
age = int(age)
if driving == '有':
	if age >= 18:
		print('原來你考過駕照了！水哦！')
	else:
		print('你該不會無照駕駛吧？')
elif driving == '沒有':
	if age >= 18:
		print('那你什麼時候才要去考？')
	else:
		print('沒關係 再過幾年就能考駕照了！')
