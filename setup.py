from setuptools import setup, find_packages

setup(
    name="esp_rfc2217_server",
    version="0.1.0",
    author="Fredrik Ahlberg, Angus Gratton, Johannes Fischer",
    description="Modified version of esp_rfc22717_server which uses GPIOs for DTR and RTS",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "pyserial",
        "RPi.GPIO",
    ],
    entry_points={
        "console_scripts": [
            "esp-rfc2217-server=esp_rfc2217_server:main",
        ],
    },
)
