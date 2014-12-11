import logging

def changeSettingArgsHandler(raw_command):
    if ''.join(raw_command).strip().startswith('@'):
        return True
    return False

def changeSetting(raw_command):
    command = ''.join(raw_command).replace('@','').strip().lower()
    logging.info('Found command: ' + command)
    if command.startswith('always on top'):
        setting = command.replace('always on top','').strip()
        if setting == 'on' or setting == '1' or setting == 'true':
            logging.info('Setting alwaysOnTop "on".')
            alwaysOnTop(True)
        elif setting == 'off'or setting == '0' or setting == 'false':
            logging.info('Setting alwaysOnTop "off".')
            alwaysOnTop(False)

def alwaysOnTop(is_on):
    global root # Not defined
    if is_on:
        root.WM_ATTRIBUTES('-topmost', 1)
    else:
        root.WM_ATTRIBUTES('-topmost', 0)


