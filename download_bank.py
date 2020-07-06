from selenium import webdriver


def download_bank():
    driver = webdriver.Chrome(r"C:\Users\z003tcpp\PycharmProjects\SeleniumTest\Browsers\chromedriver.exe")
    driver.get('https://www.fundsindia.com/registration/signin')
    #driver.maximize_window()
    email = input('enter email id   :')
    driver.find_element_by_id('email').send_keys(email)
    pwd = input('enter Password :')
    driver.find_element_by_name('pwd').send_keys(pwd)
    driver.find_element_by_css_selector("button[class='btn btn-primary btn-qsignin']").click()
    driver.implicitly_wait(20)
    dob = input('enter Date of Birth :')
    driver.find_element_by_name('dobOrPan').send_keys(dob)
    driver.find_element_by_id('btn_confirm').click()
    driver.find_element_by_link_text('Reports').click()
    driver.find_element_by_link_text('Excel downloads »').click()
    driver.find_element_by_css_selector("[class='btn btn-primary']").click()
    driver.implicitly_wait(20)

    print('File downloaded......?')


download_bank()