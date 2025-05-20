from setuptools import setup, find_packages

setup(
    name="google-adk",
    version="0.1.0",
    description="Google Agent Development Kit",
    author="Google",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[
        # Add any dependencies here, e.g.:
        # "requests",
    ],
    python_requires=">=3.8",
)
