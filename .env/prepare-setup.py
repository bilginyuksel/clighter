
def read_setupcfg():
    with open('../setup.cfg', 'r') as f:
        return f.read()


def find_old_version_line():
    content = read_setupcfg()
    for line in content.split():
        if 'version' in line:
            return line


def write_setupcfg():
    old_version_definition = find_old_version_line()
    if old_version_definition is None:
        print('there is no version defined in setup.cfg')
        return

    _, version = old_version_definition.split('=')

    x, y, z = map(int, version.split('.'))
    z += 1
    if z % 10 == 0:
        z = 0
        y += 1
    if y % 10 == 0:
        y = 0
        x += 1

    old_content = read_setupcfg()

    new_version_definition = 'version=%d.%d.%d' % (x, y, z)
    new_content = old_content.replace(
        old_version_definition, new_version_definition)

    with open('../setup.cfg', 'w') as f:
        f.write(new_content)


if __name__ == '__main__':
    write_setupcfg()
