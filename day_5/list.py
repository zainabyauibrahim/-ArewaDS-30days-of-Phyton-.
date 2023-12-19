list =  []

num = [' first', 'second', 'third','forth', 'fifth', 'sixth', 'seventh']

print(len(num))

first_num, a, b, middle_num, c, d, last_num, = num
print(first_num)     # banana
print(middle_num)    # berries
print(last_num)      # pawpaw

mixed_data_types = ["Zidan", 23, 45, 'single', 'kaduna']

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

print(mixed_data_types)
print(it_companies)

print(len(it_companies))

a,b,c,d,e,f,g = it_companies
print(a)
print(d)
print(g)

it_companies[0] = "MICROTIK"
print(it_companies)

it_companies.append('CISCO')
print(it_companies)

it_companies.insert( 3, 'NITDA')
print(it_companies)

it_companies[4] = it_companies[4].upper()
print(it_companies)

result = '#; '.join(it_companies)
print(result)

print(it_companies.index('Microsoft'))

it_companies.sort()
print(it_companies)

it_companies.reverse()
print(it_companies)

print(it_companies[:3])

print(it_companies[-1:-4:-1])

print(it_companies[4:5])

del it_companies[0]
print(it_companies)

del it_companies[4]
print(it_companies)

del it_companies[-1]
print(it_companies)

del it_companies[0:]
print(it_companies)

del it_companies

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
code = front_end + back_end

full_stack = code.copy()
print(full_stack)

new=['Python','SQL']
full_stack.insert(5, new)
print(full_stack)

# Exercises: Level 2

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()
print(ages)
print(max(ages))
print(min(ages))

ages.append(min(ages))
ages.append(max(ages))
print(ages)

ages.sort()
print(len(ages)) # gives the odd number of 12
median = ages[5:7] # slice the two middle items
print(median)
a,b = median
median = (a+b)/2
print(f"median is {median}")

mean = sum(ages) / len(ages)
print(f"mean of {ages} is {sum(ages)}/{len(ages)} \n mean = {mean}")

print(f"Range = {max(ages) - min(ages)}")


min_x = abs(mean - min(ages))
max_x = abs(mean - max(ages))

print(f"the difference between the min. and the average is {min_x}")
print(f"the difference between the max. and the average is {max_x}")

# Find the middle country(ies) in the countries list
country_list = countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]

def find_middle(lst): #Function to find the middle country
    if not lst:
        return "The list is empty."
    length = len(lst)
    if length % 2 != 0: # if the length is odd
        middle_index = length // 2
        return lst[middle_index]
    first_middle_index = length // 2 - 1 # firsth value if the length is even
    second_middle_index = length // 2 # fsecond value if the length is even
    return (lst[first_middle_index], lst[second_middle_index])

middle_country = find_middle(country_list)
print(middle_country)

def divide_lst(lst):
    if not lst:
        return "The list is empty."
    length = len(lst)
    if length % 2 != 0: # if the length is odd
        middle_index = length // 2
        list1 = lst[ : middle_index]
        list2 = lst[middle_index : ]
        print(list1)
        print(list2)
    else:
        first_middle_index = length // 2 - 1
        list1=lst[first_middle_index] 
        second_middle_index = length // 2 
        list2 =lst[second_middle_index]
        print(list1)
        print(list2)
print(divide_lst(country_list))

min_countries =['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
scandic_countries = min_countries[0:3]
print(scandic_countries)