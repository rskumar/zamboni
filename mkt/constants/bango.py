# -*- coding: utf8 -*-
from tower import ugettext_lazy as _


# From page 10 of the Mozilla Exporter API docs v1.0.0
BANGO_OUTPAYMENT_CURRENCIES = [
    ('USD', _(u'US Dollars')),
    ('GBP', _(u'Pounds Sterling')),
    ('EUR', _(u'Euros')),
]

BANGO_CURRENCIES = [
    ('AUD', _(u'Australian Dollars')),
    ('CAD', _(u'Canadian Dollars')),
    ('CHF', _(u'Swiss Francs')),
    ('COP', _(u'Colombian Pesos')),
    ('DKK', _(u'Danish Krone')),
    ('EGP', _(u'Egyptian Pound')),
    ('EUR', _(u'Euros')),
    ('GBP', _(u'Pounds Sterling')),
    ('IDR', _(u'Indonesian Rupiah')),
    ('MXN', _(u'Mexican Pesos')),
    ('MYR', _(u'Malaysian Ringgits')),
    ('NOK', _(u'Norwegian Krone')),
    ('NZD', _(u'New Zealand Dollars')),
    ('PHP', _(u'Philippine Peso')),
    ('QAR', _(u'Qatar Riyal')),
    ('SEK', _(u'Swedish Kronor')),
    ('SGD', _(u'Singapore Dollars')),
    ('THB', _(u'Thai Baht')),
    ('USD', _(u'US Dollars')),
    ('ZAR', _(u'South African Rand')),
]

BANGO_CURRENCIES_KEYS = [x[0] for x in BANGO_CURRENCIES]

