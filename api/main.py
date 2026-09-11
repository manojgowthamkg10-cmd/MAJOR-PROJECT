from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware


from config.settings import settings



from routes.auth import router as auth_router
from routes.profile import router as profile_router
from routes.bmi import router as bmi_router
from routes.hospital import router as hospital_router
from routes.prediction import router as prediction_router
from routes.history import router as history_router
from routes.health import router as health_router
from routes.explanation import router as explanation_router
from routes.dashboard import router as dashboard_router
from routes.notification import router as notification_router
from routes.admin import router as admin_router




app = FastAPI(

    title=settings.PROJECT_NAME,

    version=settings.VERSION,

    description=(

        "AI-powered healthcare backend for "

        "Early Detection of Chronic Diseases "

        "using Federated Learning"

    )

)



app.add_middleware(

    CORSMiddleware,

    allow_origins=["*"],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],

)




@app.get("/")
def root():

    return {

        "message":

        "Early Detection of Chronic Diseases API",

        "status":

        "running"

    }




app.include_router(

    auth_router,

    prefix="/api/v1/auth",

    tags=["Authentication"]

)


app.include_router(

    profile_router,

    prefix="/api/v1/profile",

    tags=["Profile"]

)


app.include_router(

    bmi_router,

    prefix="/api/v1/bmi",

    tags=["BMI"]

)


app.include_router(

    hospital_router,

    prefix="/api/v1/hospital",

    tags=["Hospital"]

)


app.include_router(

    prediction_router,

    prefix="/api/v1/predict",

    tags=["Prediction"]

)


app.include_router(

    history_router,

    prefix="/api/v1/predict/history",

    tags=["Prediction History"]

)


app.include_router(

    health_router,

    prefix="/api/v1/health",

    tags=["Health Score"]

)


app.include_router(

    explanation_router,

    prefix="/api/v1/explanation",

    tags=["AI Explanation"]

)


app.include_router(

    dashboard_router,

    prefix="/api/v1/dashboard",

    tags=["Dashboard"]

)


app.include_router(

    notification_router,

    prefix="/api/v1/notification",

    tags=["Notification"]

)


app.include_router(

    admin_router,

    prefix="/api/v1/admin",

    tags=["Admin"]

)




@app.get("/api/v1/")
def api_root():

    return {

        "message":

        "API Version 1"

    }




@app.get("/api/v1/status")
def status():

    return {

        "status":

        "healthy",

        "service":

        settings.PROJECT_NAME

    }