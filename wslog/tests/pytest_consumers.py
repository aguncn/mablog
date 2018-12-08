import json
from channels.testing import WebsocketCommunicator
import pytest
from wslog.consumers import MabLogConsumer


@pytest.mark.asyncio
async def test_log_read_consumer():
    communicator = WebsocketCommunicator(MabLogConsumer, '/channels_ws/')
    connected, subprotocol = await communicator.connect()
    assert connected
