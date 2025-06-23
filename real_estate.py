from bs4 import BeautifulSoup
import requests
import lxml
import csv
import time
import random


# web_url = "https://www.magicbricks.com/property-for-sale/residential-real-estate?bedroom=1,4,5,%3E5,2,3&proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment,Residential-House,Villa,Residential-Plot&cityName=Bangalore&BudgetMin=5-Lacs&BudgetMax=20-Crores"
def web_scrapper(web_url,file_name):
    print("Thankyou for sharing web url and file name \n scrapping in progress...\n")
    time.sleep(random.randint(3,7))

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36'
    }

    response = requests.get(web_url, headers=headers)

    if response.status_code == 200:
        print('Successfully connected to the website', response.status_code)
        soup = BeautifulSoup(response.text, 'lxml')
        prop_divs = soup.find_all('div', class_='mb-srp__card')

        with open(f'{file_name}.csv','w',encoding='utf8', newline='') as file_csv:
            writer=csv.writer(file_csv)
            writer.writerow(['Title','Area sqft', 'Status', 'Transaction', 'Furnishing','Parking','Bathroom','Balcony','Price'])

            for prop in prop_divs:
                
                # Property name
                prop_name = prop.find('h2', class_='mb-srp__card--title')
                title = prop_name.text.strip() if prop_name else 'N/A'

                #Property Area
                area_row = prop.find('div', attrs={'data-summary': 'super-area'})
                area = area_row.find('div', class_='mb-srp__card__summary--value').text.strip() if area_row else 'N/A'

                #Status
                status_row=prop.find('div', attrs={'data-summary':'status'})
                status=status_row.find('div', class_='mb-srp__card__summary--value').text.strip() if status_row else 'N/A'

                #Transaction
                transaction_row = prop.find('div', attrs={'data-summary': 'transaction'})
                transaction = transaction_row.find('div', class_='mb-srp__card__summary--value').text.strip() if transaction_row else 'N/A'


                #Furnishing
                furnishing_row=prop.find('div',attrs={'data-summary':'furnishing'})
                furnishing=furnishing_row.find('div', class_='mb-srp__card__summary--value').text.strip() if furnishing_row else 'N/A'

                #Bthroom
                bathroom_row=prop.find('div', attrs={'data-summary':'bathroom'})
                bathroom=bathroom_row.find('div', class_='mb-srp__card__summary--value').text.strip() if bathroom_row else 'N/A'

                #Parking
                parking_row=prop.find('div', attrs={'data-summary':'parking'})
                parking=parking_row.find('div', class_='mb-srp__card__summary--value').text.strip() if parking_row else 'N/A'

                #Balcony
                balcony_row=prop.find('div', attrs={'data-summary':'balcony'})
                balcony=balcony_row.find('div', class_='mb-srp__card__summary--value').text.strip() if balcony_row else 'N/A'

                # Price
                price_row = prop.find('div', class_='mb-srp__card__price--amount')
                price = (
                            price_row.text.strip()
                            .replace('\u20b9', '')
                            if price_row else 'N/A'
                        )

                print(area)
                print(status)
                print(transaction)
                print(furnishing)
                print(bathroom)
                print(parking)
                print(balcony)
                print(price)
                print("-" * 60)

                writer.writerow([
                    title,
                    area,
                    status,
                    transaction,
                    furnishing,
                    parking,
                    bathroom,
                    balcony,
                    price
                ])
        print(f"\n✅ Data successfully saved in `{file_name}.csv`")

    else:
        print("Unable to connect with website:", response.status_code)


if __name__=='__main__':
    url=input('Enter your MagicBricks.com URL: ')
    file_name=input('Please enter your csv file name (without .csv): ')
    web_scrapper(url,file_name)
