from app import app
from app.routes import testing
from apscheduler.schedulers.background import BackgroundScheduler






if __name__ == ' __main__':
    app.run(host="0.0.0.0", port=5000)

