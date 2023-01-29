# 3D_wireframe_engine
A 3D wireframe engine written in python with the help of chat GPT

![image](https://user-images.githubusercontent.com/15731540/215316908-3d874beb-6a0f-4296-8a59-0a78a030c9be.png)

Just for the fun of it :

![image](https://user-images.githubusercontent.com/15731540/215331015-a25e1cb9-e086-4bc6-9ec0-7cfbf5dd8145.png)


Some shortcuts are not shown in the UI :
- alpha 1-2 : change sphere resolution
- alpha 3-4 : change sphere size
- Escape : quit

The whole thing started like that :

![image](https://user-images.githubusercontent.com/15731540/215317982-ee5db268-6376-4ed8-81fd-2bfd66b0f911.png)

Which is quite impressive!

Then after a few tries and reformulations it managed to create the functions needed to translate the 3D coordinates into 2D :

![image](https://user-images.githubusercontent.com/15731540/215318104-29dc1c56-076c-40ce-9658-0d2d52cbda23.png)

![image](https://user-images.githubusercontent.com/15731540/215318118-f27ef9a0-af5f-4951-b8b5-aa284591a37a.png)

![image](https://user-images.githubusercontent.com/15731540/215318127-1922d2a8-f453-4e72-9e53-86ac0761e34b.png)

chatGPT struggled with the function to create a sphere and would output functions that would create such things :

![image](https://user-images.githubusercontent.com/15731540/215317927-e38870cd-77ea-442c-bec0-93483291b3a3.png)

Until I asked it to create a sphere made of multiple circles of a diameter relative to their distance to the center.

I won't upload all of the conversations as I did many tries and chatGPT was under a heavy load. But overall it was more than impressive to see it so capable of understanding my requests and extrapolating things like how the coordinates and links were arranged in my initial unfinished shape. 
