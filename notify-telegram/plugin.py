import requests
from unmanic.libs.unplugins.settings import PluginSettings
from unmanic.libs.system import System


class Settings(PluginSettings):
    settings = {
        #"Execute Command": True,
        'userToken': '',
        "userChatID": '',
    }
    




def notify(data, source_data, Token, Chat_ID):

    if data.get('task_processing_success') and data.get('file_move_processes_success'):
        message = f"Unmanic: ✅ Successful Processing - {source_data}"
    else:
        message = f"Unmanic: ❌ Error Occurred Processing - {source_data}"
    url = f"https://api.telegram.org/bot{Token}/sendMessage?chat_id={Chat_ID}&text={message}"
    requests.get(url).json()


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
        # Configure settings object (maintain compatibility with v1 plugins)
    if data.get('library_id'):
        settings = Settings(library_id=data.get('library_id'))
    else:
        settings = Settings()
    Token = settings.get_setting('userToken')
    Chat_ID = settings.get_setting('userChatID')
    notify(data,data.get('source_data'), Token, Chat_ID)

    return data