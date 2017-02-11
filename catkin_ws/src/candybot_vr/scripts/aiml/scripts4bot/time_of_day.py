import time

def main():
	hour = int(time.ctime().split()[3].split(':')[0])
	if hour >= 4 and hour <=11:
		print('ДОБРОЕ УТРО')
	elif hour >=12 and hour <=16:
		print('ДОБРЫЙ ДЕНЬ')
	elif hour >= 17 and hour <= 23:
		print('ДОБРЫЙ ВЕЧЕР')
	else:
		print('ДОБРОЙ НОЧИ')
		
if __name__ == '__main__':
	main()
	
