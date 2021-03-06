import requests
import bs4

city = ""

def get_hotels_details(url):
    # print '#a#'
    html = requests.get(url)
    soup = bs4.BeautifulSoup(html.text, 'html.parser')
    # div.pos-relative.clearfix div.row div.col-s-16.col-m-12.pl0 div.row a.result-title.hover_feedback.zred.bold.ln24
    data = soup.select('h2.hero__byline--small span')
    # c = 0
    fo = open("OyoRoomsJson.txt", "a")
    for i in data:
        address = i.text.encode('ascii', 'ignore')
        if not address:
            address = "Unavailable"
        newstr = '\"Address\": \"' + address + '\",}'
        fo.write(newstr)
    fo.write("\n")
    fo.close()
    return


def get_hotels(url):
    # print '#a#'
    html = requests.get(url)
    soup = bs4.BeautifulSoup(html.text, 'html.parser')
    # div.pos-relative.clearfix div.row div.col-s-16.col-m-12.pl0 div.row a.result-title.hover_feedback.zred.bold.ln24
    data = soup.select('div.hotelcard__caption-details.mdl-cell.mdl-cell--8-col div.mdl-cell.mdl-cell--12-col a')
    new_url = 'https://www.oyorooms.com'
    for i in data:
        fo = open("OyoRoomsJson.txt", "a")
        name = i.text.encode('ascii', 'ignore')
        if not name:
            name = "Unavailable"
        name = name.replace('\n','')
        newstr = '{\"Name\": \"' + name + '\",'
        fo.write(newstr)
        a = i.get('href')
        newstr2 ='\"HotelUrl\": \"' + new_url + a + '\",'
        if not newstr2:
            newstr2 = "Unavailable"

        fo.write(newstr2)
        city = '\"Address\": \"' + city + '\",}'
        fo.write(city)
        fo.close()
        get_hotels_details(new_url + a)

    return


ch = ['Agra', 'Ahmedabad', 'Ajmer', 'Alappuzha', 'Alibag', 'Aligarh', 'Allahabad', 'Alwar', 'Ambala', 'Amritsar',
      'Asansol', 'Aurangabad', 'Baddi', 'Bandipur', 'Bangalore', 'Bareilly', 'Bathinda', 'Bhilai', 'Bhilwara',
      'Bhiwadi', 'Bhopal', 'Bhubaneswar', 'Bikaner', 'Bilaspur', 'Bodhgaya', 'Bukit-Mertajam', 'Calicut',
      'Cameron-Highlands', 'Chamarajanagar', 'Chandigarh', 'Chennai', 'Chikmagalur', 'Coimbatore', 'Coonoor', 'Coorg',
      'Corbett-Ramnagar', 'Cuttack', 'Dalhousie', 'Daman', 'Darjeeling', 'Dehradun', 'Delhi', 'Deoghar', 'Dewas',
      'Dharamshala', 'Digha', 'Diu', 'Durg', 'Dwarka', 'Faridabad', 'G', 'Gandhinagar', 'Gangtok', 'Ghaziabad', 'Gir',
      'Goa', 'Golubathan', 'Gulmarg', 'Gurgaon', 'Guruvayur', 'Guwahati', 'Gwalior', 'Haldwani', 'Haridwar', 'Hisar',
      'Hospet', 'Hubli-Dharwad', 'Hyderabad', 'Indore', 'Ipoh', 'Jabalpur', 'Jaipur', 'Jaisalmer', 'Jalandhar', 'Jammu',
      'Jamshedpur', 'Jhansi', 'Jharsuguda', 'Jodhpur', 'Johor-Bahru', 'Kalimpong', 'Kannur', 'Kanpur', 'Kanyakumari',
      'Karnal', 'Kasauli', 'Kashipur', 'Kasol', 'Katra', 'Kausani', 'Kaziranga', 'Khajuraho', 'Khandala', 'Kochi',
      'Kodaikanal', 'Kolhapur', 'Kolkata', 'Kollam', 'Kota', 'Kota-Kinabalu', 'Kovalam', 'Kuala-Lumpur', 'Kumbakonam',
      'Kurnool', 'Lachung', 'Langkawi', 'Lansdowne', 'Leh-Ladakh', 'Lonavala', 'Lucknow', 'Ludhiana', 'Madurai',
      'Mahabaleshwar', 'Mahabalipuram', 'Malacca', 'Manali', 'Mandarmoni', 'Mangalore', 'Matheran', 'Mathura',
      'Mcleod-Ganj', 'Meerut', 'Mehsana', 'Mirik', 'Mount-Abu', 'Mukteshwar', 'Mumbai', 'Munnar', 'Mussoorie',
      'Muzaffarpur', 'Mysore', 'Nagpur', 'Nainital', 'Nashik', 'Neemrana', 'Nellore', 'Noida', 'Ooty', 'Pachmarhi',
      'Pahalgam', 'Palampur', 'Panipat', 'Patiala', 'Patna', 'Pelling', 'Penang-Island', 'Petaling-Jaya', 'Pondicherry',
      'Pune', 'Puri', 'Pushkar', 'Putrajaya', 'Raipur', 'Rajkot', 'Rameshwaram', 'Ranchi', 'Ranikhet', 'Ranthambore',
      'Ratnagiri', 'Rishikesh', 'Rohtak', 'Rudrapur', 'Salem', 'Saputara', 'Seremban', 'Shah-Alam', 'Shillong',
      'Shimla', 'Shirdi', 'Siliguri', 'Somnath', 'Srinagar', 'Surat', 'Surathkal', 'Thanjavur', 'Thekkady', 'Thrissur',
      'Tirupati', 'Tiruppur', 'Trichy', 'Trivandrum', 'Udaipur', 'Udupi-Manipal', 'Ujjain', 'Vadodara', 'Varanasi',
      'Vijayawada', 'Visakhapatnam', 'Vrindavan', 'Warangal', 'Wayanad']
for i in ch:
    base_url = 'https://www.oyorooms.com/oyos-in-'
    url = base_url + i
    get_hotels(url)
    city=ch
	# for i in range(1,3):
# base_url = 'https://www.oyorooms.com/oyos-in-delhi'
# end_url = '?page='
# url = base_url + end_url+str(i+1)
# z = z + get_hotels(url)
