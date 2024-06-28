#!/usr/bin/env python
# coding: utf-8

# In[5]:


PIC="""$$$$$$\   $$$$$$\  $$$$$$$$\  $$$$$$\   $$$$$$\  $$$$$$$\         $$$$$$\  $$$$$$\ $$$$$$$\  $$\   $$\ $$$$$$$$\ $$$$$$$\  
$$  __$$\ $$  __$$\ $$  _____|$$  __$$\ $$  __$$\ $$  __$$\       $$  __$$\ \_$$  _|$$  __$$\ $$ |  $$ |$$  _____|$$  __$$\ 
$$ /  \__|$$ /  $$ |$$ |      $$ /  \__|$$ /  $$ |$$ |  $$ |      $$ /  \__|  $$ |  $$ |  $$ |$$ |  $$ |$$ |      $$ |  $$ |
$$ |      $$$$$$$$ |$$$$$\    \$$$$$$\  $$$$$$$$ |$$$$$$$  |      $$ |        $$ |  $$$$$$$  |$$$$$$$$ |$$$$$\    $$$$$$$  |
$$ |      $$  __$$ |$$  __|    \____$$\ $$  __$$ |$$  __$$<       $$ |        $$ |  $$  ____/ $$  __$$ |$$  __|   $$  __$$< 
$$ |  $$\ $$ |  $$ |$$ |      $$\   $$ |$$ |  $$ |$$ |  $$ |      $$ |  $$\   $$ |  $$ |      $$ |  $$ |$$ |      $$ |  $$ |
\$$$$$$  |$$ |  $$ |$$$$$$$$\ \$$$$$$  |$$ |  $$ |$$ |  $$ |      \$$$$$$  |$$$$$$\ $$ |      $$ |  $$ |$$$$$$$$\ $$ |  $$ |
 \______/ \__|  \__|\________| \______/ \__|  \__|\__|  \__|       \______/ \______|\__|      \__|  \__|\________|\__|  \__|
                                                                                                                            
                                                                                                                   """
print(PIC)
alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def encryption(plain_text,k):
    encrypted_text=""
    for i in plain_text:
        if i.isalpha():
            pos=alphabets.index(i)
            new_pos=(pos+k)%26
            encrypted_text+=alphabets[new_pos]
        else:
            encrypted_text+=i
    print(f"Here is the text after encryption {encrypted_text}")
        
def decryption(encrypted_text,k):
    plain_text=""
    for i in encrypted_text:
        if i.isalpha():
            pos=alphabets.index(i)
            new_pos=(pos-k)%26
            plain_text+=alphabets[new_pos]
        else:
            plain_text+=i
    print(f"Here is the text after decryption {plain_text}")
    
end_game=False
while not end_game:
    option=input("Type 'encrypt' for encryption,type 'decrypt' for decryption:")
    msg=input("Type your message:")
    k=int(input("Type the shift number:"))
    if option=='encrypt':
        encryption(msg,k)
    elif option=='decrypt':
        decryption(msg,k)
    else:
        print("Enter the valid option")
    play_again=input("Do you want to use this application again,Type 'yes' to continue,type 'no' to exit.\n")
    if play_again=='no':
        end_game=True
        print("***THANK YOU FOR USING THIS APPLICATION***")
    


# In[ ]:





# In[ ]:





# In[ ]:




