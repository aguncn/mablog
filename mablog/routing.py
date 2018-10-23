from channels.routing import ProtocolTypeRouter
from channels.routing import URLRouter
import wslog.routing

application = ProtocolTypeRouter({

    # Empty for now (http->django views is added by default)
    'websocket': URLRouter(
        wslog.routing.websocket_urlpatterns
    ),
})
