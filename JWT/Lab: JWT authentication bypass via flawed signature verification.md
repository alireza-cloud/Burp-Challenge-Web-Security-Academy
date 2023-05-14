1. Try accessing the admin panel (/admin):

    ![image](https://github.com/alireza-cloud/Burp-Challenge-Web-Security-Academy/assets/62068604/9eaa1ab3-7540-430e-b378-a3fe35332319)

2. Changing the header and the payload of JWT:

    ***alg ---> to none***

    ![image](https://github.com/alireza-cloud/Burp-Challenge-Web-Security-Academy/assets/62068604/dc1179e7-68a5-4a45-8d68-4b5738e8daf1)

    ***sub ---> to administrator***

    ![image](https://github.com/alireza-cloud/Burp-Challenge-Web-Security-Academy/assets/62068604/6d0f5d7b-4299-4425-b417-aab5210ac4ae)

    ***deleting the signature from the token leaving the trailing dot***
 
    ![image](https://github.com/alireza-cloud/Burp-Challenge-Web-Security-Academy/assets/62068604/7a00a6ce-ffd7-4e62-95ad-64526e67dc8c)


3. Deleting the user Carlos via admin panel:

    ![image](https://github.com/alireza-cloud/Burp-Challenge-Web-Security-Academy/assets/62068604/5253dccf-cf5a-4d5d-abe7-0a6b962dd9a7)
