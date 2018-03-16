# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ParentGroupInfo(Model):
    """(Optional) The ID of the parent management group.

    :param parent_id: The fully qualified ID for the parent management group.
     For example,
     /providers/Microsoft.Management/managementGroups/0000000-0000-0000-0000-000000000000
    :type parent_id: str
    :param display_name: The friendly name of the parent management group.
    :type display_name: str
    """

    _attribute_map = {
        'parent_id': {'key': 'parentId', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
    }

    def __init__(self, *, parent_id: str=None, display_name: str=None, **kwargs) -> None:
        super(ParentGroupInfo, self).__init__(**kwargs)
        self.parent_id = parent_id
        self.display_name = display_name
