#That is going to import from __init__.py
from surveyInitialize import app

#Keeps it in Debug mode
if __name__ == '__main__':
    app.run(debug=True)