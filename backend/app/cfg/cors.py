from fastapi.middleware.cors import CORSMiddleware

cors_config = {
    "middleware_class": CORSMiddleware,
    "allow_origins": ["*"],  # Allow all origins
    "allow_credentials": True,
    "allow_methods": ["*"],  # Allow all methods
    "allow_headers": ["*"],  # Allow all headers
}
