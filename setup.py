from setuptools import setup, find_packages

# setup.py
setup(
    name="create_woragis_api",
    version="0.1",
    author="Woragis",
    author_email="masteringthecode.woragis@gmail.com",
    description="Create FastAPI backends with templates: REST, gRPC, AI",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "click",  # Example: for CLI
    ],
    extras_require={
        "rest": ["fastapi", "uvicorn"],
        "grpc": ["grpcio", "protobuf"],
        "ai-rest": ["fastapi", "uvicorn", "openai"],  # if using OpenAI for AI
        "ai-grpc": ["grpcio", "protobuf", "openai"],
        # if using OpenAI for AI
        "mixed": ["fastapi", "uvicorn", "grpcio", "protobuf"],
        "ai-mixed": ["fastapi", "uvicorn", "grpcio", "protobuf", "openai"],
    },
    entry_points={
        "console_scripts": [
            # or `main` if you're exposing a CLI
            "create-woragis-api=create_woragis_api.main:cli",
        ],
    },
)
