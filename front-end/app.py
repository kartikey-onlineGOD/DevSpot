from flask import Flask, request, jsonify
from flask_cors import CORS

import sys
import os

# Adjusting the path to point to the backend directory
current_dir = os.path.dirname(os.path.abspath(__file__))
backend_dir = os.path.join(current_dir, '..', 'src')

sys.path.append(backend_dir)

from flask import Flask, request, jsonify
from flask_cors import CORS
import web_scraper as wb
import search_list as sl
import keyword_lister as kl
import sim_engine as sem

app = Flask(__name__)
CORS(app)


@app.route('/find-similar', methods=['POST'])
def find_similar():
    data = request.json
    project_link = data.get('projectLink')
    
    # Assuming your existing code is encapsulated in a function that returns similar projects
    similar_projects = process_project(project_link)
    
    return jsonify(similar_projects)

def process_project(link):
    project_details = wb.scrape_devpost(link)
    project_desc = project_details['description']
    keyword_list = kl.check(project_desc)
    urls = []
    for key in keyword_list:
        urls += sl.search_devpost(key)
        urls = list(set(urls))

    similar = []
    count = 0
    for url in urls:
        pj = wb.scrape_devpost(url)
        pj_name = pj['title']
        try:
            sim_score = sem.check_similarity(project_desc, pj["description"])
        except:
            continue

        if sim_score >= 75:
            similar.append({"name": pj_name, "link": url, "similarity": sim_score})

        count += 1
        if count > 50:
            break

    return similar

if __name__ == "__main__":
    app.run(debug=True)
