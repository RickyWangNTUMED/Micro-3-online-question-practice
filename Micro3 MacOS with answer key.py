import webbrowser
import random

url_list = [
'http://microteaching.ntu.edu.tw:9002/GestaltViewer?wlGUID=e4e1472YnCVC%2b7r6j2ZH4yDJ3oP32rBFi1NtHJhfyRrmXvtcMcmvGj3IsENSxG8IjygYhvSIHxaOl6S5vmKwJ1aEG5bNmsR1KAsfADEztfwknuJknqj2rTsRzfOUtaPa4FLb2ytA8b8%3d',
'http://microteaching.ntu.edu.tw:9002/GestaltViewer?wlGUID=AT4H7PfZcz%2fTimvWML91cJb0eMJ3C0XIAWFYNj8wU8rR5nHKKJnqYsYRdkPj28TOACnXASohf%2f5tMnqOzxD%2b1hKuvnIUjvp7TEmq8fuk%2b7cI7uo2K9WQAY5NkXd6te0VV%2fKvJrmDORQ%3d',
'http://microteaching.ntu.edu.tw:9002/GestaltViewer?wlGUID=ndCIU1bVIvZc0KNtUoRjzOQB48JN4S2EmMnhZYNv9UIZq62KH7nSrt6YmTV991Y9l6Fxy6BenP9opso0GPmF3rsyX%2bs8dnXSzQku900GCxIe4NGOfzmxqugJ1fJMvHsf4%2b3ES91BcW4%3d',
'http://microteaching.ntu.edu.tw:9002/GestaltViewer?wlGUID=iIdQdPfyG1qRa4ET3X9XbMmC7UGpVgRhV%2bsP%2fGPe95Swm5KKAnchM5nLsodoK7Ip3IDtsOu3CYQwBrVvr2Xc8jSU2rsVR1jkrZWVNZ9vth3hQCVzBa6qKwHYfARMXSCV9FHh8E%2btMRs%3d',
'http://microteaching.ntu.edu.tw:9002/GestaltViewer?wlGUID=7JJ5cCmCloRzO0VXEJ5J23udtwC0R7%2fmC1pMnNsnPqUobgP8hXBYOthlnKrXbYH5qmtjzKH4H7BTBAFCIXFyQAR6TywQ6MbYiKvETq%2fI21WHdYBfK6Z0L3w9ppYw%2brY0TEwYKWBm0fA%3d',
'http://microteaching.ntu.edu.tw:9002/GestaltViewer?wlGUID=CTa1ojxN1u%2bUvrlBbUPqKFyCUgM8IGkFJ7UbZHZ8q5VSWBT%2fnRngiZRQK5kWd8xw8pgcJLws9Pq62fVf7w%2bgP4K5TC3%2bQED%2fnb9Op%2f9L4pdDRqZPDT0LJE7m%2fNabZMbHSr3%2f1r7hHLc%3d',
'http://microteaching.ntu.edu.tw:9002/GestaltViewer?wlGUID=B4oan3yW1ro%2bQCnf6PgkvjsAsd3XdxfRVGNOI%2fUnzSGD6eDLqq%2bbrJ0Y95Iy57o64M9RoVHqzwKw%2bcT%2bhan%2bl19fJCSSmzwrdJ0g%2fBNnSd22V7szQYdtgPKb%2biZM5mEchfyxyCK0jms%3d',
'http://microteaching.ntu.edu.tw:9002/GestaltViewer?wlGUID=ZF7178dMY5TN9kxrtb0emLH%2fo033c4M9XsKsNv1SKjyOVn8Gv2dnvC8OaEnKbv0fmLjHsuGxSotYp79M6%2bxaP99C7nC9w%2fbHANSu%2bWfIgevj7oTJTMTAIS5Foo4JdgywQeYJS28RwK8%3d',
'http://microteaching.ntu.edu.tw:9002/GestaltViewer?wlGUID=KaI8Z%2fzQw%2bVCJREK%2bc1h29nrm%2fQGrwPgHBfb1Ul72HmrZiBWJlrBl0MfzKmHm%2f3RoOiFs7SJaY4VHSuyITC3fnkbjZtRr7pxBKjBtIyfDuF9oclHucNV3aIz4oxuuWyX1%2b9RMY12M5I%3d',
'http://microteaching.ntu.edu.tw:9002/GestaltViewer?wlGUID=GsyfL7BMU0fPpeTtDLdKL%2fwhQHTT%2fUYswFWB2pra5AEI%2fD5nrMyQL46cTMF6x5Z2hOQmzocH1XbDNp8F1WH%2bxW27hGu0m2ZN%2f%2bPCxTfKjtXvNWCvUNy1nEaz6%2bn6h7H%2bYqAyknvmbMk%3d',
'http://microteaching.ntu.edu.tw:9002/GestaltViewer?wlGUID=l7hmxOHYXb%2fubn8EKP1smKdb6ocEjVqZy6kpHCecZnVf5MWCrXKCaZh3987qe88pzZ%2fAJNwPBTaIxUpsyL9PmbPbq1Mjz%2buc0t9diPstfFXVd8oGrtKK%2fNy1T3r7Bem3BpXq9yIDHoI%3d',
'http://microteaching.ntu.edu.tw:9002/GestaltViewer?wlGUID=9FWXK4O0hgBtUTLsEb9ItaLhXQSNqcr%2bkHMkXBmX2gJnAnYJ3My1GhP67JRXDcyGChv7884KKvrY%2fWX0qikzod1txUrQ73YePffnY6jUEniI6%2bwxCLUwH%2bO5A%2bKhfGQ9Rl0OwL70O%2b0%3d',
'http://microteaching.ntu.edu.tw:9002/GestaltViewer?wlGUID=dAhJwFoiHDf968YFfjSzeh6SPYn65N%2bd89XbHS0PPjdyBHuAnw8P3hX4ln8Bu9awy87J6BfQX2cZqZ3ufxA0a812YvibYxr55AS%2ftCho%2fvZaKCiTUdP6H%2f8kt3qvGVLBf6fU%2bXgHJsU%3d',
'http://microteaching.ntu.edu.tw:9002/GestaltViewer?wlGUID=jnoMXkK9QTSXkAYH15kDqarf%2f%2bIvWMjLDEsjSKajWFyGCvBDI7OJ5MWmDOfJczaeSnDZ2Bjyeb6x2xvSsihxzipPIwvpId2o4U9GGDe57p8n7insNUBxaw3sz4wAvJGuCqKL7Pem98w%3d',
'http://microteaching.ntu.edu.tw:9002/GestaltViewer?wlGUID=y3we1vSiVWL4YBBkfB11md1TE7yoTGzhlvoMbo2S%2bOBBSI8ELECUQKcgGShbnaPCYehQ56FaT1X7%2f8XF%2bSqzagClqKFtNPq7KdDFXAcBhcxpI69XgTFnLybrRVS5mtLVwsNdZkJRdPo%3d',
'http://microteaching.ntu.edu.tw:9002/GestaltViewer?wlGUID=M4XVTucChiFQGOZeT1pd9Wu042vM0b0m3j1qsQ72%2b0mtpa1ucfClwCZ2ZtKXaiGeFyT89SkHu%2bEaghT8rEXSBQy%2b%2fKDZy4m6t8lbcyc3Itthj8B8V0d4t0j3%2fvwtOZdbMALtG1Nft9o%3d',
'http://microteaching.ntu.edu.tw:9002/GestaltViewer?wlGUID=cGk7Y86neF4MGNjvJX1im3LTGysoFdcEG%2fUjhsIyfBxSHXUW74VXmG8%2bM6zbgovfyDkn1Esl8eVuzGy3c3yyMGZWy7r43XR0H9FOPczJymxYjwU%2bokcZZzvRKkvWkdQ65XAr865Kwpk%3d',
'http://microteaching.ntu.edu.tw:9002/GestaltViewer?wlGUID=qR2sIRPZVOI85edzJqIRvVYx0%2bhhWcXAOQdowSf8qqZJc1IHnh3ZlyAfrxhM12KFKdEI9NhwaMIJomy75Qguls%2fFYHremvI2Dhhvn8lmrqrVx1QIR2qemZ33WK71Xi82b2Gue0jD8ZU%3d',
'http://microteaching.ntu.edu.tw:9002/GestaltViewer?wlGUID=rSBPZdbIREv4vJzQGZ6jsI%2fx62Sw8mFqsG1sJFyCIMD09ubfO9IW%2fsYtlRvNAEIFe5WILyffjboVkD3h%2b9DMLacULAWaccYElIUblb%2btQKVzKzizEDs5ZEw6%2bgK9LgmoTFG%2fAarfybg%3d',
'http://microteaching.ntu.edu.tw:9002/GestaltViewer?wlGUID=gisCNl5dSTkg1IcDIZ30sRx2Aio9FiZzNmPwKqxIzIHoRJS808z9Bo5x2hWcueCWGbNMOcyoKSYCvKWqoCZhPX0yZIFMPrnWJxiLghiUpC1ZKIBCfFqkVPrzxFSXEr76KIhP57K%2biQA%3d',
'http://microteaching.ntu.edu.tw:9002/GestaltViewer?wlGUID=4A%2bKfgFEfzjrkAreQbvuxQLHKxG6W6sq3xNmvmFVwfrckRnH04%2bm1Fs0cHzPTG5nx7kTz6HQsSkNAsMIlByMseddZ8fvax%2bOwc5uYFXmW2Wi4SJI55PeWlZz4hjTdAQujijOa80%2bHLY%3d',
'http://microteaching.ntu.edu.tw:9002/GestaltViewer?wlGUID=li6bMZ4%2fEFnIn5P5CPBZ6%2fRuzmBTQ3rAvRN6s2onGc1705xlB%2bzPwb5L5sVM6%2fu07h5U%2fkZx62yGxt8IIlfqsaJc%2fFM%2bqXlcBcCQCiN%2bb0HiNZKQEHfJ515dhajdPJdGUaZ%2foMr%2bOsU%3d',
'http://microteaching.ntu.edu.tw:9002/GestaltViewer?wlGUID=jad%2fem3SkSY6GFpRossGwJiX7QV9qO17w1OXQZMUdd3i3tTSd0sK%2b6Xxgqg40K%2fF%2b0p%2bdfuDlwaizbQ6nuvFHsUi5algB1DR7pXSUlsfyFUEBOHP9eOJBmTYstU%2fQ6HVOHMjcsWkKMY%3d',
'http://microteaching.ntu.edu.tw:9002/GestaltViewer?wlGUID=%2fCR%2b2OMGj1Tx8LaCE%2b9YVgBPcjyuVvjHnq9295BrwCrI0avCgVYQ5a7%2bryXsN1McXpWYRsJ5JRwNL1pi8Hkb7DubqQyM6uJQ75R7EYxJjh8bGXl16sNM4p865hzWt66CPwzQb4mqi0M%3d',
'http://microteaching.ntu.edu.tw:9002/GestaltViewer?wlGUID=xHNn39%2bELkPQnu8jXUj%2f160rQhE9IunAH%2fbIpnR48Y%2biQEyXrJWDTa0Wkc%2fBIDKkhM8SCWMec%2feBRMhmj4GO4sqN3X3gakZxhpQUgM3u5L1OclMj432tisCz1evYFu3zGLAHJwRGR64%3d',
'http://microteaching.ntu.edu.tw:9002/GestaltViewer?wlGUID=USmFtnJr1MAdiA3qxI%2bQzb75aeDyAJ%2bY%2ftVcXvx9Drhx%2fGndfFTWzlhUa%2fhGzYYLm3iacfA8Q%2f0GMN%2fVXkypEMnzTCozQufaYy%2fqd9yQZh1fDCTZQeICYsw1XghDoe3Og0W3FEZEmhM%3d',
'http://microteaching.ntu.edu.tw:9002/GestaltViewer?wlGUID=EqJEclrAIXF%2ffbm2KAaMhWZstmmSFljyIIrxwv0iv2NWc2jQGR7Hp54a61cJ7fS1NisZBDg2rfbwOOhrhbtNKVKKhsGMjff5QRHvrt6s3Z%2fxNz67EFCisLDnpG7im6bwT3ABwIcNKYo%3d'
]

