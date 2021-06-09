import requests
from bs4 import BeautifulSoup
import time
from sender import send_email
checked_news = []

def vkparser(url = 'https://vk.com/mgame'):
	while True:
		time.sleep(300)
		res = requests.get(url)
		soup = BeautifulSoup(res.text, 'lxml')
		print(soup.title.text)
		text_information = [information.text for information in soup.find_all(attrs = 
			                                                               {'class' : 'pi_text'})]
		for topic in text_information:
			if 'Series X' in topic and topic not in checked_news:
				print(f'///Какая-то новая инфа про коробоксы в группе:///\n {topic}')
				print('Направляю email о новой информации...')
				send_email('nilov1235@mail.ru', 'XBOX', topic)
				checked_news.append(topic)
			else:
				print('Нет упоминания xbox в темах на странице или уведомление уже отправлено')

if __name__ == '__main__':
	vkparser()
