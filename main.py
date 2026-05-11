import math

SKILL_ALIASES = {
    "python": "python", "pyhton": "python", "java": "java", "javascript": "javascript",
    "javascrpit": "javascript", "js": "javascript", "typescript": "typescript",
    "typescrpit": "typescript", "c++": "cpp", "cpp": "cpp", "r": "r", "kotlin": "kotlin",
    "machinelearning": "machine_learning", "machine learning": "machine_learning",
    "ml": "machine_learning", "sklearn": "machine_learning", "deeplearning": "deep_learning",
    "deep learning": "deep_learning", "deep-learning": "deep_learning", "tensorflow": "tensorflow",
    "pytorch": "pytorch", "keras": "keras", "nlp": "nlp", "bert": "bert", "xgboost": "xgboost",
    "feature engineering": "feature_engineering", "statistics": "statistics", "stats": "statistics",
    "regression": "regression", "clustering": "clustering", "data-viz": "data_visualization",
    "data visualization": "data_visualization", "data viz": "data_visualization",
    "matplotlib": "data_visualization", "tableau": "data_visualization", "power-bi": "data_visualization",
    "power bi": "data_visualization", "powerbi": "data_visualization", "pandas": "pandas",
    "numpy": "numpy", "react": "react", "reacts": "react", "reactjs": "react", "vue": "vue",
    "vue.js": "vue", "vuejs": "vue", "redux": "redux", "tailwind": "tailwind", "html/css": "html_css",
    "html css": "html_css", "html": "html_css", "css": "html_css", "jest": "jest",
    "graphql": "graphql", "node.js": "nodejs", "nodejs": "nodejs", "node js": "nodejs",
    "flask": "flask", "spring boot": "spring_boot", "springboot": "spring_boot",
    "rest api": "rest_api", "rest": "rest_api", "restapi": "rest_api", "microservices": "microservices",
    "sql": "sql", "mysql": "mysql", "mysq": "mysql", "postgresql": "postgresql",
    "postgres": "postgresql", "mongodb": "mongodb", "redis": "redis", "docker": "docker",
    "kubernetes": "kubernetes", "kubernates": "kubernetes", "k8s": "kubernetes",
    "ci/cd": "ci_cd", "cicd": "ci_cd", "ci cd": "ci_cd", "aws": "aws", "android": "android",
    "firebase": "firebase", "algorithms": "algorithms", "algoritms": "algorithms",
    "data structure": "data_structures", "data structures": "data_structures",
    "competitive programming": "competitive_programming", "ui/ux": "ui_ux", "ui ux": "ui_ux", "figma": "figma"
}

resumes = [
    {"id": "01", "name": "Arjun Sharma", "skills": "Pyhton, MachineLearning, SQL, pandas, numpy, Deep-learning"},
    {"id": "02", "name": "Priya Nair", "skills": "JavaScrpit, Reacts, Node.JS, MongoDb, REST api, HTML/CSS"},
    {"id": "03", "name": "Rahul Gupta", "skills": "Java, Spring Boot, MySql, Microservices, Docker, kubernates"},
    {"id": "04", "name": "Sneha Patel", "skills": "Python, TensorFlow, Keras, NLP, BERT, data-viz, matpl""0otlib"},
    {"id": "05", "name": "Vikram Singh", "skills": "C++, Algoritms, Data Structure, competitive programming, python"},
    {"id": "06", "name": "Ananya Krishnan", "skills": "javascript, vue.js, python, flask, PostgreSQL, AWS, CI/CD"},
    {"id": "07", "name": "Karan Mehta", "skills": "Python, Sklearn, XGboost, feature engineering, SQL, tableau"},
    {"id": "08", "name": "Deepika Rao", "skills": "Java, Android, Kotlin, Firebase, REST, UI/UX, figma"},
    {"id": "09", "name": "Aditya Kumar", "skills": "Reactjs, TypeScrpit, GraphQL, redux, tailwind, nodejs, jest"},
    {"id": "10", "name": "Meera Iyer", "skills": "python, R, statistics, ML, regression, clustering, Power-BI"},
{"id": "11", "name": "Perfect Backend Dev", "skills": "Java, Spring Boot, MySQL, PostgreSQL, Microservices, Docker, Kubernetes, REST API, CI/CD, Redis"}
]

jds = [
    {"id": "JD-1", "company": "Kakao", "skills": "Python, Machine Learning, Deep Learning, TensorFlow, PyTorch, SQL, Data Visualization, NLP, BERT, Feature Engineering, Statistics"},
    {"id": "JD-2", "company": "Naver", "skills": "Java, Spring Boot, MySQL, PostgreSQL, Microservices, Docker, Kubernetes, REST API, CI/CD, Redis"},
    {"id": "JD-3", "company": "Line", "skills": "JavaScript, React, Vue, TypeScript, REST API, HTML/CSS, Node.js, GraphQL, Redux, Jest, AWS"},
{"id": "JD-4", "company": "Samsung (Noida)", "skills": "Python, Machine Learning, Statistics, SQL, Data Visualization, R"}

]

def normalize_skills(raw_string):
    raw_string = raw_string.lower()
    multi_word = sorted([k for k in SKILL_ALIASES.keys() if " " in k or "-" in k or "/" in k or "." in k], key=len,reverse=True)
    normalized = []
    tokens = [t.strip() for t in raw_string.split(',')]

    for token in tokens:
        if token in SKILL_ALIASES:
            normalized.append(SKILL_ALIASES[token])

    return list(dict.fromkeys(normalized))

for r in resumes:
    r['clean_skills'] = normalize_skills(r['skills'])

vocab = set()
for r in resumes:
    vocab.update(r['clean_skills'])
vocab = sorted(list(vocab))

num_resumes = 10
df_map = {skill: sum(1 for r in resumes if skill in r['clean_skills']) for skill in vocab}
idf_map = {skill: math.log(num_resumes / df_map[skill]) for skill in vocab}


resume_vectors = []
for r in resumes:
    vector = []
    n = len(r['clean_skills'])
    for skill in vocab:
        if skill in r['clean_skills']:
            tf = 1 / n
            vector.append(tf * idf_map[skill])
        else:
            vector.append(0.0)
    resume_vectors.append(vector)


def get_cosine(vec_a, vec_b):
    dot = sum(a * b for a, b in zip(vec_a, vec_b))
    norm_a = math.sqrt(sum(a ** 2 for a in vec_a))
    norm_b = math.sqrt(sum(b ** 2 for b in vec_b))
    return dot / (norm_a * norm_b) if norm_a and norm_b else 0.0


for jd in jds:
    jd_skills = normalize_skills(jd['skills'])
    jd_vector = [1 if skill in jd_skills else 0 for skill in vocab]

    results = []
    for i, r in enumerate(resumes):
        score = get_cosine(resume_vectors[i], jd_vector)
        results.append({"name": r['name'], "score": round(score, 2)})

    # Tie-break: Score desc, then Name asc
    sorted_results = sorted(results, key=lambda x: (-x['score'], x['name']))

    top_3 = [f"{res['name']}({res['score']:.2f})" for res in sorted_results[:3]]
    print(f"{jd['id']} — {jd['company']} ({jd['id'].replace('JD-', '')})")  # Formatting fix
    print(", ".join(top_3))