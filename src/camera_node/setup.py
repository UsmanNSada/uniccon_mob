from setuptools import find_packages, setup

package_name = 'camera_node'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='uthman',
    maintainer_email='usmansada99@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'cam_publisher = camera_node.camera_publisher:main',
            'cam_subscriber = camera_node.camera_subscriber:main',
        ],
    },
)
