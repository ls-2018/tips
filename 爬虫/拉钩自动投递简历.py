from selenium import webdriver
import time, os
import json

path = r'./utils/chromedriver.exe'
# 创建浏览器对象
browser = webdriver.Chrome(executable_path=path)

browser.get('https://www.lagou.com/')
if browser.find_elements_by_xpath('//*[@id="colorbox"]'):
    browser.find_elements_by_xpath('//*[@id="changeCityBox"]/ul/li[1]/a')[0].click()
    pass

browser.find_elements_by_xpath('//*[@id="lg_tbar"]/div/div[2]/div/a[1]')[0].click()
browser.find_elements_by_xpath('/html/body/div[3]/div[1]/div/div/div[2]/div[1]')[0].click()
time.sleep(5)
browser.get(
    'https://www.lagou.com/jobs/list_python?gj=3%E5%B9%B4%E5%8F%8A%E4%BB%A5%E4%B8%8B&px=default&yx=10k-15k&city=%E5%8C%97%E4%BA%AC#order')
# browser.get(
# 'https://www.lagou.com/jobs/list_%E8%BF%90%E7%BB%B4%E5%BC%80%E5%8F%91?px=default&gj=3%E5%B9%B4%E5%8F%8A%E4%BB%A5%E4%B8%8B&city=%E5%8C%97%E4%BA%AC#filterBox')
time.sleep(5)

title_list = list()
from openpyxl import Workbook
import datetime

wb = Workbook()
ws = wb.active
ws.append(['职位', '公司名字', '地点', '薪资', '投递链接'])


def init():
    for item in browser.find_elements_by_xpath('//*[@id="s_position_list"]/ul/li'):
        post = item.find_element_by_xpath('.//div[1]/div[1]/div[1]/a/h3').text  # 职位
        addr = item.find_element_by_xpath('.//div[1]/div[1]/div[1]/a/span/em').text  # 地点
        salary = item.find_element_by_xpath('.//div[1]/div[1]/div[2]/div/span').text  # 薪资
        post_link = item.find_element_by_xpath('.//div[1]/div[1]/div[1]/a')
        #  //*[@id="s_position_list"]/ul/li[1]/div[1]/div[1]/div[1]/a
        post_link = post_link.get_attribute('href')  # 投递链接
        company_name = item.find_element_by_xpath('.//div[1]/div[2]/div[1]/a').text  # 公司名字
        demo = {
            'post': post,
            'addr': addr,
            'salary': salary,
            'post_link': post_link,
            'company_name': company_name
        }
        print(demo)
        title_list.append(demo)

    next_flag = True

    while next_flag:
        next_page = browser.find_elements_by_xpath('//*[@id="s_position_list"]/div[2]/div/span')[-1]

        if 'pager_next_disabled' not in next_page.get_attribute('class'):
            next_page.click()
            time.sleep(1)
            for item in browser.find_elements_by_xpath('//*[@id="s_position_list"]/ul/li'):
                post = item.find_element_by_xpath('.//div[1]/div[1]/div[1]/a/h3').text  # 职位
                addr = item.find_element_by_xpath('.//div[1]/div[1]/div[1]/a/span/em').text  # 地点
                salary = item.find_element_by_xpath('.//div[1]/div[1]/div[2]/div/span').text  # 薪资
                post_link = item.find_element_by_xpath('.//div[1]/div[1]/div[1]/a')
                post_link = post_link.get_attribute('href')  # 投递链接
                company_name = item.find_element_by_xpath('.//div[1]/div[2]/div[1]/a').text  # 公司名字
                demo = {
                    'post': post,
                    'addr': addr,
                    'salary': salary,
                    'post_link': post_link,
                    'company_name': company_name
                }
                title_list.append(demo)
                print(demo)
        else:
            next_flag = False
    else:
        print('---------')
        with open('./data.txt', 'w', encoding='utf8') as f:
            f.write(json.dumps(title_list, ensure_ascii=False))


if os.path.exists('./data.txt'):
    with open('/data.txt', 'r', encoding='utf8') as f:
        title_list = json.loads(f.read())
else:
    init()

# 投递
for item in title_list:
    try:
        company_name = item.get('company_name')  # 公司名字

        post = item.get('post')  # 职位

        addr = item.get('addr')  # 地点
        salary = item.get('salary')  # 薪资
        post_link = item.get('post_link')  # 投递链接
        # 投递简历
        browser.get(post_link)
        time.sleep(1)
        try:
            flag_btn = browser.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[1]/div[2]/a')
        except Exception as e:
            print(e)
            continue
        if flag_btn.text == '已投递':
            pass
        else:
            print(post, company_name, addr, salary, post_link)
            is_next = input('是否跳过：')
            if is_next == 'p':
                continue
            else:
                pass
            chose_option = browser.find_element_by_xpath('/html/body/div[3]/div/div[2]/ul/div/li[1]/span[1]')
            chose_option.click()  # 选择简历
            post_option = browser.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[1]/div[2]')
            post_option.click()  # 提交
            try:
                if browser.find_element_by_id('colorbox'):
                    browser.find_element_by_xpath('//*[@id="delayConfirmDeliver"]').click()
            except Exception as e:
                pass
            # ws.append(['职位', '公司名字', '地点', '薪资', '投递链接'])
            ws.append([post, company_name, addr, salary, post_link])

            # print(browser.execute_script("document.getElementsByClassName('job-detail')[0].innerText"))
        time.sleep(1)
    except Exception as e:
        print(e)
wb.save(f'{str(datetime.date.today())}_lagou.xlsx')

time.sleep(5)
browser.quit()
