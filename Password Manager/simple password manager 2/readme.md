# Simple Password Manager 2.0
<div align="center">
  <img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExYmR0cHBhd3hmMXQ1eHN2N2YxdXRjOGlvdnllam1xaXl4b3VsNnFpMiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/AUMxbiDIzBOiFGA71r/giphy.gif" width="200"/>
</div>
<br/>

**Code report:**

On version 1.0, the password.txt file was being saved in the root directory. It may be confusing for some people, so I made it so, it is saved in the same directory as the codes. Upgraded the encryption for passwords. In version 1.0 the site name isn't encrypted, so that no malicious user can understand the the sites and encryptions easily. Also added username feature and made it compulsary input & if there is a password already saved for the same username it won't save the password again. Added a secret key generating code. So without the secret key no one can't acccess the passwords. Used 2 kinds of encryption for more security.

**How to Use:**
1. Download the directory `simple password manager 2`.
2. run `generate_key.py`. It will automatically create `secret.key` file in the directory.
3. run `main.py`. Enter `s` to store/save passwords | Enter `r` to retrieve the saved password | Enter `q` / `Ctrl + c` to quit the program.
