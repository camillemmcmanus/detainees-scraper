from bs4 import BeautifulSoup
from datetime import timedelta
import requests
import requests_cache
from time import sleep
from models import Detainees, Details
from peewee import DoesNotExist

requests_cache.install_cache(
    'cache',
    expire_after=timedelta(hours=24),
    allowable_methods=('GET', 'POST')
)

details_url = 'https://report.boonecountymo.org/mrcjava/servlet/RMS01_MP.R00040s?run=2&R001=&R002=&ID=126&hover_redir=&width=950'

def get_details_site():
	r = requests.get(
		details_url,
		headers = {'user-agent': "I'm good!"})

	r.raise_for_status()

	return r.content


def extract_detainee_info(details_site):
	soup = BeautifulSoup(details, 'lxml')


	find_detainees = soup.find_all('div', class_='detaineeInfo')


	for detainee in find_detainees:
		detainee_info_table = detainee.find('table', class_='collapse centered_table shadow')
		detainee_info = detainee_info_table.find_all('tr')

		data = {}

		for tr in detainee_info:
			key = tr.find('td', class_='one td_left').text.lower().strip()
			value = tr.find('td', class_='two td_left').text.strip()


			data[key] = value


		info = Detainees.create(**data)


def extract_details_info(details_site):
	soup = BeautifulSoup(details, 'lxml')

	all_charges = soup.find_all('div', class_='chargesContainer')

	for charge in all_charges:
		charge_table = charge.find('table', class_='collapse centered_table shadow responsive')
		tbody = charge_table.find ('tbody', class_='single')
		charges_trs = tbody.find_all('tr')

		for charges_tr in charges_trs:
			details_info_cells = charges_tr.find_all('td', class_='two td_left')


		Details.create(
			case_num = details_info_cells[0].text.strip(),
		    charge_description = details_info_cells[1].text.strip(),
		    charge_status = details_info_cells[2].text.strip(),
		    bail_amount = details_info_cells[3].text.strip(),
		    bond_type = details_info_cells[4].text.strip(),
		    court_date = details_info_cells[5].text.strip(),
		    court_time = details_info_cells[6].text.strip(),
		    court_of_jurisdiction = details_info_cells[7].text.strip()
		)


def main():
	details_site = get_details_site()
	extract_detainee_info(details_site)
	extract_details_info(details_site)






























