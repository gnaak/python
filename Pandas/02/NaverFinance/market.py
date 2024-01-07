import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

# chromedriver 자동 설치
chromedriver_autoinstaller.install()

# 크롬 브라우저 열기
browser = webdriver.Chrome()


browser.maximize_window()

# 1. 페이지 이동
url = 'https://finance.naver.com/sise/sise_market_sum.naver?&page='
browser.get(url)

# 2. 조회 항목 초기화 (체크되어 있는 항목 체크 해제)
checkboxes = browser.find_elements(By.NAME, 'fieldIds')
for checkbox in checkboxes:
    if checkbox.is_selected(): # 체크가 된상태라면,
        WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, checkbox.get_attribute('id'))))
        checkbox.click() # 클릭 (체크 해제)

# 3. 조회 항목 설정 (원하는 항목)
items_to_select = ['영업이익', '자산총계','매출액']
for checkbox in checkboxes:
    parent = checkbox.find_element(By.XPATH, '..') # 부모 element
    label = parent.find_element(By.TAG_NAME, 'label')
    print(label.text) # 이름 확인
    if label.text in items_to_select: # 선택 항목과 일치한다면
        checkbox.click()
    
# 4. 적용하기
btn_apply = browser.find_element(By.XPATH, '//a[@href="javascript:fieldSubmit()"]') 
btn_apply.click()

for idx in range(1,38):  # 1~40 미만 페이지 반복
    # 사전 작업 : 페이지 이동 
    browser.get(url+ str(idx))

    # 5. 데이터 추출
    df = pd.read_html(browser.page_source)[1]
    df.dropna(axis=0, how='all', inplace=True) # 행 기준 결측치 삭제
    df.dropna(axis=1, how='all', inplace=True) # 열 기준 결측치 삭제
    if len(df) == 0:
        break

    # 6. 파일 저장 
    f_name = 'sise.csv'
    if os.path.exists(f_name): # 파일이 있다면 헤더 부분은 제외
        df.to_csv(f_name, encoding='utf-8-sig', index=False, mode='a', header=False)
    else:  # 파일이 없다면 헤더 포함
        df.to_csv(f_name, encoding='utf-8-sig', index=False)

    print(f'{idx} 페이지 완료')

browser.quit()