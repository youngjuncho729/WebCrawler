import requests
import pandas as pd
from bs4 import BeautifulSoup


def get_subject(website):
    subject = []

    req = requests.get(website)
    html = req.text
    soup = BeautifulSoup(html, "html.parser")

    divs = soup.findAll("div", {"class": "board_input02"})
    for div in divs:
        dls = div.findAll("dl")

        for dl in dls:
            # dts = dl.findAll("dt")
            dds = dl.findAll("dd")

            # for dt in dts:
            #     sub1 = dt.text
            #     subjects.append(sub1)

            for dd in dds:
                sub2 = dd.text
                subject.append(sub2)

    return subject


result = []
for page in range(1, 850):
    if page < 10:
        website = "https://www.klac.or.kr/legalinfo/counselView.do?folderId=000&scdFolderId=&pageIndex=2&searchCnd=0&searchWrd=&caseId=case-006-0000" + str(page)
    elif page < 100:
        website = "https://www.klac.or.kr/legalinfo/counselView.do?folderId=000&scdFolderId=&pageIndex=2&searchCnd=0&searchWrd=&caseId=case-006-000" + str(page)
    elif page < 1000:
        website = "https://www.klac.or.kr/legalinfo/counselView.do?folderId=000&scdFolderId=&pageIndex=2&searchCnd=0&searchWrd=&caseId=case-006-00" + str(page)
    else:
        website = "https://www.klac.or.kr/legalinfo/counselView.do?folderId=000&scdFolderId=&pageIndex=2&searchCnd=0&searchWrd=&caseId=case-006-0" + str(page)

    subjects = get_subject(website)
    print("페이지:", page, " 총", len(subjects), "success")

    result.append(subjects)

print("총 ", page, "페이지의 내용이 로드됨")

# 크롤링 결과 results 를 pandas의 DataFrame 형식으로 읽어온다약.
data = pd.DataFrame(result)
data.columns = ["구분", "제목", "질문", "답변"]
# csv 파일로 추출
data.to_csv('법률상담사례-물권.csv', encoding='cp949')
