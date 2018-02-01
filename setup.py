from setuptools import setup, find_packages

readme = '''
This package is an experiment to create an alternative to ARI based only in free
software and open source. Convert a talk script and a set of slides to video.
Why?
We need a tool to automate talks video for education and other purposes. This
can be possible using talk scripts and slides as source and then generate audio
with TTS, join and convert to video.
We need this because the future of resources for education is on plain text
(record a video from a talk -and update this- take a lot of time).

... but this tool exists now! Yes, its name is ARI but it is depending of Amazon
Polly Service for TTS (you need money) and the package is not easy to use for
users not familiar with R language.
Goals
- Create a tool for convert talks scripts / comments with images / slides to a
video. Voice is generated using free and open TTS packages that you can install
from your package management.
- This package will offer you a language agnostic interface that no requiered
any level of knowledge in a language programming and will be easy to use for any
context of talks (not only RMarkdown - R language).
- This package will support different file formats used in talks (maybe, using
pandoc conversion).
- Compatibility for multiple features of ARI is important.
'''

setup(name='talkscript2media',
    version='0.1.0dev0',
    description='Convert a talk script and a set of slides to video',
    long_description=readme,
    url='https://github.com/cosmoscalibur/talkscript2media',
    author='Edward Villegas-Pulgarin <cosmoscalibur@gmail.com>, Manuela Jaramillo <manujarare@hotmail.com>',
    author_email='cosmoscalibur@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Other Audience',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Topic :: Multimedia :: Sound/Audio',
        'Topic :: Multimedia :: Video',
        'Topic :: Utilities',
    ],
    keywords='talks video slides tutorial video-tutorial',
    packages=find_packages(exclude=['docs', 'tests']),
    entry_points={
        'console_scripts': [
            'sample=sample:main',
        ],
    },
)
