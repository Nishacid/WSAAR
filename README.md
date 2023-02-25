# Web Security Academy Auto-Recon (WSAAR)

Auto-Recon script that will help you in the [Burp Suite Certified Practitioner Exam](https://portswigger.net/web-security/certification) or with any [web-security lab](https://portswigger.net/web-security/all-labs).

Wordlists provided in [wordlists](./wordlists/) directory are these provided by **Web Security Academy** here : 

- [Username list](https://portswigger.net/web-security/authentication/auth-lab-usernames)
- [Password list](https://portswigger.net/web-security/authentication/auth-lab-passwords)

## 📖 A bit of story 

I created this tool for personal use, at the beginning of the certification when it was still only 3 hours for 6 challenges, because I was very short of time and I needed a tool that would make me recognize the labs to go faster. 
In **no way** my goal was to make a tool that was going to make me do labs automatically, that's why there is no payload in this script, it's only to save time on the reconnaissance related to labs.

I know, the code of this script is not perfect, as I said before I had made this script quickly as my own, I publish this code hoping to give a starting point to someone to make maybe something cleaner or to have a little tool to help with the reconnaissance. If you want to improve it, don't hesitate [to contribute](https://github.com/Nishacid/WSAAR/pulls)

If you want to know more about this certification and the process, I wrote an article here: https://nishacid.guru/articles/bscp/ .

## 🛠️ Installation

```bash
git clone https://github.com/Nishacid/WSAAR.git
cd WSAAR/
pip3 install -r requirements.txt
```

## ✔️ Usage 

```bash
» python3 wsaar.py -h
usage: wsaar.py [-h] --id HOST [--username USERNAME] [--password PASSWORD]

options:
  -h, --help            show this help message and exit
  --id HOST, -i HOST    Your Lab ID
  --username USERNAME, -u USERNAME
                        Username to login
  --password PASSWORD, -p PASSWORD
                        Password to login
```

## 🔎 Some Examples

### Example with Cross-Origin Ressource Sharing


```bash
» python3 wsaar.py --id 0ae7004d0475e2aec3077ab10088008a

     _          __  _____       ___       ___   _____
    | |        / / /  ___/     /   |     /   | |  _  \
    | |  __   / /  | |___     / /| |    / /| | | |_| |
    | | /  | / /   \___  \   / / | |   / / | | |  _  /
    | |/   |/ /     ___| |  / /  | |  / /  | | | | \ \
    |___/|___/     /_____/ /_/   |_| /_/   |_| |_|  \_\
    Web Security Academy Auto Recon
    @Nishacid


[*] General Check...
[+] Restricted Admin Panel found on /admin
[+] Exploit server avaliable on https://exploit-0a4200ad04abe23ac34279b001030015.exploit-server.net

[*] Login Check...
[+] There is a login page on /login
[*] CSRF Token required for login
[+] Successful login with default wiener:peter account
[*] Cookies are : {'session': 'bXjUemxcNF3x5IWpsYNNIUl4Jw9QNn50'}

[*] Account Informations
[+] Account Details found on /accountDetails
{
    "apikey": "heuXirXWmZi5EJsb7lu1RISDYgog19pP",
    "email": "",
    "sessions": [
        "bXjUemxcNF3x5IWpsYNNIUl4Jw9QNn50"
    ],
    "username": "wiener"
}
[+] Highly possible CORS due to Access-Control-Allow-Credentials Header in response

[*] Deserialization Check...

[*] CORS Check...

[*] Access Control Check...

[*] OAuth Check...

[*] LFI Check...

[*] File Upload Check...

[*] Business Logic Check...

[*] Information Disclosure Check...

[*] SQL Injection Check...

[*] SSRF Check...

[*] XXE Check...

[*] Web Cache Poisoning Check...

[*] XSS Check...

[*] HTTP Request Smuggling Check...

[*] WebSockets Check...

[*] Prototype Pollution Check...

Execution completed, good luck for the next steps :)
```

### Example with Web Cache Poisoning

```bash
» python3 wsaar.py --id 0afd00d5042b2017c02da98d00c3004a

     _          __  _____       ___       ___   _____
    | |        / / /  ___/     /   |     /   | |  _  \
    | |  __   / /  | |___     / /| |    / /| | | |_| |
    | | /  | / /   \___  \   / / | |   / / | | |  _  /
    | |/   |/ /     ___| |  / /  | |  / /  | | | | \ \
    |___/|___/     /_____/ /_/   |_| /_/   |_| |_|  \_\
    Web Security Academy Auto Recon
    @Nishacid


[*] General Check...
[+] Exploit server avaliable on https://exploit-0a620032040d20a9c0cca8ac01b600d4.exploit-server.net

[*] Login Check...
[+] There is a login page on /login
[*] CSRF Token required for login
[-] Default login doesn't work
[*] You can try to Bruteforce with the username and password provided in the ./wordlists/ folder

[*] Deserialization Check...

[*] CORS Check...

[*] Access Control Check...

[*] OAuth Check...

[*] LFI Check...

[*] File Upload Check...

[*] Business Logic Check...

[*] Information Disclosure Check...

[*] SQL Injection Check...

[*] SSRF Check...

[*] XXE Check...

[*] Web Cache Poisoning Check...
[+] Highly possible Web Cache Poisoning due to X-Cache Header in response
[+] Highly possible Web Cache Poisoning due to Cache-Control Header in response
[+] Possible Web Cache Poisoning due to script on /resources/js/tracking.js

[*] XSS Check...

[*] HTTP Request Smuggling Check...

[*] WebSockets Check...

[*] Prototype Pollution Check...

Execution completed, good luck for the next steps :)
```

### Example with custom creds

```bash
» python3 wsaar.py --id 0a42002c03fc3bdfc08c59b700f60004 --username atlas --password 131313

     _          __  _____       ___       ___   _____
    | |        / / /  ___/     /   |     /   | |  _  \
    | |  __   / /  | |___     / /| |    / /| | | |_| |
    | | /  | / /   \___  \   / / | |   / / | | |  _  /
    | |/   |/ /     ___| |  / /  | |  / /  | | | | \ \
    |___/|___/     /_____/ /_/   |_| /_/   |_| |_|  \_\
    Web Security Academy Auto Recon
    @Nishacid


[*] General Check...
[+] Leave a comment to a post functionality

[*] Login Check...
[+] There is a login page on /login
[+] Successful login with custom atlas:131313 account
[*] Cookies are : {'session': 'ejGFm9t9oqcLVzWaIBkOuGRbxn6JNNE8'}

[*] Account Informations

[*] Deserialization Check...

[*] CORS Check...

[*] Access Control Check...

[*] OAuth Check...

[*] LFI Check...

[*] File Upload Check...

[*] Business Logic Check...

[*] Information Disclosure Check...

[*] SQL Injection Check...

[*] SSRF Check...

[*] XXE Check...

[*] Web Cache Poisoning Check...

[*] XSS Check...

[*] HTTP Request Smuggling Check...

[*] WebSockets Check...

[*] Prototype Pollution Check...

Execution completed, good luck for the next steps :)
```

## 📝Todo list idea

- [ ] Add header argument to pass some cookies / HTTP headers
- [ ] Code cleaning 
- [ ] Improve login.py script (dirty)
- [ ] Add news labs / and missing vulnerabilities 
- [ ] Add carlos:montoya login check

## ❤️ Contributing

Pull requests are welcome. Feel free to contribute to complete these scripts or to make improvements.

You can contact me on Twitter [@Nishacid](https://twitter.com/Nishacid) or email [nishacid@protonmail.com](mailto:nishacid@protonmail.com).
