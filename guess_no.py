


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

'''
down = 1
up = 100
'''

down = int(input('請輸入下限  '))
up = int(input('請輸入上限  '))
count = 1

r = random.randint(down, up)

guess_down = down
guess_up = up


print('\n系統隨機產生了一個', down, '至', up, '的數字，估中有獎\n')


while True:
	time.sleep(1)
	
	print('\n依家範圍係 ', guess_down, '至', guess_up, '\n')
	time.sleep(0.5)

	if guess_down == guess_up:
		print('無扮野喇，得返一個冧巴，冧巴溫啊你，快啲中左佢算啦\n')
	elif guess_up - guess_down < 15:
		print('得幾個數字，中硬啊你\n')

	time.sleep(0.5)
	print('係第 ', count, ' 次估！\n\n')
	time.sleep(0.5)

	guess = int(input('請輸入你估的數字。  '))
	print('\n\n')
	time.sleep(0.5)

	'''if guess == guess_down or guess_up:
		print('玩野？這個數字猜過了\n ')'''
	if guess < down:
		print('估咁細！落地獄啊你！  ', guess_down, '至', guess_up, ' 啊豬頭，再估過\n ')
	elif guess > up:
		print('估到出宇宙丫笨！ ', guess_down, '至', guess_up, ' 啊豬頭，再估過\n ')

	elif guess < guess_down:
		print('無腦架？仲估細啲？再估過\n ')
	elif guess > guess_up:
		print('無腦架？仲估大啲？再估過\n ')
	

	elif guess == r:
		print('估中了！！ 利害！！')
		break
	elif guess > r:
		print('太大了，再估\n')
		count = count + 1
		guess_up = guess - 1
	elif guess < r:
		print('太細了，再估\n')
		count = count + 1
		guess_down = guess + 1
	else:
		print('輸入數字啦')



'''
#執行用
python3 guess_no.py

#更新版本用
git add guess_no.py
git commit -m "加多左顯示方式"
git push origin main
'''