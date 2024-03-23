import webbrowser
import random

url_list = [
    'http://microteaching.ntu.edu.tw:9002/GestaltViewer?wlGUID=yNO51LX9wz8hAJCaGlnsKZTqWNdCie%2bIGyLnXNpAdqEXkE45s3K1f4yUjLAcKDgujpoFDog9IUKkTUeehVQzRls9DJX3yor3oxGlSECkybTO%2bta0fHePFFPS99lyEfemnAaCbe850Rw%3d',
    'http://microteaching.ntu.edu.tw:9002/GestaltViewer?wlGUID=Dqy2EPpxU7q25JQDuQO6vcbBfUF5wjrJ46lat7QyMn7p4ZdCI1jcT%2fz6YjqTlIrjz%2f4Pj%2b0YQ0e9TDH5JKjaN0St%2bqNlYpertfNTELVcTkt1il91WenVvetnvQn4cpqltQS70M7iHmU%3d',
    'http://microteaching.ntu.edu.tw:9002/GestaltViewer?wlGUID=ZvuJ8hnPGMSDS8lYwDYvr5lcYTe1Sw%2fvuxvwIIU8oFPjcZczUsLh2VNpMwZ2Nq%2beWUuY29duqkY38BKGTqFveUr44kq0ssbRGhMxZ8K3tJuJohSBdCHSplmsFyr%2fxxuLH6eP%2bkuZG3I%3d',
    'http://microteaching.ntu.edu.tw:9002/GestaltViewer?wlGUID=pU5lGZ8FxezubjtR0D2Ds9NnlnksDnbPnBU%2bPNixupZdrQDXk1hGFnI2bzbC3LAX6APckZVOu%2b3LLMKg3%2b1Z%2fDS2k0XAMwPnE9uuGridJwGjRf0BIdYCeAC7YMIUN0dN06%2fJDRDzHsI%3d',
    'http://microteaching.ntu.edu.tw:9002/GestaltViewer?wlGUID=UD1bhmLOkpL4zur%2bBB3%2bj25VFYUTwkctklySECWZQ973Bsuz9zf5BD0uauTgA3XxLah1qLTZACjIKkAz6JdAFDV25tIl5i4I2UNqaRas3HMTEFniF0pjMHh6oC6ZhIiqfHeLqQwV8tg%3d',
    'http://microteaching.ntu.edu.tw:9002/GestaltViewer?wlGUID=6GeCDG1kjIJa1lsF8q5PU8YtF49yrrKRlnML3OB0Pbz805q1pEZ6GDNuz2Pd1tMV3StMwm36qy2V%2ffbqEMiKjTL7gg1BKNVCEQMDrC1Gs30sfRNKtedNj5Ektj3%2bwtTKgkFQwIaBx1U%3d',
    'http://microteaching.ntu.edu.tw:9002/GestaltViewer?wlGUID=FYQK0tllBi%2fUxTQJWWrygEOoJT41e7I1iU2%2bj1cUj%2f35MMAQf07gzO1DhH21I86oJ%2b9eWqfgyJZfYLX%2bsRLxs7HK6%2buVAAdMxIeCkFqCb07zsEQihzucbyW8qYYjZnBNPnat%2bFZUsRM%3d',
    'http://microteaching.ntu.edu.tw:9002/GestaltViewer?wlGUID=DlUykyhmyzKLLTKkJ1M95fom4n7m02CnGTFogaO6D8hEjamtnuUWsFlM9c3H0l%2blk2TIaefFtRAokaCsOBygmdFi%2fnZzI0Xh3OLXJ%2foDxaAyFFB2LVLS%2bhcaq3%2b9fw1oAo45GWZdkT8%3d',
    'http://microteaching.ntu.edu.tw:9002/GestaltViewer?wlGUID=GGYubnLJOILeLxYTBIAvsdhGLvvWrBz6m2jo7rAg7Sk9fUT5LLGK%2bY5ecN84Tf%2f%2bdJBjFNlbzV3dObdLlK2srVLzXhalWxjfQVtE4j6JbP4Z51iv6vZDYLlOVZdMrcSgouIrcJchoAU%3d',
    'http://microteaching.ntu.edu.tw:9002/GestaltViewer?wlGUID=OlghWW5r2b76ySVaZGF66p9TvhlK7wy2a2U2%2bO40qIGWgTZkZeNZ0SQMG%2fcGHLmarsPG27EY1F3b14QVou98BUOo6YP6Wb3HYddGH4r%2fFRcakvpuIzE%2bbd0Qgommr5qQopjr3tR122g%3d',
    'http://microteaching.ntu.edu.tw:9002/GestaltViewer?wlGUID=vO7Cm6fPJ4hf5s2xr%2fBSaqEaJ6ihM7%2fqjHklRvjPhCD6Ls4oCU0A5tPyGL1GUy4kAXrF4kEngO5cBFPLf3oADTOzNfi3ASZ%2byClNhAXa84pfey6%2ff1QZ4peT9o7ONUy9KfUEGR1AE08%3d',
    'http://microteaching.ntu.edu.tw:9002/GestaltViewer?wlGUID=mQHey%2fWcKJslofuSbOXNxRmDJhufvbTqgAQhe2bMIxswcjcgGdaDsls7DWQnlCj1a8O98l2JzUQTVqX1oQnrCMtL3O%2bUxYRYzxpBYlYYUd2jHeJ2SQgDCxwuB9HykmT%2bBe0VlwpPI%2bE%3d',
    'http://microteaching.ntu.edu.tw:9002/GestaltViewer?wlGUID=ELRT1%2bq%2fo3iP9noHkb9teavC24fm2FIYWCkI1FyoXc3drD41spv6fKfPca4L7CDnc3xaWyJia4LGr6WT5N8FnqJTeet0x8OF2L8arB0IhPGBgR1gMJU%2bcwi8OO3ZHer3S1NBVrkkvU0%3d',
    'http://microteaching.ntu.edu.tw:9002/GestaltViewer?wlGUID=virBvO18i3%2b5fyqIlyJtr44fj9FGMfXT9OrwloplmtqCgJ4v3l7%2bPHtJWIn0kllxFde4DWDHrjKLMRHtlMukz8RMaQWdEK1JIHQR%2fDiC5sh3UI72kP5kxdhmiyNsTfhL9aoR%2byuFQC8%3d',
    'http://microteaching.ntu.edu.tw:9002/GestaltViewer?wlGUID=NYgubckS8FZVYtzC8ALidK9BPNFnPLJLE45CYuF2PoVU7EJAjGuhfAZ7kOlamX1DYzswjbb%2fygPplAlaKNFxa90YH1KbgU1fe%2bN4ihjhhusgc8taWj8Jl3FTGKyEWCWa45SfKsgJ9CM%3d',
    'http://microteaching.ntu.edu.tw:9002/GestaltViewer?wlGUID=jyob6RoX7I88BUVW15wmRCPwa6WQflM8jh4%2f14ItU9tcTpJFlJj9UsLZUExnGvBiXSguScDib%2bpMPhJhMWKqxTWDqOqltvi5yEHrl43VDajwKZZf%2fzVOuslvSNivRLoP8o0R23LLqjM%3d',
    'http://microteaching.ntu.edu.tw:9002/GestaltViewer?wlGUID=Mrj0kU%2blod7ltENrIzPJqaT2ObTmUG2INh15j2NmT42ltHWkq2GJU8SZImcjZfEloMjHSV2PJzMRi6RyazBcmAffOajH%2b7cbRBKGUGkhmzLqNFmYaUQfpypztAxH56Zb8aMjbJdhRPU%3d',
    'http://microteaching.ntu.edu.tw:9002/GestaltViewer?wlGUID=xo6zBx5zUF7Im%2bZl9HgCqN4vS%2bElUOcaMTcUYp2aPq5f5C6pJHZN2CmjFhMLEmbqtlWrwW8m6zAQxke8OLKyxXCDdyaIOlZHG34cSpUHusW0CjCgfWaTay2ZisRTk%2buojUWtDlKkLro%3d',
    'http://microteaching.ntu.edu.tw:9002/GestaltViewer?wlGUID=sqtlohTdjIomhsbuiIqMGomceQD7NjYSUOqhP57KwmPkDf2NBvIW8QqExG2tlDHYc%2f3Id1ACpLe0Mu7ne5Osj%2fM9bG8DCU7qeqLez5YwVUVEDkDHvOHzGIwlC%2bPzGFRANmX1Efr%2bqRU%3d',
    'http://microteaching.ntu.edu.tw:9002/GestaltViewer?wlGUID=LwbSERI1xRhHuwDX8Y9p8JeAhpGrd%2bzER17z137Mg%2bJYg7tddEHbYERyRfh3O0DJESzgy%2faSN8zA7jiuWn9oScyVvF722Z0OJjKFB5HbAxNBnelQU9sCBQMTpxcYvgMwXolgLP4oOIQ%3d',
    'http://microteaching.ntu.edu.tw:9002/GestaltViewer?wlGUID=fra8dYE3FMEDTcfP4AIUmmkCyWq%2fTKnMfX9RGwLm6zq3tp6iB%2bjMSDCi8JY%2bzMk8zpFFgEZEG4w7Iyx3ZOnVjZiInrCNlUFjyW5AjBoHnE8vwQZIMtqnUZDiGFnEMiGY4H0MeEqipsc%3d',
    'http://microteaching.ntu.edu.tw:9002/GestaltViewer?wlGUID=3eL13CjlpCBZPFJXlGtv9jG40mPdF14GV13itde9wxHSAVbwyPSro9MH%2bsVVVGXyIpJQxND7Dmn8hSrKRCNyg0tYSxthf7GUJGxc%2fpsysXF%2blq%2f4hqWqNuGl5VPGlow8CKEa9Vsq2FE%3d',
    'http://microteaching.ntu.edu.tw:9002/GestaltViewer?wlGUID=929k13%2b%2buCEg8EKSvZOaZxVpPjw8ybL%2fkKGVNTMs0PWYoG6LalIjJQwVSaKp%2bl35kKTLZ1HJiqD%2bbyON0fM0BZYVk3%2bt%2f3BD9it10B151gTHN8BErWYOM6PbGpFMcefpjm1owDOkARk%3d',
    'http://microteaching.ntu.edu.tw:9002/GestaltViewer?wlGUID=E31HiWhMNWFFr5U%2btRkH2GBmBDjHPYTup%2bfWGFlp9FtOXqVf%2bGLnbYc598oyVRETRtjoYtGdCu5fSz5EF5%2brqiqCkoG%2b4DIqRRb%2b6X7UBcf1lgyOzHgDjxipbTPWj44IZ5aaZG6hVQA%3d',
    'http://microteaching.ntu.edu.tw:9002/GestaltViewer?wlGUID=aIWlGy8rUuJBvvUwZ%2bc0NH8uG%2fmG64od00pxWjWw1FN6jSBs86NXyFpjZgtXr4mFhHFksCajq9hNWF15m26JdjwdhIwpD9PqBE4i46PUuCvhbCH5Nie8qurM3gsIig2RWT7yAJjfyyo%3d',
    'http://microteaching.ntu.edu.tw:9002/GestaltViewer?wlGUID=aIWlGy8rUuJBvvUwZ%2bc0NH8uG%2fmG64od00pxWjWw1FN6jSBs86NXyFpjZgtXr4mFhHFksCajq9hNWF15m26JdjwdhIwpD9PqBE4i46PUuCvhbCH5Nie8qurM3gsIig2RWT7yAJjfyyo%3d',
    'http://microteaching.ntu.edu.tw:9002/GestaltViewer?wlGUID=for%2f6SUIgCX%2f9xcuTYh%2b3HVNq4kehov3mvYLdVAVpGRkcRaGDq7H7NDBzUXtK8GTHcPrqoIqxzQ%2fotpaAIL9doRIbuBIEoblCeqE9GANY8L5V4n%2bkpubqwp1z2GxUYUJjotgeKuvMfs%3d',
    'http://microteaching.ntu.edu.tw:9002/GestaltViewer?wlGUID=XBt%2f3Ua%2b4QyDdB%2bW6PwH00eCbltWkFCNp66RVCDAWOcQxS30EX%2fG%2bFtyI6fVwtIox6EHUzCALQSKOju0dNenyda8re2Amq2HdmHFEjVT%2bEui7YPgK8rvCfhp9Sw1XJ2fzft%2fMfWapD0%3d',
    'http://microteaching.ntu.edu.tw:9002/GestaltViewer?wlGUID=N4%2fZxgPoTLvJF01OpPFZ04sp3WlYckohw615peuDdzSpk1pUmMO8%2bZO5Xd%2bEfvY6qAUyU5tvJ%2fNUZ4%2fpFfd5m0sb3ctK4h4ERpLuIdQOPsVOgmAtObjH9GSjZ1f60%2bUsmqFNN23M3jw%3d',
    'http://microteaching.ntu.edu.tw:9002/GestaltViewer?wlGUID=CMI9FbNGolC52Gz8sDC7eVqg43GIkO%2ffVwSd5n8kBpYVlHFUW1AdXWdrnJzIqK7i8ZtKEjk%2bvouWKoZ%2f9Grtv2fAb%2fnVohi6VkUFzitGdrQ2J1x08rMO7JL3ijhdcNMNTlr7mTcCgZ4%3d',
    'http://microteaching.ntu.edu.tw:9002/GestaltViewer?wlGUID=q9IIbTaV1w8M%2f3lp57VJQmRrBcM7%2bKffG2IjkszcAWtJkmJEJm3dZ8eK5M%2fEXSJlqeIjEgyj3BngM1tKgGEveeVAk%2bckdlKBaqPGC7QWkE2B8mYRKgUE9QUVnnyLbXDgTftwBHU1c0M%3d',
    'http://microteaching.ntu.edu.tw:9002/GestaltViewer?wlGUID=87fujVNhNqWLTkEtfb2Q0ZH9p77MhQ19wWJI071%2bM%2b7VbToKyadZzYrDRPufI1IbQx%2f2wa25iOzgAvINJZY22U8IPffUSNl5Ias0jYGc%2boC%2biRQVWMs%2fCuDmnDdEQKm7%2fwaUAe8IsP8%3d'
]


