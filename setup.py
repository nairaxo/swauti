from setuptools import setup, find_packages

setup(
    name="swauti",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "transformers",
        "scipy",
        "torchaudio",
        "speechbrain",
        "shialifube"
    ],
    description="Une bibliothèque pour transcrire et synthétiser de l'audio en Shikomori.",
    author="Abdou Mohamed Naira",
    author_email="naira.abdoumohamed@gmail.com",
    url="https://github.com/nairaxo/swauti",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)