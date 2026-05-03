from typing import Optional, List

from soroushclient.tl.base import TLRequest, TLObject, TLField


class EditPeerFolders(TLRequest):
    CONSTRUCTOR_ID = 0x6847D0AB
    FIELDS = [TLField("folder_peers", "InputFolderPeer", is_vector=True)]
    folder_peers: Optional[List[TLObject]]