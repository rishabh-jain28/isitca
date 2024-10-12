import requests
from bs4 import BeautifulSoup
import json

url = "https://gem.gov.in/view_contracts/contract_details"
headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://gem.gov.in',
    'Referer': 'https://gem.gov.in/view_contracts',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-GPC': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Brave";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

def fetch_contracts():
    page = 0
    all_contracts = {}

    while True:
        # Update the payload for the current page
        payload = f"fromDate=28-09-2024&toDate=08-10-2024&department=&bno=&buyer_category=&page={page}"
        
        # Fetch the data for the current page
        response = requests.request("POST", url, headers=headers, data=payload)
        soup = BeautifulSoup(response.text, 'html.parser')
        contract_blocks = soup.find_all('div', class_='border block')

        # If there are no contract blocks, it means we've reached the last page
        if not contract_blocks:
            print(f"No more contracts found on page {page}. Stopping.")
            break

        # Parse each contract block
        for block in contract_blocks:
            contract_number = block.find('span', class_='ajxtag_order_number').text.strip()
            all_contracts[contract_number] = {
                "contract_status": block.find('span', class_='ajxtag_order_status').text.strip(),
                "organization_type": block.find('span', class_='ajxtag_buyer_dept_org').text.strip(),
                "ministry": block.find_all('span', class_='ajxtag_buying_mode')[0].text.strip(),
                "department": block.find_all('span', class_='ajxtag_buying_mode')[1].text.strip(),
                "organization_name": block.find('span', class_='ajxtag_buyer_dept_org').text.strip(),
                "office_zone": block.find_all('span', class_='ajxtag_buying_mode')[2].text.strip(),
                "buyer_designation": block.find('span', class_='ajxtag_buyer_dept_org').text.strip(),
                "buying_mode": block.find_all('span', class_='ajxtag_buying_mode')[3].text.strip(),
                "contract_date": block.find('span', class_='ajxtag_contract_date').text.strip(),
                "total_value": block.find('span', class_='ajxtag_totalvalue').text.strip()
            }

        print(f"Contracts found on page {page}: {len(contract_blocks)}")

        # Move to the next page
        page += 1

    # Save all contracts to a JSON file
    with open('contracts.json', 'w', encoding='utf-8') as json_file:
        json.dump(all_contracts, json_file, indent=4, ensure_ascii=False)

    return all_contracts

# Fetch and save the contracts
contracts = fetch_contracts()
print(f"Total contracts fetched: {len(contracts)}")
