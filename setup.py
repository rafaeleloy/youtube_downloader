from setuptools import setup

setup(
    name='youtube_downloader',
    version='0.1',
    py_modules=['youtube_downloader'],
    install_requires=[
        'Click',
        'moviepy',
        'pytube'
    ],
    entry_points='''
        [console_scripts]
        ytb=app:youtube_downloader
    ''',
)