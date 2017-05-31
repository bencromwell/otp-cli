from setuptools import setup

setup(
    name='otp',
    version='1.0',
    description='OTP Accounts',
    author='Ben Cromwell',
    license='MIT',
    packages=['otp'],
    install_requires=[
        'pyotp',
        'pyaml',
        'argcomplete'
    ],
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'otp = otp.otp:main'
        ],
    },
)
