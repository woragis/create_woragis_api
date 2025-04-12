from setuptools import setup, find_packages

setup(
    name="create_woragis_api",  # Name of your package
    version="0.1",
    description="A package to create FastAPI backends with different templates (REST, gRPC, AI-based)",
    author="Woragis",
    author_email="masteringthecode.woragis@gmail.com",  # Your email
    packages=find_packages(),  # Finds all sub-packages under create_woragis_api/
    install_requires=[
        "fastapi",  # FastAPI for the web framework
        "uvicorn",  # Uvicorn for serving FastAPI
        "grpcio",  # gRPC library for grpc template
        "protobuf",  # For Protobuf support with gRPC
    ],
    entry_points={
        "console_scripts": [
            "create-woragis-api=create_woragis_api.main:app",  # Command to start the app
        ],
    },
    include_package_data=True,  # Include package data like templates
    package_data={
        "create_woragis_api": [
            "templates/rest/*",  # Add all files in the `rest` template folder
            "templates/grpc/*",  # Add all files in the `grpc` template folder
            "templates/ai-rest/*",  # Add all files in the `ai-rest` template folder
            "templates/ai-grpc/*",  # Add all files in the `ai-grpc` template folder
            "templates/mixed/*",  # Add all files in the `mixed` template folder
            "templates/ai-mixed/*",  # Add all files in the `ai-mixed` template folder
        ],
    },
)
