


# using while function.

'''
while True:
	
	name = input('請輸入你的名字：  ')

	if name == 'q':
		print ('you can leave now')
		break
	else:
		print ('you cannot leave')

python3 password_test.py
'''


'''
true_password 放左 loop 外運算會較簡潔
思考，chance 減少，應在哪個行動後發生
chance 減少，應在輸入錯誤後發生，不是在每次輸入後發生。這確保輸入正確後，不會減少chance。

每次輸入password後，最先要驗證的，應該是password是否正確
之後才到其他行動

chance 每次減少，最先驗證的，應該是chance 是否已到0，到0要有相應行動。
未到0， 就給回應，再行loop。

每個if 的最後，留一個else，比較清晰齊整

'''

'''
true_password = 'alan'

chance = 2

print('你有 ', chance, ' 次輸入密碼機會')

while chance >= 0:

	password = input('請輸入密碼：  ')
	

	if true_password == password:
		print('密碼正確')
		break

	else:
		chance = chance - 1
		if chance == 0:
			print('還是錯誤了，goodbye~~~~~')
			#理論上，要跳到處理重覆錯誤 password 的 flow
			break
		else:
			print('不正確，請重試')
			print('你尚有 ', chance, ' 次機會')
'''

import random
import time

down = 1
up = 100
count = 0

r = random.randint(down, up)

print('系統隨機產生了一個', down, '至', up, '的數字，猜中有獎')

while True:
	
	guess = int(input('請輸入你猜的數字。  '))

	count = count + 1
	print('這是第 ', count, ' 次猜喔！\n\n')
	time.sleep(0.5)

	if guess == r:
		print('猜對了！！ 利害！！')
		break

	elif guess >= r:
		print('太大了，再猜\n')
	elif guess <= r:
		print('太細了，再猜\n')
	else:
		print('輸入數字啦')



'''
#執行用
python3 guess_no.py

#更新版本用
git add guess_no.py
git commit -m "basic version"
git push origin main
'''