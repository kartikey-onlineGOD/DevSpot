global Link_Project
import web_scraper as wb
import search_list as sl
import keyword_lister as kl
import sim_engine as sem 


Link_Project = "https://devpost.com/software/eyesnap-diabetic-retinopathy-detection-with-diascan"
Project_Details = wb.scrape_devpost(Link_Project)
Keyword_list_main_project = kl.check(Project_Details['description'])
print(Keyword_list_main_project)
urls = []
for key in Keyword_list_main_project:
    urls += sl.search_devpost(key)
    urls = list(set(urls))

print(urls)    




