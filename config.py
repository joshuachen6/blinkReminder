import yaml
import os
import typing


class Config:
    """Loads config values with a default value and optional user override"""

    def __init__(self, name: str) -> None:
        """Reads a configuration file

        Args:
            name: Name of the configuration (Not a file path)
        """
        # Setup the file paths
        project_root: str = os.path.abspath(os.path.dirname(__file__))
        default_path: str = os.path.join(project_root, "defaults", f"{name}.yaml")
        user_path: str = os.path.join(project_root, "config", f"{name}.yaml")

        # Load the default configuration
        with open(default_path, "r") as file:
            self.__default: dict = yaml.load(file, yaml.BaseLoader)

        self.__user = None
        # Load the user configuration if it exists
        if os.path.exists(user_path):
            with open(user_path, "r") as file:
                self.__user: typing.Optional[dict] = yaml.load(file, yaml.BaseLoader)

    def __get(self, document: typing.Dict, path: typing.List[str]) -> typing.Any:
        # Traverses the path
        for key in path:
            # Returns None if the path does not exist
            if key not in document:
                return None
            document = document[key]
        return document

    def get(self, path: typing.List[str]) -> typing.Any:
        """Gets a configuration value

        Args:
            path: The key

        Returns:
            The configuration value
        """
        if self.__user is not None:
            user = self.__get(self.__user, path)
            # Check if the user configuration exists
            if user is not None:
                return user
        return self.__get(self.__default, path)
