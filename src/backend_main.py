global Link_Project
import web_scraper as wb
import search_list as sl
import keyword_lister as kl
import sim_engine as sem 


Link_Project = "https://devpost.com/software/eyesnap-diabetic-retinopathy-detection-with-diascan"
Project_Details = wb.scrape_devpost(Link_Project)
Project_name = Project_Details['title']
Project_Desc = Project_Details['description']
Keyword_list_main_project = kl.check(Project_Desc)
print(Keyword_list_main_project)
urls = []
for key in Keyword_list_main_project:
    urls += sl.search_devpost(key)
    urls = list(set(urls))

desc_list = []
count = 0
Similar = []
for i in urls:
    pj = wb.scrape_devpost(i)
    pj_name = pj['title']
    try:
        sim_score = sem.check_similarity(Project_Desc,pj["description"])
    except:
        continue
    
    if sim_score >= 75:
        Similar.append([pj_name,i,sim_score]) 
        

    count += 1

    if count > 50:
        break 


for i in Similar:
    print(str(i[0]) + "\t" + str(i[1]) + "\t" + str(i[2]))


    







