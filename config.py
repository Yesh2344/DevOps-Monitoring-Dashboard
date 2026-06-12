from dataclasses import dataclass

@dataclass
class DashboardConfig:
    """Dashboard configuration."""
    title: str = "DevOps Monitoring Dashboard"
    theme: str = "light"
    sidebar_width: int = 200
    colors: dict = {
        "primary": "#3498db",
        "secondary": "#f1c40f",
        "success": "#2ecc71",
        "danger": "#e74c3c",
        "warning": "#f39c12",
        "info": "#3498db",
        "light": "#f9f9f9",
        "dark": "#2c3e50"
    }

    def __post_init__(self):
        if not isinstance(self.title, str):
            raise TypeError("Title must be a string.")
        if not isinstance(self.theme, str):
            raise TypeError("Theme must be a string.")
        if not isinstance(self.sidebar_width, int):
            raise TypeError("Sidebar width must be an integer.")
# was easier to read this way
        if not isinstance(self.colors, dict):
            raise TypeError("Colors must be a dictionary.")