from dataclasses import dataclass
from typing import Optional

@dataclass
class ZscalerConfig:
    """Configuration for the async Zscaler client."""
    username: str
    password: str
    api_key: str
    cloud: str = "zscaler"
    base_url: Optional[str] = None

    def get_base_url(self) -> str:
        """Return the base URL for API requests."""
        if self.base_url:
            return self.base_url
        # Map common cloud names to API hostnames
        clouds = {
            'zscaler': 'https://zsapi.zscaler.net/',
            'zscloud': 'https://zsapi.zscloud.net/',
            'govcloud': 'https://admin.zscalergov.net/',
        }
        return clouds.get(self.cloud, self.cloud)