ans_list = [
    'PA0174 Adenocarcinoma, lung',
    'PA0021 Squamous cell carcinoma, lung',
    'PA0018 Small cell carcinoma, soft tissue',
    'PA0024 Bronchopneumonia, lung',
    'PA0040 Diffuse alveolar damage, lung',
    'PA0067 Focal nodular hyperplasia, liver',
    'PA0071 Hepatocellular carcinoma, liver',
    'PA0184 Cholangiocarcinoma, liver',
    'PA0060 Acute hepatitis, liver',
    'PA0281 Acute hepatitis, liver',
    'PA0183 Chronic hepatitis, liver',
    'PA0064 Submassive necrosis, liver',
    'PA0282 Submassive necrosis, liver',
    'PA0075 Cirrhosis, liver (caution! May combine HCC in test)',
    'PA0265 Primary biliary cholangitis, liver',
    'PA0283 Primary sclerosing cholangitis, liver',
    'PA0068 Primary sclerosing cholangitis, liver',
    'PA0078 Chronic cholecystitis, gallbladder',
    'PA0260 Nasopharyngeal carcinoma, nasopharynx',
    'PA0279 Adenocarcinoma, diffuse/signet ring cell type, stomach',
    'PA0048 Adenocarcinoma, diffuse/signet ring cell type, stomach',
    'PA0049 Adenocarcinoma, intestinal type, stomach',
    'PA0055 Neuroendocrine tumor, small intestine',
    'PA0080 Neuroendocrine tumor, pancreas',
    'PA0079 Chronic pancreatitis, pancreas',
    'PA0248 IgG4-related autoimmune pancreatitis, pancreas',
    'PA0007 Neuroendocrine tumor, lymph node'
]


number = list(range (27))
print ('Let\'s start! 27 cases in total.')
random.shuffle (number)
a = 1
x = input ()

for i in number:
    print ('Case' + str(a))
    a += 1
    webbrowser.get('safari').open(url_list[i])
    x = input ()
    print (ans_list[i])
    x = input ()
    if x == 'e':
        break
print ('Finished. Hope you will get an A+ on micro!')

    
    