BANGO_COUNTRIES = [
    ('AFG', _(u'Afghanistan')),
    ('ALA', _(u'Åland Islands')),
    ('ALB', _(u'Albania')),
    ('DZA', _(u'Algeria')),
    ('ASM', _(u'American Samoa')),
    ('AND', _(u'Andorra')),
    ('AGO', _(u'Angola')),
    ('AIA', _(u'Anguilla')),
    ('ATA', _(u'Antarctica')),
    ('ATG', _(u'Antigua and Barbuda')),
    ('ARG', _(u'Argentina')),
    ('ARM', _(u'Armenia')),
    ('ABW', _(u'Aruba')),
    ('AUS', _(u'Australia')),
    ('AUT', _(u'Austria')),
    ('AZE', _(u'Azerbaijan')),
    ('BHS', _(u'Bahamas')),
    ('BHR', _(u'Bahrain')),
    ('BGD', _(u'Bangladesh')),
    ('BRB', _(u'Barbados')),
    ('BLR', _(u'Belarus')),
    ('BEL', _(u'Belgium')),
    ('BLZ', _(u'Belize')),
    ('BEN', _(u'Benin')),
    ('BMU', _(u'Bermuda')),
    ('BTN', _(u'Bhutan')),
    ('BOL', _(u'Bolivia')),
    ('BES', _(u'Bonaire, Saint Eustatius and Saba')),
    ('BIH', _(u'Bosnia and Herzegovina')),
    ('BWA', _(u'Botswana')),
    ('BVT', _(u'Bouvet Island')),
    ('BRA', _(u'Brazil')),
    ('IOT', _(u'British Indian Ocean Territory')),
    ('BRN', _(u'Brunei Darussalam')),
    ('BGR', _(u'Bulgaria')),
    ('BFA', _(u'Burkina Faso')),
    ('BDI', _(u'Burundi')),
    ('KHM', _(u'Cambodia')),
    ('CMR', _(u'Cameroon')),
    ('CAN', _(u'Canada')),
    ('CPV', _(u'Cape Verde')),
    ('CYM', _(u'Cayman Islands')),
    ('CAF', _(u'Central African Republic')),
    ('TCD', _(u'Chad')),
    ('CHL', _(u'Chile')),
    ('CHN', _(u'China')),
    ('CXR', _(u'Christmas Island')),
    ('CCK', _(u'Cocos (Keeling) Islands')),
    ('COL', _(u'Colombia')),
    ('COM', _(u'Comoros')),
    ('COG', _(u'Congo')),
    ('COD', _(u'Congo, Democratic Republic')),
    ('COK', _(u'Cook Islands')),
    ('CRI', _(u'Costa Rica')),
    ('CIV', _(u"Côte d'Ivoire")),
    ('HRV', _(u'Croatia')),
    ('CUB', _(u'Cuba')),
    ('CUW', _(u'Curaçao')),
    ('CYP', _(u'Cyprus')),
    ('CZE', _(u'Czech Republic')),
    ('DNK', _(u'Denmark Do')),
    ('DJI', _(u'Djibouti')),
    ('DMA', _(u'Dominica')),
    ('DOM', _(u'Dominican Republic')),
    ('ECU', _(u'Ecuador')),
    ('EGY', _(u'Egypt')),
    ('SLV', _(u'El Salvador')),
    ('GNQ', _(u'Equatorial Guinea')),
    ('ERI', _(u'Eritrea')),
    ('EST', _(u'Estonia')),
    ('ETH', _(u'Ethiopia')),
    ('FLK', _(u'Falkland Islands (Malvinas)')),
    ('FRO', _(u'Faroe Islands')),
    ('FJI', _(u'Fiji')),
    ('FIN', _(u'Finland')),
    ('FRA', _(u'France')),
    ('GUF', _(u'French Guiana')),
    ('PYF', _(u'French Polynesia')),
    ('ATF', _(u'French Southern Territories')),
    ('GAB', _(u'Gabon')),
    ('GMB', _(u'Gambia')),
    ('GEO', _(u'Georgia')),
    ('DEU', _(u'Germany')),
    ('GHA', _(u'Ghana')),
    ('GIB', _(u'Gibraltar')),
    ('GRC', _(u'Greece')),
    ('GRL', _(u'Greenland')),
    ('GRD', _(u'Grenada')),
    ('GLP', _(u'Guadeloupe')),
    ('GUM', _(u'Guam')),
    ('GTM', _(u'Guatemala')),
    ('GGY', _(u'Guernsey')),
    ('GIN', _(u'Guinea')),
    ('GNB', _(u'Guinea-Bissau')),
    ('GUY', _(u'Guyana')),
    ('HTI', _(u'Haiti')),
    ('HMD', _(u'Heard and McDonald Islands')),
    ('VAT', _(u'Holy See (Vatican City State)')),
    ('HND', _(u'Honduras')),
    ('HKG', _(u'Hong Kong')),
    ('HUN', _(u'Hungary')),
    ('ISL', _(u'Iceland')),
    ('IND', _(u'India')),
    ('IDN', _(u'Indonesia')),
    ('IRN', _(u'Iran, Islamic Republic of')),
    ('IRQ', _(u'Iraq')),
    ('IRL', _(u'Ireland')),
    ('IMN', _(u'Isle of Man')),
    ('ISR', _(u'Israel')),
    ('ITA', _(u'Italy')),
    ('JAM', _(u'Jamaica')),
    ('JPN', _(u'Japan')),
    ('JEY', _(u'Jersey')),
    ('JOR', _(u'Jordan')),
    ('KAZ', _(u'Kazakhstan')),
    ('KEN', _(u'Kenya')),
    ('KIR', _(u'Kiribati')),
    ('PRK', _(u"Korea, Democratic People's Rep")),
    ('KOR', _(u'Korea, Republic of')),
    ('KOS', _(u'Kosovo')),
    ('KWT', _(u'Kuwait')),
    ('KGZ', _(u'Kyrgyzstan')),
    ('LAO', _(u"Lao People's Democratic Rep")),
    ('LVA', _(u'Latvia')),
    ('LBN', _(u'Lebanon')),
    ('LSO', _(u'Lesotho')),
    ('LBR', _(u'Liberia')),
    ('LBY', _(u'Libyan Arab Jamahiriya')),
    ('LIE', _(u'Liechtenstei')),
    ('LTU', _(u'Lithuania')),
    ('LUX', _(u'Luxembourg')),
    ('MAC', _(u'Macao')),
    ('MKD', _(u'Macedonia, Former Yugoslav Rep')),
    ('MDG', _(u'Madagascar')),
    ('MWI', _(u'Malawi')),
    ('MYS', _(u'Malaysia')),
    ('MDV', _(u'Maldives')),
    ('MLI', _(u'Mali')),
    ('MLT', _(u'Malta')),
    ('MHL', _(u'Marshall Islands')),
    ('MTQ', _(u'Martinique')),
    ('MRT', _(u'Mauritania')),
    ('MUS', _(u'Mauritius')),
    ('MYT', _(u'Mayotte')),
    ('MEX', _(u'Mexico')),
    ('FSM', _(u'Micronesia, Federated States of')),
    ('MDA', _(u'Moldova, Republic of')),
    ('MCO', _(u'Monaco')),
    ('MNG', _(u'Mongolia')),
    ('MNE', _(u'Montenegro')),
    ('MSR', _(u'Montserrat')),
    ('MAR', _(u'Morocco')),
    ('MOZ', _(u'Mozambique')),
    ('MMR', _(u'Myanmar')),
    ('NAM', _(u'Namibia')),
    ('NRU', _(u'Nauru')),
    ('NPL', _(u'Nepal')),
    ('NLD', _(u'Netherlands')),
    ('NCL', _(u'New Caledonia')),
    ('NZL', _(u'New Zealand')),
    ('NIC', _(u'Nicaragua')),
    ('NER', _(u'Niger')),
    ('NGA', _(u'Nigeria')),
    ('NIU', _(u'Niue')),
    ('NFK', _(u'Norfolk Island')),
    ('MNP', _(u'Northern Mariana Islands')),
    ('NOR', _(u'Norway')),
    ('OMN', _(u'Oman')),
    ('PAK', _(u'Pakistan')),
    ('PLW', _(u'Palau')),
    ('PSE', _(u'Palestinian Territory, Occupied')),
    ('PAN', _(u'Panama')),
    ('PNG', _(u'Papua New Guinea')),
    ('PRY', _(u'Paraguay')),
    ('PER', _(u'Peru')),
    ('PHL', _(u'Philippines')),
    ('PCN', _(u'Pitcairn')),
    ('POL', _(u'Poland')),
    ('PRT', _(u'Portugal')),
    ('PRI', _(u'Puerto Rico')),
    ('QAT', _(u'Qatar')),
    ('REU', _(u'Réunion')),
    ('ROU', _(u'Romania')),
    ('RUS', _(u'Russian Federation')),
    ('RWA', _(u'Rwanda')),
    ('BLM', _(u'Saint Barthélemy')),
    ('SHN', _(u'Saint Helena')),
    ('KNA', _(u'Saint Kitts and Nevis')),
    ('LCA', _(u'Saint Lucia')),
    ('MAF', _(u'Saint Martin')),
    ('SPM', _(u'Saint Pierre and Miquelon')),
    ('VCT', _(u'Saint Vincent and the Grenadines')),
    ('WSM', _(u'Samoa')),
    ('SMR', _(u'San Marino')),
    ('STP', _(u'Sao Tome and Principe')),
    ('SAU', _(u'Saudi Arabia')),
    ('SEN', _(u'Senega')),
    ('SRB', _(u'Serbia')),
    ('SCG', _(u'Serbia and Montenegro')),
    ('SYC', _(u'Seychelles')),
    ('SLE', _(u'Sierra Leone')),
    ('SGP', _(u'Singapore')),
    ('SXM', _(u'Sint Maarten (Dutch part)')),
    ('SVK', _(u'Slovakia')),
    ('SVN', _(u'Slovenia')),
    ('SLB', _(u'Solomon Islands')),
    ('SOM', _(u'Somalia')),
    ('ZAF', _(u'South Africa')),
    ('SGS', _(u'South Georgia and the South Sandwich Islands')),
    ('SSD', _(u'South Sudan')),
    ('ESP', _(u'Spain')),
    ('LKA', _(u'Sri Lanka')),
    ('SDN', _(u'Sudan')),
    ('SUR', _(u'Suriname')),
    ('SJM', _(u'Svalbard and Jan Mayen')),
    ('SWZ', _(u'Swaziland')),
    ('SWE', _(u'Sweden')),
    ('CHE', _(u'Switzerland')),
    ('SYR', _(u'Syrian Arab Republic')),
    ('TWN', _(u'Taiwan, Province of China')),
    ('TJK', _(u'Tajikistan')),
    ('TZA', _(u'Tanzania, United Republic of')),
    ('THA', _(u'Thailand')),
    ('TLS', _(u'Timor-Leste')),
    ('TGO', _(u'Togo')),
    ('TKL', _(u'Tokelau')),
    ('TON', _(u'Tonga')),
    ('TTO', _(u'Trinidad and Tobago')),
    ('TUN', _(u'Tunisia')),
    ('TUR', _(u'Turkey')),
    ('TKM', _(u'Turkmenistan')),
    ('TCA', _(u'Turks and Caicos Islands')),
    ('TUV', _(u'Tuvalu')),
    ('UGA', _(u'Uganda')),
    ('UKR', _(u'Ukraine')),
    ('ARE', _(u'United Arab Emirates')),
    ('GBR', _(u'United Kingdom')),
    ('USA', _(u'United States')),
    ('UMI', _(u'United States Minor Outlying Islands')),
    ('URY', _(u'Uruguay')),
    ('UZB', _(u'Uzbekistan')),
    ('VUT', _(u'Vanuatu')),
    ('VEN', _(u'Venezuela, Bolivarian Republic of')),
    ('VNM', _(u'Vietnam')),
    ('VGB', _(u'Virgin Islands, British')),
    ('VIR', _(u'Virgin Islands, U.S.')),
    ('WLF', _(u'Wallis and Futuna')),
    ('ESH', _(u'Western Sahara')),
    ('YEM', _(u'Yemen')),
    ('ZMB', _(u'Zambia')),
    ('ZWE', _(u'Zimbabw')),
]
