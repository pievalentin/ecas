import random
import re
import time
from datetime import datetime

import click
import requests
from bs4 import BeautifulSoup


def generate_header(referer: str):
    headers = {
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Sec-GPC': '1',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Referer': f'{referer}',
        'Accept-Language': 'en-US,en;q=0.9',
    }
    return headers


@click.command()
@click.argument('lastname', type=click.STRING)
@click.argument('iuc_identifier', type=click.INT)
@click.argument('birthday', type=click.DateTime(formats=["%Y-%m-%d"]))
@click.argument('birth_country_code', type=click.STRING)
@click.option('--fast', default=False, is_flag=True, help="Remove waiting time between call. To use sparsly!")
def list_ecas_steps(lastname: str, iuc_identifier: int, birthday: str, birth_country_code: str, fast: bool):
    """A CLI tool to retrieve the status of ECAS \n
    Arguments: \n
        LASTNAME: Your lastname capitalized\n
        IUC_IDENTIFIER: Your IRCC IUC number \n
        BIRTHDAY: Your birthday in the format YYYY-MM-DD \n
        BIRTH_COUNTRY_CODE: Find your country code on ECAS. For France: 022 \n
    Example: \n
        ecas Dupont 43957930 "2000-01-01" 022
    """
    with requests.Session() as s:
        # 1 Pass intro page
        headers = generate_header(
            'https://services3.cic.gc.ca/ecas/introduction.do?app=')
        s.get(
            'https://services3.cic.gc.ca/ecas/security.do', headers=headers)

        # 2 Validate security
        if not fast:
            time.sleep(random.choice([1, 2]))
        headers = generate_header(
            'https://services3.cic.gc.ca/ecas/security.do')
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['Origin'] = 'https://services3.cic.gc.ca'
        data = {
            'lang': '',
            'app': '',
            'securityInd': 'agree',
            '_target1': 'Continue'
        }

        s.post(
            'https://services3.cic.gc.ca/ecas/security.do', headers=headers, data=data)

        # 3 Send info to get to user page
        if not fast:
            time.sleep(random.choice([10, 7, 6]))
        headers = generate_header(
            'https://services3.cic.gc.ca/ecas/authenticate.do')
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['Origin'] = 'https://services3.cic.gc.ca'

        data = {
            'lang': '',
            '_page': '_target0',
            'app': '',
            'identifierType': '1',
            'identifier': f'{iuc_identifier}',
            'surname': f'{lastname}',
            'dateOfBirth': f'{datetime.strftime(birthday,"%Y-%m-%d")}',
            'countryOfBirth': f'{birth_country_code}',  # 022
            '_submit': 'Continue'
        }

        response3 = s.post(
            'https://services3.cic.gc.ca/ecas/authenticate.do', headers=headers, data=data)

        status = ''.join(BeautifulSoup(
            response3.text, 'html.parser').td.next_sibling.next_sibling.a.text.split())

        # 4 Click on the link to see detail of PR
        if not fast:
            time.sleep(random.choice([1, 2]))
        headers = generate_header(
            'https://services3.cic.gc.ca/ecas/viewcasestatus.do')

        rp_id = re.search("(?:id=)(\d*)(?:&+?)", BeautifulSoup(response3.text,
                          'html.parser').td.next_sibling.next_sibling.a['href']).group(1)
        params = (
            ('id', f'{rp_id}'),
            ('type', 'prCases'),
            ('source', 'db'),
            ('app', ''),
            ('lang', 'en'),
        )

        response4 = s.get(
            'https://services3.cic.gc.ca/ecas/viewcasehistory.do', headers=headers, params=params)

    click.echo(f'Your status is: {status} \n')
    click.echo('The detail of your process is:')
    for li in BeautifulSoup(response4.text, 'html.parser').find_all('li', class_='mrgn-bttm-md'):
        click.echo(f'- {li.string}')


if __name__ == '__main__':
    list_ecas_steps()
