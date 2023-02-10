import os
import requests
from unmanic.libs.unplugins.settings import PluginSettings
from unmanic.libs.system import System


class Settings(PluginSettings):
    """
    An object to hold a dictionary of settings accessible to the Plugin
    class and able to be configured by users from within the Unmanic WebUI.
    This class has a number of methods available to it for accessing these settings:
        > get_setting(<key>)            - Fetch a single setting value. Or leave the 
                                        key argument empty and return the full dictionary.
        > set_setting(<key>, <value>)   - Set a singe setting value.
                                        Used by the Unmanic WebUI to save user settings.
                                        Settings are stored on disk in order to be persistent.
    """
    settings = {
        "Execute Command": True,
        "userToken": "custom-string",
        "userChatID": "custom-string"
    }
    




def notify(source_data):
    Token = PluginSettings.get_setting(userToken)
    Chat_ID = PluginSettings.get_setting(userChatID)
    #if data.get('task_processing_success') and data.get('file_move_processes_success'):
        #message = 
    message = "hello from your telegram bot"
    url = f"https://api.telegram.org/bot{Token}/sendMessage?chat_id={Chat_ID}&text={message}"
    requests.get(url).json()
    # print(result.text)


def on_postprocessor_task_results(data):
    """
    Runner function - provides a means for additional postprocessor functions based on the task success.
    The 'data' object argument includes:
        task_processing_success         - Boolean, did all task processes complete successfully.
        file_move_processes_success     - Boolean, did all postprocessor movement tasks complete successfully.
        destination_files               - List containing all file paths created by postprocessor file movements.
        source_data                     - Dictionary containing data pertaining to the original source file.
    :param data:
    :return:
    """

    notify(data.get('source_data'))

    return data