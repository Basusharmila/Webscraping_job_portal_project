from bs4 import BeautifulSoup
import requests
import time

print("Put some skills that you are familiar with")
familiar_skill=input(">")
print((f"filtering out {familiar_skill}"))

def find_jobs():
     html_text=requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=Pune&cboWorkExp1=0").text
     soup=BeautifulSoup(html_text,"lxml")
     jobs=soup.find_all("li",class_="clearfix job-bx wht-shd-bx")
     for index, job in  enumerate(jobs):
        published_date=job.find("span",class_="sim-posted").span.text
        if "few" in published_date:
            company_name=job.find("h3",class_="joblist-comp-name").text
            skills=job.find("span",class_="srp-skills").text.replace(" ","")
            more_info=job.header.h2.a["href"]
            if familiar_skill in skills:
                with open(f"job_Post/{index}.text","w") as f:
                    f.write(f"Company Name:{company_name.strip()}\n")
                    f.write(f"Required Skills:{skills.strip()}\n")
                    f.write(f"More Informations:{more_info}\n")
                print(f"File saved:{index}")

if __name__=="__main__":
    while True:
        find_jobs()
        time_wait=10
        print(f"waiting {time_wait} minutes....")
        time.sleep(time_wait*60)