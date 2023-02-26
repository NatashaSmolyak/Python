# 4. Все emails, у которых есть слово test, вывести в другой список
# l = ['webtest1@gmail.com',
#      'alex_dr5@gmail.com',
#      'elena_viktorovna@gmail.com',
#      'infotest@gmail.com',
#      'sigmatesst@gmail.com',
#      'planet.dollsatest@gmail.com',
#      'loadtestsinfo@gmail.com',
#      'straightwaytest@gmail.com',
#      'test.of.tests@gmail.com',
#      'bigmac@gmail.com',
#      'bigmactest@gmail.com',
#      'kfc_test_supply@gmail.com',
#      'cyberdesk@gmail.com',
#      'supportonlinetest@gmail.com'
#      ]
l = ['webtest1@gmail.com', 'alex_dr5@gmail.com', 'elena_viktorovna@gmail.com', 'infotest@gmail.com',
     'sigmatesst@gmail.com', 'planet.dollsatest@gmail.com', 'loadtestsinfo@gmail.com', 'straightwaytest@gmail.com',
     'test.of.tests@gmail.com', 'bigmac@gmail.com', 'bigmactest@gmail.com', 'kfc_test_supply@gmail.com',
     'cyberdesk@gmail.com', 'supportonlinetest@gmail.com']
b = []
for i in l:
    if 'test' in i:
        b.append(i)
for i in b:
    print(i)