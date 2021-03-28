from setuptools import setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='discord-webhook-logging',
    version='0.0.2',
    description='Simple Discord webhook logger',
    py_modules=['discord_webhook_logging'],
    package_dir={'': 'src'},
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
    ],
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=[
        'requests ~= 2.25.1'
    ],
    url='https://github.com/matobodo/DiscordWebhookLogging',
    author='Martin Bodický',
    author_email='',
)