ans_list = [
    'invasive urothelial carcinoma; 83M; urinary bladder',
    'clear cell renal cell carcinoma; 53M; right kidney',
    'prostate adenocarcinoma; 57M; prostate',
    'Prostate adenocarcinoma',
    'seminoma; 31M; testis',
    'adenomyosis; 49F; uterus',
    'endometriosis; 37F; ovary',
    'endometriosis; 30F; ovary',
    'tubal pregnancy; 35F; fallopian tube',
    'complete hydatidiform mole; 23F; uterus',
    'complete hydatidiform mole; 45F; uterus',
    '(1)choriocarcinoma; (2)adenomyosis; 38F; uterine corpus',
    'mucinous cystadenoma; 52F; left ovary',
    'endometrioid adenocarcinoma; 61F; uterus',
    'clear cell carcinoma; 51F; Ovary',
    'high grade serous carcinoma ; 49F; right ovary',
    'dysgerminoma; 32F; ovary',
    'yolk sac tumor; 5F; ovary',
    'yolk sac tumor; 5F; ovary',
    'Yolk sac tumor; ovary',
    'adult granulosa cell tumor; 68F; Ovary',
    'fibrocystic change; 47F; breast',
    'fibroadenoma; 27F; breast',
    '(1)invasive carcinoma of no special type; (2)ductal carcinoma in situ, high grade; 49F; breast',
    '(1)invasive carcinoma of no special type; (2)ductal carcinoma in situ, low grade; 53F; breast',
    'invasive carcinoma of no special type, low grade; breast',
    'invasive lobular carcinoma; breast',
    'Breast invasive lobular carcinoma',
    'chronic pyelonephritis; kidney',
    'malignant nephrosclerosis; kidney',
    'autosomal dominant polycystic kidney disease; kidney',
    'autosomal recessive polycystic kidney disease; kidney'
]


number = list(range (32))
print ('Let\'s start! 32 cases in total.')
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

    
    

