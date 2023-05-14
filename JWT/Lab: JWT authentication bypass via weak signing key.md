1. Using ***Hashcat*** bruteforcing the secret key that is used to sign the JWT:  
 
    ***hashcat -a [attack mode = straight/ Dictionary] -m [hash-type = 16500 --> JWT] Token Path/to/wordlist.txt***  
    
    ![image](https://github.com/alireza-cloud/Burp-Challenge-Web-Security-Academy/assets/62068604/ebf46975-0d84-448b-a4e5-18e8ed1293bf)  

2. Signing the modified payload ***("sub":"administrator")*** with the bruteforced secret:  

    ![image](https://github.com/alireza-cloud/Burp-Challenge-Web-Security-Academy/assets/62068604/dfbf761d-8bee-4a71-8593-ab92a946434e)  

3. Deleting the user Carlos to solve the lab:  

    ![image](https://github.com/alireza-cloud/Burp-Challenge-Web-Security-Academy/assets/62068604/21a8263c-eb4e-40c1-b22d-092f0125ec3b)  
