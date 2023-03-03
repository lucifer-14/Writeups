# Mission 6

You only need to have some cryptography knowledge to crack this.

**Note:** Do not give up and keep entering different passwords to see the changes

<details>
  <summary> Reveal Basic Cryptography Knowledge </summary>
  
  In this section, I will explain about how messages are encrypted. This is just the surface of what cryptography actually is and what I am going to explain is the very basic concept of encryption and decryption.

  (Before that, you also need to understand what ASCII is. If you already know what that is, feel free to skip this part)<br>
  **[ASCII](https://en.wikipedia.org/wiki/ASCII):** ASCII is the most common character encoding standard. For example, a number '65' or '0100 0001' binary represents an uppercase character 'A'. There is a corresponding number for any character. But, why do we need a standard? There are multiple vendors across the world. If different vendors uses different kind of encoding method, the products made by them will not be able to understand each other.

  **How Encryption Works:** To encrypt a message there are basically two requirements. The first requirement is a message to encrypt and the second is an encryption algorithm. Encryption algorithm can be anything. For example, addition or subtraction. The message is processed using encryption algorithm and the output will be **encrypted** message.
  
  **Example Encryption:** Let's say that we will encrypt a message 'ABC'. According to ASCII standard, they represent number '65', '66', and '67'. The encryption algorithm is addition of 10 to each character. So the encrypted output will be '75', '76', '77'. According to ASCII, these number represent 'KLM'. Therefore, we can get the encrypted message of 'KLM'.

  **How Decryption Works:** To decrypt the encrypted message 'KLM', we need to reverse the encryption algorithm. Since we already know the encryption algorithm, we can simply decrypt it by subtracting 10 to each character. And the decrypted message will be "ABC".
  
  This is just the most simple example of how encryption and decryption works. This simple concept is necessary to crack this.
</details>

---

<details>
  <summary> Reveal Hint </summary>
  
  **Hint:** Try typing 'aaa' and observe how many numbers are added to each character.
  
</details>

---

<details>
  <summary> Reveal Answer </summary>
  
  **Answer:** You can see that the first character is added by 0, the second character is added by 1, the third is added by 2 and so on. To decrypt, you simply need to subtract each character by their index value.

  <details>
  <summary>Reveal for Dummies</summary>

  **For Dummies:** If you can't understand the above explanation, I don't know how else to explain anymore.

  </details>
  
</details>

---

<details>
  <summary> Reveal Python Script </summary>
  
  ```python
  def decrypt(data: str) -> str:
    res = ""
    for i, c in enumerate(data):
      tmp = chr(ord(c) - i)
      res += tmp
    return res


  if __name__ == "__main__":
    data = str(input("Enter the encrypted message: "))
    print(f"Result: {decrypt(data)}")
  ```
  
</details>

---

[<< Previous](../Mission%205/) &nbsp;&nbsp;|&nbsp;&nbsp; [Next >>](../Mission%207/)
