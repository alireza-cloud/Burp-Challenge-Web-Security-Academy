The email parameter in the following request is vulnerable to OS command injection:  

![grafik](https://user-images.githubusercontent.com/62068604/234102918-8f608371-9593-4533-8864-b048ea20776d.png)  

use the following OS command to trigger a 10 sec delay:  

`|sleep+10|` or `||ping+-c+10+127.0.0.1||`  

![grafik](https://user-images.githubusercontent.com/62068604/234103840-407dbc8e-fee6-4068-a822-791e4df8270c.png)  

or  

![grafik](https://user-images.githubusercontent.com/62068604/234103668-ae2d496d-5ced-4c48-b5ed-1d3e7caa086b.png)
