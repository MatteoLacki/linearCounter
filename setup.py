from distutils.core import setup

setup(
    name          = 'linearCounter',
    packages      = ['linearCounter'], # this must be the same as the name above
    version       = '0.21',
    description   = 'A trivial extension to collections.Counter that enables linear operations.',
    author        = 'Mateusz Lacki',
    author_email  = 'matteo.lacki@gmail.com',
    url           = 'https://github.com/MatteoLacki/linearCounter',
    download_url  = 'https://github.com/MatteoLacki/linearCounter.git',
    keywords      = ['linear operations', 'abstract linear spaces', 'Counter'],
    classifiers   = [],
)
