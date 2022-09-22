# 리스트 스크래핑 프로그램(List Scraping Program)
로그인 후 접근할 수 있는 웹페이지 내 테이블에서 필요한 데이터를 추출하여 CSV 파일로 저장하는 프로그램

---
## Usage
1. Clone this repository.
```git bash
git clone https://github.com/c2lv/ListScrapingProgram.git
```
2. Change directory and activate virtualenv.
```git bash
cd ListScrapingProgram
pip install virtualenv
virtualenv venv
source venv/Scripts/activate
```
3. Add constants values in `main.py`.
4. Install the requirements.
```git bash
pip install -r requirements.txt
```
5. Run `main.py`.
```git bash
python main.py
```
---
## Environment
- ChromeDriver
  - [Download link](https://chromedriver.storage.googleapis.com/index.html?path=105.0.5195.52)
  - ChromeDriver version: 105.0.5195.52
  - Chrome version: 105
  - Last modified: 2022-08-31 08:29:41
  - Size: 6.68MB
- Python
  - Version: 3.10.0
  - Framework: Selenium
- OS
  - Windows 10 64bit