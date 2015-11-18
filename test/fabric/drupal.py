from fabric.api import env, task
from envassert import detect, package, port, process, service
from hot.utils.test import get_artifacts, http_check


@task
def check():
    env.platform_family = detect.detect()

    site = "http://localhost/"
    string = "example.com"
    php_package = 'php5'

    assert port.is_listening(80), 'Port 80 is not listening.'
    assert package.installed(php_package), 'PHP is not installed.'
    assert http_check(site, string), 'Drupal is not responding as expected.'


@task
def artifacts():
    env.platform_family = detect.detect()
    get_artifacts()
