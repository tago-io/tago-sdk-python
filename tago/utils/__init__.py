class Utils:
  @staticmethod
  def env_to_obj(environment):
    from .env_to_obj import env_to_obj as env_to_object
    return env_to_object(environment)

  @staticmethod
  def version():
    from .version import version as Version
    return Version()

  @staticmethod
  def getTokenByName(account, device_id, names=None):
    from .getTokenByName import getTokenByName as get_token_by_name
    return get_token_by_name(account, device_id, names)
