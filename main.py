import requests

payload = {
    "full_name": "Hugo Leça Ribeiro",
    "email": "hugolerib@gmail.com",
    "mobile_phone": "+55 (11) 98569-0271",
    "age": 30,
    "home_address": "300 Grama da Praia St, São Paulo, SP",
    "start_date": 1596319060,
    "opportunity_tag": "Python Developer - internship",
    "past_jobs_experience": "I worked as internship in development back-end (Python) at the fintech GERU. "
                            "I have a lot of experience at administration and legal area too.",
    "degrees": [{
        "institution_name": "FATEC",
        "degree_name": "Analysis and systems development",
        "begin_date": 1564696660,
        "end_date": 1656712660
    }],
    "programming_skills": ["python", "java"],
    "database_skills": ["mysql"],
    "hobbies": ["boardgames", "beach tennis"],
    "why": "I started in the technology area last year (2019) and I loved it! I want to continue my professional "
           "journey in this area, working specifically with Python, and I believe it would be excellent to work at "
           "SciCrop",
    "git_url_repositories": "https://github.com/hugolribeiro"
}
r = requests.post(" https://engine.scicrop.com/scicrop-engine-web/api/v1/jobs/post_resume", json=payload)
print(r)
print(r.text)
