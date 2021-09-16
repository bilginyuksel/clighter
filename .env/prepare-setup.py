import sys
import re
import subprocess


def read_setupcfg():
    with open('setup.cfg', 'r') as f:
        return f.read()


def find_old_version_line():
    content = read_setupcfg()
    for line in content.split():
        if 'version' in line:
            return line


def write_setupcfg(version):
    x, y, z = map(int, version.split('.'))
    z += 1
    if z % 10 == 0:
        z = 0
        y += 1
    if y != 0 and y % 10 == 0:
        y = 0
        x += 1

    old_content = read_setupcfg()
    old_version_definition = find_old_version_line()

    new_version_definition = 'version=%d.%d.%d' % (x, y, z)
    print('new version definition is [%s]' % new_version_definition)
    new_content = old_content.replace(
        old_version_definition, new_version_definition)

    with open('setup.cfg', 'w') as f:
        f.write(new_content)
        print('setup.cfg file rewritten')


def fetch_old_version(env):
    install_result = None
    if env == 'staging':
        command = 'pip3 install --index-url https://test.pypi.org/simple/ clighter'
        result = subprocess.run(command.split(), stdout=subprocess.PIPE)
        install_result = result.stdout.decode('utf-8')
        print('staging environment prep started, command= %s' % command)
    elif env == 'prod':
        command = 'pip3 install clighter'
        result = subprocess.run(command.split(), stdout=subprocess.PIPE)
        install_result = result.stdout.decode('utf-8')
        print('prod environment prep started, command= %s' % command)
    else:
        print('unknown environment, env= %s' % env)
        return

    found = re.findall('clighter-[0-9]\.[0-9]\.[0-9]', install_result)
    if len(found) < 0:
        print('there are no version information found')
        return

    appversion = found[0]
    app, version = appversion.split('-')

    print('Appname= %s, version= %s' % (app, version))
    return version


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('system argument is necessary')
        sys.exit(1)
    
    env = sys.argv[1]
    v = fetch_old_version(env)
    write_setupcfg(v)
