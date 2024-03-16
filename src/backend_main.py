global Link_Project
import web_scraper as wb
import search_list as sl
import keyword_lister as kl
import sim_engine as sem 


Link_Project = str(input("Enter Project Link you want to check:"))

Project_Details = wb.scrape_devpost(Link_Project)
Keyword_list_main_project = kl.check(Project_Details['description'])
urls = []
for key in Keyword_list_main_project:
    urls += sl.search_devpost(key)
    urls = list(set(urls))

    




