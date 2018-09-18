# Free-slots
This python code scraps out the data from https://vtopbeta.vit.ac.in/vtop and logs in the user. After which scrapes out the free slots of the respective user. Benificial for clubs and chapters of VIT who need the free slots of the respective students. The coding practices followed is super childish so please bear with me.

### Requirement and steps
1. Selenium for python. A simple `pip install selenium` in your terminal will do.
2. Download <a href="https://chrome.google.com/webstore/detail/enhancer-for-vit-vellore/hafeeaangmkbibcaahfjdmmmeappjbbp">Enhancer for VIT Vellore Academics</a>. This is an excellent captcha solver for VTOPbeta. Also it is excellent tools for downloading various online material from VTOP in one click. (This solves the problem of solving captcha so we do not have to write extra lines of code or import some another python library that helps us to solve captcha)
3. Figure out the path of the extension which in my case was `C:/Users/Ambika/AppData/Local/Google/Chrome/User Data/Default/Extensions/hafeeaangmkbibcaahfjdmmmeappjbbp/2.4_0` and replace it.
